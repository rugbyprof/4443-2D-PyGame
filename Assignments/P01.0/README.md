## Project 1 - CovidZAR.EIEIO
#### Due: Multiple Dates

I'm not sure what will be due Thursday .... so back off!! I'm laying out the rules of CovidZAR.eieio

## Overview of Game

This game is totally made up AND a total rip off of AGAR.IO. Seriously, we will rip off AGAR.IO at a base level, but then make it our own with specialized upgrades and / or possible simplifications. In other words there is a blank canvas for you to create upon with your logical and artistic skill set; as long as you follow all the requirements. (Yup, each of those sentences was or possibly is or is not a contradiction in and amongst themselves).

<p align="center">
<img src="https://cs.msutexas.edu/~griffin/zcloud/zcloud-files/covidareieio.png" width="700">
</p>

>Note: The image above is a screen shot of the AGAR.IO game from my phone. We do not, and most likely will not use the same type of graphics that are pictured. I will show you guys how to load images and scale them. Part of the assignment will be to follow the mandatory "requirements" (which I will loosely set around basic gameplay) and for you to "create" something better above and beyond those base requirements (like finding cool images to "represent" character).

### Basic Game Premise

This is a top down game with a finite 2D world in which a camera view follows a "player" around. The view in the example is about 27x15 grid squares (not sure in pixels). The world can be as big as we want it, allowing the player to move all over the (for example) 100x100 grid world always keeping the same size "view" around him or her.


### Object Types
- Blobs (players and or NPC's)
- Viruses
- Pellets

### The World
1. Large 2D grid of finite size.
1. In this world you are a blob with mass (see the players in the image above).
2. There are other blobs as well usually controlled by other players (in the actual game) but most likely NPC's for us.
3. Your mass is defined by the size of the **visible** surface area (we can talk bounding rectangles later) of your blob.
4. Your mass increases when you eat other blobs (players or non-player characters).
5. However, you can only eat other blobs when they are smaller than you by a set percentage.
6. Larger blobs can eat you.
7. Viruses:
   - Don't move in the actual game, but maybe they do for us?
   - Will kill a blob that it contacts and is larger than the virus itself.
   - No harm comes to a blob smaller than the virus.
8. Pellets:
   - Are used to grow a blob in the actual game.
   - Don't move in the actual game.
   - Maybe we spice them up?

### Growing Your Blob
- Your blob will increase one point in mass each time you eat a pellet (small colored dots on screen).
- Also you grow when you eat smaller cells (not sure on amount maybe a percentage of their mass?)
- The **maximum** mass size you can ever reach for a blob is **22500**, when a blob reaches this size, it won’t grow anymore.

### Splitting Your blob
- Original game allows you to split your blob. I'm not sure why. Obviously there is benefit in certain situations but I refuse to play long enough to find out:)
- Hitting the space bar should divide your blob into 2.
- Consecutive hits of the space bar should further divide your blobs.
- The actual rules for splitting I will leave open for interpretation.
- If this comes up in an assignment, I will put a minimum requirement on it.
- Things to think about:
  - How will player control a split blob?
  - Can a piece of a blob thats been split act autonomously?
  - How will the pieces look when player moves (a frozen group of blobs moving as a block?)
- How do we rejoin a split blob?
- Appearance and implementation of splitting will be determined by individual implementation.

### Shrinking Your Blob
- You can actively eject mass from your blob aka **Active Shrinking**.
- This is NOT the same as splitting.
- In the actual game, your blobs mass decreased by 1% for every second that passed. This can be referred to as **Passive Shrinking**.
- Why would we eject mass actively or passively? I'm not sure. So how what or why we do this may be left up to you.


### Viruses
- A virus is the green spiky round things in the game screen.
- They do not move in the actual game.
- They are born at random locations.
- A virus makes a bigger blob explode if the blob touches it.
- Smaller blobs do not explode even if it passes through the center of a virus.
- The mass of a virus in the actual game is around 140 at birth and grows over time? I'm not sure.
- A virus can grow if a blob ejects mass into it.
- A virus thats been ejected on (gross) will create a new virus that is "thrown" towards the "ejector".


### Rules of Eating
- A blob must have a size of `25%` more of target blob in order to eat it.
- If two masses meet that are within the `25%` of mass I'm not sure what happens. Maybe they play a game of war? (you know with cards ...)
- Mass, is defined as the area of a blob. So, calculating mass will need to be defined. Its a trivial thing, but it should be consistent.
- If you are split, then one of your child blobs must meet the rules for eating on thier own.