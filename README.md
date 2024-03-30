### GoIT moduł 2 web
# Zadanie domowe #13 (cześć druga - dotycząca Django)
Twoim zadaniem jest udoskonalenie aplikacji Django z zadania domowego nr 10.
### Zadania
- Zaimplementuj mechanizm resetowania hasła dla zarejestrowanego użytkownika;
- Wszystkie zmienne środowiskowe używane w pliku `setting.py` powinny być przechowywane w pliku `.env`.

> [!TIP]
> Przed uruchomieniem programu należy utworzyć plik `.env`, zgodnie z dołączonym do projektu wzorcowym plikiem: `env`

# Zadanie domowe #10

W poprzednim zadaniu domowym wykonałeś scraping strony [http://quotes.toscrape.com](http://quotes.toscrape.com).

1. Teraz musisz zaimplementować odpowiednik tej strony w Django.
2. Zaimplementuj możliwość rejestracji na stronie i logowania się do niej.
3. Zaimplementuj możliwość dodania nowego autora do strony tylko dla zarejestrowanego użytkownika.
4. Zaimplementuj możliwość dodania nowego cytatu do serwisu ze wskazaniem autora tylko dla zarejestrowanego użytkownika.
5. Zaimplementuj możliwość odwiedzenia strony każdego autora bez uwierzytelniania użytkownika.
6. Zrób tak, by wszystkie cytaty są dostępne do przeglądania bez uwierzytelniania użytkownika.

### Część dodatkowa
1. Zaimplementuj wyszukiwarkę cytatów według tagów. Po kliknięciu na tag, powinna być wyświetlona lista cytatów z tym tagiem.
2. Zaimplementuj blok "Top Ten tags" i wyświetlaj najpopularniejsze tagi.
3. Zaimplementuj paginację. Są to przyciski next i previous.
4. Zamiast przesyłać dane z bazy danych MongoDB, zaimplementuj możliwość scrapowania danych bezpośrednio z Twojej witryny, klikając określony przycisk w formularzu i wypełniając bazę danych witryny.
