# Graphen
#Datenstruktur 
## Allgemeine Graphen
- Allgemeine Graphen besitzen Knoten mit beliebig vielen Vorgängern und beliebig vielen Nachfolgern
- In allgemeinen Graphen sind Zyklen möglich

**Beispiel (1):**
![[Pasted image 20221010190332.png]]

**Beispiel (2):**
![[Pasted image 20221010190412.png]]

## Graphen Speichern
1. Adjadenzmatrix
![[Pasted image 20221010192029.png]]
**Vorteile:**
- es kann in O(1) festgestellt werden, ob eine Kante von v nach w existiert. 
- bei kantenmarkierten Graphen kann man direkt die Kantenbeschriftung statt der booleschen Werte in die Matrix eintragen.
	- ein geeignetes Element des Wertebereichs (z.B. unendlich) von v muss dann ausdrücken, dass keine Kante vorhanden ist.
**Nachteile:**
- ein geeignetes Element des Wertebereichs (z.B. unendlich) von v muss dann ausdrücken, dass keine Kante vorhanden ist.
- das Auffinden aller k Nachfolger eines Knotens benötigt ungünstige O(n).

2. Adjadenzliste 
![[Pasted image 20221010192219.png]]
**Vorteile:**
- geringer Platzbedarf, nämlich O(n+e) für n = |V|, e = |E|
- man kann alle k Nachfolger eines Knotens in Zeit O(k) erreichen

**Nachteile:**
- das Feststellen, ob Knoten v und w benachbart sind ist nicht mehr in konstanter Zeit möglich
- die Adjazenzliste von v muss hierfür durchlaufen werden.