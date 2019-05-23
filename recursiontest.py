from tkinter import *

fibonacci_cache = {}
def Fibonacci(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = Fibonacci(n-1) + Fibonacci(n-2)
    fibonacci_cache[n] = value
    return value
def main():
    for n in range(1,10):
        root = Tk()
        thelabel = Label(root, text = Fibonacci(n))
        thelabel.pack()
    root.mainloop()
      
main()
