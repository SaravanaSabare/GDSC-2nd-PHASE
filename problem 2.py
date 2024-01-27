def sort_non_boundary(matrix):
    # Extract non-boundary elements, sort, and update the matrix
    non_boundary_elements = [matrix[i][j] for i in range(1, len(matrix) - 1) for j in range(1, len(matrix[0]) - 1)]
    non_boundary_elements.sort()
    k = 0
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            matrix[i][j] = non_boundary_elements[k]
            k += 1

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def main():
    order = int(input("Enter the Order: "))
    
    # Input Matrix
    print("Enter the Matrix:")
    matrix = [list(map(int, input().split())) for _ in range(order)]

    # Sort non-boundary elements
    sort_non_boundary(matrix)

    # Print Sorted Matrix
    print("\nSorted Matrix:")
    print_matrix(matrix)

    # Calculate and Print Sum of Diagonal Elements
    diagonal_sum = sum(matrix[i][i] for i in range(min(order, len(matrix[0]))))
    print("\nSum of Diagonals:", diagonal_sum)

if __name__ == "__main__":
    main()
