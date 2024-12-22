Нужно произвести следующую последовательность команд после git clone:

```bash
cd minio
docker build -t data_uploader .
docker-compose up -d --build
```
После запуска контейнеров:
```bash
mc alias set minio http://localhost:9000 denis ddudakov
```

Переходим по ссылке http://localhost:9000, вводим логин:denis, пароль:ddudakov.
Далее можно увидеть test-bucket с переполнением.
Все остальные команды представлены в директории Screenshots с представленными скриншотами.
