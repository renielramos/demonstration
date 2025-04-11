def celsius_to_fahrenheit(c):
    return round((c * 9/5) + 32, 2)


def fahrenheit_to_celsius(f):
    return round((f - 32) * 5/9, 2)


if __name__ == "__main__":
    c = 25
    f = celsius_to_fahrenheit(c)
    print(f"{c}°C is {f}°F")

    f = 77
    c = fahrenheit_to_celsius(f)
    print(f"{f}°F is {c}°C")
