import matplotlib.pyplot as plt
from matplotlib.path import Path

def sign(ch):
    if ch == 0: return 0
    if ch > 0: return 1
    if ch < 0: return -1

def CordsToVectors(cords):
    vec = []
    for i in range(len(cords) - 1):
        vec.append([cords[i+1][0] - cords[i][0], cords[i+1][1] - cords[i+1][0]])
    return vec
def IsVipucliy(cords):
    vec = CordsToVectors(cords)
    sgn = sign(vec[0][0] * vec[1][ 1] - vec[0][1] * vec[1][0])
    for i in range(1, len(vec)-1):
        cur = sign(vec[i][0] * vec[i + 1][1] - vec[i][1] * vec[i + 1][0])
        if not cur == sgn:
            if not cur == 0:
                return False
    return True
def IsSamoneperesec(cords):
    if IsVipucliy(cords):
        return 1
    else:
      return -1
def Graph(cords):
    cords.append(cords[0])
    xs, ys = zip(*cords)
    plt.figure()
    plt.plot(xs, ys)
    plt.show()

cords1 = [[-2, -4], [5, 2], [-5, 5], [-1, -1], [-3, -1]]
print(IsVipucliy(cords1))
print(IsSamoneperesec(cords1))
Graph(cords1)

# 2 задание
cords2 = [(1, 1), (4, 3), (5, 6), (4, 4), (3, 5)]
# создаем путь на основе вершин полигона
path = Path(cords2)

# проверяем точки
points = [(1, -2), (3, 3), (2, 3)]
for point in points:
    # проверяем, лежит ли точка внутри полигона
    if path.contains_point(point):
        print(f"Точка {point} лежит внутри полигона")
    else:
        print(f"Точка {point} лежит снаружи полигона")

Graph(cords2)