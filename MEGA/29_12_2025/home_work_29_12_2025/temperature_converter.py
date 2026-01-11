# Temperature converter
# Celsius, Fahrenheit, Kelvin

def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32


def celsius_to_kelvin(c):
    return c + 273.15


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


def kelvin_to_celsius(k):
    return k - 273.15


def below_absolute_zero(scale, value):
    if scale == "K":
        return value < 0
    if scale == "C":
        return value < -273.15
    if scale == "F":
        return value < -459.67
    return True  # защитный случай


while True:
    # ---- choose scale ----
    while True:
        scale = input("Choose a temperature scale (C, F, K or Q to quit): ").strip().upper()

        if scale == "Q":
            print("Goodbye!")
            exit()

        if scale in ("C", "F", "K"):
            break

        print("Unknown scale. Please enter C, F, K, or Q.")

    # ---- enter temperature (NUMBER only) ----
    while True:
        value_str = input("Enter temperature (or Q to quit): ").strip()

        if value_str.upper() == "Q":
            print("Goodbye!")
            exit()

        try:
            value = float(value_str)
            break
        except ValueError:
            print("Please enter a number.")

    # ---- physical validation (OUTSIDE number loop) ----
    if below_absolute_zero(scale, value):
        if scale == "K":
            print("Temperature below 0 Kelvin is not possible.")
        elif scale == "C":
            print("Temperature below absolute zero (-273.15 °C) is not possible.")
        elif scale == "F":
            print("Temperature below absolute zero (-459.67 °F) is not possible.")

        print("Let's start over.")
        print()
        continue  # вернуться к выбору шкалы

    # ---- precision handling ----
    if "." in value_str:
        decimals = len(value_str.split(".", 1)[1])
    else:
        decimals = 0

    out_decimals = decimals + 1

    def fmt(x):
        return f"{x:.{out_decimals}f}"

    # ---- conversion ----
    if scale == "C":
        print("Fahrenheit:", fmt(celsius_to_fahrenheit(value)))
        print("Kelvin:", fmt(celsius_to_kelvin(value)))

    elif scale == "F":
        c = fahrenheit_to_celsius(value)
        print("Celsius:", fmt(c))
        print("Kelvin:", fmt(celsius_to_kelvin(c)))

    else:  # "K"
        c = kelvin_to_celsius(value)
        print("Celsius:", fmt(c))
        print("Fahrenheit:", fmt(celsius_to_fahrenheit(c)))

    print()

    # ---- convert another? ----
    while True:
        again = input("Convert another temperature? (Y/N): ").strip().upper()

        if again in ("Y", "YES"):
            print()
            break  # снова в начало главного while True

        if again in ("N", "NO", ""):
            print("Goodbye!")
            exit()

        print("Please enter Y or N.")
