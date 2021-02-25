#Finished by: Kay Towner
import math
import numpy as np
import matplotlib.pyplot as plt

#Problem 1.)

def function_to_integrate(x):
    """base function.
    """
    return x**2

def analytic_integral_of_f(a=None, b=None):
    """Function to show the analytial ingegral of x^2.
    (x**3) / (3)
    output: the integral of x^2
    """
    a = 0
    b = 1
    return ((b**3) / (3)) - ((a**3) / (3))

def trapezoidal_rule(f, a=None, b=None, n=None):
    """Function to calculate trapazoidal rule.
    """
    xi = (1/2)*(a + b)*n
    return ((f(xi))+(f(xi+1)) / 2 ) * (xi + 1 - xi)

def lefthand_riemann(f, a=None, b=None, n=None):
    """Function to calculate the left-hand riemann
    sum of f(x), for the approx-int
    """
    #generate linear set of n points starting at a, ending at b
    points = np.linspace(a,b,n)
    h = points[1]-points[0]
    integral_approx = 0
    for point in points:
        integral_approx += f(point)*h
    #Fill this in
        
    return integral_approx

def simpson_rule(f, a=None, b=None, n=None):
    """Function to calculate the simpsons rule of
    f(x)
    """
    return (n/3)*(f(-n)+(4*f(0))+f(n))

def relative_error(true=None, estimate=None):
    """Function to calculate the relative error. 
    """
    #Fill this in
    true = analytic_integral_of_f(a=None, b=None)
    estimate = lefthand_riemann(a, b, n)
    relerror = ((true - estimate) / true) * 100
    return relerror

if __name__ == "__main__":
    a = 0
    b = 1
    n = 10

    #lefthand riemann: ##
    print("Lefthand riemann approx to f, between",a, ',', b," steps=",n)
    print(lefthand_riemann(function_to_integrate, a=a, b=b, n=n))
    lefthand = (lefthand_riemann(analytic_integral_of_f, a=a, b=b, n=n))

    #2.
    #trapazoidal:
    print("trapazoidal approx to f, between",a, ',', b," steps=",n)
    print(trapezoidal_rule(function_to_integrate, a=a, b=b, n=n))
    trapezoidal = (trapezoidal_rule(analytic_integral_of_f, a=a, b=b, n=n))

    #3.
    #simpson rule:
    print("simpsons rule approx to f, between",a, ',', b," steps=",n)
    print(simpson_rule(function_to_integrate, a=a, b=b, n=n))
    simpson = (simpson_rule(analytic_integral_of_f, a=a, b=b, n=n))
 
#Plotting:
    x = np.arange(a, b, n)
    fx = np.arange(a, b , n)

    plt.plot(trapezoidal, lefthand, simpson)
    plt.xscale('log', x)
    #plt.yscale(fx)

    plt.title("Integration")
    plt.legend(['lefthand', 'trapezoidal','simpson'])
    
    plt.xlabel("number of steps")
    plt.ylabel("relative error")
    plt.show()



















