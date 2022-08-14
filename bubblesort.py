p = [44,55,12,42,94,18,6,67,0,120,-20,120]

def bubblesort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j]> array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

if __name__ =="__main__":
    print(bubblesort(p))
