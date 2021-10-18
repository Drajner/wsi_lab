Mamy problem plecakowy jak na wykładzie:
    w = np.array([8, 3, 5, 2]) #waga przedmiotów
    W = 9 #maksymalna waga plecaka
    p = np.array([16, 8, 9, 6]) #wartość przedmiotów

Znaleźć rozwiązanie optymalne przez przegląd wyczerpujący
Rozwiązać problem przy użyciu heurystyki: do plecaka pakujemy przedmioty według kolejności wynikającej ze stosunku p/w 

Rozwiązania znajdują się w pliku cw1.py.

Pytania:

    1. Czy uzyskano takie same rozwiązania?
    ODP: Nie.
    2. Jakie wnioski można z tego wyciągnąć?
    ODP: Metoda heurystyczna nie zawsze się sprawdza.
    3. Jak dużą instancję problemu (liczba przedmiotów) da się rozwiązać w około minutę metodą zachłanną?
    ODP: Dla 22 przedmiotów algorytm wykonuje się około 42 sekundy na moim komputerze
    4. Jak bardzo wydłuży obliczenia dodanie jeszcze jednego przedmiotu? 
    ODP: Dla 23 przedmiotów algorytm wykonuje się około 87 sekund czyli około  2 razy dłużej
