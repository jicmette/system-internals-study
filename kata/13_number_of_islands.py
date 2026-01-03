# Problem: Count islands in a 2D grid.
# Logic: Depth First Search (DFS). When I find a '1', sink the whole island.

def num_islands(grid):
    if not grid:
        return 0

    count = 0
    rows = len(grid)
    cols = len(grid[0])

    def sink_island(r, c):
        # Base Case: Stop if out of bounds or if it's water ('0')
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
            return

        # Mark as visited (Sink the land)
        grid[r][c] = '0'

        # Visit neighbors (Up, Down, Left, Right)
        sink_island(r + 1, c)
        sink_island(r - 1, c)
        sink_island(r, c + 1)
        sink_island(r, c - 1)

    # Main Loop: Scan every cell
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                # Found a new island!
                count += 1
                # Explore and mark the entire island
                sink_island(r, c)

    return count

# --- TEST ---
map_1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
# Expected: 1 (The top left chunk connects to everything)

map_2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

map_3 = []
# Expected: 3 (Top-left, Middle, Bottom-right)

print(f"Map 1 Islands: {num_islands(map_1)}")
print(f"Map 2 Islands: {num_islands(map_2)}")
print(f"Map 3 Islands: {num_islands(map_3)}")