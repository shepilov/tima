import sympy
from sympy import symbols
from sympy.solvers import solve
#задаем сивол который будет переменной в уравнении
x = symbols('x')

#уравнение равное нулю
eq = input('enter equation: 0 = ')
#решение уравнения
solution = solve(eq, x)
#выводит все корни по очереди
for s in solution:
    print("x = ", s)
#factorise
print(sympy.factor(eq))