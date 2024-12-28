#!/bin/sh

# Run setup only if .env file doesn't exist.
if [ ! -e .env.production ]
then
cat > .env.production << EOF
APP_NAME=MyIdlers
APP_DEBUG=true
APP_KEY=

DB_CONNECTION=mysql
DB_HOST=${DB_HOST}
DB_DATABASE=${DB_DATABASE}
DB_USERNAME=${DB_USERNAME}
DB_PASSWORD=${DB_PASSWORD}
APP_URL=${APP_URL}
EOF
php artisan key:generate --no-interaction --force
fi

php artisan serve --host=0.0.0.0 --port=8000 --env=production


# docker compose exec app php artisan migrate:fresh --seed
# docker compose exec app php artisan migrate
# docker compose exec app php artisan route:cache
# docker compose exec app php artisan cache:clear