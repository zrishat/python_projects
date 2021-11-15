def show_formatted_card(card_list):
    print('-'*30)
    print('|'.join(card_list[:10]))
    print('|'.join(card_list[10:20]))
    print('|'.join(card_list[20:]))
    print('-'*30)


def all_numbers_is_out(player_cards):
    # вернет True, если все числа зачеркнуты
    return len(set(player_cards)) == 2
