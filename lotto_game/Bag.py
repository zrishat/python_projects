import random


class Bag:
    """
    Мешок
    """
    def __init__(self):
        # общее число бочонков
        self.kegs = list(range(1, 91))
        self.current_keg = None

    def __str__(self):
        """
        Генерация текущего боченка
        """
        rand_keg = random.choice(self.kegs)
        if rand_keg < 10:
            self.current_keg = f' {rand_keg}'
        else:
            self.current_keg = str(rand_keg)
        self.kegs.remove(rand_keg)
        return f'Новый бочонок: {self.current_keg} (осталось {len(self.kegs)})'