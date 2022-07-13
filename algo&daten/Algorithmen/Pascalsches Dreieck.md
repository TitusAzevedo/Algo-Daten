## Pascalsches Dreieck
#Rekursion #Algorithmus 
![[Pasted image 20220713085553.png]]

```python
def triangle(n):
	'''Erzeugt ein pascalsches Dreieck mit n Zeilen'''
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        new_row = [1]
        result = triangle(n-1)
        last_row = result[-1]
        for i in range(len(last_row)-1):
            new_row.append(last_row[i] + last_row[i+1])
        new_row += [1]
        result.append(new_row)
    return result

def pas(x,y):
    tri = triangle(10)
    return tri[x][y]
```