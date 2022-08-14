## Bubble Sort 

Sortieren durch direktes Austauschen. Paare werden verglichen und ggf. ausgetauscht. Das größte Element steigt wie eine Luftblase nach oben.
	→ Komplexität $O(n^2)$

#### Aufbau
1) äußere Schleife mit der Länge der Liste
2) innere Schleife in der die Elemente verglichen & ausgetauscht werden
	1) Element $i$ mit $i+1$ vergleichen und ggf. tauschen
	2) nach dem Durchlauf den nächsten um $1$ kürzen 

#### Implementation 

```Python
def bubblesort(array):
	for i in range(len(array)):
		for j in range(len(array)-i-1):
			if array[j]> array[j+1]:
				array[j], array[j+1] = array[j+1], array[j]

return array
```