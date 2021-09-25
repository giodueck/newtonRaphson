from math import exp

# variables and functions
f = lambda x : exp(-x) * (2 - x ** 3)                   # original function
fprime = lambda x : exp(-x) * (x ** 3 - 3 * x * x - 2)  # derivative of f
precision = 10 ** -6                                    # desired precision
x0 = 1                                                  # starting guess. Has to be close to result, otherwise div by 0 occurs

# Takes in xn and returns x(n+1) based off of f, fprime and precision
def newtonRaphson(xn, n = 0):
    xm = xn - f(xn) / fprime(xn)
    n += 1

    # precision checking
    if (abs(xm - xn) < 0.5 * precision):
        return xn, n - 1
    else:
        return newtonRaphson(xm, n)

# Main procedure
def main():
    print("x0 = ", x0)
    x, n = newtonRaphson(x0)
    print("xn = ", x)
    print("Iterations: n = ", n)

# Runs program
if __name__ == '__main__':
    main()