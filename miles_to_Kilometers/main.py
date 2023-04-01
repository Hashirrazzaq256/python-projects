from tkinter import *


def converter():
    miles = float(miles_input.get())
    km = miles*1.6
    kilometer_result.config(text=int(km))
    
    
windows = Tk()
windows.title("Mile to Kilometer")
windows.config(padx=20, pady=20)


miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

text_label = Label(text="is equal to")
text_label.grid(column=0, row=1)

kilometer_result = Label(text="0")
kilometer_result.grid(column=1, row=1)

kilometer_label = Label(text="KM")
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text="calculate", command=converter)
calculate_button.grid(column=1, row=2)


windows.mainloop()
