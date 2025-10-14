import tkinter as tk
window=tk.Tk()

for i in range(3):
    for j in range(3):
        frame = tk. Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1)

        frame.grid(row=0, column=0, padx=5, pady=S)

        label = tk.Label(master=frame, text = f"Row {i}\nColumn {5}")
        label.pack()

window.mainloop()
