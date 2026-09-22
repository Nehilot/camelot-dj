"""Main graphical window for Camelot DJ."""

import tkinter as tk
from tkinter import ttk, messagebox

from camelot_core.camelot import CAMELOT_KEYS, camelot_to_key
from camelot_core.compatibility_explanations import explain_compatibility


class CamelotDJWindow:
    """Standalone Camelot DJ application window."""

    def __init__(self, root):
        self.root = root
        self.root.title("Camelot DJ — Harmonic Mixing Assistant")
        self.root.geometry("620x500")
        self.root.minsize(520, 420)

        self.selected_code = tk.StringVar(value="8A")

        self._build_interface()
        self.update_selection()

    def _build_interface(self):
        main = ttk.Frame(self.root, padding=20)
        main.pack(fill="both", expand=True)

        title = ttk.Label(
            main,
            text="Camelot DJ",
            font=("TkDefaultFont", 20, "bold"),
        )
        title.pack(anchor="w")

        subtitle = ttk.Label(
            main,
            text="Harmonic Mixing Assistant",
        )
        subtitle.pack(anchor="w", pady=(0, 18))

        selector_frame = ttk.Frame(main)
        selector_frame.pack(fill="x", pady=(0, 14))

        ttk.Label(
            selector_frame,
            text="Selecciona una tonalidad Camelot:",
        ).pack(side="left")

        codes = list(CAMELOT_KEYS.keys())

        self.code_selector = ttk.Combobox(
            selector_frame,
            textvariable=self.selected_code,
            values=codes,
            state="readonly",
            width=8,
        )
        self.code_selector.pack(side="left", padx=(10, 0))
        self.code_selector.bind(
            "<<ComboboxSelected>>",
            self._on_selection_changed,
        )

        self.key_label = ttk.Label(
            main,
            text="",
            font=("TkDefaultFont", 14, "bold"),
        )
        self.key_label.pack(anchor="w", pady=(0, 16))

        ttk.Label(
            main,
            text="Tonalidades compatibles:",
            font=("TkDefaultFont", 12, "bold"),
        ).pack(anchor="w")

        self.results_frame = ttk.Frame(main)
        self.results_frame.pack(fill="both", expand=True, pady=(8, 12))

        self.results = tk.Listbox(
            self.results_frame,
            font=("TkDefaultFont", 11),
            height=8,
            activestyle="none",
        )
        self.results.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(
            self.results_frame,
            orient="vertical",
            command=self.results.yview,
        )
        scrollbar.pack(side="right", fill="y")
        self.results.configure(yscrollcommand=scrollbar.set)

        self.status_label = ttk.Label(
            main,
            text="Motor musical: Camelot Core",
        )
        self.status_label.pack(anchor="w", pady=(8, 0))

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

        self.key_label.config(
            text=f"{code}  —  {key.name} {mode_name}"
        )

        self.results.delete(0, tk.END)

        for compatible_code, reason in explanations.items():
            compatible_key = camelot_to_key(compatible_code)
            compatible_mode = (
                "menor" if compatible_key.mode == "minor" else "mayor"
            )

            line = (
                f"{compatible_code} — {compatible_key.name} "
                f"{compatible_mode}: {reason}"
            )
            self.results.insert(tk.END, line)


def create_window():
    """Create and run the Camelot DJ application."""
    root = tk.Tk()
    CamelotDJWindow(root)
    root.mainloop()
