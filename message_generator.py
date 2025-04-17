import tkinter as tk
from tkinter import messagebox
import difflib

# Function to compare the changes (for simplicity, using difflib)
def generate_commit_message(old_text, new_text, extra_info):
    diff = list(difflib.ndiff(old_text.splitlines(), new_text.splitlines()))
    added_lines = [line[2:] for line in diff if line.startswith('+ ')]
    removed_lines = [line[2:] for line in diff if line.startswith('- ')]
    
    # Simple logic to generate commit message
    commit_message = "Update commit: "
    
    if added_lines:
        commit_message += f"Added {len(added_lines)} lines. "
    
    if removed_lines:
        commit_message += f"Removed {len(removed_lines)} lines. "
    
    commit_message += f"Details: {extra_info}"

    return commit_message

# GUI Functionality
def on_generate_click():
    old_text = old_text_area.get("1.0", tk.END).strip()
    new_text = new_text_area.get("1.0", tk.END).strip()
    extra_info = extra_info_entry.get().strip()

    if not old_text or not new_text:
        messagebox.showerror("Error", "Both old and new texts are required!")
        return

    commit_message = generate_commit_message(old_text, new_text, extra_info)

    messagebox.showinfo("Generated Commit Message", commit_message)

# Set up the Tkinter window
root = tk.Tk()
root.title("Commit Message Generator")

# Create Text Boxes for old and new text
tk.Label(root, text="Old Text").pack(padx=10, pady=5)
old_text_area = tk.Text(root, height=8, width=50)
old_text_area.pack(padx=10, pady=5)

tk.Label(root, text="New Text").pack(padx=10, pady=5)
new_text_area = tk.Text(root, height=8, width=50)
new_text_area.pack(padx=10, pady=5)

# Entry for extra information
tk.Label(root, text="Extra Information").pack(padx=10, pady=5)
extra_info_entry = tk.Entry(root, width=50)
extra_info_entry.pack(padx=10, pady=5)

# Generate Commit Button
generate_button = tk.Button(root, text="Generate Commit Message", command=on_generate_click)
generate_button.pack(padx=10, pady=20)

# Start the Tkinter main loop
root.mainloop()
