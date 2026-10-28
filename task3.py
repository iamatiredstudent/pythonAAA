from typing import TypedDict


class Order(TypedDict):
    id: int
    buyer: str
    status: str
    amount: int


def main():
    orders: list[Order] = [
        {"id": 1, "buyer": "anya", "status": "delivered", "amount": 900},
        {"id": 2, "buyer": "boris", "status": "returned", "amount": 4_500},
        {"id": 3, "buyer": "anya", "status": "delivered", "amount": 1_500},
        {"id": 4, "buyer": "vera", "status": "delivered", "amount": 3_200},
        {"id": 5, "buyer": "boris", "status": "delivered", "amount": 700},
        {"id": 6, "buyer": "gleb", "status": "returned", "amount": 2_100},
    ]

    returned_sum = 0
    returned_buyers: set[str] = set()
    delivered_count = 0
    delivered_amount = 0

    for order in orders:
        if order["status"] == "returned":
            returned_sum += order["amount"]
            returned_buyers.add(order["buyer"])
        elif order["status"] == "delivered":
            delivered_count += 1
            delivered_amount += order["amount"]

    print("сумма возвратов:", returned_sum)
    print("кто возвращал заказы:", ", ".join(sorted(returned_buyers)))
    print("количество доставленных заказов:", delivered_count)

    if delivered_count > 0:
        average_check = delivered_amount / delivered_count
        print(f"средний чек доставленных заказов: {average_check:.2f}")
    else:
        print("средний чек не определён: нет доставленных заказов")


if __name__ == "__main__":
    main()