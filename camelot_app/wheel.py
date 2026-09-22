"""Interactive Camelot Wheel widget."""

import math
import tkinter as tk

from camelot_core.camelot import CAMELOT_KEYS
from camelot_core.compatibility import compatible_keys


class CamelotWheel(tk.Canvas):
    """Draw a clickable Camelot Wheel with 24 positions."""

    def __init__(self, master, on_select, **kwargs):
        super().__init__(
            master,
            width=440,
            height=440,
            highlightthickness=0,
            **kwargs,
        )
        self.on_select = on_select
        self.selected_code = "8A"
        self.compatible = set(compatible_keys(self.selected_code))

        self.bind("<Button-1>", self._handle_click)
        self.bind("<Configure>", lambda _event: self.draw_wheel())

        self.draw_wheel()

    def set_selection(self, code):
        """Update the selected code and redraw the wheel."""
        if code not in CAMELOT_KEYS:
            raise ValueError(f"Invalid Camelot code: {code}")

        self.selected_code = code
        self.compatible = set(compatible_keys(code))
        self.draw_wheel()

    @staticmethod
    def _point(cx, cy, radius, angle_degrees):
        angle = math.radians(angle_degrees)
        return (
            cx + radius * math.cos(angle),
            cy + radius * math.sin(angle),
        )

    def _segment_points(self, cx, cy, inner, outer, start, end):
        points = []

        # Outer edge, moving clockwise.
        for step in range(7):
            angle = start + (end - start) * step / 6
            points.extend(self._point(cx, cy, outer, angle))

        # Inner edge, moving back toward the start.
        for step in range(6, -1, -1):
            angle = start + (end - start) * step / 6
            points.extend(self._point(cx, cy, inner, angle))

        return points

    def draw_wheel(self):
        """Redraw all 24 Camelot positions."""
        self.delete("all")

        width = max(self.winfo_width(), 440)
        height = max(self.winfo_height(), 440)
        cx = width / 2
        cy = height / 2

        outer_radius = min(width, height) * 0.47
        inner_outer = outer_radius * 0.66
        inner_inner = outer_radius * 0.36

        for number in range(1, 13):
            start = -105 + (number - 1) * 30
            end = start + 30
            middle = (start + end) / 2

            for letter, inner, outer in (
                ("A", inner_inner, inner_outer),
                ("B", inner_outer + 4, outer_radius),
            ):
                code = f"{number}{letter}"

                if code == self.selected_code:
                    fill = "#f2c14e"
                    text_color = "#17202a"
                    outline = "#ffffff"
                    line_width = 3
                elif code in self.compatible:
                    fill = "#56b88a"
                    text_color = "#10251b"
                    outline = "#ffffff"
                    line_width = 2
                else:
                    fill = "#35465c" if letter == "A" else "#53657b"
                    text_color = "#ffffff"
                    outline = "#d9e0e8"
                    line_width = 1

                points = self._segment_points(
                    cx, cy, inner, outer, start, end
                )

                self.create_polygon(
                    points,
                    fill=fill,
                    outline=outline,
                    width=line_width,
                )

                label_radius = (inner + outer) / 2
                x, y = self._point(cx, cy, label_radius, middle)

                self.create_text(
                    x,
                    y,
                    text=code,
                    fill=text_color,
                    font=("TkDefaultFont", 11, "bold"),
                )

        self.create_oval(
            cx - inner_inner + 5,
            cy - inner_inner + 5,
            cx + inner_inner - 5,
            cy + inner_inner - 5,
            fill="#18212d",
            outline="#d9e0e8",
            width=2,
        )
        self.create_text(
            cx,
            cy - 10,
            text="CAMELOT",
            fill="#ffffff",
            font=("TkDefaultFont", 13, "bold"),
        )
        self.create_text(
            cx,
            cy + 14,
            text="DJ",
            fill="#f2c14e",
            font=("TkDefaultFont", 17, "bold"),
        )

    def _handle_click(self, event):
        """Determine which wheel segment was clicked."""
        width = max(self.winfo_width(), 440)
        height = max(self.winfo_height(), 440)
        cx = width / 2
        cy = height / 2

        dx = event.x - cx
        dy = event.y - cy
        radius = math.hypot(dx, dy)

        outer_radius = min(width, height) * 0.47
        inner_outer = outer_radius * 0.66
        inner_inner = outer_radius * 0.36

        if inner_inner <= radius <= inner_outer:
            letter = "A"
        elif inner_outer + 4 <= radius <= outer_radius:
            letter = "B"
        else:
            return

        angle = math.degrees(math.atan2(dy, dx))
        index = int(((angle + 105) % 360) // 30)
        number = index + 1
        code = f"{number}{letter}"

        self.on_select(code)
