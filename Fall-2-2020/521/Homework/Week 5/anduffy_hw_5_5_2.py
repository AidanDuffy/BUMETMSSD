"""
Aidan Duffy
Class: CS 521 - Fall 2
Date: December 8, 2020
Homework Problem 5.5.2
Description: Takes a date and time, validates those, and then prints them in various formats.
"""

def is_validate_datetime(date_and_time):
    """
    This validates the user input date and time.
    :param date_and_time: is the user input.
    :return: is the boolean value determining whether the input is a valid date/time.
    """
    if(date_and_time[2] != "/" or date_and_time[5] != "/"):
        print("Error: Your entry format was incorrect!")
        return False
    elif(date_and_time[10] != " " or len(date_and_time) != 19):
        print("Error: Your entry format was incorrect!")
        return False
    elif(date_and_time[13] != ":" or date_and_time[16] != ":"):
        print("Error: Your entry format was incorrect!")
        return False
    else:
        try:
            month = int(date_and_time[0:2])
            if month > 12 or month < 1:
                print("Error: the month should be between 1 and 12!")
                return False
            day = int(date_and_time[3:5])
            if month == 2 and day > 28:
                print("Error: there are at most 28 days in February!")
                return False
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                if day < 1 or day > 31:
                    print("Error: the day should be between 1 and 31 for this month!")
                    return False
            else:
                if day < 1 or day > 30:
                    print("Error: the day should be between 1 and 30 for this month!")
                    return False
            year = int(date_and_time[6:10])
            hours = int(date_and_time[11:13])
            if hours < 0 or hours > 23:
                print("Error: the hours should be between 00 and 23!")
                return False
            minutes = int(date_and_time[14:16])
            if minutes < 0 or minutes > 59:
                print("Error: the minutes should be between 00 and 59!")
                return False
            seconds = int(date_and_time[17:])
            if seconds < 0 or seconds > 59:
                print("Error: the seconds should be between 00 and 59!")
                return False
            return True
        except:
            print("Error: Your entry format was incorrect!")
            return False

def main():
    date_and_time = input("Please input a date and time in the American date/24 hour clock (MM/DD/YYYY and HH:mm:SS): ")
    valid = is_validate_datetime(date_and_time)
    if (valid is False):
        print("Error: please try again with a valid date and time!")
    else:
        month = int(date_and_time[0:2])
        day = int(date_and_time[3:5])
        year = int(date_and_time[6:10])
        hours = int(date_and_time[11:13])
        minutes = int(date_and_time[14:16])
        seconds = int(date_and_time[17:])
        print("MM/DD/YYYY is ", '{:02}'.format(month), "/", '{:02}'.format(day), "/", year, sep="")
        print("HR:MIN:SEC is ", '{:02}'.format(hours), ":", '{:02}'.format(minutes), ":", '{:02}'.format(seconds),sep="")
        print("MM/YYYY is ", '{:02}'.format(month), "/", year, sep="")
        if hours >= 12:
            print("The time is PM")
        else:
            print("The time is AM")

if __name__ == "__main__":
    main()