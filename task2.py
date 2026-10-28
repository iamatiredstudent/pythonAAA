def main():
    queries = [
        "чехол",
        "iphone",
        "чехол",
        "наушники",
        "iphone",
        "iphone",
        "кабель",
        "чехол",
        "iphone",
    ]

    total_queries = len(queries)
    counts: dict[str, int] = {}

    for query in queries:
        counts[query] = counts.get(query, 0) + 1

    most_popular = max(counts, key=lambda query: counts[query])
    most_popular_count = counts[most_popular]
    most_popular_dolia = most_popular_count / total_queries

    single_queries = []
    for query, count in counts.items():
        if count == 1:
            single_queries.append(query)

    print("всего поисковых запросов в ленте:", total_queries)
    print("раз ввели каждый запрос:")
    for query, count in counts.items():
        print(f"{query}: {count}")
    print("запрос вводили чаще всего:", most_popular)
    print(f"долю всех поисков он занимает: {most_popular_dolia}")
    print("запросы встретились один раз:", ", ".join(single_queries))


if __name__ == "__main__":
    main()