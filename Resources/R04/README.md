## Pygame - Part 1: The Basics
#### NA

## Overview


#### [Lesson 001](001_pyglesson.py)

- http://www.poketcode.com/en/pygame/windows/index.html

In pygame, everything is viewed on a single user-created display, which can be a static window, resizable window,  or full screen.

- `pygame.display.set_mode((400, 400))`
- `pygame.display.set_mode((400, 400), pygame.RESIZABLE)`
- `pygame.display.set_mode((800, 600), pygame.FULLSCREEN)`

#### [Lesson 002](002_pyglesson.py)

- http://www.poketcode.com/en/pygame/windows/index.html#window_icon

```python
# sets the icon path
icon_path = os.path.join(u'images', u'icon_32.png')

# loads the icon
icon = pygame.image.load(icon_path)

# sets the window icon
pygame.display.set_icon(icon)
```

You can change the icon of the running process. In windows it should add the icon to the game window. In OSX it changes the icon that shows up on computers "Dock".

#### [Lesson 003](003_pyglesson.py)

- http://www.poketcode.com/en/pygame/surfaces/index.html

A pygame [Surface](https://www.pygame.org/docs/ref/surface.html) can be thought of as a window in which things are placed for display. You can have multiple surfaces in the same game window or it can be one surface for the entire window. To display anything, it has to be put onto a surface and then the surface is told to `blit` at some interval.

>To "blit" is to copy bits from one part of a computer's graphical memory to another part. This technique deals directly with the pixels of an image, and draws them directly to the screen, which makes it a very fast rendering technique that's often perfect for fast-paced 2D action games.<sup>[REF](https://gamedevelopment.tutsplus.com/articles/gamedev-glossary-what-is-blitting--gamedev-2247#:~:text=To%20%22blit%22%20is%20to%20copy,fast%2Dpaced%202D%20action%20games.)</sup>

Once a surface has called its `blit` method to change the pixels of whatever game construct needs changing, it still needs to be drawn to the actual display. For this we can use:

- `pygame.display.flip()`
- `pygame.display.update()`
- [Good Stackoverflow about them both] (https://stackoverflow.com/questions/29314987/difference-between-pygame-display-update-and-pygame-display-flip)

We can use multiple surfaces and clipping to be very specific about which portions of the screen get updated . This allows us to be a little more efficient. However, for now we will start using one surface at a time.



- `screen.fill(color)` (osx doesn't work without a surface defined)






### Images and Rects

Your basic pygame program drew a shape directly onto the display’s Surface, but you can also work with images on the disk. The image module allows you to load and save images in a variety of popular formats. Images are loaded into Surface objects, which can then be manipulated and displayed in numerous ways.

As mentioned above, Surface objects are represented by rectangles, as are many other objects in pygame, such as images and windows. Rectangles are so heavily used that there is a special Rect class just to handle them. You’ll be using Rect objects and images in your game to draw players and enemies, and to manage collisions between them.

Sources:

http://www.poketcode.com/en/pygame/index.html
https://realpython.com/pygame-a-primer/#collision-detection