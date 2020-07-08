## Assignment 4 - Simple Second Program
#### Due: 07-09-2020 (Thursday @ 12:30 p.m.)

### Overview

We are going to incorporate the concept of "command line parameters" feeding configuration information into a program. This seemingly doesn't relate to gaming but it does. Think of a multiplayer game, or a game that has leader-boards. When a game instance starts, it needs specific player information depending on the game. We are going to do just that using our simple (non game like) window from the previous assignment.

The example below shows the output from the original example.

<img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/hello3_tkinter.png" width="200">

What we want to do is send in some configuration information from the command line. But beyond that, I want you to read your information in from an external file. That file will be formatted as json (Javascript Object Notation) which is a textual format that can be parsed into a python data structure (aka Dictionary). The json library will handle all of the heavy lifting for you. Here is an example json object containing the necessary information:

#### Player Info

```json
{
    "fname":"Sasha",
    "lname":"Ivanov",
    "rank": 15339,
    "screen_name":"spetsnaz983",
    "email":"sashaivanov1998@gru.gov",
    "power-boost":98.34,
    "available-boosts": ["skull-crush","flower-child","acid-trip","disco-ball"]
}
```

We don't need to get into window placement to deep right now. But the snippet below basically says to place some text on `row 0 column 0`.

```python
    hello = tk.Label(self, text=f"Hello World! My name is {name}!")
    hello.grid(row=0, column=0)
```

And adding another `tk.label`

```python
    hello = tk.Label(self, text=f"Hello World! My name is {name}!")
    hello.grid(row=0, column=0)
    hello1 = tk.Label(self, text=f"Hello World! My name is {name}!")
    hello1.grid(row=1, column=50)
```

we can get:

<img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/hellox3_tkinter.png" width="400">

This is pretty basic stuff :)

### Requirements

- Alter the "Original Window Code" so that it uses a command line parameter to pass in a json file name to be read.
- The json file will contain necessary player info.
- Parse the json file into a python dictionary.
- Traverse the dictionary printing the specifics of your player data onto the tkinter window in an organized fashion similar to the example below.
- Make sure you change json information to someone else. Humor is appreciated.
- You can change any and all fields as long as you have a similar amount of data AND you keep at least one of the keys pointing to a list of items.
- Add code to "Original Window Code" so that you traverse the dictionary with a loop construct examining each and every data element in the dictionary.
- Pulling individual items out with hard coded keys is not ok.

<img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/player_tkinter_json.png" width="400">

### Original Window Code

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

- Create a folder called `A04` in your `Assignments` folder.
- Add a file to your folder called `main.py` with the above code.
- Include your `player-info.json` file in this folder (or whatever you named it).
- Include a shot of the output window your program creates. Please don't screen shot your whole desktop with our output as a tiny little window on it.
- Add a `README.md` file to your `A04` folder with instructions on how to run your program guided by [R03](../../Resources/R03/README.md)


## Pseudo Rubric

- Does the program run?
- Does it print out all of the information on the GUI window?
- Is the information neatly presented in an organized way?
- Did the program traverse the dictionary using a for loop printing each data field from within the loop?
- Did the program have issues traversing the dictionary when processing the list element?