import random
import sys


class Player:
    """
    Игрок
    """
    def __init__(self):
        self.name = ''
        self.player_card = self.generate_card()
        self.cpu = False

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


def show_formatted_card(card_list):
    print('-'*30)
    print('|'.join(card_list[:10]))
    print('|'.join(card_list[10:20]))
    print('|'.join(card_list[20:]))
    print('-'*30)


print('ЛОТЕРЕЯ\n',
      '-'*10, "\n"
      "Выберите количество игроков: \n",
      '-'*10)
number_players = int(input('Введите число: '))

players = []
for id in range(number_players):
    print(f'Введите тип {id+1} игрока (1 - комп, 2 - человек)')
    player_type = int(input('Введите число: '))
    new_player = Player()
    if player_type == 1:
        new_player.cpu = True
    players.append(new_player)

bag = Bag()

while len(bag.kegs)+1:
    print(bag)

    for id, player in enumerate(players):
        player_cards = player.player_card

        if len(set(player_cards)) == 2:
            print(f'Игрок {id+1} выиграл!')
            sys.exit()

        print(f'Ходит игрок {id+1}')
        show_formatted_card(player_cards)

        while True:
            if player.cpu:
                if bag.current_keg in player_cards:
                    answer = 'y'
                else:
                    answer = 'n'
            else:
                answer = input("Зачеркнуть цифру? (y/n) ").lower()
            if answer == 'y':
                if bag.current_keg not in player_cards:
                    print(f"Игрок {id+1} проиграл, такого бачонка нет в карточке")
                    sys.exit()
                player_cards[player_cards.index(bag.current_keg)] = '--'
                break
            elif answer == 'n':
                if bag.current_keg in player_cards:
                    print(f"Игрок {id+1} проиграл, такой бачонок был в карточке")
                    sys.exit()
                break

    print('Мешаем бочонки....')
print('Бочонки кончились. Конец игры')
sys.exit()
