# HaiTalent API

FastAPI приложение для вопросов и ответов.

## Быстрый запуск

git clone https://github.com/ryabinin13/haitalent.git
cd haitalent
docker compose up -d

Приложение запустится на http://localhost:8008/

## Запуск тестов

docker build -f Dockerfile.test -t my-tests .
docker run my-tests