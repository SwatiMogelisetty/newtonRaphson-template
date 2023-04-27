def newtonRaphson(g, x0, eps, delta, itermax):
#    Summary of this function goes here
#
#   Inputs:
#       g - An external function which returns the value of the function and its derivative at a given x.
#       x0 - The initial guess.
#       eps - The alue to define convergence criteria.
#       delta - The value to define divergence criteria.
#       itermax - The maximum number of iterations to allowed.
#   Outputs:
#       x - The root of the function.
#       iter - The number of iterations it took to get to the root.
    f, fx = g(x0)
    x = x0 - f/fx
    iter = 1
    x_prev = x0
    x_new = x
    diff = abs(x_new - x_prev)
    if diff < eps and iter <= itermax:
        return x, iter
    if diff > delta or iter > itermax:
        raise Exception("Error: there is divergence or the maximum number of iterations is exceeded")
    
    while iter < itermax:
        f, fx = g(x_new)
        x_prev = x_new
        x_new = x_prev - f/fx
        iter += 1
        diff = abs(x_new - x_prev)
        if diff < eps:
            return x_new, iter
    raise Exception("Error: Maximum Number of Iterations")