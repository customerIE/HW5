from typing import Generator

# Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии


names = ['Игорь', 'Василий', 'Сергей', 'Антон']
stavka = [20000, 25000, 50000, 60000]
award = ['10.25%', '12.25%', '15.25%', '17.00%']


def salary_gen(names: list[str], sstavka: list[int], award: list[str]) -> dict[str: float]:
    return {name: prize / 100 * awar for name, prize, awar in zip(names, stavka, (float(i[:-1]) for i in award))}.items()


print(*(salary_gen(names, stavka, award)))
