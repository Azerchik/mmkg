import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Заданные углы
delta_yx = -np.arccos(1 / 8)
delta_yz = np.arccos(np.sqrt(7) / 4)

# Создаем матрицы поворота
rotation_matrix_yx = np.array([
    [np.cos(delta_yx), 0, np.sin(delta_yx)],
    [0, 1, 0],
    [-np.sin(delta_yx), 0, np.cos(delta_yx)]
])

rotation_matrix_yz = np.array([
    [1, 0, 0],
    [0, np.cos(delta_yz), -np.sin(delta_yz)],
    [0, np.sin(delta_yz), np.cos(delta_yz)]
])

# Объединенная матрица поворота
rotation_matrix = np.dot(rotation_matrix_yz, rotation_matrix_yx)

# Координаты вершин тетраэдра
vertices = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])

# Применяем поворот
transformed_vertices = np.dot(vertices, rotation_matrix.T)

# Создаем фигуру и оси для 3D-проекции
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Определяем грани тетраэдра
faces = [
    [transformed_vertices[0], transformed_vertices[1], transformed_vertices[2]],
    [transformed_vertices[0], transformed_vertices[1], transformed_vertices[3]],
    [transformed_vertices[0], transformed_vertices[2], transformed_vertices[3]],
    [transformed_vertices[1], transformed_vertices[2], transformed_vertices[3]]
]

# Добавляем грани на график
ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

# Подписи осей
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Устанавливаем лимиты осей
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])

# Показать график
plt.show()