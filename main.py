import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Demo')
window.geometry("350x150")

# title
title_label = ttk.Label(master = window, text = 'Miles to kilometers', font = 'Calibri 24 bold')
title_label.pack()

# input field
input_frame = ttk.Frame(master = window)
entry = ttk.Entry(master = input_frame)
button = ttk.Button(master = input_frame, text = 'Convert')
entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
input_frame.pack(pady = 10)
# pack places thing under the previous pack. Unless specified
# entry and button are placed inside frame through master and the frame is under label

# output
output_label = ttk.Label(master = window, text = 'Output', )
output_label.pack()

# run
window.mainloop()
