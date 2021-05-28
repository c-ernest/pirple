import tkinter as tk

class Assignment(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.welcome = tk.Button(self)
        self.welcome["text"] = "A simple way to\nto use tkinker library\n(click me)"
        self.welcome["command"] = self.respond
        self.welcome.pack(side = "top")

        self.quit = tk.Button(self, text = "Quit", fg = "red", command = self.master.destroy)
        self.quit.pack(side = "bottom")

    def respond(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Assignment(master = root)
app.mainloop()