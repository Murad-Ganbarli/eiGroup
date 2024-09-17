import numpy as np

def cartesian_spiral_fill(N):
    """ Fill a NxN matrix in a spiral pattern using Cartesian coordinates. """
    matrix = np.zeros((N, N), dtype=int)
    
    # direction vectors (right, down, left, up)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x, y = N // 2, N // 2
    direction = 0  # Starts by moving 'right'
    value = 1 # Initial value to fill in the matrix
    
    steps = 1  # Initial step size (number of steps in one direction)
    
    while value <= N**2:
        for _ in range(2):  # Each step size applies to two directions
            for _ in range(steps):
                if 0 <= x < N and 0 <= y < N:
                    matrix[x, y] = value
                    value += 1
                # Moves in the current direction
                x += directions[direction][0]
                y += directions[direction][1]
            direction = (direction + 1) % 4  # Changes direction after each segment
        
        steps += 1 
    
    return matrix

def calculate_left_diagonal_sum(N):
    n = (N - 1) // 2
    S = 1 + 4*n*(n+1)*(2*n+1)//3 + 2*n
    return S

def calculate_right_diagonal_sum(N):
    n = (N - 1) // 2
    S = 4*n*(n+1)*(2*n+1)//3 + 2*n*(n+1)  + 2*n + 1
    return S
N = 7
matrix = cartesian_spiral_fill(N)
print(matrix)
print(f"Sum of the left diagonal elements using the formula for N = {N} : {calculate_left_diagonal_sum(N)}")
print(f"Sum of the right diagonal elements using the formula for N = {N}: {calculate_right_diagonal_sum(N)}")

