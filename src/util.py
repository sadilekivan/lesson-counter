import itertools

from datetime import date, datetime, timedelta
from typing import Generator


def days_inbetween(start: date, end: date) -> Generator[date]:
    for day in range((end - start).days + 1):
        yield start + timedelta(day)


def parse_date(string: str) -> Generator[date]:
    if "-" in string:
        d = [datetime.strptime(x, "%d.%m.%Y") for x in string.split("-", 1)]
        for d in days_inbetween(d[0], d[1]):
            yield d
    else:
        for x in string.split("+"):
            yield datetime.strptime(x, "%d.%m.%Y")


def non_learning_days(year) -> Generator[date]:
    nyear = year + 1
    holiday_list = [
        # First Day of school
        f"1.9.{year}",
        # Fall break
        f"27.10.{year}+29.10.{year}",
        # Christmas break
        f"22.12.{year}-2.1.{nyear}",
        # Half-year break
        f"30.1.{nyear}",
        # Spring break
        f"16.2.{nyear}-22.2.{nyear}",
        # Easter break
        f"2.4.{nyear}",
        # Main break
        f"1.7.{nyear}-31.8.{nyear}",
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
        f"1.1.{nyear}",
        # Good Friday
        f"3.4.{nyear}",
        # Easter Monday
        f"6.4.{nyear}",
        # Labor Day
        f"1.5.{nyear}",
        # Victory in Europe Day
        f"8.5.{nyear}",
        # ========
        # Principal break
        f"30.10.{year}",
        f"31.10.{year}",
    ]
    for day in itertools.chain(*map(parse_date, holiday_list)):
        yield day
