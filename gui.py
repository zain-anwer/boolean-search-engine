"""

Prompt for developing GUI (sir said to mention prompts used):

Can you make a simple Tkinter UI that has a search bar for writing queries that it feeds to my search 
function and that takes the result converts to string makes a filepath, with the convention 
data/Trump Speeches/ speech_X.txt and displays it as a link?


"""


import tkinter as tk
from tkinter import messagebox
import os
import webbrowser

# Import your actual search function here!
from src.search import search 

def open_file(filepath):
    """Opens the text file using the OS default application."""
    abs_path = os.path.abspath(filepath)
    if os.path.exists(abs_path):
        # webbrowser handles cross-platform file opening smoothly
        webbrowser.open(f"file://{abs_path}")
    else:
        messagebox.showwarning("File Not Found", f"Could not find:\n{abs_path}")

def perform_search(event=None):
    """Fetches the query, runs the search, and displays the links."""
    query = search_entry.get().strip()
    if not query:
        return

    # 1. Run your search engine
    doc_ids = search(query) 

    # 2. Clear the previous results
    results_box.config(state=tk.NORMAL)
    results_box.delete("1.0", tk.END)

    # 3. Handle Empty Results
    if not doc_ids:
        results_box.insert(tk.END, "No results found for your query.\n")
        results_box.config(state=tk.DISABLED)
        return

    # 4. Display the Links
    results_box.insert(tk.END, f"Found {len(doc_ids)} results:\n\n")
    
    for doc_id in doc_ids:
        # Construct the file path convention
        filepath = f"data/Trump Speeches/speech_{doc_id}.txt"
        
        # Create a unique tag for this specific link
        tag_name = f"link_{doc_id}"
        
        # Insert the text and apply the tag
        results_box.insert(tk.END, filepath + "\n", tag_name)
        
        # Style it like a blue hyperlink
        results_box.tag_config(tag_name, foreground="blue", underline=True)
        
        # Bind mouse clicks and hover effects to this specific tag
        results_box.tag_bind(tag_name, "<Button-1>", lambda event, p=filepath: open_file(p))
        results_box.tag_bind(tag_name, "<Enter>", lambda event: results_box.config(cursor="hand2"))
        results_box.tag_bind(tag_name, "<Leave>", lambda event: results_box.config(cursor=""))

    results_box.config(state=tk.DISABLED) # Lock the text box so user can't type in it

# --- Main UI Setup ---
root = tk.Tk()
root.title("Trump Speeches Search Engine")
root.geometry("500x400")
root.configure(padx=20, pady=20)

# Title Label
title_label = tk.Label(root, text="Search Speeches", font=("Arial", 16, "bold"))
title_label.pack(pady=(0, 10))

# Search Bar Frame
search_frame = tk.Frame(root)
search_frame.pack(fill=tk.X, pady=5)

search_entry = tk.Entry(search_frame, font=("Arial", 12))
search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
search_entry.bind("<Return>", perform_search) # Pressing Enter triggers search

search_button = tk.Button(search_frame, text="Search", command=perform_search, bg="#0078D7", fg="white", font=("Arial", 10, "bold"))
search_button.pack(side=tk.RIGHT)

# Results Box (with Scrollbar)
results_frame = tk.Frame(root)
results_frame.pack(fill=tk.BOTH, expand=True, pady=10)

scrollbar = tk.Scrollbar(results_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

results_box = tk.Text(results_frame, yscrollcommand=scrollbar.set, font=("Consolas", 11), state=tk.DISABLED, bg="#f9f9f9", wrap=tk.WORD)
results_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=results_box.yview)

# Start the application
root.mainloop()