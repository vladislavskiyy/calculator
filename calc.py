import tkinter as tk
import math


def plus(a, b):
    return float(a + b)


def minus(a, b):
    return float(a - b)


def mul(a, b):
    return float(a * b)


def div(a, b):
    return float(a / b)


def sin(a):
    return math.sin(a)


def cos(a):
    return math.cos(a)


def floor(a):
    return math.floor(a)


def ceil(a):
    return math.ceil(a)


def mod(a, b):
    return a % b


root = tk.Tk()
root.title("Калькулятор")
root.geometry("400x200")


def calculate():
    try:
        num1 = float(entry1.get())
        operation = dropdown.get()

        if operation in ['sin', 'cos', 'floor', 'ceil']:
            entry2.config(state='disabled')
            num2 = None
        else:
            entry2.config(state='normal')
            num2 = float(entry2.get())

        if operation == '/' and num2 == 0:
            result_label.config(text="Ошибка, нельзя делить на 0")
            return

        if operation == '+':
            result = plus(num1, num2)
        elif operation == '-':
            result = minus(num1, num2)
        elif operation == '*':
            result = mul(num1, num2)
        elif operation == '/':
            result = div(num1, num2)
        elif operation == 'sin':
            result = sin(num1)
        elif operation == 'cos':
            result = cos(num1)
        elif operation == 'floor':
            result = floor(num1)
        elif operation == 'ceil':
            result = ceil(num1)
        elif operation == 'mod':
            result = mod(num1, num2)
        else:
            result = "Ошибка"

        result_label.config(text="Результат: " + str(result))
    except ValueError:
        result_label.config(text="Непредвиденная ошибка")


def on_dropdown_change(*args):
    operation = dropdown.get()
    if operation in ['sin', 'cos', 'floor', 'ceil']:
        entry2.delete(0, tk.END)
        entry2.config(state='disabled')
    else:
        entry2.config(state='normal')


entry1 = tk.Entry(root, width=20)
entry1.pack()
entry2 = tk.Entry(root, width=20)
entry2.pack()

dropdown = tk.StringVar(root)
dropdown.set('+')
options = ['+', '-', '*', '/', 'sin', 'cos', 'floor', 'ceil', 'mod']
dropdown.trace('w', on_dropdown_change)
dropdown_menu = tk.OptionMenu(root, dropdown, *options)
dropdown_menu.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

result_label = tk.Label(root, text="Result:")
result_label.pack()

root.mainloop()
