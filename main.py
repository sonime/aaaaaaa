from tkinter import *
import random

root = Tk()
root.geometry("800x600")

diceSizeEntry = Entry(root, width = 20)#declares the entry for die size
diceSizeEntry.pack()

def RollDice():#function for actually rolling the dice
    diceSize = int(diceSizeEntry.get())#gets the value from entry form
    rollResult = str(random.randint(1,diceSize))#rolls the die and converts to string
    historyList.append(rollResult)#adds the result to the list
    historyListVar.set(historyList)#updates the history box

def clearHistory():#function for clearing history
    historyList.clear()#wipes the list clean
    historyListVar.set(historyList)#updates the list to be clear

rollDice = Button(root, text = "Roll the dice!", command = lambda: RollDice())#click to call the dice roller function
rollDice.pack()

clearHistory = Button(root, text = "Clear the history!", command = clearHistory)#clears the history
clearHistory.pack()

historyLabel = Label(root, text = "History:").pack()


historyList = []#declares history list, empty
historyListVar = StringVar(value = historyList)#declares the variable that actually goes in the box
rollHistory = Listbox(root, yscrollcommand = true, listvariable = historyListVar).pack()#creates the history box

root.mainloop()#DO NOT REMOVE
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
