Aplikacja wymaga:
Django 1.10.4
django-registration

Przygotowanie środowiska wirtualnego:
~$ virtualenv dj_10_4
~$ cd dj_10_4
~$ source ./bin/activate
~$ pip install Django==1.10.4
~$ pip install django-registration

W katalogu "dj_10_4" należy umieścić katalog projektu "malybar".
Serwer uruchamiamy po aktywowaniu środowiska wirtualnego (poleceniem:
source ./bin/activate), w katalogu "malybar":

~/dj_10_4/malybar$ python manage.py runserver

W bazie są już konta użytkowników (login - hasło):
admin – q1w2e3r4
adam - q1w2e3r4
ewa – q1w2e3r4
