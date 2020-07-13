import tkinter as tk
from tkinter import font


# GUI window is a subclass of the basic tkinter Frame object
class HelloWorldFrame(tk.Frame):
    def __init__(self, master,data_dict):

        # Prints all available fonts to stdout
        print(font.families())

        # Choose your font
        appfont = font.Font(family='Courier New', size=12, weight='bold')

        # Call superclass constructor
        tk.Frame.__init__(self, master)

        # Place frame into main window
        self.grid()


        row = 0
        for key,val in data_dict.items():
            left = tk.Label(self, text=key,font=appfont)
            mid = tk.Label(self, text=":",font=appfont)
            right = tk.Label(self, text=val,font=appfont)
            # sticky=tk.W means stick to the west
            left.grid(row=row,column=0,sticky=tk.W)
            mid.grid(row=row,column=1)
            right.grid(row=row,column=2,sticky=tk.W)
            row += 1


# Spawn window
if __name__ == "__main__":
    d = {
        "fname":"Sasha",
        "lname":"Ivanov",
        "rank": 15339,
        "screen_name":"spetsnaz983",
        "email":"sashaivanov1998@gru.gov",
        "power-boost":98.34
        #"available-boosts": ["skull-crush","flower-child","acid-trip","disco-ball"]
    }
    # Create main window object
    root = tk.Tk()
    # Set title of window
    root.title(d['screen_name'])
    # Instantiate HelloWorldFrame object
    hello_frame = HelloWorldFrame(root,d)
    # Start GUI
    hello_frame.mainloop()