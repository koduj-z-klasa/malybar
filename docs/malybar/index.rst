Django
#######

`Django <https://www.djangoproject.com/>`_ to napisany w Pythonie framework
przeznaczony do szybkiego tworzenia aplikacji internetowych.
Został zaprojektowany przez zespół doświadczonych praktyków w taki sposób,
żeby odciążyć programistę od wykonywania typowych, a jednocześnie uciążliwych czynności.
Zalety Django to szybkość, bezpieczeństwo i skalowalność. Inne cechy wymienione są
na polskiej stronie Wikipedii: `Django (framework) <https://pl.wikipedia.org/wiki/Django_(framework)>`_.

Przygotowanie środowiska
========================

.. attention::

  Zanim zaczniesz zwróć uwagę, że:

  - podane niżej polecenia zakładają, że pracujesz w systemie Linux;
  - ``/`` znak *slash* jest separatorem katalogów i plików;
  - ``~`` – oznacza katalog domowy użytkownika w Linuksie;
  - ``~/Django`` – oznacza katalog, w którym należy wydawać polecenia;
  - ``$`` – oznacza znak zachęty, po nim następują właściwe polecenia;
  - ``.pve`` – kropka poprzedzająca nazwę katalogu lub pliku oznacza, że jest on ukryty;
  - Linux rozróżnia małe i duże litery w nazwach katalogów i plików!
  - ścieżki do katalogów i plików w treści podawane są względnie, np. :file:`pizza/urls.py`;


Do pracy z Django potrzebny jest przede wszystkim **interpreter Pythona 2.7.x**.
Jest on domyślnie obecny w systemach Linux. Poza Pythonem potrzebny jest również
instalator pakietów Pythona `pip`. W systemach Linux opartych na Debianie (Ubuntu, Linux Mint)
wystarczy wydać w terminalu polecenie:

.. code-block:: bash

    ~$ sudo apt install python-pip


Następnie instalujemy narzędzie `virtualenv`:

.. code-block:: bash

    ~$ sudo pip install virtualenv


Posłuży nam ono do przygotowania **wyizolowanego środowiska Pythona**,
zawierającego wybraną wersję Django. Wydajemy polecenia:

.. code-block:: bash

		~$ mkdir Django; cd Django
		~/Django$ virtualenv .pve
		~/Django$ source .pve/bin/activate
		(.pve) ~/Django$ pip install Django==1.10.4 django-registration


Na początku tworzymy katalog do przechowywania projektu i wchodzimy do niego.
Katalog nie jest niezbędny, jednak ułatwi utrzymanie porządku na dysku.
Polecenie ``virtualenv .pve`` tworzy ukryty katalog o umownej nazwie :file:`.pve`.
Zawiera on najważniejsze komponenty Pythona. Aby skorzystać z przygotowanego środowiska,
należy go zawsze na początku aktywować za pomocą polecenia ``source .pve/bin/activate``.
Opuszczenie środowiska umożliwia komenda ``deactivate``.

Polecenie ``pip install ...`` instaluje wskazaną wersję Django oraz dodatkową aplikację
ułatwiającą zarządzanie użytkownikami. Tak zainstalowane moduły będą dostępne
tylko w środowisku wirtualnym.

.. tip::

  W systemie Windows:

  * separatorem katalogów i plików jest znak ``\`` (backslash),
  * projekt lepiej budować w katalogu położonym na partycji innej niż systemowa,
  * wielkość liter w nazwach katalogów i plików nie jest brana pod uwagę,
  * instalacja Pythona: `Interpreter Pythona <http://python101.readthedocs.io/pl/latest/env/index.html#inerpreter-pythona>`_,
  * instalacja virtualenv: `pip <http://python101.readthedocs.io/pl/latest/env/index.html#id11>`_,
  * aktywacja środowiska wirtualnego: ``.pve\Scripts\activate.bat``


Ćwiczenie
---------

Zgodnie z powyższym opisem przygotuj samodzielnie wirtualne środowisko do pracy z Django.

.. tip::

	Projektując aplikację będziemy często korzystać z linii poleceń.
	Nie zamykaj więc okna terminala. Jednak **jeżeli przypadkowo zamkniesz terminal**, uruchom go ponownie, wejdź do katalogu nadrzędnego środowiska wirtualnego (``cd ~/Django``), wydaj polecenie ``source .pve/bin/activate``, a na koniec przejdź do katalogu projektu (``cd malybar``), który zaraz utworzymy.


Projekt
========

Upewnij się, że wirtualne środowisko Pythona jest aktywne.
Utworzymy teraz projekt i uruchomimy serwer deweloperski. Wydajemy polecenia:

.. code-block:: bash

    (.pve) ~/Django$ django-admin stratproject malybar
    (.pve) ~/Django$ cd malybar
    (.pve) ~/Django/malybar$ python manage.py runserver


Pierwsze polecenie tworzy szkielet serwisu, ostatnie uruchomia serwer deweloperski,
który możemy wywołać wpisując w przeglądarce adres: ``127.0.0.1:8000``.
Większość zmian w kodzie nie wymaga restartowania serwera. W razie potrzeby
serwer zatrzymujemy naciskając w terminalu skrót :kbd:`CTRL+C`.


.. figure:: img/django_01.jpg


**Struktura plików projektu** – w terminalu wydajemy jedno z poleceń:

.. code-block:: bash

    (.pve) ~/Django/malybar$ tree
    [lub]
    (.pve) ~/Django/malybar$ ls -R


.. figure:: img/django_02.jpg


Nazwa zewnętrznego katalogu :file:`malybar` nie ma znaczenia, można ją dowolnie zmieniać,
to tylko pojemnik na projekt. Zawiera on:

	- :file:`manage.py` – skrypt Pythona do zarządzania projektem;
	- :file:`db.sqlite3` – bazę danych w domyślnym formacie SQLite3.


**Katlog projektu** :file:`malybar/malybar` zawiera:

	- :file:`settings.py` – konfiguracja projektu;
	- :file:`urls.py` – swego rodzaju "menu" naszego projektu, a więc lista wpisów
	  definiująca adresy URL, które będziemy obsługiwać;
	- :file:`wsgi.py` – plik konfiguracyjny wykorzystywany przez serwery WWW.


