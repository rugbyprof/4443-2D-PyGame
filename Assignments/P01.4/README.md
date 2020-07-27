## Project 1.4 - CovidZAR Shooting & Sound
#### Due: 07-28-2020 (Tuesday @ 12:30 p.m.)

## Overview of Part 4

### Helper Code

- [Help Files](../../Resources/RP01/P01.4/README.md)

### Requirements

Add a projectile that has a direction to be used as a bullet. What does that mean? Look at the image below:

<img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/bullets_directed.png">

If you were to use this as a projectile, you would need to orient the image to be facing the correct direction. You would also need to run through the animation (once) as it flys toward the target. If it were to fly a long direction, you could start with the frame on the far right, and when it got to the last frame (far left) you could alternate between the last two frames to keep up appearances of being "alive".

- To orient the sprite correctly:
  - we need to calculate the angle between the player and the target
  - then we need to "rotate" the image to point it in that direction

#### Rotate Image

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

#### Yes - Command Line Params

- Your game will be configured by command line parameters (always!).
  - `width`: Window width
  - `height`: Window height
  - `startx`: Starting X coord of player ( -1 could mean random)
  - `starty`: Starting Y coord of player ( -1 could mean random)
  - `title`: Game Title
  - `player_image`: Path to your player sprite.
  - Example command: `python basic.py title="Shooter" player_image=./images/player.png width=640 height=480 startX=100, starty=100`


## Deliverables

- Create a folder called `P01.4` in your `Assignments` folder.
- Add a file to your folder called `game_pt4.py` with the above code.
- Screen Shots
  - pass
- Add a `README.md` file to your `P01.4` folder with instructions on how to run your program guided by [R03](../../Resources/R03/README.md)


## Pseudo Rubric

- Does the program run?
- Does the floor scroll realistically when player moves?
- Does the player stay near the center while moving?
- Does the player approach the wall when the window gets to the edge of the world.
- Does a visual alert show when player hits wall?
- Does two alerts show in a corner?
- Is your code commented? (Letter Grade)


