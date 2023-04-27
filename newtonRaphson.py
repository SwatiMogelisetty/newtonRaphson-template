def newtonRaphson(g, x0, eps, delta, itermax):
#    Summary of this function goes here
#
#   Inputs:
# g - Description of variable a, including expected data type and/or values
# x0 - Description of variable b, including expected data type and/or values
#
# Outputs:
# c - Description of variable c, including expected data type and/or values
# d - Description of variable d, including expected data type and/or values
    x = x0
    for i in range(itermax):
        f, fx = g(x)
        if abs(f) < eps:
            return x, i
        dx = f / fx
        x -= dx
        if abs(dx) > delta:
            raise Exception("Error: Divergence")
    raise Exception("Error: Maximum Number of Iterations")