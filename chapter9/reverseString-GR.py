Number = int(input("Please Enter any number: "))


def reverse(s):
    Reverse = 0

    while s > 0:
        Reminder = s % 10
        Reverse = (Reverse * 10) + Reminder
        s = s // 10
    print("\n Reverse of entered number is = %d" % Reverse)


reverse(Number)
