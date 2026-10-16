from math import inf


def task1():
    moscow = {201, 202, 203, 204}
    kazan = {203, 204, 205, 206}
    return moscow, kazan


def exec1():
    moscow, kazan = task1()
    both = moscow.intersection(kazan)
    print(f'что можно забрать в любом из двух городов: {both}')
    print(f'что есть только в Москве: {moscow.difference(kazan)}')
    print(f'что есть только в Казани: {kazan.difference(moscow)}')
    kaz = len(kazan.difference(moscow))
    msc = len(moscow.difference(kazan))
    print(f'сколько разных товаров на обоих складах вместе: {kaz + msc}')


def task2():
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
    return queries


def exec2():
    queries = task2()
    print(f'сколько всего поисковых запросов в ленте: {len(queries)}')
    ans = {q: queries.count(q) for q in set(queries)}
    print(f'сколько раз ввели каждый запрос: {ans}')
    print(f'какой запрос вводили чаще всего: {max(ans, key=ans.get)}')
    share = max(ans.values()) / len(queries)
    print(f'какую долю всех поисков он занимает: {share}')
    once = [q for q in ans if ans[q] == 1]
    print(f'какие запросы встретились один раз: {once}')


def task3():
    orders = [
        {"id": 1, "buyer": "anya", "status": "delivered", "amount": 900},
        {"id": 2, "buyer": "boris", "status": "returned", "amount": 4_500},
        {"id": 3, "buyer": "anya", "status": "delivered", "amount": 1_500},
        {"id": 4, "buyer": "vera", "status": "delivered", "amount": 3_200},
        {"id": 5, "buyer": "boris", "status": "delivered", "amount": 700},
        {"id": 6, "buyer": "gleb", "status": "returned", "amount": 2_100},
    ]
    return orders


def exec3():
    orders = task3()
    ret_sum = 0
    ret_people = set()
    deliv_cnt = {}
    deliv = {}
    for order in orders:
        if order["status"] == "returned":
            ret_sum += order["amount"]
            ret_people.add(order['buyer'])
        else:
            deliv_cnt[order["buyer"]] = deliv_cnt.get(order["buyer"], 0) + 1
            deliv[order["buyer"]] = (
                deliv.get(order["buyer"], 0) + order["amount"]
            )

    print(f'оформили возвраты на сумму {ret_sum}')
    print(f'хотя бы раз вернул заказ: {ret_people}')
    print(f'заказов доставлено покупателю: {deliv_cnt}')
    print(f'средний чек доставленных заказов: '
          f'{sum(deliv.values()) / len(deliv)}')


def task4():
    days = [
        {"day": "пн", "orders": 20, "revenue": 40_000, "returns": 2},
        {"day": "вт", "orders": 16, "revenue": 19_200, "returns": 4},
        {"day": "ср", "orders": 25, "revenue": 55_000, "returns": 1},
        {"day": "чт", "orders": 10, "revenue": 12_000, "returns": 3},
        {"day": "пт", "orders": 30, "revenue": 48_000, "returns": 3},
    ]
    return days


def exec4():
    days = task4()
    rev = {}
    perc_20 = {}
    for day in days:
        rev[day["day"]] = (day["orders"] - day["returns"]) * day["revenue"]
        perc_20[day["day"]] = (day["returns"] / day["orders"] > 0.2)
    print(f"выручка за всю неделю: {sum(rev.values())}")
    print(f"день с самой большой выручкой: {max(rev, key=rev.get)}")
    print("средняя выручка на один заказ в каждый день: {}".format({
        day['day']: day['revenue'] / day['orders'] for day in days
    }))
    print(f"дни, где возвратов больше 20% заказов: "
          f"{[day for day in perc_20 if perc_20[day]]}")


def task5():
    reviews = [
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
    for i in range(len(reviews)):
        reviews[i]["product"] = reviews[i]["product"].lower()

    return reviews


def exec5():
    reviews = task5()
    revs = {
        review["product"]: {"sum": 0, "cnt": 0}
        for review in reviews
    }
    cnt = 0
    for review in reviews:
        revs[review["product"]]["sum"] += review["stars"]
        revs[review["product"]]["cnt"] += 1
        if review["stars"] <= 2:
            cnt += 1
    worst_star, worst_prod = +inf, ""
    for review in reviews:
        if revs[review["product"]]["cnt"] > 1:
            if (
                revs[review["product"]]["sum"]
                / revs[review["product"]]["cnt"] < worst_star
            ):
                worst_prod = review["product"]

    print('средняя оценка каждого товара: {}'.format({
        product: revs[product]["sum"] / revs[product]["cnt"]
        for product in revs
    }))
    print('худший товар по средней оценке среди тех, '
          f'у кого хотя бы два отзыва: {worst_prod}')
    print(f'отзывов на 1 или 2 звезды: {cnt}')
    print('какую долю всех отзывов составляют отзывы на 1 или 2 звезды: '
          f'{cnt / len(reviews)}')


if __name__ == '__main__':
    exec1()
    exec2()
    exec3()
    exec4()
    exec5()
