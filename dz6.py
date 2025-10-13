class Vector:
    def __init__(self, x, y=None, z=None):
        if y is None and z is None:
            # Обработка строки формата "{x, y, z}"
            if isinstance(x, str):
                x = x.strip('{} ')
                parts = x.split(',')
                if len(parts) != 3:
                    raise ValueError("Строка должна быть в формате '{x, y, z}'")
                x = float(parts[0].strip())
                y = float(parts[1].strip())
                z = float(parts[2].strip())
            else:
                raise ValueError("Неверные аргументы")
        else:
            x = float(x)
            y = float(y)
            z = float(z)

        # Проверка, что все координаты - числа
        assert all(isinstance(coord, (int, float)) for coord in [x, y, z]), "Координаты должны быть числами"

        self.x = x
        self.y = y
        self.z = z

    def __abs__(self):
        """Модуль вектора"""
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __add__(self, other):
        """Сложение векторов"""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        raise TypeError("Можно складывать только векторы")

    def __sub__(self, other):
        """Вычитание векторов"""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        raise TypeError("Можно вычитать только векторы")

    def __mul__(self, other):
        """Умножение: вектор * вектор = скалярное произведение, вектор * число = умножение на скаляр"""
        if isinstance(other, Vector):
            # Скалярное произведение
            return self.x * other.x + self.y * other.y + self.z * other.z
        elif isinstance(other, (int, float)):
            # Умножение на число
            return Vector(self.x * other, self.y * other, self.z * other)
        raise TypeError("Можно умножать только на вектор или число")

    def __rmul__(self, other):
        """Умножение числа на вектор"""
        if isinstance(other, (int, float)):
            return self * other
        raise TypeError("Можно умножать только на вектор или число")

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"


def vector_cross_product(v1, v2):
    """Векторное произведение двух векторов"""
    x = v1.y * v2.z - v1.z * v2.y
    y = v1.z * v2.x - v1.x * v2.z
    z = v1.x * v2.y - v1.y * v2.x
    return Vector(x, y, z)


def triangle_area(p1, p2, p3):
    """Площадь треугольника по трем точкам"""
    v1 = p2 - p1
    v2 = p3 - p1
    cross = vector_cross_product(v1, v2)
    return abs(cross) / 2


def center_of_mass(points):
    """Упражнение 1.1: координаты центра масс множества точек"""
    if not points:
        return Vector(0, 0, 0)

    sum_x = sum_y = sum_z = 0
    for point in points:
        sum_x += point.x
        sum_y += point.y
        sum_z += point.z

    n = len(points)
    return Vector(sum_x / n, sum_y / n, sum_z / n)


def find_max_triangle_area(points):
    """Упражнение 1.2: найти три точки, образующие треугольник с наибольшей площадью"""
    max_area = 0
    best_triangle = None

    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                area = triangle_area(points[i], points[j], points[k])
                if area > max_area:
                    max_area = area
                    best_triangle = (points[i], points[j], points[k])

    return max_area, best_triangle


# Демонстрация работы
if __name__ == "__main__":
    print("=" * 50)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ КЛАССА Vector")
    print("=" * 50)

    # Создание векторов разными способами
    v1 = Vector(1, 2, 3)
    v2 = Vector("{4, 5, 6}")
    v3 = Vector(7.5, 8.5, 9.5)

    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print(f"v3 = {v3}")
    print()

    # Операции с векторами
    print("ОПЕРАЦИИ С ВЕКТОРАМИ:")
    print(f"v1 + v2 = {v1 + v2}")
    print(f"v1 - v2 = {v1 - v2}")
    print(f"v1 * v2 (скалярное) = {v1 * v2}")
    print(f"v1 * 2 = {v1 * 2}")
    print(f"3 * v1 = {3 * v1}")
    print(f"|v1| = {abs(v1):.2f}")
    print()

    # Упражнение 1.1 - Центр масс
    print("УПРАЖНЕНИЕ 1.1 - ЦЕНТР МАСС")
    points = [
        Vector(0, 0, 0),
        Vector(1, 0, 0),
        Vector(0, 1, 0),
        Vector(0, 0, 1)
    ]

    center = center_of_mass(points)
    print("Точки:")
    for i, point in enumerate(points):
        print(f"  P{i + 1} = {point}")
    print(f"Центр масс: {center}")
    print()

    # Упражнение 1.2 - Максимальная площадь треугольника
    print("УПРАЖНЕНИЕ 1.2 - МАКСИМАЛЬНАЯ ПЛОЩАДЬ ТРЕУГОЛЬНИКА")
    test_points = [
        Vector(0, 0, 0),
        Vector(3, 0, 0),
        Vector(0, 4, 0),
        Vector(0, 0, 5),
        Vector(1, 1, 1)
    ]

    max_area, triangle = find_max_triangle_area(test_points)

    print("Точки для анализа:")
    for i, point in enumerate(test_points):
        print(f"  P{i + 1} = {point}")

    print(f"\nТреугольник с максимальной площадью:")
    print(f"  Вершина 1: {triangle[0]}")
    print(f"  Вершина 2: {triangle[1]}")
    print(f"  Вершина 3: {triangle[2]}")
    print(f"  Площадь: {max_area:.2f}")

    # Проверка на известном треугольнике (3-4-5)
    p1 = Vector(0, 0, 0)
    p2 = Vector(3, 0, 0)
    p3 = Vector(0, 4, 0)
    area_3_4_5 = triangle_area(p1, p2, p3)

