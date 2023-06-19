# 0x09. Island Perimeter

## Description

<p>The <strong>'island_perimeter'</strong> function calculates the perimeter of an island described in a grid. The grid is a rectangular area with cells that either land (represented by 1) or water (represntated by 0). The goal is to determine the perimeter of the island based on its shape</p>

## Requirements
<ul>
    <li>The grid is represented as a list of lists, where each inner list represnts a row of cells</li>
    <li>The grid is completely surrounded by water</li>
    <li>Each cells is square with a side length of 1</li>
    <li>Cells are connected horizontally/vertically (not diagonally)</li>
    <li>The width and height of the grid do exceed 100</li>
</ul>

## Approach
To calculate the perimeter of the island, the <strong>'island_perimeter'</strong> function follows these steps:

<ol>
    <li>If not grid, return 0</li>
    <li>Initialize the 'perimeter' variable to 0,  rows = len(grid), cols = len(grid[0])</li>
    <li>declare the function: def island_perimeter(grid)</li> 
    <li>iterate through each cell in the grid</li>
    <li>if cell represent land(1), increment the perimeter by 4</li>
    <li>Check the adjacent cells to the left and top of the current cell:
    If the adjacent cell is also land(1), decrement the perimeter by 2</li>
    <li>After iterating through all cells, return the perimeter value.<li>
</ol>

## Test case

<code>
    #!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
</code>
