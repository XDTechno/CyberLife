import os
import re
from traceback import print_stack
from typing import override

import colorama
from core.entity.entity import Entity
from core.world.tile import Tile
from view.base_view import View


class TuiView(View):
    @override
    def update_map(self, map):
        super().update_map(map)
        self.refresh_ui()

    def refresh_ui(self):
        try:
            term_size = os.get_terminal_size()
        except OSError:
            # Set default terminal size
            term_size = os.terminal_size((80, 24))
        term_side_len_min = min(term_size.columns, term_size.lines)
        map_side_len_max = max(self.mapdata.width, self.mapdata.height)
        block_size = (term_side_len_min // map_side_len_max) + 1
        if block_size < 2:
            print("Terminal too small!!")
            return
        print(colorama.ansi.clear_screen(), end="")
        print(colorama.ansi.Cursor.POS(0, 0), end="")

        texts = [
            [self.stringify_tile(cell) for cell in row] for row in self.mapdata.map
        ]
        self.print_table(texts, block_size)

    @staticmethod
    def stringify_tile(x):
        if not isinstance(x, Tile):
            s = x.__str__()
            return s
        entity = x.peek_or_default(" ")
        if not isinstance(entity, Entity):
            return entity.__str__()
        return f"E_{entity.__hash__()}"

    @staticmethod
    def print_table(data, cell_edge_len):
        def wrap_text(text, width):
            """Wrap text to fit within a given width."""
            lines = [text[i : i + width] for i in range(0, len(text), width)]
            return lines

        def center_text(text, width):
            """Center text within a given width."""
            return text.center(width)

        def get_lines(text, width, height):
            """Wrap the text into lines and center it vertically within the given height."""
            lines = wrap_text(text, width)
            total_lines = len(lines)

            if total_lines < height:
                # Add blank lines to center vertically
                blank_lines = (height - total_lines) // 2
                lines = (
                    [""] * blank_lines
                    + lines
                    + [""] * (height - total_lines - blank_lines)
                )
            elif total_lines > height:
                # Cut lines to fit within the height
                lines = lines[:height]

            # Ensure the last line fits within the width
            if len(lines[-1]) > width:
                lines[-1] = lines[-1][: width - 2] + ".."

            return lines

        rows = len(data)
        cols = len(data[0]) if rows > 0 else 0

        cell_height = cell_edge_len // 2  # Height is half of the width
        horizontal_border = "+" + ("-" * cell_edge_len + "+") * cols

        for row in data:
            print(horizontal_border)
            cell_lines = [get_lines(cell, cell_edge_len, cell_height) for cell in row]
            for line_index in range(cell_height):
                print("|", end="")
                for lines in cell_lines:
                    print(center_text(lines[line_index], cell_edge_len), end="|")
                print()
        print(horizontal_border)
