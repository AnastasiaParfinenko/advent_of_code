from heapq import heappush, heappop

class Maze:
    def __init__(self):
        with open('input16.txt', 'r') as file:
            self.grid = [list(line) for line in file.read().splitlines()]
            self.size = len(self.grid)
            self.deer = next((i, j) for i in range(self.size) for j in range(self.size) if self.grid[i][j] == 'S')
            self.end = next((i, j) for i in range(self.size) for j in range(self.size) if self.grid[i][j] == 'E')

    def algoritm_d(self):
        maze = self.grid
        directions = ['^', '>', 'v', '<']
        di = {'^': -1, '>': 0, 'v': 1, '<': 0}
        dj = {'^': 0, '>': 1, 'v': 0, '<': -1}
        turn_cost = 1000
        move_cost = 1

        deer_i, deer_j = self.deer
        start_dir = '>'
        end_i, end_j = self.end

        queue = []
        heappush(queue, (0, deer_i, deer_j, start_dir))

        visited = {}

        while queue:
            cost, i, j, dir = heappop(queue)

            if (i, j, dir) in visited and visited[(i, j, dir)] <= cost:
                continue

            visited[(i, j, dir)] = cost

            new_i, new_j = i + di[dir], j + dj[dir]
            if maze[new_i][new_j] != '#':
                new_state = (new_i, new_j, dir)
                if new_state not in visited or visited[new_state] > cost + move_cost:
                    heappush(queue, (cost + move_cost, new_i, new_j, dir))

            for new_dir in directions:
                if new_dir != dir:
                    new_state = (i, j, new_dir)
                    if new_state not in visited or visited[new_state] > cost + turn_cost:
                        heappush(queue, (cost + turn_cost, i, j, new_dir))

        min_cost_to_goal = float('inf')
        for dir in directions:
            if (end_i, end_j, dir) in visited:
                min_cost_to_goal = min(min_cost_to_goal, visited[(end_i, end_j, dir)])
        print(min_cost_to_goal)

        if min_cost_to_goal == float('inf'):
            return 0


        queue = []
        cells_on_shortest_paths = set()

        for dir in directions:
            if (end_i, end_j, dir) in visited and visited[(end_i, end_j, dir)] == min_cost_to_goal:
                queue.append((end_i, end_j, dir))

        while queue:
            i, j, dir = queue.pop(0)
            if (i, j) not in cells_on_shortest_paths:
                cells_on_shortest_paths.add((i, j))

            for prev_dir in directions:
                if prev_dir == dir:
                    prev_x, prev_y = i - di[dir], j - dj[dir]
                    if (prev_x, prev_y, prev_dir) in visited and visited[(prev_x, prev_y, prev_dir)] + move_cost == \
                            visited[(i, j, dir)]:
                        queue.append((prev_x, prev_y, prev_dir))

                else:
                    if (i, j, prev_dir) in visited and visited[(i, j, prev_dir)] + turn_cost == visited[
                        (i, j, dir)]:
                        queue.append((i, j, prev_dir))

        return len(cells_on_shortest_paths)


def part12():
    maze = Maze()
    print(maze.algoritm_d())


part12()