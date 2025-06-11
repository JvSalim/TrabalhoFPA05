#!/usr/bin/env python3
import random
import time

def flood_fill(grid, x, y, new_color, original_color, visualize=False):
    rows = len(grid)
    cols = len(grid[0])

    if x < 0 or x >= rows or y < 0 or y >= cols:
        return
    if grid[x][y] != original_color:
        return
    if grid[x][y] == 1:
        return

    grid[x][y] = new_color

    if visualize:
        print("\nPreenchendo...")
        print_grid(grid)
        time.sleep(0.1) # Pequeno atraso para visualização

    flood_fill(grid, x + 1, y, new_color, original_color, visualize)
    flood_fill(grid, x - 1, y, new_color, original_color, visualize)
    flood_fill(grid, x, y + 1, new_color, original_color, visualize)
    flood_fill(grid, x, y - 1, new_color, original_color, visualize)

def find_and_fill_all_regions(grid, start_color=2, visualize=False):
    rows = len(grid)
    cols = len(grid[0])
    current_color = start_color

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                if visualize:
                    print(f"\nIniciando preenchimento da região com a cor {current_color} a partir de ({r}, {c})")
                flood_fill(grid, r, c, current_color, 0, visualize)
                current_color += 1
    return grid

def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

def generate_random_grid(rows, cols, obstacle_density=0.3):
    grid = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            if random.random() < obstacle_density:
                row.append(1) # Obstáculo
            else:
                row.append(0) # Terreno navegável
        grid.append(row)
    return grid

if __name__ == "__main__":
    print("--- Teste com Exemplos do PDF ---")
    # Exemplo 1
    grid1 = [
        [0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 1, 1, 1],
        [1, 1, 0, 0, 0]
    ]
    print("\nGrid Inicial Exemplo 1:")
    print_grid(grid1)
    filled_grid1 = find_and_fill_all_regions([row[:] for row in grid1]) # Usar copy para não modificar o original
    print("\nGrid Preenchido Exemplo 1:")
    print_grid(filled_grid1)

    # Exemplo 2
    grid2 = [
        [0, 1, 0, 0, 1],
        [0, 1, 0, 0, 1],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 1, 0]
    ]
    print("\nGrid Inicial Exemplo 2:")
    print_grid(grid2)
    filled_grid2 = find_and_fill_all_regions([row[:] for row in grid2]) # Usar copy para não modificar o original
    print("\nGrid Preenchido Exemplo 2:")
    print_grid(filled_grid2)

    print("\n--- Ponto Extra: Geração de Grid Aleatório e Visualização Dinâmica (Textual) ---")
    random_grid = generate_random_grid(5, 7, 0.2)
    print("\nGrid Aleatório Inicial:")
    print_grid(random_grid)
    print("\nIniciando visualização dinâmica (textual) do preenchimento...")
    filled_random_grid = find_and_fill_all_regions([row[:] for row in random_grid], visualize=True)
    print("\nGrid Aleatório Preenchido Final:")
    print_grid(filled_random_grid)