Plik :file:`__init__.py` obecny w danym katalogu wskazuje, że dany katalog jest modułem Pythona.


Aplikacja
=========

W ramach jednego projektu (serwisu internetowego) może działać wiele aplikacji.
Utworzymy teraz naszą aplikację `pizza` i zbadamy jej strukturę plików:

.. code-block:: bash

  	(.pve) ~/Django/malybar$ python manage.py startapp pizza
  	(.pve) ~/Django/malybar$ tree pizza
  	lub:
  	(.pve) ~/Django/malybar$ ls -R pizza


.. figure:: img/django_03.jpg


**Katalog aplikacji** :file:`malybar/pizza` zawiera:

	- :file:`apps.py` – ustawienia aplikacji;
	- :file:`admin.py` – konfigurację panelu administracyjnego;
	- :file:`models.py` – plik definiujący modele danych przechowywanych w bazie;
	- :file:`views.py` – plik zawierający funkcje lub klasy definiujące tzw. *widoki* (ang. *views*), obsługujące żądania klienta przychodzące do serwera;


Ustawienia projektu
===================

Otwieramy i edytujemy plik :file:`malybar/settings.py`.

**Dostępne w projekcie aplikacje** znajdują się w liście ``INSTALLED_APPS``. Domyślnie Django udostępnia
kilka obsługujących podstawowe funkcjonalności serwisu internetowego. Na początku tej listy
dodamy konfigurację aplikacji `pizza`, na końcu zainstalowanej wcześniej `django-registration`:


.. raw:: html

	<div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script>: <i>malybar/settings.py</i></div>

.. highlight:: python
.. literalinclude:: malybar/settings_01.py
    :linenos:
    :lineno-start: 33
    :lines: 33-42
    :emphasize-lines: 2, 9

**Lokalizacja projektu** obejmuje ustawienie języka i strefy czasowej:

.. raw:: html

	<div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script>: <i>malybar/settings.py</i></div>

.. highlight:: python
.. literalinclude:: malybar/settings_01.py
    :linenos:
    :lineno-start: 108
    :lines: 108-110

Po zapisaniu zmian, uruchomieniu serwera i otwarciu adresu 127.0.0.1:8000 w przeglądarce, zobaczymy:

.. figure:: img/django_04.jpg

Widok domyślny
==============

**Mapowanie adresów URL aplikacji** tworzymy w nowym pliku :file:`pizza/urls.py`,
który wypełniamy następującym kodem:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: pizza/urls_01.py
    :linenos:
    :lineno-start: 1
    :lines: 1-
    :emphasize-lines: 6


Zmienna ``app-name`` – pozwala określić przestrzeń nazw, w której dostępne będą adresy URL
obsługujące aplikację.

Lista ``urlpatterns`` zawiera powiązania między adresami URL a obsługującymi je widokami
zapisanymi w pliku :file:`views.py`, który importujemy w drugiej linii.

Funkcja ``path()`` przyporządkowuje adresowi URL widok, który go obsługuje. Pierwszy parametr to wyrażenie
regularne, do którego Django próbuje dopasować adres otrzymany w żądaniu od klienta. Drugi to nazwa widoku.
Trzeci to unikalna nazwa, dzięki której można odwoływać się w aplikacji do zdefiniowanego adresu.

**Konfiguracja adresów URL projektu** zawarta jest w pliku :file:`malybar/urls.py`.
W tym miejscu dołączamy listy adresów URL zdefiniowane przez poszczególne aplikacje.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: malybar/urls_01.py
    :linenos:
    :lineno-start: 1
    :lines: 1-
    :emphasize-lines: 2, 5

Funkcja ``include()`` jako parametr przyjmuje ścieżkę dostępu do konfiguracji adresów danej
aplikacji. W praktyce jest to nazwa katalogu, w którym znajduje się aplikacja, operator ``.`` (kropka)
oraz domyślna nazwa pliku konfiguracyjnego :file:`urls.py` bez rozszerzenia.

**Widok** definiuje jakiś typ strony WWW, za pomocą którego użytkownik wykonuje w aplikacji
jakieś operacje, np. wyświetla zestawienie danych. Technicznie widok zazwyczaj składa się
z funkcji otrzymującej żądanie klienta i jakiegoś szablonu służącego prezentowaniu danych.

Widok domyślny obsługujący żądania typu GET przychodzące na adres podstawowy serwera
zdefiniujemy w pliku :file:`pizza/views.py`:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: pizza/views_01.py
    :linenos:
    :lineno-start: 1
    :lines: 1-


.. attention::

	**Zapamiętaj:**

	- linia ``# -*- coding: utf-8 -*-`` to określenie kodowania znaków. Należy umieszczać je w pierwszej linii każdego pliku, w którym zamierzamy używać polskich znaków, czy to w komentarzach czy w kodzie.
	- napisy zawierające polskie znaki poprzedzamy literą `u`, np. ``u'składnik'``.


Nazwa funkcji – ``index()`` – jest umowna. Każdy widok otrzymuje szczegóły żądania wysłanego przez klienta
(obiekt typu ``HttpRequest``) i powinien zwrócić jakąś odpowiedź (``HttpResponse``).
W tym wypadku zwracamy funkcję ``render()`` wywołującą wskazany jako drugi parametr szablon,
który otrzymuje dane w postaci słownika ``kontekst`` (nazwa umowna).


**Szablon** (ang. *template*) – to plik tekstowy, służący generowaniu najczęściej plików HTML.
Oprócz tagów HTML-a, zawiera zmienne oraz tagi sterujące języka szablonów Django.

.. note::

	Szablony umieszczamy w katalogu: :file:`pizza/templates/pizza`!

Zawartość szablonu :file:`pizza/templates/pizza/index.html`:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: html
.. literalinclude:: pizza/templates/pizza/index_01.html
    :linenos:
    :lineno-start: 1
    :lines: 1-


Zobacz, jak w znaczniku ``<p>`` wstawiamy przekazaną do szablonu zmienną ``komunikat``,
używamy podwójnych nawiasów sześciennych: ``{{ nazwa_zmiennej }}``.


