class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def is_leap(y: int) -> bool:
            return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

        # days in months for a non-leap year
        mdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def days_from_1971(d: str) -> int:
            y, m, day = map(int, d.split("-"))
            # days from 1971-01-01 to Jan 1 of year y
            days = 0
            for yr in range(1971, y):
                days += 366 if is_leap(yr) else 365
            # add months of current year
            for mm in range(1, m):
                days += mdays[mm - 1]
                if mm == 2 and is_leap(y):
                    days += 1
            # add days in current month
            days += day
            return days

        return abs(days_from_1971(date1) - days_from_1971(date2))

