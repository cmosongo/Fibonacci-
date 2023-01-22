# Python program for Plotting Fibonacci
# spiral fractal using Turtle
import turtle
import math


cache = {0: 0, 1: 1}
def fibonacci_of(n = 5):
    if n in cache:  # Base case
        return cache[n]
    # Compute and cache the Fibonacci number
    cache[n] = fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case
    return cache[n]


def fiboPlot(fib_values):
	# Setting the colour of the plotting pen to blue
	x.pencolor("blue")

	# Drawing the first square
	x.forward(fib_values[1] * factor)
	x.left(90)
	x.forward(fib_values[1] * factor)
	x.left(90)
	x.forward(fib_values[1]  * factor)
	x.left(90)
	x.forward(fib_values[1]  * factor)
	
	# Drawing the rest of the squares
	for i in range(2, n):
		x.backward(fib_values[i-1] * factor)
		x.right(90)
		x.forward(fib_values[i]  * factor)
		x.left(90)
		x.forward(fib_values[i]  * factor)
		x.left(90)
		x.forward(fib_values[i]  * factor)

	# Bringing the pen to starting point of the spiral plot
	x.penup()
	x.setposition(factor, 0)
	x.seth(0)
	x.pendown()

	# Setting the colour of the plotting pen to red
	x.pencolor("red")

	# Fibonacci Spiral Plot
	for i in range(n):
		print(fib_values[i] )
		fdwd = math.pi * fib_values[i]  * factor / 2
		fdwd /= 90
		for j in range(90):
			x.forward(fdwd)
			x.left(1)


# Here 'factor' signifies the multiplicative
# factor which expands or shrinks the scale
# of the plot by a certain factor.
factor = 2

# Taking Input for the number of
# Iterations our Algorithm will run
n = int(input('Enter the number of iterations (must be > 1): '))

# Plotting the Fibonacci Spiral Fractal
# and printing the corresponding Fibonacci Number
if n > 0:
	print("Fibonacci series for", n, "elements :")
	x = turtle.Turtle()
	fib_values = [fibonacci_of(i) for i in range(n)]
	x.speed(1000)
	fiboPlot(fib_values)
	turtle.done()
else:
	print("Number of iterations must be > 0")

		   

