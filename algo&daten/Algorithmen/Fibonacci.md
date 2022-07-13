## Fibonacci Zahlen
#Algorithmus 

Algorithmus der die Fibonacci Zahlen bis n berechnet

```python
def fibonacci(n):
	if (n == 0 or n == 1):
		return n
	else:
		vorvor = 0
		vor = 1
		fib = 0
		
		for x in range(2,n):
			fib = vorvor + vor
			vorvor = vor
			vor = fib
		return fib

```