from tkinter import *

root = Tk()
root.title("Force Quit Apps By SmashedFrenzy16")

label = Label(root, text="Force Quit Apps By @SmashedFrenzy16", font=("Arial", 24))
label.pack()

blank_label = Label(root, text="")
blank_label.pack()

app_entry = Entry(root, width=100, borderwidth=5)
app_entry.pack()

app_entry.insert(0, "Enter the name of the app you want to force quit")

root.mainloop()
