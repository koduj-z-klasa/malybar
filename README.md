# Mały Bar
Przykładowa aplikacja sieciowa w Django

# Aplikacja wykorzystuje
- Django 1.10.4
- django-registration

# Przygotowanie środowiska wirtualnego:

W katalogu projektu `malybar` należy utworzyć środowisko wirtualne `.pve`
i zainstalować w nim wymagane biblioteki

    ~$ git clone https://github.com/xinulsw/malybar.git
    ~$ cd malybar
    ~$ virtualenv .pve
    ~$ source .pve/bin/activate
    ~$ pip install -r requirements.txt

Serwer uruchamiamy po aktywowaniu środowiska wirtualnego
(poleceniem: `source .pve/bin/activate`), w katalogu `malybar`:

    ~/malybar/malybar$ python manage.py runserver

W bazie są już konta użytkowników (login - hasło):

1. admin – q1w2e3r4
2. adam - q1w2e3r4
3. ewa – q1w2e3r4

# Testy

Sprawdzenia poprawnego działania aplikacji dokonujemy uruchamiając testy:

    ~/malybar/malybar$ python manage.py test

Dokumentacja: http://django-maly-bar.readthedocs.io/