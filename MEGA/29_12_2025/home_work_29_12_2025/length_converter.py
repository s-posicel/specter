# Length converter
# km + m + cm <-> feet + inches
# - accepts comma or dot
# - empty input = 0
# - no negative numbers
# - UI-correction to avoid showing 100.00 cm or 12.00 inches due to rounding in output

KM_TO_M = 1000
M_TO_CM = 100

CM_TO_INCH = 0.393700787
INCH_TO_CM = 1 / CM_TO_INCH

INCHES_IN_FOOT = 12

# If we print with 2 decimals:
# 99.995 -> "100.00", 11.995 -> "12.00"
CM_CARRY_THRESHOLD = 99.995
INCH_CARRY_THRESHOLD = 11.995


while True:
    print("\nChoose conversion direction:")
    print("1 - km, m, cm -> feet, inches")
    print("2 - feet, inches -> km, m, cm")
    print("3 - exit")

    choice = input("Your choice: ").strip()

    if choice == "3":
        print("Goodbye!")
        break

    # ---------- km + m + cm -> feet + inches ----------
    if choice == "1":

        # ---- kilometers ----
        while True:
            s = input("Enter kilometers (or press Enter for 0): ").replace(",", ".").strip()
            if s == "":
                km = 0.0
                break
            try:
                km = float(s)
                if km < 0:
                    print("Value cannot be negative.")
                    continue
                break
            except ValueError:
                print("Please enter a number.")

        # ---- meters ----
        while True:
            s = input("Enter meters (or press Enter for 0): ").replace(",", ".").strip()
            if s == "":
                m = 0.0
                break
            try:
                m = float(s)
                if m < 0:
                    print("Value cannot be negative.")
                    continue
                break
            except ValueError:
                print("Please enter a number.")

        # ---- centimeters ----
        while True:
            s = input("Enter centimeters (or press Enter for 0): ").replace(",", ".").strip()
            if s == "":
                cm = 0.0
                break
            try:
                cm = float(s)
                if cm < 0:
                    print("Value cannot be negative.")
                    continue
                break
            except ValueError:
                print("Please enter a number.")

        total_cm = km * KM_TO_M * M_TO_CM + m * M_TO_CM + cm
        total_inches = total_cm * CM_TO_INCH

        feet = int(total_inches // INCHES_IN_FOOT)
        inches = total_inches - feet * INCHES_IN_FOOT

        # UI-correction for printing with 2 decimals (avoid 12.00 inches)
        if inches >= INCH_CARRY_THRESHOLD:
            feet += 1
            inches = 0.0

        print(f"{km} km {m} m {cm:.2f} cm = {feet} feet {inches:.2f} inches")

    # ---------- feet + inches -> km + m + cm ----------
    elif choice == "2":

        # ---- feet ----
        while True:
            s = input("Enter feet (or press Enter for 0): ").replace(",", ".").strip()
            if s == "":
                feet_in = 0.0
                break
            try:
                feet_in = float(s)
                if feet_in < 0:
                    print("Value cannot be negative.")
                    continue
                break
            except ValueError:
                print("Please enter a number.")

        # ---- inches ----
        while True:
            s = input("Enter inches (or press Enter for 0): ").replace(",", ".").strip()
            if s == "":
                inches_in = 0.0
                break
            try:
                inches_in = float(s)
                if inches_in < 0:
                    print("Value cannot be negative.")
                    continue
                break
            except ValueError:
                print("Please enter a number.")

        total_inches = feet_in * INCHES_IN_FOOT + inches_in
        total_cm = total_inches * INCH_TO_CM

        km = int(total_cm // (KM_TO_M * M_TO_CM))
        rest_cm = total_cm - km * KM_TO_M * M_TO_CM

        m = int(rest_cm // M_TO_CM)
        cm = rest_cm - m * M_TO_CM

        # UI-correction for printing with 2 decimals (avoid 100.00 cm)
        if cm >= CM_CARRY_THRESHOLD:
            m += 1
            cm = 0.0

        # carry meters to kilometers if needed
        if m >= KM_TO_M:
            km += 1
            m -= KM_TO_M

        print(f"{feet_in} feet {inches_in:.2f} inches = {km} km {m} m {cm:.2f} cm")

    else:
        print("Invalid choice. Try again.")
