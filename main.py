from tkinter import *
from tkinter import filedialog
from tkinter import font

window = Tk()
window.title("WriteRoom Clone")
window.geometry("1000x1000")

# Frame
my_frame = Frame(window)
my_frame.pack(pady=5)

# Scroll Bar for text box
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Text box
my_text = Text(my_frame, width=100, height=95, font=("Courier New", 16), foreground="light green",
               selectbackground="light green", selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
my_text.pack()

#Configure Scroll bar
text_scroll.config(command=my_text.yview)

# Create menu
menu_bar = Menu(window)
window.config(menu=menu_bar)

# Add file menu
file_menu = Menu(menu_bar, tearoff=False)
file_menu.add_cascade(label="File", menu=menu_bar)

# file_menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_command(label="Save AS")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)
#
# # Add edit menu
# edit_menu = Menu(my_menu)
# edit_menu.add_cascade(label="Edit", menu=edit_menu)
# edit_menu.add_command(label="Undo")
# edit_menu.add_command(label="Redo")
# edit_menu.add_separator()
# edit_menu.add_command(label="Cut")
# edit_menu.add_command(label="Copy")
# edit_menu.add_command(label="Paste")

window.mainloop()
