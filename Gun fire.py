from cmath import *

def solution(dimensions, your_position, trainer_position, distance):
    max_val = float('inf')
    walls = [[max_val, 0], [0, max_val], [max_val, dimensions[1]], [dimensions[0], max_val]]
    # representation of the rectangular walls.
    default = phase(length(your_position, trainer_position))
    # the angle between trainer position and your position
    unique = set()
    # a set to store the valid angles
    invalid = set()
    # a set to store the possible angles you can shoot to hit yourself in the end.
    pathway = [(0,), (1,), (2,), (3,)]
    count = 0
    # the next while loop checks if the mirror image point is valid. i.e if it's not in invalid and less or equal to
    # the maximum distance. If it's not it removes points until pathway is empty.
    while pathway:
        path = pathway[count]
        mpt = tuple(your_position)
        pt = tuple(trainer_position)
        for reflect in path:
            pt = reflection(walls[reflect], pt)
            mpt = reflection(walls[reflect], mpt)
        bear_angle = phase(length(your_position, pt))
        angle = phase(length(your_position, mpt))
        invalid.add(angle)
        if bear_angle not in unique and abs(length(your_position, pt)) <= distance:
            if bear_angle not in invalid:
                unique.add(bear_angle)
            else:
                pathway.remove(path)
                count -= 1
        else:
            pathway.remove(path)
            count -= 1
        count += 1
        if count == len(pathway):
            count = 0
            pathway = cartesian_product(pathway)
    if abs(length(trainer_position, your_position)) <= distance:
        unique.add(default)
    return len(unique)


def reflection(axis, pt):
    # it is to find a reflection mirror image of a point on a wall.
    min_val = min(axis)
    min_val_index = axis.index(min_val)
    if min_val == 0:
        if min_val_index == 0:
            pt = (-pt[0], pt[1])
        elif min_val_index == 1:
            pt = (pt[0], -pt[1])
    else:
        if min_val_index == 0:
            pt = (2 * min_val - pt[0], pt[1])
        elif min_val_index == 1:
            pt = (pt[0], 2 * min_val - pt[1])
    return pt


def cartesian_product(possibilities):
    # function to find the possible wall hits.
    walls_index = [0, 1, 2, 3]
    holder = []
    for item in possibilities:
        for num in walls_index:
            temp = list(item)
            temp.append(num)
            holder.append(tuple(temp))

    return holder


def length(x, y):
    num = complex(y[0] - x[0], y[1] - x[1])
    return num


