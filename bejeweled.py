class Game:

    def __init__(self, filename):
        self._grid = []
        with open(filename) as source:
            for line in source:
                self._grid.append(list(int(d) for d in line.strip()))
            self.width = len(self._grid[0])
            self.height = len(self._grid)

    def __str__(self):
        return "\n".join("".join(map(str, row))
                         for row in self._grid)

    def jewel_at(self, row, col):
        return self._grid[row][col]
            
    def group(self, row, col):
        def adjacents(row, col):
            yield (row+1, col)
            yield (row-1, col)
            yield (row, col+1)
            yield (row, col-1)

        def inbounds(pos):
            row, col = pos
            return 0 <= row < self.height and 0 <= col < self.width

        visited = [[False for _ in range(self.width)]
                   for _ in range(self.height)]

        chosen_type = self.jewel_at(row, col)

        def visit(row, col):
            nonlocal visited
            visited[row][col] = True
            yield (row, col)

            for adj in filter(inbounds, adjacents(row,col)):
                r, c = adj
                if self.jewel_at(r, c) == chosen_type and visited[r][c] == False:
                    yield from visit(r, c)

        yield from visit(row, col)
                
    def remove(self, row, col):
        group = list(self.group(row, col))
        if len(group) > 1:
            for jewel_pos in group:
                r, c = jewel_pos
                self._grid[r][c] = ' '

    def shake(self):
        def pack_right(row):
            width = len(row)
            row = [j for j in row if j != ' ']
            return [' ']*(width - len(row)) + row

        def diagonal(grid):
            width, height = len(grid[0]), len(grid)

            return [[grid[row][col] for row in range(height)]
                    for col in range(width)]

        self._grid = diagonal(list(map(pack_right,
                                       diagonal(self._grid))))
