import numpy as np
import matplotlib.pyplot as plt

# Заданная матрица A
A = np.array([[1, 0],
              [2, 4]])

# Новые базисные векторы
e1_new = np.array([3, 2])
e2_new = np.array([2, 2])

# Матрица перехода от нового базиса к старому
P = np.column_stack((e1_new, e2_new))

# Обратная матрица перехода
P_inv = np.linalg.inv(P)

# Преобразованная матрица
A_new = P_inv @ A @ P

print("Матрица оператора в новом базисе:")
print(A_new)

# Визуализация
fig, ax = plt.subplots()

# Векторы старого базиса
ax.quiver(0, 0, 1, 0, angles='xy', scale_units='xy', scale=1, color='r', label='e1')
ax.quiver(0, 0, 0, 1, angles='xy', scale_units='xy', scale=1, color='b', label='e2')

# Векторы нового базиса
ax.quiver(0, 0, e1_new[0], e1_new[1], angles='xy', scale_units='xy', scale=1, color='g', label="e'1")
ax.quiver(0, 0, e2_new[0], e2_new[1], angles='xy', scale_units='xy', scale=1, color='y', label="e'2")

# Настройки графика
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 5)
ax.set_aspect('equal')
ax.grid(True)
ax.legend()
plt.title("Старый и новый базисы")
plt.xlabel("x")
plt.ylabel("y")
plt.show()