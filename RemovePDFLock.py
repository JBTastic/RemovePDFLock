import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pypdf import PdfReader, PdfWriter


def select_folder():
    folder_selected = filedialog.askdirectory()
    folder_var.set(folder_selected)


def decrypt_pdfs():
    folder = folder_var.get()
    password = password_var.get()
    keep_originals = save_separate_var.get()

    if not folder:
        messagebox.showerror("Error", "Please select folder.")
        return
    if not password:
        messagebox.showerror("Error", "Please enter password.")
        return

    count_decrypted = 0
    count_skipped = 0

    for root, dirs, files in os.walk(folder):
        for file in files:
            if not file.lower().endswith(".pdf"):
                continue

            file_path = os.path.join(root, file)

            # Open reader
            try:
                reader = PdfReader(file_path)
            except Exception:
                count_skipped += 1
                continue

            # Skip unencrypted
            if not reader.is_encrypted:
                count_skipped += 1
                continue

            # Apply password
            try:
                reader.decrypt(password)
            except Exception:
                count_skipped += 1
                continue

            # Test: Can a page be read?
            try:
                _ = reader.pages[0]
            except Exception:
                count_skipped += 1
                continue

            # Determine target
            if keep_originals:
                new_path = os.path.join(root, f"decrypted_{file}")
            else:
                new_path = file_path

            # Write
            try:
                writer = PdfWriter()
                for p in reader.pages:
                    writer.add_page(p)

                with open(new_path, "wb") as f:
                    writer.write(f)

                count_decrypted += 1
            except Exception:
                count_skipped += 1

    messagebox.showinfo(
        "Done",
        f"Decrypted PDFs: {count_decrypted}\n"
        f"Skipped files: {count_skipped}"
    )


# ---------- GUI ----------

root = tk.Tk()
root.title("PDF Decrypter - by JBTastic")

folder_var = tk.StringVar()
password_var = tk.StringVar()
save_separate_var = tk.BooleanVar(value=True)

tk.Label(root, text="Folder with PDFs:").pack(anchor="w", padx=10, pady=(10, 0))

frame = tk.Frame(root)
frame.pack(fill="x", padx=10)

tk.Entry(frame, textvariable=folder_var, width=50).pack(side="left", fill="x", expand=True)
tk.Button(frame, text="Select Folder", command=select_folder).pack(side="right")

tk.Label(root, text="Password:").pack(anchor="w", padx=10, pady=(10, 0))
tk.Entry(root, textvariable=password_var, show="*", width=30).pack(padx=10)

tk.Checkbutton(
    root,
    text="Keep originals (decrypted_NAME.pdf)",
    variable=save_separate_var
).pack(anchor="w", padx=10, pady=10)

tk.Button(root, text="Decrypt PDFs", command=decrypt_pdfs).pack(pady=15)
root.mainloop()
