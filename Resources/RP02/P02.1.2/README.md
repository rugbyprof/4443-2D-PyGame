## P02 - Part 2

Project overview [here](../README.md)

## Step 2

This next part for Project 2 is loading a map. And not just a single map you make by hand. Well you can do that, but
most games have many many levels, so you might want to think about how to generate and load levels. 

Quick summary: Currently we have a sprite loader that helps with our player class. We have code that helps us control our player and  move around some primitively loaded platforms. The collision detection is not amazing, but we are using built in  PyGame methods, so I don't know how to reach in and improve what we have. Having said that, it works ok and we should be good to go.

So, we need levels. Levels are created from maps and maps are created from tile sets (typically). So whats a tile set?

### Tile Sets Overview

|     Tile Set       |    Background    |      Results            |
| :--------------: | :--------------:|:-----------------: |
| <img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/tile_set_example_4443_nums.png" width="300"> | <img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/tileset_example_background_4443.png" width="300"> | <img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/tileset_output_4443.jpg" width="300"> |


In the table above you see a tile set on the left. I numbered the majority of them to show in the examples below how certain objects are constructed. When a particular subset of the tiles are arranged correctly, we get objects (like platforms and blocks). The image in the middle is a background in which all objects (made from tiles) are placed to give a game level a better look.

The examples below show a minimal example on the left, and another example on the right showing that a block or chunk of any size can be made using these tiles.

<p align="center">

|  Example 1   |   Example 2  |
|:----------:|:------------:|
| <img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/tile_group_example_4403.png" width="300"> | <img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/tiled_group_example_2_4443.png" width="300"> |

</p>

### Maps

A map has many different meanings. In the context of our game, a map is a set of tiles mapped to specific locations on a game screen. Of course, the larger a game gets, we might need a map in the traditional sense show our location within a large set of game screens. But for now, we think of a map as an assignment of tiles to locations.

One question you should ask yourself is: Ummmmmm. How do I make that happen? Well let me list a few:

1. Open "tile set" image, and use PyGame "blit" to crop each tile and place it accordingly using lots of hardcoded statements.
2. Separate each tile into images, then load them and assign them a location on the game screen. Basically the same as the previous, but without using blit to crop the image. And yes, lots of code to "position" tiles. 
3. Create a text file (of any format you are comfortable with) and use this to load and assign the tiles into the appropriate locations. 

Whatever scheme you come up with to represent maps (as in item 3) it doesn't matter. Item 3 is by far the best solution for loading levels. Why? Because I said so.... Ok, its the best because its the most robust, meaning it has the greatest ability to be very robust! Think about it. Replacing a map with a new tile-set and with proper planning, could render an entirely different scene! The tile-sets [here](https://craftpix.net/categorys/tilesets/) are not free (but I'm sure you can figure out how to clone them for educational purposes) and I'm sure you can see how this individual basically creates many differing worlds with nearly the same template. Look at his platformer templates and you will see the common threads. 

### TileMap Loader

So what are we to do? Download a bunch of tile-sets? Create your own? I happen to have some code written for you to pick and choose from, all in the realm of splitting, making, and creating tile-sets from existing images. 

I REALIZE that it's not always easy to read / use someone else's code. However, I don't know what the alternative is. 

In the [resources/maps/forest_clean](resources/maps/forest_clean/) folder, there are a few folders with different size tile-sets and a `tileset.json` file. It contains enough stuff that can be use to build a level with the forest theme. However, there are not any items to help make traps, and only a couple of mushrooms to spread around for points. There are definitely no monsters. 

I previously posted a bit about `platformGenerator.py` and how it can generate a basic random layout for you. It definitely needs tweaking but given a tile-set that it would consistently use, and some time to taylor it, I'm sure it would have no problem generating usable layouts. For us however this will take too much time. I will suggest
that you use it to create a few interesting layouts, and then fix by hand any levels it generates. How do we do this? Look at the example output below:

```
                            ___________33333______________
                            ______________________________
                            __22222222_________22222______
                            ______________________________
                            _1111111_______1111______1111_
                            ______________________________
                            00000_____0000000_____00000000
                            00000_____0000000_____00000000
                            00000_____0000000_____00000000
                            00000_____0000000_____00000000
```

The zeros are ground. The empty spaces between the zeros are pits and the 1's 2's and 3's are platforms. I used different numbers for each platform for no specific reason. Anyway, this [json file](./resources/maps/forest_clean/tileset.json) gives a definition of a tile-set I found. This json is not some
industry standard, its my creation, and you can format yours as you see fit:

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


Now we can apply our tile set knowledge to our platformGenerator output. OR! You can simply hand code your own maps using your own tile-sets. Its up to you. I always felt it was easier to make small changes to an
existing file, rather than starting from scratch. If we had time, I would alter the `platformGenerator` to output the proper tile numbers based on a tile-set (aka have it read in a json, like above, and use it to
help generate a level).

Anyway, lets convert our first example to something the forest tile-set can represent. Remember the original output is a single digit, and 

```
                            ___________33333______________
                            ______________________________
                            __22222222_________22222______
                            ______________________________
                            _1111111_______1111______1111_
                            ______________________________
                            00000_____0000000_____00000000
                            00000_____0000000_____00000000
                            00000_____0000000_____00000000
                            00000_____0000000_____00000000
```

```
                            ___________13141414141415________________________
                            _________________________________________________
                            __13141141441415_________131414141415____________
                            _________________________________________________
                            _13141414141415_______1314141415______1314141415_
                            _________________________________________________
                            00000_____0000000_____00000000
                            00000_____0000000_____00000000
                            00000_____0000000_____00000000
                            00000_____0000000_____00000000
```
