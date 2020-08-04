## Project 2 - Platformer
#### Due: 08-6-2020 (Thursday @ 12:30 p.m.)

### Basic Overview / Big Picture

We are going to write a platformer game with multiple levels. Your game can be almost any style of platformer you want as long as it fulfills the basic requirements of a platform game. Those requirements are:

1. It has platforms.
2. A character uses an animated sprite to move around the game level using a "jump" feature to gain access to platforms.
3. As the player moves around the level, she can accrue points by gathering (colliding with) objects on the screen.
4. There are traps on each level. A trap can be a pit that the player falls in or something more nefarious when the player triggers the trap at a predetermined location.

Each of these basic requirements can be seen in the example below:

<img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/platformer_example_2020_4443.png" width="500">

Configuring a level by mixing up the above requirements is what makes for good gameplay. Here are some examples you can incorporate into your game. 

- Moving platforms. 
  - Typically if they do move they move 1 dimensionally (up/down or left/right). This makes for predictable behavior when trying to jump onto the platform. I guess it could move randomly within some bounding box, that is up to you.
- No floor! 
  - Meaning the player must stay on platforms and not miss when jumping otherwise they will die.
- Random objects falling or flying across the screen. These could be deadly or power-ups. 
  - A Power-up is a temporary boost in some character component (e.g. speed, or strength, jumping ability, etc.).
- Surprising traps. 
  - A trap can be hidden and triggered when the player is in close proximity to the trap. It can be anything from instant death to a temporary power-down (making the player slower or jump less high).

-----

## Game Components

What your game will need:

- A player with sprite animation that can move left and right as well as jump. Shooting is optional.
- 3 Levels that vary quite a bit.
- Additional sprites to score points with or kill the player with.
- A Splash screen.
- Game over screen. 
- Some other goodies I will bring up later.

We already have a sprite with animation, so lets discuss how to create our levels.

### Player

You will have a player that can move right, left, and jump. 

<img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/dude.png" width="100">

Additional animations should be applied as the situation dictates. For example, I downloaded a Mario sprite sheet [HERE](HelperFiles/Graphics/mario_frames/) and there is a [json file](HelperFiles/Graphics/mario_frames/moves.json) in that same folder defining all the different animations I created from the [big sprite sheet](HelperFiles/Graphics/mario.png). I created many additional animations in anticipation of using them in my game: jumps, long jumps, hammer blows, and even a simple frame to show him dropping off a platform:

<img src="./HelperFiles/Graphics/mario_frames/mario_016.png" width="75">

### Creating a Level

To create a game level, you need:

- A tile set
- A level (map) definition
- A way to map a tile set to your level definition

### Tile Sets

