import tkinter as tk   
import subprocess  
import os
from tkinter import filedialog 
from tkinter import simpledialog
# import webbrowser # for about me


# main window 
root = tk.Tk()  
root.title("launcher")
root.geometry("300x500")  # window size  
root.resizable(False, False)  # no resizing for control purpose
root.attributes("-toolwindow", True) # hides maximize button
# root.grid_rowconfigure(1, weight=1)
# root.grid_columnconfigure(0, weight=1)


###

game_paths = {} # path dictionary

# add to library
def add_game():  
    file_path = filedialog.askopenfilename(title="Select Title", filetypes=[("Executable Files", "*.exe")])  
    if file_path:  
        game_name = os.path.basename(file_path) # program.exe instead of full path
        game_name = os.path.splitext(game_name)[0]  # remove .exe on display
        game_paths[game_name] = file_path # actuall full path
        # dictionary sort
        sorted_games = dict(sorted(game_paths.items()))
        # clear list
        games_list.delete(0, tk.END)
        # sort alphbetically
        for game in sorted_games.keys():
            games_list.insert(tk.END, game)
        game_paths.clear()
        game_paths.update(sorted_games)

# launch exe  
def launch_game(event=None):  
    selected_game = games_list.get(tk.ACTIVE)  
    if selected_game:  
        game_path = game_paths.get(selected_game) #get full path
        if game_path and os.path.exists(game_path): #check if exist
            subprocess.Popen(game_path)
    else:
        print("Error! Title not found.") #debug

# # rename exe
# def rename_game():
#     """ Rename. """
#     selected_index = games_list.curselection()
#     if selected_index:
#         old_name = games_list.get(selected_index)
#         new_name = simpledialog.askstring("Rename", "Enter new name:")
#         if new_name:
#             # Update dictionary
#             game_paths[new_name] = game_paths.pop(old_name)  # rename inside dictionary
#             # sort alphbeatically
#             sorted_games = dict(sorted(game_paths.items()))
#             # refresh database
#             games_list.delete(0, tk.END)
#             for game in sorted_games.keys():
#                 games_list.insert(tk.END, game)
#             # checks dictionary
#             game_paths.clear()
#             game_paths.update(sorted_games)


def start_inline_rename():
    """ Start inline renaming after right-clicking 'Rename'. """
    selected_index = games_list.curselection()
    if not selected_index:
        return  # No selection, do nothing

    selected_index = selected_index[0]
    old_name = games_list.get(selected_index)

    # Create an entry widget over the selected item
    entry = tk.Entry(games_list)
    entry.insert(0, old_name)  # Pre-fill with current name
    entry.select_range(0, tk.END)  # Highlight text for easy editing
    entry.place(x=5, y=selected_index * 20, width=150)  # Position in Listbox

    # Confirm rename when Enter is pressed
    def confirm_rename(event):
        new_name = entry.get()
        if new_name and new_name != old_name:
            game_paths[new_name] = game_paths.pop(old_name)  # Update dictionary
            refresh_list()  # Refresh listbox to reflect new name
        entry.destroy()  # Remove entry box after renaming

    entry.bind("<Return>", confirm_rename)  # Enter key confirms rename
    entry.focus()  # Auto-focus the entry widget

def refresh_list():
    """ Refresh listbox to maintain alphabetical order. """
    sorted_games = sorted(game_paths.keys())  # Sort stored games alphabetically
    games_list.delete(0, tk.END)  # Clear listbox
    for game in sorted_games:
        games_list.insert(tk.END, game)  # Re-add sorted games


# remove from libraary 
def remove_game():  
    selected_index = games_list.curselection()  
    if selected_index:  
        game_name = games_list.get(selected_index)
        games_list.delete(selected_index)  
        game_paths.pop(game_name, None)  # Remove from stored paths

# right context menu
context_menu = tk.Menu(root, tearoff=0)
context_menu.add_command(label="Run", command=launch_game)
# context_menu.add_command(label="Rename", command=rename_game)
context_menu.add_command(label="Rename", command=start_inline_rename)  # right-click → Rename
context_menu.add_command(label="Remove", command=remove_game)


def show_context_menu(event):
    """ Show right-click menu. """
    selected_index = games_list.nearest(event.y)  # Get the nearest item
    games_list.selection_clear(0, tk.END)
    games_list.selection_set(selected_index)

    context_menu.post(event.x_root, event.y_root)  # Show at mouse position





# menu bar
    ## Function = Exit
def exit_program():
    root.quit()
    ## Function = About

    ### About v1
# def open_about():
#     print("WIP 2025") #placeholder for reference
    ### About v2
# def open_about():
#     about_window = tk.Toplevel(root)

#     about_window.title("About")
#     about_window.geometry("250x180")


#     about_label = tk.Label(
#         about_window,
#         text="wip2025\nVersion 0.13\nfor future reference",
#         justify="center",
#         padx=10, pady=10
#     )
#     about_label.pack()

    ### About v3
# about_frame = tk.Frame(root, bg="lightgray", relief="raised", borderwidth=2)
# about_label = tk.Label(about_frame, text="wip2025\nVersion 0.13\nfor future reference", justify="center")
# about_label.grid(row=0, column=0, padx=10, pady=5)

# def toggle_about():
#     global about_frame
#     if about_frame.winfo_ismapped():
#         about_frame.grid_forget()
#     else:
#         # about_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")  # dropdown?
#         about_frame.place(x=10, y=30, width=280, height=100)  # Show popup manually
#     root.grid_rowconfigure(1, weight=1)
#     root.grid_columnconfigure(0, weight=1)

#     ## Function = Link
#     def open_github():
#         webbrowser.open("https://github.com/i-k-dev")  # hi
    
#         github_button = tk.Button(about_frame, text="GitHub", command=open_github, fg="blue", cursor="hand2")
#         github_button.grid(row=1, column=0, pady=5)


menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)  # "File" menu
menu_bar.add_cascade(label="File", menu=file_menu)  # Add "File" dropdown to menu bar
    # Add menu options
file_menu.add_command(label="Add Program", command=add_game)
# file_menu.add_command(label="About", command=toggle_about)

file_menu.add_separator()  # Adds a separator before Exit
file_menu.add_command(label="Exit", command=exit_program)

    # Attach menu bar to window
root.config(menu=menu_bar)





# UI  

# button frame _new_ 
button_frame = tk.Frame(root)  # Define button_frame before using it
button_frame.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

button_frame.grid_columnconfigure(0, weight=1)
button_frame.grid_columnconfigure(1, weight=0)


# # add button
# add_button = tk.Button(root, text="Add to Library", command=add_game, width=15)  
# add_button.grid(row=0, column=0, padx=10, pady=10, sticky="w")  #aligned-left
# # remove button
# remove_button = tk.Button(button_frame, text="❌", command=remove_game, width=3)
# remove_button.grid(row=0, column=1, padx=10, pady=10, sticky="e")  #aligned-right

#library
games_list = tk.Listbox(root)  
# games_list.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)  # follow window size
games_list.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)  #fill-space
games_list.bind("<Double-Button-1>", launch_game)  # double click launch

#library-fill-space 
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)


# launch_button = tk.Button(root, text="Play", command=launch_game)  
# launch_button.pack(fill=tk.X, padx=5, pady=5)  


# Bind right-click to show context menu
games_list.bind("<Button-3>", show_context_menu)  # Works on Windows/Linux
games_list.bind("<Button-2>", show_context_menu)  # Works on macOS


root.mainloop()
