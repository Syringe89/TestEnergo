# Тестовое задание для ПК "Энергосбережение"

### Запуск проекта
Установка пакетов
```
pip install -r requirements.txt
```
Настройки проекта находятся в файле config.py

Для миграции моделей выполнить команду:
```
alembic upgrade head
```
Запустить main.py
```
python main.py
```
Приложение сконфигурировано для работы по адресу localhost:8000

### Тестовое задание

Наш стек: aioredis, fastapi, asyncpg/aiopg

Тестовое приложение должно подключатся к PostgreSQL или Redis и реализовать следующие API:

1. Проверка анаграммы - принимает две строки, определяет являются ли они анаграммами.  Если являются - необходимо увеличить счетчик в Redis.   Возвращает JSON - являются ли они анаграммами и счетчик из Redis.

2.  Занести в базу данных 10 устройств (таблица devices), тип (dev_type) определяется случайно из списка: emeter, zigbee, lora, gsm. Поле dev_id - случайные 48 бит в hex-формате (MAC-адрес). К пяти устройствам из добавленных необходимо привязать endpoint (таблица endpoints).  После записи необходимо возвращать HTTP код состояния 201.

3. В базе данных получить список всех устройств, которые не привязаны к endpoint.  Вернуть количество, сгруппированное по типам устройств.
