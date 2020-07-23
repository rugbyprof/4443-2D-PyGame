## Project 1.3 - CovidZAR Camera View
#### Due: 07-26-2020 (Sunday @ 12:30 p.m.)

## Overview of Part 3

This part of the assignment is to incorporate your own sprite animation and create an effect that is triggered when your player hits the wall (see last assignment). I don't care what the effect is, but it must have multiple frames that are shown in succession using the blit function.


<img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/game_camera_view_example2.png" width="300">


When in actuality the window (camera view) is moving all over the game "world" but only displaying a small portion at a time.

|                                                                                                  |                                                                                                  |                                                                                                  |
| :----------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------: |
| <img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/game_window_101.png" width="200"> | <img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/game_window_102.png" width="200"> | <img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/game_window_103.png" width="200"> |

This means we can have a game that has a world that is many times bigger than the view port. Both of my examples are probably a little disproportionate but I hope you get the idea. What I want you to do for the version is to create a world that is approximately 3-5 times bigger than your game window, and allow a player to move around to the extremes of the world. If you don't load a background image that has "texture" (lines at least or squares something visual) than you will not be able to tell that you are moving. Don't use the same texture I used in the example code, try and find your own. The player should be able to move to the borders of the world and be stopped. I know that we can "wrap" around (e.g. if location greater than width, location = 0) but I don't want you to do that right now. Its more difficult to stop a sprite with good collision detection and not get stuck on the edge of the screen (or world).


### Player Location In Window

The player location in the window varies depending on the type of scrolling game. Some side scrollers let you move left and right over the entire y-length of the window. Some scrollers will let the player move around a window in both the x and the y for a certain distance, before the window starts moving (sliding) in the direction the player is going.

Our scroller will keep the player in the center of the screen until the "window" reaches the edge of the "world" and then the player will be able to approach the edge of the window which in this case is now the edge of the world.

### Edge of World
|                                                                                                  |                                                                                                  |                                                                                                  |
| :----------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------: |
| <img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/window_movement_001.png" width="300"> | <img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/window_movement_002.png" width="300"> | <img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/window_movement_003.png" width="300"> |
| Player in center.  | Window reaches edge of world, player moves toward wall. | Visual alert at wall.


### Requirements
- Your game will be configured by command line parameters (always!).
  - `width`: Window width
  - `height`: Window height
  - `startx`: Starting X coord of player ( -1 could mean random)
  - `starty`: Starting Y coord of player ( -1 could mean random)
  - `title`: Game Title
  - `background_image`: Background image / texture.
  - `player_image`: Path to your player sprite.
  - Example command: `python basic.py title="Move My Player" player_image=./images/player.png width=640 height=480 startX=100, starty=100 background_image=./media/mybackground.png`
- You should be able to move your player within the game window using `either` the keyboard OR the mouse (don't have to do both).
- Player stays centered in window until window hits edge of world, then player can move towards wall.
- When a player touches one of the world boundaries (top bottom left right) you should print a visual alert. See above. You can make it your own design, but something that shows WALL!
- Again, your README will explain to us how to run your game from the command line.


### Helper Code

- [P01-009_scrolling_background_any.py](../../Resources/R04/P01_ProjectStarter/P01-009_scrolling_background_any.py)
- This moves the player around with a scrolling background, but does not implement world boundaries.
- It also uses the mouse or the keyboard, so you can keep both or remove one or the other if you wish to.


## Deliverables

- Create a folder called `P01.2` in your `Assignments` folder.
- Add a file to your folder called `game_pt2.py` with the above code.
- Screen Shots
  - Run your game with a minimum of 4 screen sizes. They can be divisible by some value (like 100) to make the math easier.
  - Include 3 screen shots with your player touching a unique boundary (top,bottom,left,right) to show your wall warning.
  - Include 1 screen shot showing your player in a corner (touching 2 walls).
  - Out of 4 screen shots, use at least 2 different size game windows (the width and height when starting the game).
  - Link to the four screen shots in your readme. Here is how to link to a file.
    - Upload the image to your repo folder. Lets say its called `screen_shot1.png`.
    - Link to it the markdwown way: `![alt text](screen_shot1.png)`. This works, but will not let you size the image.
    - Link to it the html way: `<img src="screen_shot1.png" width="300">`. This also works AND will let you pick the size.
- Add a `README.md` file to your `P01.1` folder with instructions on how to run your program guided by [R03](../../Resources/R03/README.md)


## Pseudo Rubric

- Does the program run?
- Does the floor scroll realistically when player moves?
- Does the player stay near the center while moving?
- Does the player approach the wall when the window gets to the edge of the world.
- Does a visual alert show when player hits wall?
- Does two alerts show in a corner?
- Is your code commented? (Letter Grade)


