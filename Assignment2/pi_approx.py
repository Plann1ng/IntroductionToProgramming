from math import sin, cos, pi


def path(x, y):
    from math import sqrt
    s = 0
    n = len(x)
    for i in range(1, n):
        s += sqrt((x[i] - x[i-1])**2 + (y[i] - y[i-1])**2)
    return s


print("    N    approximation       error")
for k in range(2, 5):
    N = 10**k
    x = [1/2*cos(2.*pi*i/N) for i in range(N+1)]
    y = [1/2*sin(2.*pi*i/N) for i in range(N+1)]
    approx = path(x, y)
    print('%5d %16f %11.2e' % (N, approx, abs(pi - approx)))



    
