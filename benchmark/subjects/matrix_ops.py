"""
Matrix Operations module - Subject for test generation benchmarking.
Contains matrix manipulation functions.
"""

from typing import List, Union

Matrix = List[List[Union[int, float]]]


class MatrixError(Exception):
    """Base exception for matrix operations."""
    pass


class DimensionMismatchError(MatrixError):
    """Raised when matrix dimensions don't match for an operation."""
    pass


class InvalidMatrixError(MatrixError):
    """Raised when a matrix is invalid (e.g., ragged rows)."""
    pass


def validate_matrix(matrix: Matrix) -> None:
    """
    Validate that a matrix is well-formed.

    Raises:
        InvalidMatrixError: If the matrix is not a valid 2D list
    """
    if not isinstance(matrix, list):
        raise InvalidMatrixError("Matrix must be a list")
    if len(matrix) == 0:
        raise InvalidMatrixError("Matrix cannot be empty")
    if not all(isinstance(row, list) for row in matrix):
        raise InvalidMatrixError("Each row must be a list")
    row_len = len(matrix[0])
    if row_len == 0:
        raise InvalidMatrixError("Matrix rows cannot be empty")
    if not all(len(row) == row_len for row in matrix):
        raise InvalidMatrixError("All rows must have the same length")


def dimensions(matrix: Matrix) -> tuple:
    """
    Get the dimensions of a matrix.

    Returns:
        Tuple of (rows, columns)
    """
    validate_matrix(matrix)
    return len(matrix), len(matrix[0])


def add(a: Matrix, b: Matrix) -> Matrix:
    """
    Add two matrices element-wise.

    Raises:
        DimensionMismatchError: If matrices have different dimensions
    """
    validate_matrix(a)
    validate_matrix(b)
    rows_a, cols_a = dimensions(a)
    rows_b, cols_b = dimensions(b)
    if rows_a != rows_b or cols_a != cols_b:
        raise DimensionMismatchError(
            f"Cannot add matrices of dimensions ({rows_a}x{cols_a}) and ({rows_b}x{cols_b})"
        )
    return [[a[i][j] + b[i][j] for j in range(cols_a)] for i in range(rows_a)]


def subtract(a: Matrix, b: Matrix) -> Matrix:
    """
    Subtract matrix b from matrix a element-wise.

    Raises:
        DimensionMismatchError: If matrices have different dimensions
    """
    validate_matrix(a)
    validate_matrix(b)
    rows_a, cols_a = dimensions(a)
    rows_b, cols_b = dimensions(b)
    if rows_a != rows_b or cols_a != cols_b:
        raise DimensionMismatchError(
            f"Cannot subtract matrices of dimensions ({rows_a}x{cols_a}) and ({rows_b}x{cols_b})"
        )
    return [[a[i][j] - b[i][j] for j in range(cols_a)] for i in range(rows_a)]


def multiply(a: Matrix, b: Matrix) -> Matrix:
    """
    Multiply two matrices.

    Raises:
        DimensionMismatchError: If inner dimensions don't match
    """
    validate_matrix(a)
    validate_matrix(b)
    rows_a, cols_a = dimensions(a)
    rows_b, cols_b = dimensions(b)
    if cols_a != rows_b:
        raise DimensionMismatchError(
            f"Cannot multiply matrices: ({rows_a}x{cols_a}) * ({rows_b}x{cols_b})"
        )
    result = [[0] * cols_b for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += a[i][k] * b[k][j]
    return result


def scalar_multiply(matrix: Matrix, scalar: Union[int, float]) -> Matrix:
    """Multiply every element by a scalar."""
    validate_matrix(matrix)
    rows, cols = dimensions(matrix)
    return [[matrix[i][j] * scalar for j in range(cols)] for i in range(rows)]


def transpose(matrix: Matrix) -> Matrix:
    """
    Transpose a matrix.

    Returns:
        The transposed matrix
    """
    validate_matrix(matrix)
    rows, cols = dimensions(matrix)
    return [[matrix[i][j] for i in range(rows)] for j in range(cols)]


def identity(n: int) -> Matrix:
    """
    Create an n x n identity matrix.

    Raises:
        ValueError: If n is not a positive integer
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def determinant(matrix: Matrix) -> float:
    """
    Calculate the determinant of a square matrix.

    Raises:
        DimensionMismatchError: If the matrix is not square
    """
    validate_matrix(matrix)
    rows, cols = dimensions(matrix)
    if rows != cols:
        raise DimensionMismatchError("Determinant requires a square matrix")

    if rows == 1:
        return matrix[0][0]
    if rows == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for j in range(cols):
        minor = [row[:j] + row[j + 1:] for row in matrix[1:]]
        cofactor = ((-1) ** j) * matrix[0][j] * determinant(minor)
        det += cofactor
    return det


def is_square(matrix: Matrix) -> bool:
    """Check if a matrix is square."""
    validate_matrix(matrix)
    rows, cols = dimensions(matrix)
    return rows == cols


def trace(matrix: Matrix) -> Union[int, float]:
    """
    Calculate the trace (sum of diagonal elements) of a square matrix.

    Raises:
        DimensionMismatchError: If the matrix is not square
    """
    validate_matrix(matrix)
    if not is_square(matrix):
        raise DimensionMismatchError("Trace requires a square matrix")
    return sum(matrix[i][i] for i in range(len(matrix)))


def flatten(matrix: Matrix) -> List[Union[int, float]]:
    """Flatten a matrix into a 1D list."""
    validate_matrix(matrix)
    return [elem for row in matrix for elem in row]
