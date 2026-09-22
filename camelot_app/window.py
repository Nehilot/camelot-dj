"""Main graphical window for Camelot DJ."""

import tkinter as tk
from tkinter import ttk, messagebox

from camelot_core.camelot import CAMELOT_KEYS, camelot_to_key
from camelot_core.compatibility_explanations import explain_compatibility
from camelot_app.wheel import CamelotWheel


class CamelotDJWindow:
    """Standalone Camelot DJ application window."""

    def __init__(self, root):
        self.root = root
        self.root.title("Camelot DJ — Harmonic Mixing Assistant")
        self.root.geometry("980x700")
        self.root.minsize(800, 600)

        self.selected_code = tk.StringVar(value="8A")

        self._build_interface()
        self.update_selection()

    def _build_interface(self):
        main = ttk.Frame(self.root, padding=16)
        main.pack(fill="both", expand=True)

        ttk.Label(
            main,
            text="Camelot DJ",
            font=("TkDefaultFont", 20, "bold"),
        ).pack(anchor="w")

        ttk.Label(
            main,
            text="Harmonic Mixing Assistant",
        ).pack(anchor="w", pady=(0, 12))

        content = ttk.Frame(main)
        content.pack(fill="both", expand=True)

        wheel_frame = ttk.Frame(content)
        wheel_frame.pack(side="left", fill="both", expand=True)

        self.wheel = CamelotWheel(
            wheel_frame,
            on_select=self._select_code,
            background="#18212d",
        )
        self.wheel.pack(expand=True)

        details = ttk.Frame(content, padding=(18, 8, 0, 8))
        details.pack(side="right", fill="both", expand=True)

        ttk.Label(
            details,
            text="Selecciona una tonalidad:",
        ).pack(anchor="w")

        self.code_selector = ttk.Combobox(
            details,
            textvariable=self.selected_code,
            values=list(CAMELOT_KEYS.keys()),
            state="readonly",
            width=10,
        )
        self.code_selector.pack(anchor="w", pady=(6, 14))
        self.code_selector.bind(
            "<<ComboboxSelected>>",
            self._on_selection_changed,
        )

        self.key_label = ttk.Label(
            details,
            text="",
            font=("TkDefaultFont", 14, "bold"),
        )
        self.key_label.pack(anchor="w", pady=(0, 16))

        ttk.Label(
            details,
            text="Tonalidades compatibles:",
            font=("TkDefaultFont", 12, "bold"),
        ).pack(anchor="w")

        results_frame = ttk.Frame(details)
        results_frame.pack(fill="both", expand=True, pady=(8, 12))

        self.results = tk.Text(
            results_frame,
            wrap="word",
            font=("TkDefaultFont", 10),
            height=14,
            padx=8,
            pady=8,
            spacing1=2,
            spacing3=8,
            relief="solid",
            borderwidth=1,
            state="disabled",
        )
        self.results.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(
            results_frame,
            orient="vertical",
            command=self.results.yview,
        )
        scrollbar.pack(side="right", fill="y")
        self.results.configure(yscrollcommand=scrollbar.set)

        self.status_label = ttk.Label(
            main,
            text="Motor musical: Camelot Core",
        )
        self.status_label.pack(anchor="w", pady=(10, 0))

    def _select_code(self, code):
        self.selected_code.set(code)
        self.update_selection()

    def _on_selection_changed(self, _event=None):
        self.update_selection()

    def update_selection(self):
        code = self.selected_code.get()

        try:
            key = camelot_to_key(code)
            explanations = explain_compatibility(code)
        except ValueError as error:
            messagebox.showerror("Error", str(error))
            return

        mode_name = "menor" if key.mode == "minor" else "mayor"
        self.key_label.config(text=f"{code} — {key.name} {mode_name}")

        self.results.configure(state="normal")
        self.results.delete("1.0", tk.END)

        for compatible_code, reason in explanations.items():
            compatible_key = camelot_to_key(compatible_code)
            compatible_mode = (
                "menor"
                if compatible_key.mode == "minor"
                else "mayor"
            )

            heading = (
                f"{compatible_code} — {compatible_key.name} "
                f"{compatible_mode}"
            )

            self.results.insert(tk.END, heading + "\n", "heading")
            self.results.insert(tk.END, reason + "\n\n")

        self.results.tag_configure(
            "heading",
            font=("TkDefaultFont", 10, "bold"),
        )
        self.results.configure(state="disabled")

        self.wheel.set_selection(code)


def create_window():
    """Create and run the Camelot DJ application."""
    root = tk.Tk()
    CamelotDJWindow(root)
    root.mainloop()
