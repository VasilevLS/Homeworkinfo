gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


class Star():
    """Тип данных, описывающий звезду."""
    type = "star"
    m = 0
    x = 0
    y = 0
    Vx = 0
    Vy = 0
    Fx = 0
    Fy = 0
    R = 5
    color = "red"
    image = None


class Planet():
    """Тип данных, описывающий планету."""
    type = "planet"
    m = 0
    x = 0
    y = 0
    Vx = 0
    Vy = 0
    Fx = 0
    Fy = 0
    R = 5
    color = "green"
    image = None


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело."""
    body.Fx = body.Fy = 0.0
    for obj in space_objects:
        if body == obj:
            continue  # Пропускаем сам объект

        # Вычисляем расстояние между телами
        dx = obj.x - body.x
        dy = obj.y - body.y
        r = (dx ** 2 + dy ** 2) ** 0.5

        # Избегаем деления на ноль
        if r == 0:
            continue

        # Вычисляем силу по закону всемирного тяготения Ньютона
        F = gravitational_constant * body.m * obj.m / (r ** 2)

        # Вычисляем проекции силы на оси
        cos_alpha = dx / r
        sin_alpha = dy / r
        body.Fx += F * cos_alpha
        body.Fy += F * sin_alpha


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой."""
    # Вычисляем ускорение по второму закону Ньютона: a = F/m
    ax = body.Fx / body.m
    ay = body.Fy / body.m

    # Обновляем скорость по формуле: v = v0 + a * dt
    body.Vx += ax * dt
    body.Vy += ay * dt

    # Обновляем координаты по формуле: x = x0 + v * dt
    body.x += body.Vx * dt
    body.y += body.Vy * dt


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов."""
    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")