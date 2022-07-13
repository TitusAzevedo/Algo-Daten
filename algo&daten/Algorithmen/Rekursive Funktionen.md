## Rekursive Funktionen
### Rekursion
#Rekursion #Algorithmus 
Eine Funktion die sich selbst aufruft. Der Durchlauf wird stapelartig aufgebaut und abgerabeitet.

-> direkt
```python
def alpha():
	#stuff
	alpha()
```

-> indirekt
```python
def cesar():
	#stuff
	beta()

def beta():
	#stuff
	cesar()
```

### Endrekursion
- Verfahren zur optimierung von rekursiven Funktionsaufrufen
- anwendbar wenn letzter Funktionsaufruf innerhalb der rekursiven Funktion, sie selbst ist
- Der zusätzliche Funktionsaufruf wird gestrichen und die aktuelle Instanz der Funktion samt Stack Wiederzuverwenden
- Spart den Aufbau eines neuen Stacks, den Funktionsaufruf und Abbau des Stacks
- Vorteil: kein Stack-Overflow
- Nachteil: schwer zu debuggen; kein klarer Stack mehr

-> nicht endrekursiv
```python
def sum(x):
	if x == 0:
		return 0
	else:
		return x + sum(x - 1)
```

-> endrekursiv
```python
def gauss(y):
	return sum(0, y)

def sum(x, y):
	if y == 0:
		return x
	else:
		return sum(x + y, y - 1)
```


### Backtracking
-	geht nach dem Versuch- und Irrrtumprinzip vor (trial and error)
-	es wird versucht, eine erreichte Teillösung zu einer Gesamtlösung
sukzessive auszubauen.
-	Führt ein Lösungspfad nicht zum Ziel, werden die Teillösungsschritte
zurückgenommen und ein anderer Lösungsweg gewählt.
- Nicht sehr effizient (exponentielle Laufzeit)
- Typische Problemstellungen sind:
	- Suche eines Weges im Labyrinth
	- 8-Damenproblem
	- Rucksackproblem