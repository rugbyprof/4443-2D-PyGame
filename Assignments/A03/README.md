## Assignment 3 - Dev Setup and First Program
#### Due: 07-08-2020 (Wednesday @ 12:30 p.m.)

## Getting Dev Environment Setup

This will be different for most individuals with some common overlap. But it does seem that there are always outlying issues that you are going to have to deal with on your own. I have listed a few resources below to assist you getting Python and PyGame set up on your computer. You need to do this as quickly as possible so we can start coding, but mostly to handle any issues that will pop up for at least a few of you.

If it makes any difference to you, I will be using VsCode. I tried PyCharm and Spyder and liked them both, but I like the customize-ability (is that a word?) of VsCode with all of its 3rd party plugins. I will not force anyone to use my dev setup, by I would encourage you to (if your on windows) at least get WSL up and working (this is a linux command line system windows now supports that is NOT the old DOS window. It's real linux!) I have a link to a tutorial below.

But also be warned, I will not be a lot of help if you use Spyder or PyCharm and you are having problems with the IDE. I will obviously help debug code, but configuring paths and libraries for those other 2 IDE's will be on you guys. Having said that. I think its very straightforward and simple.

### Python Editors
- PyCharm
  - https://www.jetbrains.com/pycharm/
- VSCode
  - https://code.visualstudio.com/

### Windows Setup
- Installing Python and PyGame on Windows 10
  - https://www.youtube.com/watch?v=EKjALzLLgVs
- PyGame Install Wiki
  - https://www.pygame.org/wiki/GettingStarted
- Python development on Windows using terminal
  - https://pbpython.com/wsl-python.html
- Windows WSL terminal video
  - https://www.youtube.com/watch?v=A0eqZujVfYU
- Python and WSL in windows
  - https://www.youtube.com/watch?v=y3TquoKDTPs

### Mac Setup
- Install Python 3
  - https://opensource.com/article/19/5/python-3-default-mac#what-to-do
- Install PyGame
  - https://www.pygame.org/wiki/GettingStarted

### Linux Setup
- If your on linux, you can probably figure this part out :)
- https://www.pygame.org/wiki/GettingStarted


## Minimum Tkinter Program

- Get the code below to run on your home system.
- You don't have to code at all. Simply cut and paste into a file and run it in whatever editor or environment you have chosen.
- I would like you to change "Terry Griffin" to whatever your name is :)
- The first couple days of class will be a python crash course. Then this code will make sense!

### Program Description

This small Tkinter program simply creates a very small Tkinter gui window that is populated
by the name passed to the HelloWorld class as a parameter. The window is populated with text
that says: "Hello World! My name is _______________"


### Program Code

```python
import tkinter as tk

# GUI window is a subclass of the basic tkinter Frame object
class HelloWorldFrame(tk.Frame):
    def __init__(self, master,name):
        # Call superclass constructor
        tk.Frame.__init__(self, master)
        # Place frame into main window
        self.grid()
        # Create text box with "Hello World" text
        hello = tk.Label(self, text=f"Hello World! My name is {name}!")
        # Place text box into frame
        hello.grid(row=0, column=0)

# Spawn window
if __name__ == "__main__":
    # Create main window object
    root = tk.Tk()
    # Set title of window
    root.title("Hello World!")
    # Instantiate HelloWorldFrame object
    hello_frame = HelloWorldFrame(root,"Nikola Tesla")
    # Start GUI
    hello_frame.mainloop()

```

## Deliverables

- Create a folder called `A03` in your `Assignments` folder.
- Add a file to your folder called `main.py` with the above code.
- Add a `README.md` file in your `A03` folder with instructions on how to run your program as dictated in [A02](../A02/README.md).
- Instructions are ALWAYS how to run your code from a command line, and NEVER: "hit the play button on your editor".
  - For this program it should be as simple as: `python main.py`
- I realize this is your first assignment and you don't have tons of instructions or requirements to be communicated, but follow the guidelines from [A02](../A02/README.md) as close as possible when creating your README.md.