.. tip::

	W tym miejscu warto usystematyzować dodawanie kolejnych funkcji do naszej aplikacji.
	**Zazwyczaj** proces ten przebiega wg. schematu:

	1) w pliku :file:`urls.py`: przyporządkowujemy adres widokowi;
	2) w pliku :file:`views.py`: definiujemy widok, który najczęściej zwraca szablon połączony z przekazanymi do nego danymi;
	3) w katalogu :file:`templates/nazwa_aplikacji`: tworzymy szablon, który łączy znaczniki HTML-a i dane.


Ćwiczenie
---------

W tym momencie powinieneś przetestować działanie aplikacji. Sprawdź, czy działa serwer. Jeżeli
nie, uruchom go. W przeglądarce odśwież lub wpisz adres domyślny serwera testowego, tj.:
``127.0.0.1:8000``. Powinieneś zobaczyć nazwę projektu i powitanie.

.. figure:: img/django_06.jpg


.. tip::

    **Programowanie to sztuka wykrywania i poprawiania błędów!**
    W przypadku błędów Django wyświetla obszerne informacje, które na pierwszy rzut oka
    są bardzo skomplikowane. Nie musisz studiować całości, żeby zrozumieć, co poszło nie tak.
    Skup się na początku komunikatu!


.. figure:: img/django_05.jpg


Model danych
============

Podstawą użytecznej aplikacji są dane. Django realizuje obiektowy wzorzec programowania,
więc dane definiujemy jako klasy opisujące tzw. modele.
**Model danych** – to kompletne źródło informacji o jakimś obiekcie, zawiera jego właściwości
(pola) oraz metody działań na nich.

W pliku :file:`pizza/models.py` definiujemy klasy opisujące źródła danych naszej aplikacji:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: pizza/models_01.py
    :linenos:
    :lineno-start: 1
    :lines: 1-

Nazwa każdego modelu (klasy) powinna zaczynać się dużą literą. Każdy model jest potomkiem
klasy *Models* (dziedziczenie). Definicja każdej zmiennej (właściwości) zawiera wywołanie
metody tworzącej pole wymaganego typu. Za pomocą nazwanych argumentów określamy dodatkowe cechy pól.


.. note:: Najczęstsze typy pól:

	* ``CharField`` – pole znakowe, przechowuje niezbyt długie napisy, np. nazwy;
	* ``TextField`` – pole tekstowe, dla długich tekstów, np. opisów;
	* ``DecimalField`` – pole dziesiętne, nadaje się do przechowywania liczb rzeczywistych, np. cen;
	* ``Date(Time)Field`` – pole daty (i czasu);
	* ``BooleanField`` – pole logiczne, przechowuje wartość ``True`` lub ``False``;
	* ``ForeignKey`` – pole klucza obcego, czyli relacji; wymaga nazwy powiązanego modelu jako pierwszego argumentu.

  Właściwości pól:

    * ``verbose_name`` lub napis podany jako pierwszy argument – przyjazna nazwa pola;
    * ``max_length`` – maksymalna długość pola znakowego;
    * ``blank = True`` – pole może zawierać ciąg pusty;
    * ``help_text`` – tekst podpowiedzi;
    * ``max_digits``, ``decimal_places`` – określenie maksymalnej ilości cyfr i ilości miejsc po przecinku liczby rzeczywistej;
    * ``auto_now_add = True`` – data (i czas) wstawione zostaną automatycznie;
    * ``default`` – określenie wartości domyślnej pola;
    * ``choices`` – wskazuje listę wartości dopuszczalnych dla danego pola;
    * ``on_delete`` – określa, co ma się stać w przypadku usunięcia obiektu nadrzędnego (pizzy), na który wskazuje klucz obcy, opcja ``models.CASCADE`` wymusza usunięcie obiektów zależnych (składników);
    * ``realted_name`` – nazwa używana w relacji zwrotnej, kiedy z obiektu nadrzędnego (pizzy) chcemy odwołać się do obiektów zależnych (składników), np. ``pizza.skladniki``.

W bazie chcemy przechowywać dane o pizzach. Każda z nich składać się może z wielu składników.
Tak więc między modelami `Pizza` i `Skladnik` istnieje relacja jeden-do-wielu.

Po dokonaniu zmian w bazie tworzymy tzw. *migrację*, w terminalu wydajemy polecenia:

.. raw:: html

  <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>


.. code-block:: bash

  (.pve) ~/Django/malybar$ python manage.py makemigrations pizza
  (.pve) ~/Django/malybar$ python manage.py migrate


**Migracja** – tworzona przez pierwsze polecenie, to informacje o zmianie w bazy danych zapisywana
przez Django w języku SQL w katalogu :file:`pizza/migrations`.

Drugie polecenie na podstawie migracji wszystkich zarejestrowanych aplikacji (w tym domyślnych)
buduje lub aktualizuje bazę danych. Z nazw modeli Django utworzy odpowiednie tabele, w oparciu o zdefiniowane
właściwości – odpowiednie kolumny.

.. figure:: img/django_07.jpg

Zmiany modeli
-------------

Modele można zmieniać.

1. Do modelu `Pizza` dodamy pole przechowujące użytkownika, który dodał ją do bazy.

	- przed definicjami klas dodaj import ``from django.contrib.auth.models import User``
	- dodaj klucz obcy o nazwie ``autor`` wskazujący na model ``User``: ``autor = models.ForeignKey(User, on_delete=models.CASCADE)``

2. Dodamy możliwość "autoprezentacji" modeli, czyli wyświetlania ich znakowej reprezentacji.

	- do każdej klasy dodaj następującą metodę:

.. code-block:: python

        def __unicode__(self):
            return u'%s' % (self.nazwa)

3. W panelu administracyjnym przydatna jest forma liczby mnogiej służąca nazywaniu egzemplarzy danego modelu.

	- w każdym modelu umieść dodatkową klasę `Meta` z odpowiednią formą liczby mnogiej, np.:

.. code-block:: python

        class Meta:
            verbose_name_plural = 'pizze'

.. attention::

  **Zapamiętaj**: po zmianie modelu należy utworzyć migrację aplikacji
  i zaktualizować bazę danych projektu (polecenia ``makemigrations`` i ``migrate``)!


.. tip::

  Jeżeli z jakichś powodów kolejnej migracji nie da się zastosować, można:

  - usunąć bazę :file:`db.sqlite3`;
  - usunąć katalog :file:`migrations` aplikacji;
  - ponownie utworzyć migrację i zaktualizować bazę projektu.


