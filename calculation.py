# -*- coding: Utf-8 -*

def derivative_point(actual: tuple, previous: tuple, next_: tuple):
    volume_prev, ph_prev = previous
    volume, ph = actual
    volume_next, ph_next = next_
    derivative_left = (ph - ph_prev) / (volume - volume_prev)
    derivative_right = (ph_next - ph) / (volume_next - volume)
    coeff_left = (volume_next - volume) / (volume_next - volume_prev)
    coeff_right = (volume - volume_prev) / (volume_next - volume_prev)
    return (derivative_left * coeff_left) + (derivative_right * coeff_right)

def interpolation(x: float, x_a: float, x_b: float, y_a: float, y_b: float):
    y = y_a + ((x - x_a) * (y_b - y_a) / (x_b - x_a))
    return y

def get_first_derivatives(values: list):
    d_list = list()
    for i in range(1, len(values) - 1):
        volume = values[i][0]
        d = derivative_point(values[i], values[i - 1], values[i + 1])
        d_list.append((volume, d))
    return d_list, max(d_list, key=lambda e: e[1])[0]

def get_second_derivatives(values: list, equivalent_volume: int):
    d_list = list()
    bounds_index = list()
    for i in range(1, len(values) - 1):
        volume = values[i][0]
        d = derivative_point(values[i], values[i - 1], values[i + 1])
        d_list.append((volume, d))
        if volume == equivalent_volume:
            bounds_index = [len(d_list) - 2, len(d_list) - 1, len(d_list)]
    return d_list, tuple(d_list[i] for i in bounds_index)

def get_estimated_second_derivatives(bounds: tuple):
    first, second, third = bounds
    x_a, y_a = first
    x_b, y_b = second
    x_c, y_c = third
    x = x_a
    d_list = list()
    while x <= x_c:
        if x <= x_b:
            d_list.append([x, interpolation(x, x_a, x_b, y_a, y_b)])
        else:
            d_list.append([x, interpolation(x, x_b, x_c, y_b, y_c)])
        x += 0.1
        x = round(x, 2)
    return d_list, min(d_list, key=lambda e: abs(e[1]))[0]

def titration(values: list):
    print("Derivative:")
    try:
        derivatives, equivalent_volume = get_first_derivatives(values)
    except ZeroDivisionError:
        return 84
    for volume, k in derivatives:
        print(f"{volume} ml -> {k:.2f}")
    print()
    print(f"Equivalence point at {equivalent_volume} ml")
    print()
    print("Second derivative:")
    try:
        second_derivatives, bounds = get_second_derivatives(derivatives, equivalent_volume)
    return ZeroDivisionError:
        return 84
    for volume, k in second_derivatives:
        print(f"{volume} ml -> {k:.2f}")
    try:
        second_derivatives_estimated, equivalent_volume = get_estimated_second_derivatives(bounds)
    except ZeroDivisionError:
        return 84
    print()
    print("Second derivative estimated:")
    for volume, k in second_derivatives_estimated:
        print(f"{volume} ml -> {k:.2f}")
    print()
    print(f"Equivalence point at {equivalent_volume} ml")
    return 0