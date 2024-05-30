import matplotlib.pyplot as plt
from shapely.geometry import Polygon, LineString, Point

# Заданные точки
A = (-6, 3)
B = (0, -3)
C1 = (1, 2)
C2 = (-2, 3)
C3 = (-4, 0)
C4 = (-1, -2)
C5 = (1, -1)

# Многоугольник и отрезок
polygon = Polygon([C1, C2, C3, C4, C5])
line = LineString([A, B])

# Отсечение отрезка многоугольником
clipped_line = line.intersection(polygon)

# Визуализация
fig, ax = plt.subplots()

# Рисуем многоугольник
polygon_patch = plt.Polygon(polygon.exterior.coords, closed=True, fill=None, edgecolor='black', linewidth=2)
ax.add_patch(polygon_patch)

# Рисуем отрезок
x, y = line.xy
ax.plot(x, y, color='black', linewidth=1)

# Рисуем отсеченный отрезок
if isinstance(clipped_line, LineString):
    x, y = clipped_line.xy
    ax.plot(x, y, color='blue', linewidth=2)
elif isinstance(clipped_line, Point):
    ax.plot(clipped_line.x, clipped_line.y, 'bo')

# Настройки графика
ax.set_aspect('equal')
ax.grid(True)

# Устанавливаем пределы осей
plt.xlim(-7, 2)
plt.ylim(-4, 4)

plt.show()