"""Command line / standalone entry point: ``image-slide file.npy [--axes 2 3]``."""

import argparse
import sys
import tkinter as tk
from tkinter import filedialog, messagebox


def _pick_array_name(names):
    """Small dialog to choose one array from an .npz archive."""
    root = tk.Tk()
    root.title("Select array")
    choice = {"name": None}
    listbox = tk.Listbox(root, height=min(15, len(names)), width=40)
    for n in names:
        listbox.insert(tk.END, n)
    listbox.selection_set(0)
    listbox.pack(padx=10, pady=10)

    def ok(_=None):
        sel = listbox.curselection()
        choice["name"] = names[sel[0]] if sel else None
        root.destroy()

    listbox.bind("<Double-Button-1>", ok)
    root.bind("<Return>", ok)
    tk.Button(root, text="Open", command=ok).pack(pady=(0, 10))
    root.mainloop()
    return choice["name"]


def load_array(path):
    import numpy as np

    data = np.load(path, allow_pickle=False)
    if isinstance(data, np.lib.npyio.NpzFile):
        names = list(data.files)
        if not names:
            raise ValueError("The .npz file contains no arrays")
        name = names[0] if len(names) == 1 else _pick_array_name(names)
        if name is None:
            return None
        return data[name]
    return data


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="image-slide", description="Interactive viewer for numpy arrays"
    )
    parser.add_argument("file", nargs="?", help=".npy or .npz file to open")
    parser.add_argument(
        "--axes",
        nargs=2,
        type=int,
        metavar=("ROW", "COL"),
        help="array dimensions to display as image (default: 0 1)",
    )
    args = parser.parse_args(argv)

    path = args.file
    if path is None:
        root = tk.Tk()
        root.withdraw()
        path = filedialog.askopenfilename(
            title="Open numpy file",
            filetypes=[("NumPy files", "*.npy *.npz"), ("All files", "*.*")],
        )
        root.destroy()
        if not path:
            return 0

    try:
        from image_slide.viewer import image_slide

        data = load_array(path)
        if data is None:
            return 0
        axes = tuple(args.axes) if args.axes else None
        image_slide(data, title=path, axes=axes)
    except Exception as e:  # windowed exe has no console, so show a dialog
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("image-slide", f"{type(e).__name__}: {e}")
        root.destroy()
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
