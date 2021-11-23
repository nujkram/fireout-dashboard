# readme

## build images

docker-compose -f docker-compose.dev.yml build

## initialize

docker-compose -f docker-compose.dev.yml exec web python manage.py flush --no-input

docker-compose -f docker-compose.dev.yml exec web python manage.py migrate

docker-compose -f docker-compose.dev.yml exec --user root web python manage.py collectstatic