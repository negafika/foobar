from collections import *

def solution(g):
    data = {True: [[2, 0], [1, 0], [0, 2], [0, 1]],
            False: [[3, 0], [1, 2], [0, 3], [1, 3], [2, 2], [1, 1], [3, 1], [3, 3], [2, 1], [3, 2], [2, 3], [0, 0]]}
    # data represents 2x2 binary matrix each row changed to decimal numbers so they are converted to 2x1 matrices.
    # according to each value of a column of g, they will build all the possible predecessors of that column.
    m = 2 ** (len(g))
    v = 2 ** (len(g) - 1)
    category = defaultdict(list)
    # category is to map the possible predecessors' left column by using the right column as a key.
    repeat = defaultdict(int)
    # repeat's purpose is the same as category except that it holds the length of each left columns associated with
    # that key. The next for loop tries to create and merge all the possible column predecessors.
    for i in range(len(g[0])):
        old = deque(data[g[0][i]])
        for e in range(len(g) - 1):
            new = deque(data[g[e + 1][i]])
            old1 = deque(old)
            old.clear()
            for cube in old1:
                for cubes in new:
                    if cube[-1] == cubes[0]:
                        if e == 0:
                            trans = [(cube[0] // 2) * m + (cube[1] // 2) * v,
                                     (cube[0] % 2) * m + (cube[1] % 2) * v, cubes[1]]
                        else:
                            trans = [cube[0] + (cube[2] // 2) * 2 ** (len(g) - 1 - e),
                                     cube[1] + (cube[2] % 2) * 2 ** (len(g) - 1 - e), cubes[1]]
                        old.append(trans)
                        if e == len(g) - 2:
                            category[trans[1] + trans[-1] % 2].append(trans[0] + trans[-1] // 2)

        total = 0
        # total counts possible answers
        if i == 0:
            for (k, z) in category.items():
                repeat[k] = len(z)
        else:
            other = defaultdict(int, repeat)
            repeat.clear()

            for (key, value) in category.items():
                initial = 0
                for val in value:
                    initial += other[val]
                repeat[key] = initial
                total += initial
        category.clear()
    return total

