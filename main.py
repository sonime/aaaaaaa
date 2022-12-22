from tkinter import *
import random

root = Tk()


selectedDiceSize = IntVar()
diceSizeMenu = OptionMenu(root, selectedDiceSize, 1, 2, 3, 4, 5, 6)
diceSizeMenu.pack()

global diceSize
diceSize = selectedDiceSize.get()
def RollDice():
    rollResult = random.randint(1,diceSize)
    resultText = Label(root, text = rollResult)
    resultText.pack()

poop = Button(root, text = "poop", command = lambda: RollDice())
poop.pack()

root.mainloop()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
