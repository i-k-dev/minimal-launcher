import tkinter as tk  
from tkinter import filedialog  
import subprocess  
game_paths = {} # path dictionary

# main window 
root = tk.Tk()  
root.title("launcher")
root.geometry("300x500")  # window size  
root.resizable(False, False)  # no resizing for control purpose

import os # import os file path

# add to library
def add_game():  
    file_path = filedialog.askopenfilename(title="Select Title", filetypes=[("Executable Files", "*.exe")])  
    if file_path:  
        game_name = os.path.basename(file_path) # program.exe instead of full path
        games_list.insert(tk.END, game_name) 
        game_paths[game_name] = file_path # actuall full path

# remove from libraary 
def remove_game():  
    selected_index = games_list.curselection()  
    if selected_index:  
        games_list.delete(selected_index)  

# launch exe  
def launch_game(event=None):  
    selected_game = games_list.get(tk.ACTIVE)  
    if selected_game:  
        game_path = game_paths.get(selected_game) #get full path
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
