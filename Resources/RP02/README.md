## P02 - Project Overview

## Interim Summary (review)

Time is running out and we will cut it close getting a platform game up and running. 1 level? Sure. Multiple levels with a main menu and a game 
over screen? Doubtful. So I'll break it up into pieces again, and try to get all my lecturing done before Monday so you can concentrate on the 
game itself. 

There are quite a few game genre's in the 2D world, and I think next time I teach this class I will 1) Remember all the stuff I wrote over this last
month and 2) Try and teach it in a big semester. Some classes rotate so far apart that I re-learn every time! I'm tired! But seriously, we didn't have
enough time to hit on a lot of the differing styles that exist. With what you know so far, you can get pretty far though.

Knowing how to store and retrieve assets is also a good skill to have. I tried incorporating some of those skills with every assignment, but they really
make sense until projects start growing to the point where being organized is no longer a choice, either do it or create lots of work keeping track of
assets.

On the flip side, thats what got me today. I was Uber confident and just started cutting and pasting and moving and renaming and blah blah blah and I 
broke my code. My wife was laughing at my profanities directed at the computer. I finally did manage to get things organized and get myself to a point
were I can go back and start creating the actual lesson. First lets establish a list of skills we currently have (not an exhaustive list, highlights):

1. Understanding the game loop. 
2. Loading of Sprites and various methods to configure / manipulate them. 
3. Sprite groups and methods that work on these (kill, etc).
4. Collision between sprites (aka rectangles).
5. Capturing keyboard and mouse events.
6. Moving a player via keyboard and/or mouse.
7. Changing the direction of a sprite based on boundaries.
8. Animated sprites, and the changing of frames to perform an animation. Whether on a sprite sheet, or the loading of multiple images.
9. JSON! Managing assets with a configuration file that can be saved, changed,  and loaded to configure game play.
10. Rotating and moving an animated sprite based on an angle between player and target (huge deal!).
11. The python game clock, and using its ticks to control (slow down) the timing of certain animations OR control how often a player can do something (like shoot a bullet).
12. Sound! Adding a sound based on an event. 
13. Just to repeat ... EVENTS! A lot of you were not familiar with event driven programming, and now you are! In class we do procedural or "top down" coding. Event driven is an entirely different paradigm, and you're better for it!

Now that I sum it all up, sounds like a lot! And it is. 

## Big Overview

Entire project:

In my initial approach I created a couple of based classes, then extended them, trying to reach for a smaller and simpler `main` program. I failed. I think I just confused the crap out of everything. So I'm going to create a snapshot of that solution, link to it, and then break everything down into good old stand alone classes. And then use those classes to add the necessary functionality we need to write a platform based game. That minimum functionality is: **gravity** and **jumping**. But let me list what I want this game to contain (aside from just game code):

1. A **Splash Screen** that a user first sees when game loads. This usually has some game company logo on it.
2. This splash screen will transition to a **Menu Screen**. The menu can have all worthless non-working choices, except 1: "start". But we need one nonetheless.
3. **Levels**. Every game needs levels and we need to learn how to load them, and transition between them.
4. **Map Loading**. You can't have levels without graphics and a layout! 
5. **Accruing Points.** Whether its only on a single level, or between levels, or between levels and multiple restarts, we need to be able to accrue assets and keep them between game sessions.
6. **Game Over Screen**. Ummm you got this one?

Ok. Many of those are not that hard. Menu can be text with some mouseover effects to make it look animated. Splash screen can be a ripped off logo (for now), as well as game over screen. The big deal about incorporating all of these items is that we don't just shove our code into a single file and GO! We need to `import` modules and organize our code into different files. We won't get deep into module creation but we will learn about importing and splitting up our code base into multiple files and folders.

On to [Part 1](P02.1/README.md)