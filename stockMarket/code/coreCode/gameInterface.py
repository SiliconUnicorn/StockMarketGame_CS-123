import tkinter as tk

class BasicGUI:
    def __init__(self): # consttruter to create instance of the class
        self.rootWin = tk.Tk()
        self.rootWin.config(background= "white")
        self.rootWin.title("blue is beautiful")
        self.testButton = tk.Button(self.rootWin)
        self.testButton["text"] = "Quit"
        self.testButton.grid(row=5, column=5)
        self.testButton["command"] = self.testButtonResponse()
        self.testButton["bg"] = "cyan"

    def run(self):
        self.rootWin.mainloop()
    def testButtonResponse(self):
        self.testButton["text"] = "Start"

if __name__ == "__main__":
    myGUI = BasicGUI()
    myGUI.run()