The tile-sets [here](https://craftpix.net/categorys/tilesets/) are not free (but I'm sure you can figure out how to clone them for educational purposes) and I'm sure you can see how this individual basically creates many differing worlds with nearly the same template. I have an example [HERE](HelperFiles/code/spriter/README.md) on how to copy his sprite sheets. As long as were using it for education, and not making money, I think it is ok. In my example I explode the images out of a larger image. Thats my preferred method. You can handle the sheets however you like but for your individual game: **you must find a tile map of your own and use it in your platformer** to create at least 3 levels. 


### Using Tile Sets

So you went and found a tile sheet and you want to use it. Now what? In the table below you see a tile set on the left. I left this one in the original image just to make it easier to view. I added id numbers for the block tiles on the left side of the image. The objects (trees, bushes, etc.) on the right I did not label. Notice that each tile has a unique number. And when I pull each image out of the tile sheet, those numbers correspond with the file names (01.png, 02.png etc.). 

If you don't pull the tiles out of the image, you need to create a reference file (most likely a json file) that links some integer id to a rectangle that corresponds to a tile. Example: `"05":(183,102,78,78)` , `"06":(267,102,78,78)` and so on.

|     Tile Set       |    Background    |      Results            |
| :--------------: | :--------------:|:-----------------: |
| <a href="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/tile_set_example_4443_nums2.png"><img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/tile_set_example_4443_nums2.png" width="300"></a> | <a href="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/tileset_example_background_4443.png"><img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/tileset_example_background_4443.png" width="300"></a> | <a href="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/tileset_output_4443.jpg"><img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/tileset_output_4443.jpg" width="300"></a> |



Why is each tile numbered? Because it makes things a little simpler. Its easier in code or a map file to reference the value `04` rather than `middle_left_dirt_block_edge`, and when we build text maps that correspond to tiles its easier to represent a block like:

```
010203
040506
120916
```

Rather than: 

```
top_left_dirt_blocktop_middle_dirt_blocktop_right_dirt_block
blah blah
```

It's also easier to parse a file where each tile is 1-4 digits and consistent! Parsing that crap right above would be a nightmare.

So, using our numbering scheme, we can see below that `Block 1` is a minimal arrangement of tiles that creates a usable structure, and `Block 2` shows that a structure of basically any size can be made using those same tile references.

<p align="center">

|  Block 1   |   Block 2  |
|:----------:|:------------:|
| <img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/tile_group_example_4403.png" width="300"> | <img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/tiled_group_example_2_4443.png" width="300"> |

</p>

### Tile Sets in Map Definitions

A map has many different meanings. In the context of our game, a map is a set of tiles mapped to specific locations on a game screen. Of course, the larger a game gets, we might need a map in the traditional sense show our location within a large set of game screens. But for now, we think of a map as an assignment of tiles to locations.

One question you should ask yourself is: Ummmmmm. How do I make that happen? Well I could list a few ways to load tile-sets, and they would be a waste of time because the easiest way is to create a text file where 1 or more characters represents a specific tile and that character(s) location in the text file has a direct relationship as to where it is stored in the actual game window. 

Look at our simple example from above representing a small block:

```
010203
040506
120916
```

This is technically a map file! Keep adding to this, before long you will have a full fledged game level. 

Remember that however you represent a map in a text file, that map definition will be expanded (pixel wise) by the size of your tiles. So if you use 1 character to represent a tile, and your tiles are 25x25 ... (hold on ... hmmm ...  carry the 1 ...) YES! It will be 25 times larger in pixels when displayed on your PyGame window.

### Creating Map Definitions

So what are we to do? Should we download a bunch of tile-sets? Should we create your own? I happen to have some code written for you to pick and choose from, all in the realm of splitting, making, and creating tile-sets from existing images. 

- I have examples on how to explode a tile sheet [HERE](./HelperFiles/code/spriter/README.md)
- I have code that creates random platforms that can be tweaked [HERE](HelperFiles/code/platformGenerator.py)
- I have code that will resize a directory of tiles to whatever sizeXsize you want [HERE](HelperFiles/code/resizeTiles.py)
- I have an example tile set with a json file that helps understand how to organize the tile set [HERE](HelperFiles/Graphics/maps/forest_tileset/)

I REALIZE that it's not always easy to read / use someone else's code or scripts. However, I don't know what the alternative is. Do it all by hand, I'm cool with that. Find it on the web. I'm cool with that as well. Just as long as your platform game is your own work and not a rip off of something me or your classmates did. 

#### Platform Generator

I previously posted a bit about `platformGenerator.py` and how it can generate a basic random layout for you. It definitely needs tweaking but given a tile-set that it would consistently use, and some time to taylor it, I'm sure it would have no problem generating usable layouts. For us however this will take too much time. I will suggest
that you use it to create a few interesting layouts, and then fix by hand any levels it generates. How do we do this? Look at the example output below:

```
................................................................................
................................................................................
................................................................................
................................................................................
......131515151514......................1315151515151514................13151514
................................................................................
....131515151514................................................................
................................................................................
................................................................................
........1315151515151515141514..................................................
13151514........................................................................
............................................................131515151515151514..
..1315151515151514151515151514..................................................
................................................................................
................................................................................
........................010202020202020203......................................
010202020317171717171717040505050505050506................................010203
0405050506181818181818180405050505050505060102020203......................040506
04050505061818181818181804050505050505050604050505061717171717171717170103040506
12090909160102020202020312090909090909091612090909161818181818181818181216120916
```

The platform generator is hardcoded for this [json file](./resources/maps/forest_clean/tileset.json). It gives a definition of a tile-set I found that looked easy to deal with. This json is not some industry standard, its my creation, and you can format yours as you see fit:

```json
{
    "folder":"Tiles_25",
    "size":{
        "width":25,
        "height":25
    },
    "groups":{
        "block":[
            ["01","02","03"],
            ["04","05","06"],
            ["12","09","16"]
        ],
        "platform":[
            ["13","14","15"]
        ],
        "water":[
            ["17"],
            ["18"]
        ],
        "sub_block_left":[
            ["07","08"]
        ],
        "sub_block_right":[
            ["10","11"]
        ]
    },
    "objects":{
        "folder":"Objects_25",
        "items":{
            "mushrooml_1":"Mushroom_1.png",
            "mushrooml_2":"Mushroom_2.png"
        }
    }
}
```
What you could do is generate a level, and then based on the values in your tileset, search and replace? I'm not sure, but if your game levels are like two platforms with no floor your gonna be screwed.

-----

### Levels

Ok, so now you have a level or two and your player sprite can run around jumping from platform to platform. What do we do now? You need to add objects to each level using a minimum of two categories: 1) Objects that score points for the player when he/she collides with them, 2) objects that kill or injure the player. 

