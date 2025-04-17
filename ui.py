import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox

class CommitApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Commit Message Generator")
        self.root.geometry("600x700")

        # Sign In Button
        self.sign_in_btn = tk.Button(root, text="Sign in to GitHub", command=self.sign_in)
        self.sign_in_btn.pack(pady=5)

        # Folder Select
        self.folder_btn = tk.Button(root, text="Select Folder", command=self.select_folder)
        self.folder_btn.pack(pady=5)

        # Repo Selector (dropdown - placeholder for now)
        self.repo_var = tk.StringVar()
        self.repo_dropdown = tk.OptionMenu(root, self.repo_var, "Select Repo")
        self.repo_dropdown.pack(pady=5)

        # Changes Display Box
        tk.Label(root, text="Detected Changes:").pack()
        self.changes_box = scrolledtext.ScrolledText(root, height=10, width=70)
        self.changes_box.pack(pady=5)

        # Optional Additional Info
        tk.Label(root, text="Optional Notes:").pack()
        self.notes_entry = tk.Text(root, height=4, width=70)
        self.notes_entry.pack(pady=5)

        # Refresh Button
        self.refresh_btn = tk.Button(root, text="Refresh Changes", command=self.refresh_changes)
        self.refresh_btn.pack(pady=5)

        # Generate Commit Message Button
        self.generate_btn = tk.Button(root, text="Generate Commit Message", command=self.generate_commit)
        self.generate_btn.pack(pady=5)

        # Output Box
        tk.Label(root, text="Generated Commit Message:").pack()
        self.commit_output = tk.Text(root, height=4, width=70)
        self.commit_output.pack(pady=5)

    def sign_in(self):
        messagebox.showinfo("Sign In", "Pretend we're signing into GitHub!")

    def select_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            messagebox.showinfo("Folder Selected", f"Selected: {folder}")
            # Replace this with actual loading logic later

    def refresh_changes(self):
        self.changes_box.delete(1.0, tk.END)
        self.changes_box.insert(tk.END, "Fake change:\n- Modified file1.py\n- Added feature to file2.py")
        # Replace this with actual git or API logic later

    def generate_commit(self):
        notes = self.notes_entry.get(1.0, tk.END).strip()
        changes = self.changes_box.get(1.0, tk.END).strip()
        message = f"Commit based on:\n{changes}\n\nNotes:\n{notes}"
        self.commit_output.delete(1.0, tk.END)
        self.commit_output.insert(tk.END, message)

if __name__ == "__main__":
    root = tk.Tk()
    app = CommitApp(root)
    root.mainloop()
