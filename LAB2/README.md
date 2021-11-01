Zadania: 
- Zaimplementować metodę najszybszego wzrostu. Gradient wyliczamy numerycznie.
- Narysować zachowanie algorytmu (kolejne kroki algorytmu jako strzałki na tle poziomic funkcji celu). Uwaga: w praktycznych zadaniach optymalizacji nie da się narysować funkcji celu ponieważ zadania mają wiele wymiarów (np. 100), oraz koszt wyznaczenia oceny jednego punktu jest duży.
- Zastosować metodę do znalezienia optimum funkcji booth, po czym do znalezienia optimum funkcji o numerach od 1 do 3 z CEC 2017.

Pytania:
1. Jak wartość parametru beta wpływa na szybkość dojścia do optimum i zachowanie algorytmu?
ODP.: Parametr beta przy zwiększeniu, zmniejsza dokładność oraz zwiększa szybkość wykonywania się algorytmu, a jego zmniejszenie
        zwiększa dokładność i czas działania. Źle dobrany (np.: zbyt duży) parametr beta może sprawić również, że algorytm nie dotrze do optimum.

2. Zalety/wady algorytmu? 
ODP.: Plusy:
        - algorytm jest prosty w implementacji
        - algorytm może działać nawet dla wielowymiarowych funkcji
      Minusy:
        - konieczność dobierania parametru beta
        - szansa na nie dotarcie do optimum przy nieodpowiednie becie

3. Wnioski
ODP.: Algorytm największego spadku jest jest dość prosty w użytku, ale przez to często może nie być najlepszym wyjściem w danej sytuacji
        na przykład przy nietypowych funkcjach lub przy takich o których nie mamy dużo informacji, bo moglibyśmy mieć problem chociażby z dobraniem współczynnika beta.