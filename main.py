from tkinter import *
import random

root = Tk()


selectedDiceSize = IntVar()
selectedDiceSize.set(1)
diceSizeMenu = OptionMenu(root, selectedDiceSize, 1, 2, 3, 4, 5, 6)
diceSizeMenu.pack()

def RollDice():
    diceSize = selectedDiceSize.get()
    rollResult = random.randint(1,diceSize)
    resultText = Label(root, text = rollResult)
    resultText.pack()

poop = Button(root, text = "poop", command = lambda: RollDice())
poop.pack()

root.mainloop()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
