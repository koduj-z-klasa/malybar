# Mały Bar

Przykładowa aplikacja sieciowa w Django

http://django-maly-bar.readthedocs.io/


# Aplikacja wykorzystuje

- Django 1.10.4
- django-registration

# Przygotowanie środowiska wirtualnego:

W katalogu projektu `malybar` należy utworzyć środowisko wirtualne `.pve`
i zainstalować w nim wymagane biblioteki

    ~$ git clone https://github.com/xinulsw/malybar.git
    ~$ cd malybar
    malybar$ virtualenv .pve
    malybar$ source .pve/bin/activate
    malybar$ pip install -r requirements.txt

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
    
Dodatkowo testy można wykonać na wielu wersjach Pythona przy pomocy narzędzia [TOX](https://tox.readthedocs.io/en/latest/), 
konfiguracja tego narzędzia w pliku [tox.ini](tox.ini) wykonuje także testy pokrycia kodu testami.

    ~/malybar$ tox

Ponadto to repozytorium w GitHub jest spięte z testami wykonywanymi w chmurze. 

![](https://img.shields.io/travis/koduj-z-klasa/malybar.svg)
![](https://img.shields.io/coveralls/koduj-z-klasa/malybar.svg)

Każda kopia repozytorium na GitHubie może uruchomić testy na własnym bezpłatnym koncie by objąć testami własne modyfikacje.

Dokumentacja: http://django-maly-bar.readthedocs.io/

# Heroku: Bezpłatny hosting aplikacji w Chmurze

Każdy może utworzyć jedną bezpłatną aplikację na Heroku, po ściągnięciu Heroku CLI:

    malybar$ heroku login
    malybar$ heroku create
    malybar$ git push heroku master
    malybar$ heroku open

Jeśli chcemy szybko uruchomić nowy serwer to wystarczy użyć przycisku poniżej:

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/koduj-z-klasa/malybar/)

A potem łączymy nowo utworzoną aplikację z naszym lokalnym repozytorium GIT:

    malybar$ heroku login
    malybar$ heroku git:remote -a <NAZWA NOTO UTWORZONEJ APLIKACJI NA HEROKU>
    
Możemy ją zmodyfikować, a potem wykonać wdrożenie zmian na heroku:

    malybar$ git add --all
    malybar$ git commit -am "moje super modyfikacje"
    malybar$ git push heroku master
    malybar$ heroku open

    
Po więcej informacji zapraszamy [do dokumentacji](https://devcenter.heroku.com/articles/getting-started-with-python#introduction)
