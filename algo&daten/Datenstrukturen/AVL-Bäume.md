## AVL-Bäume
#Datenstruktur 
Definition:	Ein AVL-Baum ist ein binärer Suchbaum, in dem sich für jeden
Knoten die Höhen seiner zwei Teilbäume höchstens um 1 unterscheiden.

Binäre Suchbäume zeigen im Durchschnitt gutes Verhalten, allerdings kann bei einer **sortierten Eingabe** der sehr **schlechte worst case** eintreten. AVL-Bäume sind eine Datenstruktur, die keine solche entarteten Bäume selbst im worst case zulassen, da sie zu den **balancierten Suchbäumen** gehören.
-> garantiert $O(log(n))$

Die Grundidee besteht darin, eine Strukturinvariante für einen binären
Suchbaum zu formulieren und diese bei Updates (also Einfügen, Löschen)
aufrechtzuerhalten.

Falls durch eine Einfüge- oder Löschoperation diese Strukturinvariante
verletzt wird, so muss sie durch eine **Rebalancieroperation** wiederhergestellt werden.

Beim Rebalancieren wird der eine Teilbaum etwas angehoben, der andere
etwas abgesenkt.

### Rebalancieren
- Ein AVL-Baum hat die Höhendifferenz-Werte von d = −1, 0, 1
- Einfügen und Löschen von Knoten geschieht wie in Suchbäumen
- Durch Einfügen oder Löschen können Knoten mit d = 2 oder d = −2 entstehen
- Durch Rotation kann in diesen Fällen die AVL-Bedingung wieder hergestellt werden
- Beim Update können grundsätzlich insgesamt 4 verschiedene Situationen auftreten, die im Folgenden beschrieben werden

###### 1)	Einfache Rechts-Rotation
Zahl 5 wurde eingefügt, dadurch ergeben sich folgende Balancewerte: 
bal(10) = -2 und bal(7) = -1

![[Pasted image 20220713131433.png]]

###### 2) Einfache Links-Rotation
Zahl 15 wurde eingefügt, dadurch ergeben sich folgende Balancewerte: 
bal(10) = 2 und bal(7) = 1

![[Pasted image 20220713131543.png]]

###### 3) Doppelte Rechts-/ Links-Rotation
Zahl 12 wurde eingefügt, dadurch ergeben sich folgende Balancewerte: 
bal(10) = 2 und bal(15) = -1

![[Pasted image 20220713131643.png]]

###### 4) Doppelte Links-/ Rechts-Rotation
Zahl 7 wurde eingefügt, dadurch ergeben sich folgende Balancewerte:
bal(10) = -2 und bal(5) = 1

![[Pasted image 20220713131730.png]]