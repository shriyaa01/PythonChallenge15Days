import calendar
print("Select calendar format:")
print("1. Display a single month")
print("2. Display the entire year")
choice = int(input("Enter your choice: "))
yy = int(input("Enter year: "))
if choice == 1:
    mm = int(input("Enter month: "))
    print(calendar.month(yy, mm))
elif choice == 2:
    for i in range(1, 13):
        print(calendar.month(yy, i))
else:
    print("Invalid choice")
