def twelve_to_twentyfour(hours, minutes, period):
    try:
        if (0 <= hours <= 12) and (0 <= minutes <= 59) and (period == 'am' or period == 'pm'):
            if period == 'am' and hours < 12:
                return f"{hours:02d}{minutes:02d}HRS"
            if period == 'am' and hours == 12:
                return f"00{minutes:02d}HRS"
            if period == 'pm' and hours < 12:
                return f"{hours+12:02d}{minutes:02d}HRS"
            if period == 'pm' and hours == 12:
                return f"{hours:02d}{minutes:02d}HRS"
        else:
            return "Enter a valid time..."
    except TypeError:
        print("TypeError: Ensure Minutes and Hours are integer values.")



print("Enter the time values below.")
hours = int(input("Hours (int): "))
minutes = int(input("Minutes (int): "))
period = input("Period (am / pm): ")
# print("ValueError: Ensure value is an integer")

print(twelve_to_twentyfour(hours, minutes, period))