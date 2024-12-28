#!/bin/sh

# Run setup only if .env file doesn't exist.
if [ ! -e .env.production ]
then
cat > .env.production << EOF
APP_NAME=MyIdlers
APP_DEBUG=false
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

# Wait for database to be ready
until php artisan db:monitor > /dev/null 2>&1; do
    echo "Waiting for database connection..."
    sleep 2
done

# Check if database needs initialization by checking if OS table has entries
DB_STATUS=$(php artisan tinker --execute="try { if(DB::table('os')->count() === 0) { echo 'needs_init'; } else { echo 'initialized'; } } catch(\Exception \$e) { echo 'needs_init'; }")
if echo "$DB_STATUS" | grep -q "needs_init"; then
    echo "Initializing database..."
    php artisan migrate:fresh --seed --force
    php artisan route:cache
    php artisan cache:clear
else
    echo "Database already initialized"
    php artisan migrate --force
    php artisan route:cache
    php artisan cache:clear
fi

php artisan serve --host=0.0.0.0 --port=8000 --env=production
