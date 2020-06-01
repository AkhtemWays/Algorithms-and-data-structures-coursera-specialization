# 1 task
import math
def cube(x):
    return x**3

def num_boxes(n):
    n_boxes = [math.inf for i in range(n+1)]
    n_boxes[0] = 0
    cubed_values = [[] for i in range(n+1)]    
    for i in range(1, n+1):
        for value in range(1, i+1):
            if cube(value) <= i:      
                if n_boxes[i] > n_boxes[i - cube(value)] + 1:
                    n_boxes[i] = n_boxes[i - cube(value)] + 1
                    cube_values_to_add = cubed_values[i - cube(value)].copy()

                    cube_values_to_add.append(value)
                    cubed_values[i] = cube_values_to_add
    return n_boxes[-1], cubed_values[-1]
# print(num_boxes(10))

# 2 task
def check(word_length, L, time):
    if ((time+1)*word_length) + time == L:
        return True
    elif ((time+1)*word_length) + time > L:
        return False
    else:
        return check(word_length, L, time+1)

def passwords(L, words):
    count = 0
    for word in words:
        if len(word) == L:
            count += 1
        elif check(len(word), L, time=1):
            count += 1
        
    return count
# print(passwords(20, ['hello', 'oh', 'o', 'gogo', 'ba']))

                
# 3 task

maze = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
maze2 = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0]
]



def optimal_coordinates2(maze, coordinates, sps, n, m, i, j):

    if (i + 1 < n and maze[i+1][j] == 0) or (j + 1 < m and maze[i][j+1] == 0):
        for a, b in [(i + 1, j), (i, j + 1)]:
            if 0 <= a < n and 0 <= b < m and maze[a][b] == 0 and sps[a][b] >= sps[i][j] + 1:
                if not coordinates[a][b]:
                    sps[a][b] = sps[i][j] + 1
                    for prev_path in coordinates[i][j]:
                        new_path = []
                        for coor in prev_path:
                            new_path.append(coor)
                        new_path.append((a, b))
                        coordinates[a][b].append(new_path)
                    optimal_coordinates2(maze, coordinates, sps, n, m, a, b)
                elif len(coordinates[a][b][0]) == len(coordinates[i][j][0]) + 1:
                    sps[a][b] = sps[i][j] + 1

                    for prev_path in coordinates[i][j]:
                        new_path = []
                        for coor in prev_path:
                            new_path.append(coor)
                        new_path.append((a, b))
                        if new_path not in coordinates[a][b]:
                            coordinates[a][b].append(new_path)
                            optimal_coordinates2(maze, coordinates, sps, n, m, a, b)
                elif len(coordinates[a][b][0]) < len(coordinates[i][j][0]) + 1:
                    sps[a][b] = sps[i][j] + 1
                    prev_paths = coordinates[i][j].copy()
                    for prev_path in prev_paths:
                        prev_path.append((a, b))
                    coordinates[a][b] = prev_paths
                    optimal_coordinates2(maze, coordinates, sps, n, m, a, b)
    if (i + 1 < n and maze[i+1][j] != 0) or (j + 1 < m and maze[i][j+1] != 0):
        for a, b in [(i - 1, j), (i, j - 1)]:
            if maze[a][b] == 0 and 0 <= a < n and 0 <= b < m and sps[a][b] >= sps[i][j] + 1:

                if not coordinates[a][b]:
                    sps[a][b] = sps[i][j] + 1
                    maze[a][b] = 1
                    for prev_path in coordinates[i][j]:
                        new_path = []
                        for coor in prev_path:
                            new_path.append(coor)
                        new_path.append((a, b))
                        coordinates[a][b].append(new_path)
                    optimal_coordinates2(maze, coordinates, sps, n, m, a, b)
                elif len(coordinates[a][b][0]) == len(coordinates[i][j][0]) + 1:
                    sps[a][b] = sps[i][j] + 1
                    for prev_path in coordinates[i][j]:
                        new_path = []
                        for coor in prev_path:
                            new_path.append(coor)
                        new_path.append((a, b))
                        if new_path not in coordinates[a][b]:
                            coordinates[a][b].append(new_path)
                            maze[a][b] = 1
                            optimal_coordinates2(maze, coordinates, sps, n, m, a, b)
                
                elif len(coordinates[a][b][0]) < len(coordinates[i][j][0]) + 1:
                    sps[a][b] = sps[i][j] + 1
                    prev_paths = coordinates[i][j].copy()
                    for prev_path in prev_paths:
                        prev_path.append((a, b))
                    coordinates[a][b] = prev_paths
                    maze[a][b] = 1
                    optimal_coordinates2(maze, coordinates, sps, n, m, a, b)

    return coordinates

def optimal_coordinates(maze, i = 0, j = 0):
    n, m = len(maze), len(maze[0])
    sps = [[math.inf for k in range(m)] for _ in range(n)]
    
    coordinates = [[[] for k in range(m)] for _ in range(n)]
    start_coor = tuple((0, 0))
    coordinates[i][j].append([start_coor])
    sps[i][j] = 1
    optimal_coordinates2(maze, coordinates, sps, n, m, i=0, j=0)
    return coordinates[n - 1][m - 1]
    

# print(optimal_coordinates(maze))

