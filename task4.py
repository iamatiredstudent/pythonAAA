from typing import TypedDict


class Day(TypedDict):
    day: str
    orders: int
    revenue: int
    returns: int


days: list[Day] = [
    {"day": "пн", "orders": 20, "revenue": 40_000, "returns": 2},
    {"day": "вт", "orders": 16, "revenue": 19_200, "returns": 4},
    {"day": "ср", "orders": 25, "revenue": 55_000, "returns": 1},
    {"day": "чт", "orders": 10, "revenue": 12_000, "returns": 3},
    {"day": "пт", "orders": 30, "revenue": 48_000, "returns": 3},
]

total_revenue = sum(day["revenue"] for day in days)
best_day = max(days, key=lambda day: day["revenue"])

print("выручка за неделю:", total_revenue)
print("день с самой большой выручкой:", best_day["day"])

high_return_days: list[str] = []

print("средняя выручка на один заказ в каждый день:")
for day in days:
    average_revenue = day["revenue"] / day["orders"]
    print(f'{day["day"]}: {average_revenue:.2f}')

    return_share = day["returns"] / day["orders"]
    if return_share > 0.2:
        high_return_days.append(day["day"])

print("дни, где возвратов больше 20%:", ", ".join(high_return_days))
