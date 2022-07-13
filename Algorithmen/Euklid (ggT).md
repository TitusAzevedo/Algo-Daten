## Euclid 
#Algorithmus

Bestimmt den größten gemeinsamen teiler zweier variabeln 

Pseudocode:
```
solange x ≠ y ist, wiederhole:
	wenn x > y, dann:
		ziehe y von x ab und weise das Ergebnis x zu.
	andernfalls: ziehe x von y ab und weise das Ergebnis y zu. 
ENDE solange
x (bzw. y) ist der gesuchte ggT
```

Python:
```python
while x != y:
	if x > y:
		x = x - y
	else:
		y = y - x
```