# foobar
I present you the last two hardest programming challenges of google.
==========
# Challenge:- Bringing a gun to a guard fight
Uh-oh - you've been cornered by one of Commander Lambdas elite guards! Fortunately, you grabbed a beam weapon from an abandoned guard post while you were running through

the station, so you have a chance to fight your way out. But the beam weapon is potentially dangerous to you as well as to the elite guard: its beams reflect off walls, meaning you'll have to be very careful where you shoot to avoid bouncing a shot toward yourself!
Luckily, the beams can only travel a certain maximum distance before becoming too weak to cause damage. You also know that if a beam hits a corner, it will bounce back in exactly the same direction. And of course, if the beam hits either you or the guard, it will stop immediately (albeit painfully).

Write a function solution(dimensions, your_position, guard_position, distance) that gives an array of 2 integers of the width and height of the room, an array of 2 integers of your x and y coordinates in the room, an array of 2 integers of the guard's x and y coordinates in the room, and returns an integer of the number of distinct directions that you can fire to hit the elite guard, given the maximum distance that the beam can travel.

The room has integer dimensions [1 < x_dim <= 1250, 1 < y_dim <= 1250]. You and the elite guard are both positioned on the integer lattice at different distinct positions (x, y) inside the room such that [0 < x < x_dim, 0 < y < y_dim]. Finally, the maximum distance that the beam can travel before becoming harmless will be given as an integer 1 < distance <= 10000.

For example, if you and the elite guard were positioned in a room with dimensions [3, 2], your_position [1, 1], guard_position [2, 1], and a maximum shot distance of 4, you could shoot in seven different directions to hit the elite guard (given as vector bearings from your location): [1, 0], [1, 2], [1, -2], [3, 2], [3, -2], [-3, 2], and [-3, -2]. As specific examples, the shot at bearing [1, 0] is the straight line horizontal shot of distance 1, the shot at bearing [-3, -2] bounces off the left wall and then the bottom wall before hitting the elite guard with a total shot distance of sqrt(13), and the shot at bearing [1, 2] bounces off just the top wall before hitting the elite guard with a total shot distance of sqrt(5).


==========

Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --

Input:
solution.solution([3,2], [1,1], [2,1], 4)
Output:
  7

Input:
solution.solution([300,275], [150,150], [185,100], 500)
Output:
  9

==================

# Challenge:- Expanding Nebula
From the scans of the nebula, you have found that it is very flat and distributed in distinct patches, so you can model it as a 2D grid. You find that the current existence of gas in a cell of the grid is determined exactly by its 4 nearby cells, specifically, (1) that cell, (2) the cell below it, (3) the cell to the right of it, and (4) the cell below and to the right of it. If, in the current state, exactly 1 of those 4 cells in the 2x2 block has gas, then it will also have gas in the next state. Otherwise, the cell will be empty in the next state.

For example, let's say the previous state of the grid (p) was:

.O..
..O.
...O
O...
To see how this grid will change to become the current grid (c) over the next time step, consider the 2x2 blocks of cells around each cell. Of the 2x2 block of [p[0][0], p[0][1], p[1][0], p[1][1]], only p[0][1] has gas in it, which means this 2x2 block would become cell c[0][0] with gas in the next time step:

.O -> O
..
Likewise, in the next 2x2 block to the right consisting of [p[0][1], p[0][2], p[1][1], p[1][2]], two of the containing cells have gas, so in the next state of the grid, c[0][1] will NOT have gas:

O. -> .
.O
Following this pattern to its conclusion, from the previous state p, the current state of the grid c will be:

O.O
.O.
O.O
Note that the resulting output will have 1 fewer row and column, since the bottom and rightmost cells do not have a cell below and to the right of them, respectively.

Write a function answer(g) where g is an array of array of bools saying whether there is gas in each cell (the current scan of the nebula), and return an int with the number of possible previous states that could have resulted in that grid after 1 time step. For instance, if the function were given the current state c above, it would deduce that the possible previous states were p (given above) as well as its horizontal and vertical reflections, and would return 4. The width of the grid will be between 3 and 50 inclusive, and the height of the grid will be between 3 and 9 inclusive. The answer will always be less than one billion (10^9).

Inputs:
(boolean) g = [
                [true, false, true],
                [false, true, false],
                [true, false, true]
              ]
Output:
(int) 4

Inputs:
(boolean) g = [
                [true, false, true, false, false, true, true, true],
                [true, false, true, false, false, false, true, false],
                [true, true, true, false, false, false, true, false],
                [true, false, true, false, false, false, true, false],
                [true, false, true, false, false, true, true, true]
              ]
Output:
(int) 254

Inputs:
(boolean) g = [
                [true, true, false, true, false, true, false, true, true, false],
                [true, true, false, false, false, false, true, true, true, false],
                [true, true, false, false, false, false, false, false, false, true],
                [false, true, false, false, false, false, true, true, false, false]
              ]
Output:
(int) 11567
