import matplotlib.pyplot as plt

# Function to compute the region code for a point (x, y)
def compute_code(x, y, xmin, xmax, ymin, ymax):
    code = 0
    if x < xmin:
        code |= 1  # Left
    elif x > xmax:
        code |= 2  # Right
    if y < ymin:
        code |= 4  # Bottom
    elif y > ymax:
        code |= 8  # Top
    return code

# Cohen-Sutherland clipping algorithm
def cohen_sutherland_clip(x0, y0, x1, y1, xmin, xmax, ymin, ymax):
    code0 = compute_code(x0, y0, xmin, xmax, ymin, ymax)
    code1 = compute_code(x1, y1, xmin, xmax, ymin, ymax)
    accept = False

    while True:
        if code0 == 0 and code1 == 0:  # Trivially accept
            accept = True
            break
        elif (code0 & code1) != 0:  # Trivially reject
            break
        else:
            x, y = 0.0, 0.0
            # Pick the outside point
            if code0 != 0:
                code_out = code0
            else:
                code_out = code1

            # Calculate the intersection point
            if code_out & 8:  # Top
                x = x0 + (x1 - x0) * (ymax - y0) / (y1 - y0)
                y = ymax
            elif code_out & 4:  # Bottom
                x = x0 + (x1 - x0) * (ymin - y0) / (y1 - y0)
                y = ymin
            elif code_out & 2:  # Right
                y = y0 + (y1 - y0) * (xmax - x0) / (x1 - x0)
                x = xmax
            elif code_out & 1:  # Left
                y = y0 + (y1 - y0) * (xmin - x0) / (x1 - x0)
                x = xmin

            # Replace the outside point with the intersection point
            if code_out == code0:
                x0, y0 = x, y
                code0 = compute_code(x0, y0, xmin, xmax, ymin, ymax)
            else:
                x1, y1 = x, y
                code1 = compute_code(x1, y1, xmin, xmax, ymin, ymax)

    if accept:
        return [(x0, y0), (x1, y1)]
    else:
        return []

# Window boundaries
xmin, xmax = 0, 10
ymin, ymax = 0, 7

# Line segment endpoints
A = (10, -1)
B = (0, 2)

# Clip the line segment
clipped_segment = cohen_sutherland_clip(A[0], A[1], B[0], B[1], xmin, xmax, ymin, ymax)

# Visualization using Matplotlib
fig, ax = plt.subplots()

# Draw the clipping window
rect = plt.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin, fill=None, edgecolor='black')
ax.add_patch(rect)

# Draw the original line segment
ax.plot([A[0], B[0]], [A[1], B[1]], 'r--', label='Исходный отрезок')

# Draw the clipped line segment
if clipped_segment:
    ax.plot([clipped_segment[0][0], clipped_segment[1][0]], [clipped_segment[0][1], clipped_segment[1][1]], 'b-', label='Отсеченный отрезок')

# Set the limits of the plot
ax.set_xlim(-5, 15)
ax.set_ylim(-5, 10)

# Add a grid, legend, and labels
ax.grid(True)
ax.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Отсечение отрезка алгоритмом Коэна-Сазерленда')

# Show the plot
plt.show()