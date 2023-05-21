import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to visualize matrix
def visualize_matrix(matrix):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    nx, ny = matrix.shape
    x = range(nx)
    y = range(ny)
    
    X, Y = np.meshgrid(x, y)
    Z = matrix[X, Y]
    
    ax.scatter(X, Y, Z)
    plt.show()

# Function to get user input for matrix size
def get_matrix_size():
    options = list(range(1, 11))
    matrix_sizes = [2 * option for option in options]
    print("Valid matrix sizes to pick from: ")
    for i, size in enumerate(matrix_sizes, 1):
        print(f"{i}: {size} x {size}")

    while True:
        n = int(input("Enter the option number for the size of the matrix: "))
        if n in options:
            break
        else:
            print("Invalid choice. Please choose a valid option.")
    
    return matrix_sizes[n-1]  # subtract one because list indices start at zero

# Function to generate random matrices of a given size
def generate_matrices(n):
    A = np.random.rand(n, n)
    B = np.random.rand(n, n)
    return A, B

# Matrix multiplication function
def multiply_matrices(A, B):
    C = np.dot(A, B)
    return C

# Main program
def main():
    n = get_matrix_size()
    A, B = generate_matrices(n)
    C = multiply_matrices(A, B)
    
    print("Matrix A:")
    print(A)
    
    print("Matrix B:")
    print(B)
    
    print("Matrix C (result of A x B):")
    print(C)
    
    print("Visualizing matrix C:")
    visualize_matrix(C)

if __name__ == "__main__":
    main()
