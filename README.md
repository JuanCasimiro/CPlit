CplitProyect 
Realizado en python con Django

Web app para dividr gastos entre amigos

Hosted on: https://c-plit.vercel.app/

#al clonar el proyecto

python pip install -U pip

python -m pip install -r requirements.txt

# Hay que ejecutar estos comandos antes de hacer un push al repo 
python manage.py makemigrations --noinput

python manage.py migrate --noinput

python manage.py collectstatic --noinput --clear

