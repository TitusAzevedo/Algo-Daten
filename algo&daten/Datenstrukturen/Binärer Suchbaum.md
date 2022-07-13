## Binärer Suchbaum
#Datenstruktur 
###### Konzept 
Ein binärer Baum (Knoten kann nicht mehr als zwei Nachfolger haben) wird strukturiert aufgefüllt und ermöglicht das effiziente suchen von Knoten

-> Element im <span style="color: blue">linken</span> Teilbaum < Wurzelelement < Element im <span style="color: blue">rechten</span> Teilbaum

###### Suche
1)	Vergleiche von **z** mit Wurzelelement;<br>wenn gleich dann gefunden -> fertig
2)	Wenn kleiner, suche im linken Teilbaum <br> wenn größer, suche im rechten Teilbaum
3)	Falls **z** nicht gefunden wurde, bis das erste Blatt erreicht wurde, dann ist **z** nicht im Suchbaum enthalten

###### Komplexität
- [[Bäume#^79008f|Vollständiger Baum]]: $\log_{2}(n)$
- [[Bäume#^efd12a|Entarteter Baum]]: $n$

###### Traversierung
-> Das systematische Besuchen jedes Knotens
-> Genutzt zur Ausgabe, Berechnung von Summen etc. und Änderung der Struktur

Arten der Traversierung:
-	Inorder; aufsteigend sortiert ausgegeben
-	Preorder; erzeugt eine Liste, die beim Einlesen denselben Baum erzeugt
-	Postorder; liefert die Postfix-Notation des arithmetischen Ausdrucks, welcher durch einen Binärbaum repräsentiert wird
-	Levelorder; Beginnend bei der Wurzel Ebenen weise ausgegeben 

![[Pasted image 20220713115226.png]]