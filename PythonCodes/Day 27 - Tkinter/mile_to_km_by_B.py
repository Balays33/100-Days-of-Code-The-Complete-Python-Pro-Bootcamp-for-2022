from tkinter import *

window = Tk()
window.title("Balazs")
window.minsize(width=300, height=300)

# window.maxsize(width=900, height=400)
def action():
    km = round(int(input.get())*1.60934)
    print(km)
    label4.config(text=km)


input = Entry()
input.grid(row = 0, column = 1)
label = Label(text="Miles")
label.grid(row = 0, column = 2, padx = 20, pady = 20)

label2 = Label(text="is equal to")
label2.grid(row = 1, column = 0)

label4 = Label(text="0")
label4.grid(row = 1, column = 1)

label3 = Label(text="KM")
label3.grid(row = 1, column = 2)

Cal_button = Button(text = "Calculate", command=action)
Cal_button.grid(row = 3, column = 1)



window.mainloop()