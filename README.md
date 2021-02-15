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

`> FLUSH PRIVILEGES;`

`> exit;`

## Create root user (to call apis either modify postman environment or use: mashuq/star@wars)

`python manage.py createsuperuser`

## Pre-requisite for mysql
### Ubuntu
`$ sudo apt-get install python3-dev default-libmysqlclient-dev build-essential`
### Fedora
`$ sudo yum install python3-devel mysql-devel`

## Pip Installs
`$ pip3 install mysqlclient django djangorestframework markdown django-filter djangorestframework_simplejwt django-cors-headers factory_boy`

## Run Server
`$ python manage.py runserver`