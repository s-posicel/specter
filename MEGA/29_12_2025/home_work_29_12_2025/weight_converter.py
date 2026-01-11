KG_TO_POUNDS = 2.2046226218

print("Weight converter: (kg + g) ↔ pounds\n")

while True:
    print("Choose conversion:")
    print("  1) kg + g  → pounds")
    print("  2) pounds → kg + g")
    print("  0) exit")

    choice = input("Your choice: ").strip()

    # ===== kg + g → pounds =====
    if choice == "1":

        # ---- kilograms ----
        while True:
            kg_str = input("Enter kilograms: ").strip()
            kg_str = kg_str.replace(",", ".")

            try:
                kg = float(kg_str)
                if kg < 0:
                    print("Kilograms cannot be negative. Try again.\n")
                    continue
                break
            except ValueError:
                print("Please enter a number for kilograms.\n")

        # ---- grams ----
        while True:
            g_str = input("Enter grams (press Enter for 0): ").strip()

            if g_str == "":
                g = 0.0
                break

            g_str = g_str.replace(",", ".")

            try:
                g = float(g_str)
                if g < 0:
                    print("Grams cannot be negative. Try again.\n")
                    continue
                if g >= 1000:
                    print("Grams must be less than 1000. Try again.\n")
                    continue
                break
            except ValueError:
                print("Please enter a number for grams.\n")

        total_kg = kg + g / 1000
        pounds = total_kg * KG_TO_POUNDS

        print(f"\n{kg} kg {g} g = {pounds:.2f} pounds\n")

    # ===== pounds → kg + g =====
    elif choice == "2":

        # ---- pounds ----
        while True:
            lb_str = input("Enter pounds: ").strip()
            lb_str = lb_str.replace(",", ".")

            try:
                pounds = float(lb_str)
                if pounds < 0:
                    print("Pounds cannot be negative. Try again.\n")
                    continue
                break
            except ValueError:
                print("Please enter a number for pounds.\n")

        total_kg = pounds / KG_TO_POUNDS
        kg = int(total_kg)
        g = round((total_kg - kg) * 1000, 1)

        if g >= 1000:
            kg += 1
            g -= 1000

        print(f"\n{pounds} pounds = {kg} kg {g} g\n")

    # ===== exit =====
    elif choice == "0":
        print("\nGoodbye!")
        break

    else:
        print("Please enter 1, 2, or 0.\n")
