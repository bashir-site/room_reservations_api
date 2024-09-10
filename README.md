# room_reservations_api

Cистема бронирование переговорных комнат для офиса.

## Запуск проекта

Склонируйте git репозиторий:
```bash
git clone git@github.com:bashir-site/room_reservations_api.git
```

Сбилдите контейнеры:
```bash
docker-compose build
```

Запустите контейнеры:
```bash
docker-compose build -d
```
* флаг -d запустит контейнеры в фоне, можно убрать флаг, если хотите смотреть логи

После запуска контейнеров, API можно посмотреть по адресу:
```bash
http://127.0.0.1:8000/
```

## Дополнительные команды

Чтобы запустить тестирование, нужно запустить данную команду:
```bash
docker-compose exec web python manage.py test reservations
```

Чтобы сделать миграции, нужно запустить данную команду:
```bash
docker-compose exec web python manage.py migrate
```




