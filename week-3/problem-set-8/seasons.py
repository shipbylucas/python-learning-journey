from datetime import date, datetime
import sys
import re
import inflect


def main():
    birth = input("Date of Birth: ")
    print(age(birth))

def age(birth):
    try:
        born = date.fromisoformat(birth)
        born = born.isoformat()
        year_0, month_0, date_0 = born.split("-")
        start = datetime(int(year_0), int(month_0), int(date_0), 0, 0)

        today = date.today()
        today = today.isoformat()
        year_1, month_1, date_1 = today.split("-")
        end = datetime(int(year_1), int(month_1), int(date_1), 0, 0)

        d = end - start

        match = re.search(r"^(\d+) days, (\d+):(\d\d):(\d\d)$", str(d))
        day = match.group(1)
        hour = match.group(2)
        minute = match.group(3)
        second = match.group(4)

        total = round(int(day) * 24 * 60 + int(hour) * 60 + int(minute) + int(second) / 60)

        word = inflect.engine().number_to_words(total, andword="")

        return (f"{word[0].upper() + word[1:]} minutes")

    except ValueError:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()
