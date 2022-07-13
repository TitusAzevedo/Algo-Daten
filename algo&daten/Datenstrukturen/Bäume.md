## Bäume
#Datenstruktur 
###### Eigenschaften 
- Jedes Element (<span style="color: red">Knoten</span>) hat eine endliche, begrenzte Anzahl von Nachfolgern (<span style="color: red">Kindern</span>), des Elements
- Es gibt ein ausgezeichnetes Element (<span style="color: red">Wurzel </span>), das keinen Vorgänger hat
- Elemente ohne Nachfolger heissen <span style="color: red">Blätter</span>, Elemente mit Vorgänger und Nachfolger(n) <span style="color: red">innere Knoten</span>

###### Ausprägungen
1)	Vollständiger Binärbaum ^79008f
```mermaid
graph TB;
    A((1))-->B((2))
    A-->C((3));
    B-->E((4))
    B-->F((5))
    C-->H((6))
    C-->I((7))
```

2) Entarteter Baum ^efd12a
```mermaid
graph TB;
    A((1))-->B((2))
    A-->C((3));
	C-->D((4));
	D-->E((5));
```	



###### Baumarten
-	[[Binärer Suchbaum]]
-	[[AVL-Bäume]]