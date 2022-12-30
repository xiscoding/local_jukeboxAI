import tkinter as tk
from tkinter import filedialog
import os
import re
#INITIAL AUDIO DIRECTORY
INITIAL_DIR = 'THIS SHOULD BE THE PATH TO THE FOLDER CONTAINING THE AUDIO SAMPLES YOU WOULD LIKE TO USE'

class FileSelectionDialog:
  def __init__(self):
    parent = tk.Tk()
    # Get the screen width and height
    screen_width = parent.winfo_screenwidth()
    screen_height = parent.winfo_screenheight()

    # Calculate the center of the screen
    window_width = 500
    window_height = 200
    x_coordinate = (screen_width / 2) - (window_width / 2)
    y_coordinate = (screen_height / 2) - (window_height / 2)

    # Set the size and position of the window
    parent.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")
    # Create the UI elements
    self.button = tk.Button(parent, text="Select Files", command=self.select_files)
    self.label = tk.Label(parent, text="")
    # Button for closing
    self.exit_button = tk.Button(parent, text="Exit", command=parent.destroy)
    # Pack the UI elements
    self.button.pack()
    self.label.pack()
    self.exit_button.pack()
    parent.mainloop()

  def select_files(self):
    # Open the file selection dialog and get the selected files
    selected_files = filedialog.askopenfilenames(initialdir=INITIAL_DIR, title='Select files')
    # Extract the file names from the file paths and join them with newlines
    file_names=[]
    #NOTE: REPLACE/LAMBDA
    #https://stackoverflow.com/questions/6116978/how-to-replace-multiple-substrings-of-a-string/58814507#58814507
    #https://stackoverflow.com/questions/59072514/efficiently-make-many-multiple-substitutions-in-a-string/59072515#59072515
    mrep = lambda s, d: s if not d else mrep(s.replace(*d.popitem()), d)
    for file in selected_files:
        # os.rename(INITIAL_DIR+(os.path.basename(file)), INITIAL_DIR+(os.path.basename(file).replace(" ", "").replace("(FREE)", "")))
        os.rename(INITIAL_DIR+(os.path.basename(file)), INITIAL_DIR+(mrep(os.path.basename(file), {' ': '', '(': '', ')':'', '[':'', ']':'', '{':'', '}':''})))
        file_names.append(mrep(INITIAL_DIR+os.path.basename(file), {' ': '', '(': '', ')':'', '[':'', ']':'', '{':'', '}':''}))
    # file_names = [os.path.basename(file).replace(" ", "") for file in selected_files]
    self.file_names_string = ','.join(file_names)  # Save the file names string in an instance variable
    # Display the file names in the label
    self.label.config(text=self.file_names_string)

  def get_file_names_string(self):
    # Return the file names string
    return self.file_names_string

if __name__ == '__main__':
    dialog = FileSelectionDialog()
    print(dialog.get_file_names_string())
