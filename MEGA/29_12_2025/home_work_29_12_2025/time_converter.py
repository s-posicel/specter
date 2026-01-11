# convert time
'''
AM/PM <-> 24-hour format
Accepts flexible input:
- 9:56 AM, 09:56AM, 9.56 AM, 9,56AM, 09  : 56    AM
- 21:56, 21  : 56, 21.56, 21,56
'''

while True:
    print("Choose conversion direction:")
    print("1 - AM/PM -> 24-hour format")
    print("2 - 24-hour format -> AM/PM")
    print("Press Enter to exit")

    choice = input("Your choice: ").strip()

    if choice == "":
        print("Goodbye!")
        break

    # ---------- AM/PM -> 24-hour ----------
    if choice == "1":
        time_str = input("Enter time (hh:mm AM/PM): ").strip()

        try:
            # normalize input: remove spaces, allow '.' or ',' instead of ':'
            s = time_str.upper().replace(" ", "")
            s = s.replace(".", ":").replace(",", ":")

            # allow AM/PM with or without a space
            if s.endswith("AM"):
                period = "AM"
                time_part = s[:-2]
            elif s.endswith("PM"):
                period = "PM"
                time_part = s[:-2]
            else:
                print("Please use AM or PM.\n")
                continue

            hour_str, minute_str = time_part.split(":")
            hour = int(hour_str)
            minute = int(minute_str)

            # validation
            if hour < 1 or hour > 12 or minute < 0 or minute > 59:
                print("Invalid time values.\n")
                continue

            # conversion
            if period == "AM":
                if hour == 12:
                    hour = 0
            else:  # PM
                if hour != 12:
                    hour += 12

            print(f"Result: {hour:02d}:{minute:02d}\n")

        except ValueError:
            print("Invalid format. Examples: 9:56 AM, 9.56AM\n")

    # ---------- 24-hour -> AM/PM ----------
    elif choice == "2":
        time_str = input("Enter time (hh:mm): ").strip()

        try:
            # normalize input: remove spaces, allow '.' or ',' instead of ':'
            s = time_str.replace(" ", "")
            s = s.replace(".", ":").replace(",", ":")

            hour_str, minute_str = s.split(":")
            hour = int(hour_str)
            minute = int(minute_str)

            # validation
            if hour < 0 or hour > 23 or minute < 0 or minute > 59:
                print("Invalid time values.\n")
                continue

            # conversion
            if hour == 0:
                display_hour = 12
                period = "AM"
            elif hour < 12:
                display_hour = hour
                period = "AM"
            elif hour == 12:
                display_hour = 12
                period = "PM"
            else:
                display_hour = hour - 12
                period = "PM"

            print(f"Result: {display_hour:02d}:{minute:02d} {period}\n")

        except ValueError:
            print("Invalid format. Examples: 21:56, 21.56, 21,56\n")

    else:
        print("Please choose 1 or 2.\n")
