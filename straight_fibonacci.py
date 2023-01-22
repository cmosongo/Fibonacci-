# Python program for Plotting Fibonacci
# spiral fractal using Turtle
import turtle
import math


start_x = -600
start_y = -300

cache = {0: 0, 1: 1}
def fibonacci_of(n = 5):
    if n in cache:  # Base case
        return cache[n]
    # Compute and cache the Fibonacci number
    cache[n] = fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case
    return cache[n]


def fiboPlot(fib_values):
    x.penup()
    x.setposition(start_x,start_y)
    x.pendown()
    for z in range(1,n):
        x.forward(fib_values[z] * factor)
        x.left(90)
        x.forward(fib_values[z] * factor)
        x.left(90)
        x.forward(fib_values[z] * factor)
        x.left(90)
        x.forward(fib_values[z]  * factor)
        x.left(90)
        x.forward(fib_values[z]  * factor)
        

    x.pencolor("red")    
    x.penup()
    x.setposition(start_x,start_y)
    x.left(90)
    x.pendown()


    for z in range(1,n):
        print(fib_values[z])
        
        fdwd = math.pi * fib_values[z] * factor *0.5
        fdwd /= 90

        if z%2 == 0:
            x.left(90)
            x.forward((fib_values[z] -fib_values[z-1]) *factor)
            x.right(90)
            for j in range(90):
                x.forward(fdwd)
                x.right(1)
            x.left(180)

        if z%2 != 0:
            for j in range(90):
                x.forward(fdwd)
                x.right(1)



# Taking Input for the number of
# Iterations our Algorithm will run
n = int(input('Enter the number of iterations (must be > 1): '))
factor = 5

# Plotting the Fibonacci Spiral Fractal
# and printing the corresponding Fibonacci Number
if n > 0:
	print("Fibonacci series for", n, "elements :")
	fib_values = [fibonacci_of(i) for i in range(n)]
	x = turtle.Turtle()
	x.speed(1000)
	fiboPlot(fib_values)
	turtle.done()
else:
	print("Number of iterations must be > 0")






		   

