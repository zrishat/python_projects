import random


class Player:
    """
    Игрок
    """
    def __init__(self, is_cpu=False):
        self.name = ''
        self.player_card = self.generate_card()
        self.cpu = is_cpu

    def generate_card(self):
        player_card = []
        all_numbers = list(range(1, 91))
        # генерируем числа в карточке
        for i in range(15):
            random_value = random.choice(all_numbers)
            all_numbers.remove(random_value)
            # добавляем пробел к числу для лучшего форматирования
            if random_value < 10:
                random_value = f' {random_value}'
            player_card.append(str(random_value))
        # генерируем пробелы в карточке
        for i in range(len(player_card)):
            player_card.insert(random.choice(range(15)), '  ')
        return player_card
