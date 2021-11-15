import sys
from Bag import Bag
from Player import Player
from utils import all_numbers_is_out, show_formatted_card
from configurations import CPU_TYPE

print('ЛОТЕРЕЯ\n',
      '-'*10, "\n"
      "Выберите количество игроков: \n",
      '-'*10)
number_players = int(input('Введите число: '))

players = []
for id in range(number_players):
    print(f'Введите тип {id+1} игрока (1 - комп, 2 - человек)')
    player_type = int(input('Введите число: '))
    if player_type == CPU_TYPE:
        new_player = Player(True)
    else:
        new_player = Player()
    players.append(new_player)

bag = Bag()


while len(bag.kegs)+1:
    print(bag)

    for id, player in enumerate(players):
        player_cards = player.player_card

        if all_numbers_is_out(player_cards):
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