Strona administracyjna
======================

Zarządzanie treściami czy użytkownikami wymaga panelu administracyjnego,
Django dostarcza nam go automatycznie.

**Konto administratora** tworzymy, wydając w terminalu polecenie:

.. code-block:: bash

    ~/Django/malybar$ python manage.py createsuperuser

Django zapyta o nazwę, e-mail i hasło. Podajemy: `admin`, `""` (pomijamy), `q1w2e3r4`.

Aplikacja w panelu administratora: uzupełniamy plik :file:`pizza/admin.py`:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: pizza/admin_01.py
    :linenos:
    :lineno-start: 1
    :lines: 1-

Po zaimportowaniu modeli danych rejestrujemy je w panelu, dzięki temu będziemy mogli dodawać
i modyfikować dane użytkowników i aplikacji.

.. figure:: img/django_08.jpg


Zarządzanie danymi
------------------

1. Uruchom serwer i wywołaj w przeglądarce adres: ``127.0.0.1:8000/admin``.
2. Zaloguj się jako administrator, dodaj pizzę i przynajmniej jeden składnik.
3. Utwórz konto dla użytkownika "uczen" z hasłem "q1w2e3r4". Przydziel mu prawa do dodawania, modyfikowania i usuwania pizz i składników. Uwaga: nie zapomnij zaznaczyć opcji "W zespole"!
4. Zaloguj się na konto "uczen" i dodaj jeszcze jedną pizzę z co najmniej jednym składnikiem.

.. note::

	Obsługa panelu administracyjnego jest dobrą okazją, żeby zobaczyć jak wygląda komunikacja
	między klientem a serwerem w aplikacjach sieciowych wykorzystujących protokół http.
	Serwer testowy wyświetla pełen zapis sesji w oknie terminala.


.. figure:: img/django_09.jpg


Lepszy panel
------------

W podstawowej konfiguracji modele `Pizza` i `Skladnik` rejestrowane i obsługiwane są osobno.
Z logicznego i praktycznego punktu widzenia dobrze byłoby, gdyby pizza i jej składniki stanowiły
całość, również podczas dodawania. W tym celu zmienimy treść pliku :file:`pizza/admin.py` na:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: pizza/admin_02.py
    :linenos:
    :lineno-start: 1
    :lines: 1-


Formularze generowane automatycznie w panelu administracyjnym obsługiwane są
przez klasę `ModelAdmin`. Dostosujemy ją do naszych potrzeb.
Na początku używamy klasy `TabularInline` pozwalającej edytować kilka modeli na jednej stronie.
Nam chodzi o składniki, dlatego tworzymy klasę `SkladnikiInline` i ustawiamy
odpowiednie opcje:

- ``model`` – nazwa modelu, dla którego modyfikujemy formularz;
- ``fields`` – lista pól, dla których mają być generowane formularze;
- ``extra`` – ilość pustych formularzy umożliwiających wprowadzanie danych;
- ``max_num`` – maksymalna ilość obiektów możliwych do dodania za jednym razem.

W klasie `PizzaAdmin` projektujemy wygląd całego formularza dodawania pizz.
Używamy następujących opcji:

- ``exclude`` – lista pól wykluczonych z formularza;
- ``inlines`` – nazwa klasy definiującej sposób wyświetlania formularzy dla innych modeli;
- ``search_fields`` – lista pól, które będą przeglądane podczas wyszukiwania obiektów;
- ``list_per_page`` – maksymalna ilość obiektów pokazywanych na stronie;
- ``formfield_overrides`` – słownik, w którym kluczami są klasy pól formularza; służy modyfikacji ich wyświetlania, w naszym przypadku ustalamy tu właściwości pola tekstowego.

Utworzenie swojej klasy administracyjnej pozwala również na modyfikację zachowań
panelu, np. zapisywania danych. Metoda ``save_model()`` pozwala nam przypisać
zalogowanego użytkownika jako autora dodawanego obiektu. Dzięki temu użytkownik
nie musi wybierać autora (czyli siebie) z listy.

Do rejestrowania klas modyfikujących domyślną klasę ``ModelAdmin`` używamy dekoratora
w postaci ``@admin.register(models.Pizza)``.


.. figure:: img/django_10.jpg


Użytkownicy
===========

Do zarządzania użytkownikami użyjemy zainstalowanej na początku aplikacji `django-registration`.
W pliku :file:`malybar/settings.py` dodaliśmy ją już do listy aplikacji ``INSTALLED_APPS``.
Teraz na końcu tego pliku dodamy kilka ustawień:

.. raw:: html

	<div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script>: <i>malybar/settings.py</i></div>

.. highlight:: python
.. literalinclude:: malybar/settings_02.py
    :linenos:
    :lineno-start: 124
    :lines: 124-127


.. tip::

  Uwaga: komentarze w powyższym kodzie zawierają polskie znaki, jeżeli wstawisz je do pliku,
  pamiętaj o dodaniu informacji o kodowaniu znaków w pierwszej linii!


Następnie włączamy konfigurację adresów URL aplikacji do pliku :file:`malybar/urls.py`:

.. raw:: html

	<div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: malybar/urls_02.py
    :linenos:
    :lineno-start: 20
    :lines: 20-25
    :emphasize-lines: 4

Teraz możemy zobaczyć, jakie adresy udostępnia aplikacja `django-registration`,
wpisując w przeglądarce adres ``127.0.0.1:8000/konta/``:

.. figure:: img/django_11.jpg


Jak widać, mamy do dyspozycji m.in następujące adresy:

	- ``/konta/register`` o nazwie ``registration_register`` – do tworzenia konta;
	- ``/konta/login`` o nazwie ``auth_login`` – do logowania;
	- ``/konta/logout`` o nazwie ``auth_logout`` – do wylogowywania.

Szablony
-----------

Na początku utworzymy szablon służący do rejestracji w pliku
:file:`pizza/templates/registration/registration_form.html`:

.. raw:: html

	<div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: html
.. literalinclude:: pizza/templates/registration/registration_form_01.html
    :linenos:
    :lineno-start: 1
    :lines: 1-

