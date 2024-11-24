def besh_algo(P1,P2):
    x_points = [P2[0]]
    y_points = [P2[1]]

    slope = (P2[1] - P1[1]) / (P2[0] - P1[0])

    current_x = P2[0]
    while current_x > P1[0]:
        current_x = current_x - 1
        x_points.append(current_x)
        y_points.append(round(slope * current_x))
    return x_points, y_points

p1 = (0,0)
p2 = (10,5).

x_p, y_p = besh_algo(p1,p2)
print(x_p)
print(y_p)
