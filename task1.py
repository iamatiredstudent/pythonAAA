moscow = {201, 202, 203, 204}
kazan = {203, 204, 205, 206}


both = moscow & kazan
only_moscow = moscow - kazan
only_kazan = kazan - moscow
all_products = moscow | kazan

print("можно забрать в любом из двух городов:", both)
print("есть только в Москве:", only_moscow)
print("есть только в Казани:", only_kazan)
print("разных товаров на обоих складах вместе:", len(all_products))