W powyższym kodzie widać, w jaki sposób używamy przygotowanych wcześniej formularzy
w szablonach. Znacznik HTML-a ``<form>`` i przycisk typu ``submit`` musimy wstawić sami,
resztę może za nas zrobić Django:

	- ``{% csrf_token %}`` – ten tag dodaje ukryte pole zabezpieczające formularz przed atakami typu `CSRF <https://pl.wikipedia.org/wiki/Cross-site_request_forgery>`_;
	- ``{{ form.as_p }}`` – metoda ``as_p`` renderuje przekazany do szablonu w zmiennej ``form`` formularz przy użyciu znaczników akapitów ``<p>``.

Potrzebujemy również szablonu logowania, który umieszczamy w pliku
:file:`pizza/templates/registration/login.html`:

.. raw:: html

	<div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: html
.. literalinclude:: pizza/templates/registration/login_01.html
    :linenos:
    :lineno-start: 1
    :lines: 1-

**Adresy URL w szablonach** wstawiamy za pomocą tagu ``url``, który jako pierwszy obowiązkowy argument
przyjmuje nazwę adresu zdefiniowaną w argumencie ``name`` w plikach :file:`urls.py`.

.. attention::

	**Zapamiętaj**: nawiasy ``{{ zmienna }}`` służą do wstawiania wartości zmiennych,
	nawiasów ``{% tag %}`` używamy do tagów języka szablonów.


Na koniec szablon wyświetlany po wylogowaniu, czyli plik
:file:`pizza/templates/registration/logout.html`:

.. raw:: html

	<div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: html
.. literalinclude:: pizza/templates/registration/logout_01.html
    :linenos:
    :lineno-start: 1
    :lines: 1-


Ćwiczenie
----------

Po dodaniu szablonów można już przetestować tworzenie konta, logowanie i komunikat po wylogowaniu
wpisując w przeglądarce po nazwie serwera ``127.0.0.1:8000`` adresy:

	- ``/konta/register`` – tworzenie nowego konta; utwórz konto `ewa` z hasłem `q1w2e3r4`;
	- ``/konta/login`` – logowanie; zaloguj się na utworzone wcześniej konto `uczen`;
	- ``/konta/logout`` – potwierdzenie wylogowania;

Spróbuj wstawić do szablonu :file:`templates/pizza/index.html` odnośniki do powyższych adresów.
Na końcu pliku umieść kod:

.. code-block:: html

  <ul>
    {% if not user.is_authenticated %}
      <li><a href="{% url 'nazwa_adresu' %}">Zaloguj się</a></li>
      <li><a href="{% url 'nazwa_adresu' %}">Utwórz konto</a></li>
    {% else %}
      <li><a href="{% url 'nazwa_adresu' %}">Wyloguj się</a></li>
    {% endif %}
  </ul>


– i zamień tekst `nazwa_adresu` na właściwe nazwy adresów URL.

.. attention::

	**Zapamiętaj**: w szablonach dostępne są konstrukcje warunkowe wstawiane za pomocą tagów
	``{% if warunek %} ... {% else %} ... {% endif %}``.
	W szablonach dostępny jest obiekt ``user`` zawierający informacje o użytkowniku.
	Metoda ``is_authenticated`` zwraca prawdę, jeżeli użytkownik został zalogowany.


.. figure:: img/django_12.jpg


ListView
========

Praktycznie w każdym serwisie występują strony zawierające zestawienie danych.
Utworzymy więc widok prezentujący listę pizz.

**Definicja adresu** – w pliku :file:`pizza/urls.py` dodajemy importy:

.. raw:: html

	<div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: pizza/urls_02.py
    :linenos:
    :lineno-start: 3
    :lines: 3-5

Następnie przyporządkujemy adres ``lista/`` o nazwie ``lista`` widokowi `ListView`.
Dodajemy kod:

.. raw:: html

	<div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: pizza/urls_02.py
    :linenos:
    :lineno-start: 8
    :lines: 8-12
    :emphasize-lines: 3-4

**Widoki generyczne** (ang. *generic views*), udostępniane przez Django, służą przygotowywaniu typowych
stron WWW. `ListView` – jak wskazuje nazwa – tworzy stronę z listą obiektów. Najważniejszym
argumentem widoku jest ``model``, czyli nazwa modelu obiektów, które mają być wyświetlane.

Lista obiektów będzie dostępna w szablonie w zmiennej o domyślnej nazwie ``object_list``.


.. note::

	Widoki generyczne są klasami. Jeżeli używamy ich w pliku :file:`urls.py`,
	musimy użyć ich metody ``as_view()``, aby potraktowane zostały jak funkcje.


Jeżeli chcemy, aby jakiś adres dostępny był tylko dla zalogowanych użytkowników,
wywołanie widoku umieszczamy w funkcji ``login_required()``.

**Szablon dla widoku** generycznego ma schematyczną nazwę, w tym wypadku `nazwa_modelu_list.html`.
Tworzymy więc plik :file:`templates/pizza/pizza_list.html` o zawartości:

.. raw:: html

	<div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: html
.. literalinclude:: pizza/templates/pizza/pizza_list_01.html
    :linenos:
    :lineno-start: 1
    :lines: 1-

Konstrukcję ``for p in object_list`` należy rozumieć następująco:
`dla każdego obiektu pobranego z listy object_list do zmiennej p wykonaj:`.
W pętli wyświetlamy kolejne zmienne: numer iteracji (``forloop.counter``),
nazwę, autora i datę dodania pizzy. Jeżeli zalogowany użytkownik dodał daną pizzę,
wyświetlamy odnośniki umożliwiające edycję i usuwanie obiektów.

.. attention::

	**Zapamiętaj**: tagów ``{% for zmienna in lista %} ... {% endfor %}`` używamy w szablonach,
	jeżeli potrzebujemy pętli.


Na koniec dodaj do szablonu :file:`index.html` odnośnik do listy. W atrybucie ``href`` odnośnika użyj kodu:

.. code-block:: html

    {% url 'pizza:lista' %}

Zwróć uwagę, że **nazwa URL-a poprzedzona została nazwą przestrzeni nazw**, którą zdefiniowaliśmy
w parametrze ``namespace`` podczas włączania listy adresów naszej aplikacji do listy projektu.

.. figure:: img/django_13.jpg


