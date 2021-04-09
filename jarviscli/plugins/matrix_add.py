from plugin import plugin
from colorama import Fore

@plugin("matrix add")
class Matrix:

    def __call__(self, jarvis, s): 
        self.matrix_add(jarvis, s)

    def get_matrix(self, jarvis, r, c):
        matrix = []

        for i in range(r):
            row_str = jarvis.input("enter row #{:d}: ".format(i))
            cur_row = []
            for n in row_str.split():
                try:
                    int(n)
                except BaseException:
                    cur_row.append(0)
                else:
                    cur_row.append(int(n))

            while len(cur_row) != c:
                row_str = jarvis.input("enter row #{:d}: ".format(i))

                for n in row_str.split():
                    try:
                        int(n)
                    except BaseException:
                        cur_row.append(0)
                    else:
                        cur_row.append(int(n))
            matrix.append(cur_row)
        return matrix


    def print_matrix(self, matrix, r, c):
        for i in range(r):
            print(matrix[i])

    def sum(self, matrix1, matrix2, row, col):
        for i in range(row):
            for j in range(col):
                matrix1[i][j] += matrix2[i][j]
        return matrix1
    
    def matrix_add(self, jarvis, s):
        print("Sum of matrices with dimensions M x N", Fore.GREEN)

        row = int(jarvis.input_number('Enter M (rows): '))
        col = int(jarvis.input_number('Enter N (cols): '))

        initial = self.get_matrix(jarvis, row, col)

        print("\nEnter Next Matrix:")
        next_matrix = self.get_matrix(jarvis, row, col)
        self.sum(initial, next_matrix, row, col)
    
        print("\nFinal Sum:")
        self.print_matrix(initial, row, col)
