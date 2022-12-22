from tkinter import *
import random

root = Tk()
def RollDice():
    global rollResult
    rollResult = random.randint(1,6)
    resultText = Label(root, text = rollResult)
    resultText.pack()

poop = Button(root, text = "poop", command = RollDice)
poop.pack()

root.mainloop()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