Create View
===========

Zajmiemy się teraz możliwością dodawania danych, czyli pizz i składników.
Na początku utworzymy nowy plik :file:`pizza/forms.py`, z następującą zawartością:

.. raw:: html

	<div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: pizza/forms_01.py
    :linenos:
    :lineno-start: 1
    :lines: 1-

**Definicje formularzy** umieszczamy w plikach o nazwie :file:`forms.py`.
Co prawda Django potrafi automatycznie tworzyć formularze na podstawie modeli,
ale wymagają one dostosowania. Dlatego tworzymy klasę `PizzaForm`, w której
definiujemy formularz do dodawania i edytowania pizz. Właściwe opcje umieszczamy
w podklasie `Meta`:

	- ``model`` – model, dla którego dostosowujemy formularz;
	- ``exclude`` – tupla z polami, które wykluczamy z formularza;
	- ``widgets`` – opcjonalny słownik, w którym ustalamy właściwości widżetów HTML.

Django automatycznie generuje widżety HTML odpowiadających typom pól modelu.
Np. pola ``CharField`` reprezentowane są przez tagi ``<input>``, a pola ``TextField`` przez ``<textarea>``.
Możemy zmienić domyślne ustawienia. W powyższym przykładzie określiliśmy
rozmiar pola tekstowego na 2 wiersze i 80 kolumn.

**Zestaw (pod)formularzy** – wyświetlany razem z formularzem nadrzędnym,
definiowany jest jako tzw. `formset` przy użyciu funkcji ``inlineformset_factory()``:

- ``parent_model`` – model nadrzędny dla składników, czyli `Pizza`;
- ``model`` – model, dla którego definiujemy zestaw formularzy;
- ``max_num``, ``min_num`` – maksymalna i minimalna ilość obiektów, które można dodać;
- ``validate_max``, ``validate_min`` – podczas walidacji sprawdzana będzie minimalna i maksymalna ilość obiektów;
- ``extra`` – ilość początkowych formularzy do dodawania obiektów;
- ``fields`` – lista pól, dla których wygenerowane zostaną widżety.

Klasę `SkladnikiFormSet` wykorzystamy po to, aby można było dodawać dane pizzy
i składników w obrębie jednej strony, podobnie jak w panelu administracyjnym.


.. tip::

	Definiowanie formularzy używanych w panelu administracyjnym,
	czy na stronach, w tym formularzy `inline`, wymaga określania podobnych
	lub identycznych opcji, np. ``model``, ``fields``, ``extra`` itd.

	Jeżeli określimy właściwość ``fields``, nie musimy podawać ``extra``.
	Działa to również w drugą stronę.


**Dodanie adresu** – w pliku :file:`pizza/urls.py` tworzymy adres ``/dodaj``:

.. raw:: html

	<div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: pizza/urls_03456.py
    :linenos:
    :lineno-start: 13
    :lines: 13


**CreateView** – to kolejny widok generyczny, który posłuży zgodnie z nazwą
do dodawania danych. Użyjemy go w pliku :file:`pizza/views.py`. Na początku
dodajemy, jak zwykle, importy:


.. raw:: html

	<div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: pizza/views_02.py
    :linenos:
    :lineno-start: 4
    :lines: 4-10

Następnie na końcu pliku :file:`pizza/views.py` umieszczamy kod:

.. raw:: html

	<div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: pizza/views_02.py
    :linenos:
    :lineno-start: 19
    :lines: 19-

Widok ``PizzaCreate`` to klasa dziedzicząca i dostosowująca właściwości i metody
klasy rodzica, czyli `CreateView`. Właściwości:

- ``model`` – pozwala określić model, dla którego tworzymy widok;
- ``form_class`` – klasa formularza do dodawania obiektu, którą zdefiniowaliśmy w :file:`forms.py`;
- ``success_url`` – adres URL, pod który zostaniemy przekierowani po poprawnym obsłużeniu formularza;
  aby nie wstawiać adresu literalnie, używamy funkcji ``reverse_lazy()``.

.. note::

	**GET i POST** – to dwa podstawowe typy żądań zdefiniowane w protokole `HTTP <https://pl.wikipedia.org/wiki/Hypertext_Transfer_Protocol>`_:

	1. GET – to żądanie klienta (przeglądarki), które dotyczy zazwyczaj pobrania zasobu z serwera bez zmieniania danych, innymi słowy są to operacje odczytu;
	2. POST – to żądania klienta wysyłające dane na serwer, aby zmienić dane po jego stronie: utworzyć nowe, zaktualizować lub usunąć.

Zadaniem widoku jest wygenerowanie pustego formularza, kiedy użytkownik wyświetla
go po raz pierwszy (żądanie typu GET), później sprawdzenie przesłanych
danych (żądanie typu POST) i ich zapisanie w bazie. Ponieważ chcemy dodawać
pizze (obiekt nadrzędny) i składniki (obiekty zależne) razem, musimy
widok dostosować do obsługi zestawu formularzy (ang. *formset*) składników.

**Kontekst widoku** – zawiera słownik z danymi, metoda ``get_context_data()`` domyślnie
dopisuje do niego formularz główny dla pizzy. My wykorzystujemy ją, aby dodać
*formset* dla składników. W zależności od typu żądania
tworzymy pusty (GET) lub wypełniony przesłanymi danymi zestaw (POST).

**Walidacja danych** – to sprawdzanie poprawności przesłanych danych.
Przeprowadzamy ją w metodzie ``post()``, którą nadpisujemy.
Na podstawie przesłanych danych tworzymy:

- ``form = self.get_form()`` – obiekt formularza głównego;
- ``skladniki = forms.SkladnikiFormSet(self.request.POST)`` – *formset*
  składników.

Metoda ``is_valid()`` sprawdza poprawność danych, np. to, czy wartości
pól wymaganych zostały podane.

**Zapisanie danych** ma miejsce w metodzie ``form_valid()`` wywoływanej po
pozytywnej walidacji. W metodzie uzupełniamy pole ``autor``,
które wykluczyliśmy z formularza głównego.
Po zapisaniu przekierowujemy użytkownika na zdefiniowany wcześniej adres.

