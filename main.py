from tkinter import *
import random

root = Tk()
root.geometry("800x600")

diceSizeEntry = Entry(root, width = 20)
diceSizeEntry.pack()

def RollDice():
    diceSize = int(diceSizeEntry.get())
    rollResult = str(random.randint(1,diceSize))
    historyList.append(rollResult)
    historyListVar.set(historyList)

rollDice = Button(root, text = "Roll the dice!", command = lambda: RollDice())
rollDice.pack()

clearHistory = Button(root, text = "Clear the history!",)
clearHistory.pack()

historyLabel = Label(root, text = "History:").pack()

historyList = []
historyListVar = StringVar(value=historyList)
rollHistory = Listbox(root, listvariable = historyListVar).pack()

root.mainloop()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
