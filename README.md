# academia

## Create database: 

`CREATE DATABASE academia CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;`

## Change Root Password
`$ mysql -u root -p`

`> SET GLOBAL validate_password.LENGTH = 4;`

`> SET GLOBAL validate_password.policy = 0;`

`> SET GLOBAL validate_password.mixed_case_count = 0;`

`> SET GLOBAL validate_password.number_count = 0;`

`> SET GLOBAL validate_password.special_char_count = 0;`

`> SET GLOBAL validate_password.check_user_name = 0;`

`> ALTER USER 'root'@'localhost' IDENTIFIED BY 'root';`

`> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root';`

`> FLUSH PRIVILEGES;`

`> exit;`

## Create root user (to call apis either modify postman environment or use: mashuq/star@wars)

`python3 manage.py createsuperuser`

## Pre-requisite for mysql
### Ubuntu
`$ sudo apt-get install python3-dev default-libmysqlclient-dev build-essential python3-pip gunicorn`
### Fedora
`$ sudo yum install python3-devel mysql-devel python3-pip`

## Pip Installs
`$ pip3 install mysqlclient django djangorestframework markdown django-filter djangorestframework_simplejwt django-cors-headers factory_boy django-polymorphic django-rest-polymorphic django-environ gunicorn Pillow Faker requests gunicorn psycopg2-binary`

## Migration
`$ python3 manage.py makemigrations core`

`$ python3 manage.py migrate`

## Run Server
`$ python manage.py runserver`


## Install vue cli
`npm install -g @vue/cli`

## recaptcha admin console
https://www.google.com/recaptcha/admin

## Localhost site key: 

Site key: 6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI

Secret key: 6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe


## run with gunicorn

gunicorn -b 0.0.0.0:8000 backend.wsgi > log.txt 2>&1 &

sudo gunicorn --workers 8 --threads 8 -b 0.0.0.0:443 backend.wsgi > log.txt 2>&1 &

sudo gunicorn backend.wsgi > log.txt 2>&1 &


curl -fsSL https://deb.nodesource.com/setup_15.x | sudo -E bash -
sudo apt-get install -y nodejs


sudo npm install -g serve
sudo serve -s dist -l 80 > log.txt 2>&1 &



`> CREATE USER 'nlquran'@'167.99.68.235' IDENTIFIED WITH mysql_native_password BY 'root';`

`> GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT on academia.* TO 'nlquran'@'167.99.68.235';`

`> FLUSH PRIVILEGES;`

`> exit;`


./manage.py collectstatic