Jeżeli walidacja nie powiedzie się, wywoływana jest metoda ``fomr_invalid()``.
Nadpisujemy ją po to, aby zwrócić błędy nie tylko formularza głównego,
ale również formularzy zależnych.

**Szablon dodawania** – dla widoku typu `CreateView` ma nazwę tworzoną wg schematu
:file:`nazwa_modelu_form.html`. Tworzymy więc plik :file:`pizza/templates/pizza/pizza_form.html`:

.. raw:: html

	<div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: html
.. literalinclude:: pizza/templates/pizza/pizza_form_01.html
    :linenos:
    :lineno-start: 1

Wygenerowanie HTML-owej wersji formularza głównego pozostawiamy Django.
Natomiast formularze dla składników renderujemy ręcznie.

.. attention::

	Podczas ręcznego renderowania zestawów formularzy *formset* nie wolno
	zapomnieć o polu ``management_form`` i polach ``id`` (identyfikatorów)
	kolejnych formularzy.


Po zdefiniowaniu formularzy, utworzeniu adresu, widoku i szablonu
możemy dodawać nowe pizze! Nie zapomnij o dodaniu odnośnika na stronie głównej!

.. figure:: img/django_14.jpg


UpdateView
==========

**UpdateView** – to widok umożliwiający edycję utworzonych danych, współdzieli
z widokiem dodawania formularz, *formset* i szablon.

**Import** – na początku, jak zwykle, importujemy klasę `UpdateView`. Dodajemy ją po przecinku za widokiem `CreateView`.

**Adres edycji** definiujemy w pliku :file:`pizza/urls.py`:

.. raw:: html

	<div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: pizza/urls_03456.py
    :linenos:
    :lineno-start: 14
    :lines: 14

Adres składać się będzie z części ``/edytuj/``, po której podany powinien zostać
argument o nazwie ``pk`` będący liczbą. Przykładowy poprawny adres może mieć
więc postać ``/edytuj/2``. Nazwa argumentu ``pk`` nie jest przypadkowa,
to skrót od słów ang. `primary key` (klucz podstawowy). Jest on automatycznie
przekazywany do klas widoków opartych na modelach.

Sam widok umieszczamy na końcu pliku :file:`pizza/views.py`:

.. raw:: html

	<div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: pizza/views_03.py
    :linenos:
    :lineno-start: 57
    :lines: 57-
    :emphasize-lines: 20, 22-24

Jak widać większość kodu jest identyczna z widokiem dodawania. Są jednak ważne różnice:

1. W metodzie ``post()`` instrukcja ``self.object = self.get_object()`` – utworzenie
   instancji edytowanego obiektu;
2. Argument ``instance`` zestawu formularzy, zawierający dane edytowanych składników,
   przyjmuje wartości z ``self.object`` już w metodzie ``post()``, a nie w metodzie
   ``form_valid()``.

.. tip::

  W szablonie :file:`pizza_list.html` warto uzupełnić odnośnik do edycji.
  Użyj kodu ``{% url 'pizza:edytuj' p.id %}``.


Na koniec warto wspomnieć, że zapisywanie edytowanych danych dochodzi do skutku,
o ile dane zostały zmienione.

DeleteView
==========

**DeleteView** – służy do usuwania danych, których identyfikator przesłany jest
za pomocą żądania `POST`, w przypadku `GET` wyświetla formularz potwierdzenia.

**Import** – importujemy klasę `DeleteView`. Dodajemy ją po przecinku za widokiem `UpdateView`.

**Adres widoku** będzie podobny, jak dla edycji danych, tzn. przekażemy w nim identyfikator
obiektu, który chcemy usunąć. W pliku :file:`pizza/urls.py` dopisujemy:

.. raw:: html

	<div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: pizza/urls_03456.py
    :linenos:
    :lineno-start: 15
    :lines: 15

**Sam widok** umieszczamy na końcu pliku :file:`pizza/views.py`:

.. raw:: html

	<div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: pizza/views_04.py
    :linenos:
    :lineno-start: 98
    :lines: 98-

**Uzupełniamy kontekst**, ponieważ chcemy w szablonie potwierdzenia wyświetlić
również listę składników pizzy. W metodzie ``get_context_data()``
pobieramy listę składników w zapytaniu ``skladniki = models.Skladnik.objects.filter(pizza=self.object)``.
Warto zwrócić uwagę na kryterium filtrowania rekordów.
Używamy klucza obcego (pola ``pizza`` z modelu `Skladnik`), który musi
odpowiadać obiektowi pizzy przypisanemu do właściwości ``self.object`` widoku.

**Szablon widoku** nazywamy wg domyślnego schematu `model_confirm_delete.html`,
czyli tworzymy plik :file:`pizza/templates/pizza/pizza_confirm_delete.html`
z następującą zawartością:

.. raw:: html

	<div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: html
.. literalinclude:: pizza/templates/pizza/pizza_confirm_delete_01.html
    :linenos:
    :lineno-start: 1
    :lines: 1-

Obiekt pizzy, który usuwamy, dostępny jest w zmiennej ``object``. Dodatkowo
w pętli wyświetlamy przekazane przez kontekst składniki.


.. figure:: img/django_16.jpg


DetailView
==========

**DetailView** – widok szczegółowy służy prezentowaniu wszystkich informacji dotyczących
jakiegoś obiektu na jednej stronie.

**Import** – importujemy klasę dopisując w pliku :file:`pizza/views.py`:
``from django.views.generic import DetailView``.

**Adres widoku** jest zbudowany na takiej samej zasadzie, jak w przypadku edycji i usuwania danych,
czyli zawiera identyfikator obiektu. W pliku :file:`pizza/urls.py` dopisujemy:

.. raw:: html

  <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: pizza/urls_03456.py
    :linenos:
    :lineno-start: 16
    :lines: 16

**Widok** umieszczamy na końcu pliku :file:`pizza/views.py`:

.. raw:: html

  <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: pizza/views_05.py
    :linenos:
    :lineno-start: 111
    :lines: 111-

**W kontekście widoku** dodajemy, podobnie jak w przypadku widoku usuwania,
listę składników danej pizzy.

.. note::

  Widoki `UpdateView`, `DeleteView` oraz `DetailView` na podstawie przekazanego
  w zmiennej ``pk`` identyfikatora automatycznie pobierają odpowiedni obiekt z bazy
  przy użyciu metody ``get_object()``.

