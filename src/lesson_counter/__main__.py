import time
import typer

from . import util


def count_lessons(weekday: int, print_delay: float = 0.0) -> None:
    half1 = util.parse_date_range("1.9.2025-31.1.2026")
    half2 = util.parse_date_range("1.2.2026-30.6.2026")

    h = list(util.non_learning_days(2025))

    monthly_lessons: dict[int, dict[int, int]] = {}

    for month in range(1, 13):
        monthly_lessons[month] = {x: 0 for x in range(7)}

    for i, half in enumerate([half1, half2]):
        lesson_count = 0
        print(f"{i + 1}. Pololetí")
        for d in half:
            if d.weekday() not in [5, 6] and d not in h:
                monthly_lessons[d.month][d.weekday()] += 1

            if d.weekday() == weekday:
                d_str = d.strftime("%d.%m")
                if d not in h:
                    lesson_count += 1
                    print(f"\t{d_str} máme IVT, celkem {lesson_count}")
                else:
                    print(f"\t{d_str} IVT odpadá :(")
                time.sleep(print_delay)
    print("Měsíc\tPo Út Stř Čt Pá So Ne")
    for month, lessons in monthly_lessons.items():
        print(f"{month}\t{list(lessons.values())}")


if __name__ == "__main__":
    typer.run(count_lessons)
