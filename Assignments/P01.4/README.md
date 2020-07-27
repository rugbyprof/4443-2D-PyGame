## Project 1.4 - CovidZAR Shooting & Sound
#### Due: 07-29-2020 (Wednesday @ 12:30 p.m.)

## Overview of Part 4

### Helper Code

- [Help Files](../../Resources/RP01/P01.4/README.md)

### Overview

Add a directed projectile to be used as a bullet. What does that mean? Look at the image below:

<img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/bullets_directed.png">

If you were to use this as a projectile, you would need to orient the image to be facing the correct direction. You would also need to run through the animation (once) as it flys toward the target. If it were to fly a long direction, you could start with the frame on the far right, and when it got to the last frame (far left) you could alternate between the last two frames to keep up appearances of being "alive".

- To orient the sprite correctly:
  - we need to calculate the angle between the player and the target
  - then we need to "rotate" the image to point it in that direction using our angle

#### Rotate Image

Example function to rotate a sprite image / rect ?? 
>Note: Be careful. When rotating are you getting a reference to a rectangle for a single frame for in an animation? And, do you need to rotate every frame every time? 

```python
def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image
```
## Requirements

### General

- Add an oriented bullet sprite to your game
- Ensure it is "oriented" and flys in the direction of the target.
- The bullet should be a sprite that looks animated as it flys (e.g. flaming projectile, rocket, energy weapon, etc.)
- A sound should play when fired (related to your weapon - not a gunshot sound for a flaming ball).
- A sound should play when target hit (same as above)
- An animation should play when target is hit (same as above)
- You need to use your own sounds and animations. 
- You need to use your own player sprite and mob sprites.
- Other than these requirements, you can use all the code I've uploaded as you see fit.

### Command Line Params

- Your game will be configured by command line parameters (always!).
  - `width`: Window width
  - `height`: Window height
  - `startx`: Starting X coord of player ( -1 could mean random)
  - `starty`: Starting Y coord of player ( -1 could mean random)
  - `title`: Game Title
  - `player_image`: Path to your player sprite.
  - `enemy_count`: Number of enemy's to spawn (mob size).
  - Example command: `python basic.py title="Shooter" player_image=./images/player.png width=640 height=480 startX=100, starty=100 enemy_count=10`

### Config 

- Every param I have in the example config dictionary, you should have in your program as well. 
- Any reference to game assets, should be initiated via the config dictionary at the top (e.g. `width = config['window_size']['width']` and now use `width` wherever).
- In a longer semester, we would place the config in an imported file (or have a class that builds the config based on some directory contents).
- **Any new files used by your program will be added to the config at the top of the program and then referenced using the config dictionary.**

## Deliverables

- Create a folder called `P01.4` in your `Assignments` folder.
- Add a file to your folder called `game_pt4.py` with your solution.
- All files accessed by your game should be in a media folder.
- Screen Shots
  - Screen shot your player shooting in 4 directions showing the bullet orientation.
  - Make your image sizes 400x (wide) and leave the height to maintain aspect ratio.
  - Make a 2x2 markdown table and show the screen shots in your README within this table. 
- You cannot show sound in your README but you should reference (link to) the sound files as part of your writeup.
- A link and description to all used game files will be in your READMD.md as well as a thorough description and instructions.
- README guide: [R03](../../Resources/R03/README.md)


## Pseudo Rubric

- Does the program run?
- Does a sound play when a shot is fired?
- Does a sound play when a mob individual is hit?
- Does a animation play when a mob individual is hit?
- Is the bullet oriented in the correct direction pointing at the enemy?
- Does the bullet animation play when fired?
- Is your code commented? (Letter Grade)