**Szablon widoku** nazywamy wg domyślnego schematu `model_detail.html`,
czyli tworzymy plik :file:`pizza/templates/pizza/pizza_detail.html`
z następującą zawartością:

.. raw:: html

  <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: html
.. literalinclude:: pizza/templates/pizza/pizza_detail_01.html
    :linenos:
    :lineno-start: 1
    :lines: 1-

Ćwiczenie
---------

Dodaj do szablonu listy obiektów (pizz) link o nazwie np. "Szczegóły",
który wyświetli dodatkowe inforamcje o danej pizzy.


Szablon bazowy
==============

Ponieważ o atrakcyjności serwisu w dużej mierze decyduje jego wygląd, a także
interaktywny interfejs, zobaczymy, jak względnie łatwo dodać do projektu
framework `Bootstrap <http://getbootstrap.com/>`_ dostarczający gotowe elementy
HTML, CSS i JavaScript przeznaczone do projektowania mobilnych i responsywnych stron WWW.

**Szablon bazowy** – to szkielet stron w naszym serwisie; zawiera powtarzające się elementy,
np. menu, jak również bloki, które można wypełniać dostosowaną treścią w szablonach dziedziczących.
Tworzymy plik :file:`pizza/templates/pizza/base.html`:

.. raw:: html

  <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>


.. highlight:: html
.. literalinclude:: pizza/templates/pizza/base.html
    :linenos:
    :lineno-start: 1
    :lines: 1-

**Zasoby statyczne**, czyli rzadko zmieniane, to arkusze stylów CSS, skrypty JS,
pliki graficzne, ewentualnie czcionki i ikony, umieszcza się w podkatalogu
:file:`pizza/static/pizza`. Dla przejrzystości grupuje się je zazwyczaj
w folderach :file:`css`, :file:`js` czy :file:`images` – ich nazwy są umowne.

Wstawianie zasobów statycznych do szablonu wymaga umieszczenia na początku
dokumentu tagu ``{% load static %}``. Dzięki temu możemy generować poprawne
adresy URL dla atrybutów ``href`` czy ``src`` za pomocą tagu
``{% static 'względna_ścieżka_do_zasobu' %}``, np.:
- ``href="{% static 'pizza/css/pizza.css' %}"``;
- ``src="{% static 'pizza/images/pizza.jpg' %}"``.

**Bloki szablonu** – to miejsca, które szablony dla poszczególnych stron
serwisu mogą wypełniać własną zawartością. Blok definiujemy przy użyciu
tagów: ``{% block nazwa_bloku %} treść_domyślna {% endblock %}``.

Rozszerzanie szablonu
---------------------

Szablony poszczególnych widoków rozszerzają szablon bazowy dziedzicząc elementy
powtarzalne i wypełniając bloki własną zawartością. Dotychczasową zawartość
szablonu :file:`pizza/index.html` zastępujemy kodem:

.. raw:: html

  <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: html
.. literalinclude:: pizza/templates/pizza/index_bs.html
    :linenos:
    :lineno-start: 1
    :lines: 1-

Tag ``{% extendes "pizza/base.html" %}`` informuje, że korzystamy z podanego szablonu
podstawowego. Sekwencje tagów ``{% block nazwa_bloku %} ... {% endblock %}``
wypełniają zdefiniowane w szablonie bazowym bloki odpowiednią zawartością.

Jeszcze jeden przykład. Szablon :file:`registration/login.html` będzie wyglądał następująco:

.. raw:: html

  <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: html
.. literalinclude:: pizza/templates/registration/login_bs.html
    :linenos:
    :lineno-start: 1
    :lines: 1-


Ćwiczenie
---------

Dostosuj pozostałe szablony, tak aby korzystały z szablonu bazowego.

.. figure:: img/django_17.jpg


Bootstrap
=========

Szablon bazowy oparty został na przykładowym layoucie dostępnym na stronach Bootstrapa.
W nagłówku strony w znaczniku ``<link>`` ładowany jest podstawowy komponent frameworka,
tzn. arkusz stylów CSS :file:`bootstrap.min.css`. Na końcu szablonu w znacznikach
``<script>`` dołączamy skrypty JavaScript: bibliotekę JQuery i komponent JS
Bootstrapa, plik :file:`bootstrap.min.js`.

Podstawą Bootsrapa jest system podziału strony na 12 części o
tej samej szerokości zwany `grid system <http://getbootstrap.com/css/#grid>`_.
Tworząc układ strony ustalamy szerokość kolumn łącząc części w grupy
za pomocą klas CSS, np.:

.. code-block:: html

  <div class="container">
    <div class="row">
      <div class="col-sm-8">
        <!-- zawartość -->
      </div>
      <div class="col-sm-4">
        <!-- zawartość -->
      </div>
    </div>
  </div>

Powyższy kod daje nam podział na 1. kolumnę o szerokości 8 części
i 2. kolumnę o szerokości 4. Przyrostek ``-sm`` informuje, że podział
ten obowiązuje dla rozdzielczości >= 768px. Podziałem części na kolumny
możesz manipulować, pamiętać tylko trzeba, żeby ich suma dawała 12.

Znacznik ``<div class="container">``, wyodrębnia sekcję strony,
``<div class="row">`` tworzy podział na wiersze.

Kolejnym często używanym elementem Bootstrapa jest menu umieszczane
w znaczniku ``<nav>``. W szablonie wykorzystujemy menu przytwierdzone
na stałe u góry strony, widoczne również w trakcie jej przewijania.
Decyduje o tym klasa ``navbar-fixed-top``.

Menu składa się z 2 części. Pierwsza wyznaczona klasą ``navbar-header``
zawiera przycisk mobilny i obrazek, druga z identyfikatorem ``id=navbar``
zawiera właściwe odnośniki w postaci elementów listy ``<ul>``.

Cały layout ma więc trzy części:

1. menu;
2. kontener zawierający jeden wiersz podzielony na dwie kolumny;
3. kontener zawierający stopkę dokumentu.


.. raw:: html

  <hr>

.. note::

  Kompletny kod aplikacji dostępny jest w repozytorium:
  `https://github.com/xinulsw/malybar <https://github.com/xinulsw/malybar>`_.