That is a loaded paragraph above. Scoring points, pretty trivial. Create a sprite group and when a collision happens add to players score ... score :thinking: Wait! I need to track a score! I also need to remember my score when transitioning between levels.

And don't forget objects that kill or injure the player ... hmmmm :thinking: should produce some kind of animated effect. The easy solution is to slow down a player, but the better solution is to slow down a player and add some animation effect showing depleted power. 

Which reminds me: **power bar!!** Just kidding. But it would be cool to show a players remaining life.

-----

### Sounds

- A non-annoying game track should play while your game is in play. This means not loud.
- Also there should be sounds associated with events in the game:
  - collection of coins or point objects
  - dying

-----

### Splash Screen, Menu Screen, and Game Over

**Splash Screen**

This screen shows when your game is starting. It should show a logo, and the name of your game. A loading bar would be cool, but is not mandatory.

**Menu Screen**

With respect to this being the last week, and little time to be frivolous, I will say that the "menu" screen
will simply have a button OR animated "start game" text box. When I say animated, I simply mean that when the mouse hovers over it, it changes its color or drops a shadow, or something. 

**Game Over**

This screen will say .... "Game Over" :roll_eyes: and show the players score. Keeping a high score between games would be a cool extra credit addition.


## Deliverables

- Create a folder called `P02` in your `Assignments` folder.
- Inside your `P02` folder you should have multiple files representing your game.
- Here is a possible list of files:
  - `menu.py`
  - `gameover.py`
  - `level_01.py`
  - `level_02.py`
  - `level_03.py`
  - `splash.py`
- You might have a `main.py` file the runs it all. 
- There should be a resources folder with 
  - a graphics folder
  - a maps / levels folder
- Screen Shots
  - A screen shot of each different screen should be in your README.md
  - Make your image sizes 300x (wide) and leave the height to maintain aspect ratio.
  - Show each screen shot in a table with 3 shots in one row. 
- You cannot show sound in your README but you should reference (link to) the sound files as part of your writeup.
- A link and description to all used game files will be in your READMD.md as well as a thorough description and instructions.
- README guide: [R03](../../Resources/R03/README.md)

## Pseudo Rubric

- Splash screen shows long enough to notice it.
- Menu screen shows.
  - The choices have some animation (rollover event)
  - A simple "Start Game" is good enough as long as it has some animation.
- Player moves left and right.
- Player can jump to platforms. The jumping is "realistic" (lol) meaning not too high!
- Player has a ability to collect points.
- Player can move to next level (doesn't have to come back).
- Player can die when:
  - Hits a trap.
  - Runs out of life.
  - Falls into pit or off platform into infinity.
- Sounds play associated with events.
- 1 Trap per level is implemented. A trap kills or injures a player. A pit is not a trap.
- more soon

