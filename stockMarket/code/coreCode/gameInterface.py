import tkinter as tk

class BasicGUI:
    def __init__(self): # consttruter to create instance of the class
        self.rootWin = tk.Tk()
        self.rootWin.config(background= "Green")
        self.rootWin.title("blue is beautiful")
        self.testButton = tk.Button(self.rootWin)
        self.testButton["text"] = "Quit"
        self.testButton.grid(row=1, column=1)
        self.testButton["command"] = self.testButtonResponse()
        self.testButton["bg"] = "green"

    def run(self):
        self.rootWin.mainloop()
    def testButtonResponse(self):
        print("hello world")
        self.testButton["text"] = "goodbye"

if __name__ == "__main__":
    myGUI = BasicGUI()
    myGUI.run()