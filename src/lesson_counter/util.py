import itertools
from collections.abc import Generator
from datetime import date, datetime, timedelta


def days_inbetween(start: date, end: date) -> Generator[date]:
    for day in range((end - start).days + 1):
        yield start + timedelta(day)


def parse_date_range(string: str) -> Generator[date]:
    if "-" in string:
        range = [datetime.strptime(x, "%d.%m.%Y") for x in string.split("-", 1)]
        yield from days_inbetween(range[0], range[1])
    else:
        for x in string.split("+"):
            yield datetime.strptime(x, "%d.%m.%Y")


def non_learning_days(year: int) -> Generator[date]:
    next_year = year + 1
    holiday_list = [
        # First Day of school
        f"1.9.{year}",
        # Fall break
        f"27.10.{year}+29.10.{year}",
        # Christmas break
        f"22.12.{year}-2.1.{next_year}",
        # Half-year break
        f"30.1.{next_year}",
        # Spring break
        f"16.2.{next_year}-22.2.{next_year}",
        # Easter break
        f"2.4.{next_year}",
        # Main break
        f"1.7.{next_year}-31.8.{next_year}",
        # ========
        # St. Wenceslas Day
        f"28.9.{year}",
        # Independent Czechoslovak State day
        f"28.10.{year}",
        # Struggle for Freedom and Democracy day
        f"17.11.{year}",
        # Christmas Eve
        f"24.12.{year}",
        # Christmas Day
        f"25.12.{year}",
        # Boxing Day
        f"26.12.{year}",
        # New Year's Day
        f"1.1.{next_year}",
        # Good Friday
        f"3.4.{next_year}",
        # Easter Monday
        f"6.4.{next_year}",
        # Labor Day
        f"1.5.{next_year}",
        # Victory in Europe Day
        f"8.5.{next_year}",
        # ========
        # Principal break
        f"30.10.{year}",
        f"31.10.{year}",
    ]
    yield from itertools.chain(*map(parse_date_range, holiday_list))
