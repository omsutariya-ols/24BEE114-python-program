print("OM SUTARIYA")
print("24BEE114")
class Matrix:
    def __init__(self, data):
        if len(data) != 3 or len(data[0]) != 3 or len(data[1]) != 3 or len(data[2]) != 3:
            raise ValueError("Matrix must be 3x3.")
        self.data = data

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.data])

    def add(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("Operand must be a Matrix.")
        return Matrix([[self.data[i][j] + other.data[i][j] for j in range(3)] for i in range(3)])

    def multiply(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("Operand must be a Matrix.")
        result = [[0] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    result[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(result)

    def transpose(self):
        return Matrix([[self.data[j][i] for j in range(3)] for i in range(3)])

if __name__ == "__main__":
    A = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    B = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

    print("Matrix A:")
    print(A)
    print("\nMatrix B:")
    print(B)

    print("\nA + B:")
    print(A.add(B))

    print("\nA * B:")
    print(A.multiply(B))

    print("\nTranspose of A:")
    print(A.transpose())
