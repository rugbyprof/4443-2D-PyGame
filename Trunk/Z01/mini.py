import tkinter as tk

# GUI window is a subclass of the basic tkinter Frame object
class HelloWorldFrame(tk.Frame):
    def __init__(self, master,name):
        # Call superclass constructor
        tk.Frame.__init__(self, master)
        # Place frame into main window
        self.grid()
        # Create text box with "Hello World" text
        # hello = tk.Label(self, text=f"Hello World! My name is {name}!")
        # # Place text box into frame
        # hello.grid(row=2, column=0)

        wlabels = []
        for i in range(10):
            wlabels.append(tk.Label(self, text=" "*100))
            wlabels[i].grid(row=i,column=0)


# Spawn window
if __name__ == "__main__":
    # Create main window object
    root = tk.Tk()
    # Set title of window
    root.title("Player: spetsnaz983")
    # Instantiate HelloWorldFrame object
    hello_frame = HelloWorldFrame(root,"Harry Tesla")
    # Start GUI
    hello_frame.mainloop()