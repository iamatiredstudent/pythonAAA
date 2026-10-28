from typing import TypedDict


class Review(TypedDict):
    id: int
    product: str
    stars: int


def main():
    reviews: list[Review] = [
        {"id": 1, "product": "Чехол", "stars": 5},
        {"id": 1, "product": "Чехол", "stars": 3},
        {"id": 1, "product": "Чехол", "stars": 4},
        {"id": 2, "product": "Наушники", "stars": 2},
        {"id": 2, "product": "наушники", "stars": 2},
        {"id": 2, "product": "НАУШНИКИ", "stars": 5},
        {"id": 3, "product": "Планшет", "stars": 5},
        {"id": 4, "product": "Колонка", "stars": 4},
        {"id": 4, "product": "Колонка", "stars": 4},
        {"id": 5, "product": "Кабель", "stars": 1},
    ]

    ratings: dict[str, list[int]] = {}
    low_count = 0

    for review in reviews:
        name = review["product"].lower()

        if name not in ratings:
            ratings[name] = []

        ratings[name].append(review["stars"])

        if review["stars"] in (1, 2):
            low_count += 1

    averages: dict[str, float] = {}

    for name, stars in ratings.items():
        average = sum(stars) / len(stars)
        print(f"Средняя оценка товара {name}: {average:.2f}")

        if len(stars) >= 2:
            averages[name] = average

    worst_product = min(averages, key=lambda name: averages[name])

    print("худший товар с минимум двумя отзывами:", worst_product)
    print("отзывов на 1 или 2 звезды:", low_count)
    print(f"доля таких отзывов: {low_count / len(reviews):.2%}")


if __name__ == "__main__":
    main()