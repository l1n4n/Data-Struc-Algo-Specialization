# python3


EPS = 1e-6
PRECISION = 20

class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Position:
    def __init__(self, row, column): # observe the order of the variables!!!
        self.column = column
        self.row = row

def ReadEquation():
    size = int(input())
    a = []
    b = []
    for row in range(size):
        line = list(map(float, input().split()))
        a.append(line[:size])
        b.append(line[size])
    return Equation(a, b)

# def SelectPivotElement(a, used_rows, used_columns):
def SelectPivotElement(a, step):
    # This algorithm selects the first free element.
    # You'll need to improve it to pass the problem.
    # pivot_element = Position(0, 0)
    # while used_rows[pivot_element.row]:
    #     pivot_element.row += 1        
    # while used_columns[pivot_element.column]:
    #     pivot_element.column += 1
    # return pivot_element
    mx = step
    # find the largest(abs) element in the row as the pivot
    for i in range(step+1, len(a)):
        if abs(a[i][step]) > abs(a[mx][step]):
            mx = i
    # if every element is zero, no solution
    if abs(a[mx][step]) < 0.000001:
        raise ValueError('coefficients cannot all be zero.')

    return Position(mx, step)


def SwapLines(a, b, used_rows, pivot_element):
    a[pivot_element.column], a[pivot_element.row] = a[pivot_element.row], a[pivot_element.column]
    b[pivot_element.column], b[pivot_element.row] = b[pivot_element.row], b[pivot_element.column]
    used_rows[pivot_element.column], used_rows[pivot_element.row] = used_rows[pivot_element.row], used_rows[pivot_element.column]
    pivot_element.row = pivot_element.column;

def ProcessPivotElement(a, b, pivot_element): # after swap    

    col = pivot_element.column
    rw = pivot_element.row
    for i in range(col+1, len(b)): 
        scaling_fac = a[i][col] / a[rw][col]
        b[i] -= b[rw] * scaling_fac
        for j in range(col, len(a)):
            a[i][j] -= a[rw][j] * scaling_fac
   

def MarkPivotElementUsed(pivot_element, used_rows, used_columns):
    used_rows[pivot_element.row] = True
    used_columns[pivot_element.column] = True

def SolveEquation(equation):
    a = equation.a
    b = equation.b
    size = len(a)

    used_columns = [False] * size
    used_rows = [False] * size
    # to get the echelon form
    for step in range(size):
        pivot_element = SelectPivotElement(a, step)
        SwapLines(a, b, used_rows, pivot_element)
        ProcessPivotElement(a, b, pivot_element)
        MarkPivotElementUsed(pivot_element, used_rows, used_columns)

    # apply Gauss-Jordan elimination
    for i in range(size-1, -1, -1): 
        coeff = a[i][i]
        if coeff == 0: # no solution
            return None
        for j in range(i+1, size):
            b[i] -= b[j] * a[i][j]
        b[i] /= coeff

    return b

def PrintColumn(column):
    size = len(column)
    for row in range(size):
        print("%.20lf" % column[row])

if __name__ == "__main__":
    equation = ReadEquation()
    solution = SolveEquation(equation)
    PrintColumn(solution)
    # exit(0)
