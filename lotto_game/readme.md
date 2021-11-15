Правила игры 
```
https://gist.github.com/DanteOnline/038d59cb9c5b704d02238f4e11b95c97
```
Запуск игры через python
```
python3 start_game.py
```
Запуск игры через Docker
```
docker image build -t lotto_game:latest .
docker container run -it lotto_game
```
Запуск игры через Docker-compose
```
docker-compose up -d && docker logs lotto_game_app_1 && docker attach lotto_game_app_1
```
В интерактивном режиме выбирается количество игроков и тип игрока.