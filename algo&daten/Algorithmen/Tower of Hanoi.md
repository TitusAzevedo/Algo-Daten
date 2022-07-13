## Tower of Hanoi
#Rekursion #Algorithmus 
![[Pasted image 20220713083318.png]]

Lösung mittels rekursiver funktion in drei Schritten:
1)	Der um 1 kleinere Turm wird uaf das Zwischenziel verschoben; funktion ruft sich selbst auf -> Ziel und zwischenziel tauschen dabei ihre Rollen
2)	Verbliebene einzelne Scheibe zum Ziel verschieben
3)	Der zuvor auf das Zwischenziel verschobene um 1 kleinere
Turm wird auf das Ziel verschoben; Funktion ruft sich selbst auf 

```python
def TowerOfHanoi(n , source, destination, auxiliary):
    if n==1:
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)
         
# Driver code
n = 4
TowerOfHanoi(n,'A','B','C')

```