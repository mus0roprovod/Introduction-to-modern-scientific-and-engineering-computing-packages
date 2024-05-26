import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
def zhukko(room_side, speed):
    initial_positions = [
        [0, 0],
        [room_side, 0],
        [room_side, room_side],
        [0, room_side]
    ]
    def equations(t, positions):
        x1, y1, x2, y2, x3, y3, x4, y4 = positions
        dx1 = speed * (x2 - x1) / np.linalg.norm([x2 - x1, y2 - y1])
        dy1 = speed * (y2 - y1) / np.linalg.norm([x2 - x1, y2 - y1])
        dx2 = speed * (x3 - x2) / np.linalg.norm([x3 - x2, y3 - y2])
        dy2 = speed * (y3 - y2) / np.linalg.norm([x3 - x2, y3 - y2])
        dx3 = speed * (x4 - x3) / np.linalg.norm([x4 - x3, y4 - y3])
        dy3 = speed * (y4 - y3) / np.linalg.norm([x4 - x3, y4 - y3])
        dx4 = speed * (x1 - x4) / np.linalg.norm([x1 - x4, y1 - y4])
        dy4 = speed * (y1 - y4) / np.linalg.norm([x1 - x4, y1 - y4])
        return [dx1, dy1, dx2, dy2, dx3, dy3, dx4, dy4]
    initial_conditions = [coord for pos in initial_positions for coord in pos]
    t_span = (0, 10)
    t_eval = np.linspace(t_span[0], t_span[1], 1000)
    sol = solve_ivp(equations, t_span, initial_conditions, t_eval=t_eval)
    x1, y1, x2, y2, x3, y3, x4, y4 = sol.y
    plt.plot(x1, y1)
    plt.plot(x2, y2)
    plt.plot(x3, y3)
    plt.plot(x4, y4)
    plt.grid(True)
    plt.show()
