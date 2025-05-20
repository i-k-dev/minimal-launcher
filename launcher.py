import tkinter as tk  
from tkinter import filedialog  
import subprocess  

# main window 
root = tk.Tk()  
root.title("launcher")
root.geometry("300x500")  # window size  
root.resizable(False, False)  # no resizing for control purpose

# add to library
def add_game():  
    file_path = filedialog.askopenfilename(title="Select Title", filetypes=[("Executable Files", "*.exe")])  
    if file_path:  
        games_list.insert(tk.END, file_path)  

# launch exe  
def launch_game():  
    selected_game = games_list.get(tk.ACTIVE)  
    if selected_game:  
        subprocess.Popen(selected_game)  

# UI  
add_button = tk.Button(root, text="Add to Library", command=add_game)  
add_button.pack(fill=tk.X, padx=5, pady=5)  # add

remove_button = tk.Button(root, text="Remove from Library", command=remove_game)  
remove_button.pack(fill=tk.X, padx=5, pady=5) # remove 

games_list = tk.Listbox(root)  
games_list.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)  # follow window size  
games_list.bind("<Double-Button-1>", launch_game)  # double click launch

# launch_button = tk.Button(root, text="Play", command=launch_game)  
# launch_button.pack(fill=tk.X, padx=5, pady=5)  

root.mainloop()
