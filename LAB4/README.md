Czy gracz sterowany przez AI zachowuje się rozsądnie z ludzkiego punktu widzenia? Jeśli nie to co jest nie tak? 
Gracz zazwyczaj zachowuje się rozsądnie. Przykładowo wykorzystuje okazje do bicia przeciwnika. Jednakże często miewa momenty dziwnego zachowania,
w szczególności kiedy był na przegranej pozycji i posiadał damkę. Powtarzał ruchy w przód i w tył. Często również robił to w potyczkach z innym przeciwnikiem sterowanym algorytmem.

Badanie wpływu funkcji stanu:
Funkcje stanu nie zdają się mieć wpływu na działanie algorytmu, gdyż za każdym razem kiedy przeciwnicy o tych samych głębokościach algorytmu stawali na przeciwko siebie dochodziło do remisu niezależnie od funkcji stanu.

Badanie wpływu głębokości przeszukania:


głębokość-białego/głębokość-niebieskiego /  1  /  2  /  3  /  4  /  5  /
                                    1       R     R     R     B     R
                                    2       N     R     R     R     R
                                    3       N     N     R     R     R
                                    4       N     N     R     N     R
                                    5       N     R     R     R     R

Przeciwnik o mniejszej głębokości przeszukiwania zdaje się lepiej sobie radzić z przeciwnikiem o większej głębokości w przypadku kiedy gracz o mniejszym współczynniku głębokości ma kolor niebieski. Ciężko jest wyciągnąć więcej wniosków, bo w wielu przypadkach algorytm powtarzał ruchy w przód i w tył damkami w nieskończoność co często doprowadzało do sytuacji remisowych. 
