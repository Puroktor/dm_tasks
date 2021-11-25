from queue import Queue


def _dfs(mat, v, visited):
    visited[v] = True
    visited_count = 1
    for i in range(len(mat)):
        if mat[v][i] == 1 and not visited[i]:
            visited_count += _dfs(mat, i, visited)
    return visited_count


def dfs(mat, v):
    visited = [False for _ in range(len(mat))]
    return _dfs(mat, v, visited)


def bfs(mat, v):
    visited = [False for _ in range(len(mat))]
    visited[v] = True
    visited_count = 1
    queue = Queue()
    queue.put(v)
    while not queue.empty():
        x = queue.get()
        for i in range(len(mat)):
            if mat[x][i] == 1 and not visited[i]:
                visited[i] = True
                visited_count += 1
                queue.put(i)
    return visited_count


def main():
    with open('input.txt', 'r') as file:
        mat = [[int(num) for num in line.strip().split()] for line in file]
    dfs_visited_count = dfs(mat, 0)
    bfs_visited_count = bfs(mat, 0)
    with open('output.txt', 'w') as file:
        file.write('{} {}'.format(dfs_visited_count, bfs_visited_count))


if __name__ == '__main__':
    main()
