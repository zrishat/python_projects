import pytest

from lotto_game.Bag import Bag
from lotto_game.Player import Player
from lotto_game.utils import all_numbers_is_out, show_formatted_card
from lotto_game.configurations import CPU_TYPE

class TestGame:
    def test_player_init(self):
        player = Player()
        assert player, "Не инициализируется класс Player"

    def test_player_generate_card(self):
        player = Player()
        assert player.player_card

    def test_bag_init(self):
        bag = Bag()
        assert bag,"Не инициализируется класс Bag"

    def test_bag_str(self):
        bag = Bag()
        val = bag.__str__()
        assert 'Новый бочонок' in val and 'осталось' in val

    def test_show_formatted_card(self, capsys):
        player = Player()
        show_formatted_card(player.player_card)
        captured = capsys.readouterr()
        assert "-"*30 == captured.out[0:30], \
            "Неверное форматирование первой строки"

    @pytest.mark.parametrize("player_card", [
        ['', '--'],
        ['--', ''],
        [1, 2]
    ])
    def test_all_numbers_is_out(self, player_card):
        assert all_numbers_is_out(player_card), \
            "Возвращается неверное значение"

    def test_cpu_defined(self):
        assert CPU_TYPE, "Не установлена переменная CPU_TYPE"
