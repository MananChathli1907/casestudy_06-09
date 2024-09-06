import tkinter as tk
from calculator import add, subtract, multiply, divide

def perform_operation():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operation = operation_var.get()

    if operation == 'Add':
        result = add(num1, num2)
    elif operation == 'Subtract':
        result = subtract(num1, num2)
    elif operation == 'Multiply':
        result = multiply(num1, num2)
    elif operation == 'Divide':
        try:
            result = divide(num1, num2)
        except ValueError as e:
            result_label.config(text=str(e))
            return

    result_label.config(text=f"Result: {result}")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create and place the widgets
tk.Label(root, text="Enter first number:").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Enter second number:").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

tk.Label(root, text="Choose operation:").grid(row=2, column=0)
operation_var = tk.StringVar(root)
operation_var.set("Add")  # default value
operations_menu = tk.OptionMenu(root, operation_var, "Add", "Subtract", "Multiply", "Divide")
operations_menu.grid(row=2, column=1)

tk.Button(root, text="Calculate", command=perform_operation).grid(row=3, column=0, columnspan=2)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2)

# Run the application
root.mainloop()
