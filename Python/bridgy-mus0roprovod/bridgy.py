def calc_distance(x1, x2, func1, func2):
    return abs(func2(x1) - func1(x2))

def bridgy(func1, func2, dx=0.001):
    x0 = 0.0
    while True:
        x1 = x0 + dx
        if calc_distance(x0, 0, func1, func2) - calc_distance(x1, 0, func1, func2) <= 0:
            break
        x0 = x1
    opt_x1 = x0
    x0 = 0.0
    while True:
        x1 = x0 + dx
        if calc_distance(0, x0, func1, func2) - calc_distance(0, x1, func1, func2) <= 0:
            break
        x0 = x1
    opt_x2 = x0
    return opt_x1, opt_x2
