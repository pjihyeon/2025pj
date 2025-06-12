maze = [
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 1],
    [0, 0, 1, 1]
]

N = len(maze)
path = []

def dfs(x, y, visited):
    if x == N - 1 and y == N - 1:
        path.append((x, y))
        return True

    if x < 0 or y < 0 or x >= N or y >= N or maze[x][y] == 0 or visited[x][y]:
        return False

    visited[x][y] = True
    path.append((x, y))

    for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
        if dfs(x+dx, y+dy, visited):
            return True

    path.pop()
    return False

visited = [[False]*N for _ in range(N)]
if dfs(0, 0, visited):
    print("Path found:", path)
else:
    print("No path found")
