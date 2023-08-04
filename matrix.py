class Matrix: 
    def __init__(self, data): 
        self.data = data 
 
    def __str__(self): 
        return '\n'.join([' '.join(map(str, row)) for row in self.data]) 
 
    def __add__(self, other): 
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]): 
            raise ValueError("Матрицы должны быть одного размера для сложения.") 
         
        result_data = [] 
        for i in range(len(self.data)): 
            row = [self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))] 
            result_data.append(row) 
         
        return Matrix(result_data) 
 
    def __sub__(self, other): 
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]): 
            raise ValueError("Матрицы должны быть одного размера для вычитания.") 
         
        result_data = [] 
        for i in range(len(self.data)): 
            row = [self.data[i][j] - other.data[i][j] for j in range(len(self.data[0]))] 
            result_data.append(row) 
         
        return Matrix(result_data) 
 
    def __mul__(self, other): 
        if len(self.data[0]) != len(other.data): 
            raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы для умножения.") 
         
        result_data = [] 
        for i in range(len(self.data)): 
            row = [] 
            for j in range(len(other.data[0])): 
                element = sum(self.data[i][k] * other.data[k][j] for k in range(len(self.data[0]))) 
                row.append(element) 
            result_data.append(row) 
 
        return Matrix(result_data) 
    # Создаем две матрицы 
matrix1 = Matrix([[1, 2], [3, 4]]) 
matrix2 = Matrix([[5, 6], [7, 8]]) 
 
# Тестируем сложение матриц 
result_add = matrix1 + matrix2 
print("Сложение матриц:") 
print(result_add) 
 
# Тестируем вычитание матриц 
result_sub = matrix1 - matrix2 
print("Вычитание матриц:") 
print(result_sub) 
 
# Тестируем умножение матриц 
result_mul = matrix1 * matrix2 
print("Умножение матриц:") 
print(result_mul) 