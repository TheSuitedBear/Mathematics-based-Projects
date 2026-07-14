# Prime Factorization.

# tkinter is used for the UI, I know it's limited but for this it works.
import tkinter

# Function which takes the input in the entry box, and calculates the prime factors of the number.
def ButtonPress():
    number = entrybox.get()
    if not number.isdigit() or int(number) < 2:
        resultlabel.config(text="Please enter a valid integer greater than 1.")
        return

    number = int(number)
    factors = []
    divisor = 2

    while number > 1:
        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        divisor += 1

    resultlabel.config(text="Prime factors: " + " x ".join(map(str, factors)))

# Creates the main window.
window = tkinter.Tk()
window.title("Prime Factorization")
window.geometry("400x300")
window.configure(background="lightblue")

# UI elements. I feel like this could be condensed somehow?
firstlabel = tkinter.Label(window, text = "Please enter a number to factor:", font = ("Arial", 12), bg = "lightblue")
firstlabel.pack()
entrybox = tkinter.Entry(window, font = ("Arial", 12), bg = "white")
entrybox.pack()
submitbutton = tkinter.Button(window, text = "Submit", font = ("Arial", 12), bg = "lightgreen", command = lambda: ButtonPress())
submitbutton.pack()
resultlabel = tkinter.Label(window, text = "", font = ("Arial", 12), bg = "lightblue")
resultlabel.pack()

# Whenever I test Tkinter stuff I forget to add this line lmao.
window.mainloop()