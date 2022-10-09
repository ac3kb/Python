#insertion sort

data = [31, 41, 59, 26, 41, 58, 27, 35, 70, 40]

#decreasing order
def insertionSort(array):
  for j in range(1, len(array)):
    current = array[j]
    i = j - 1
    while i >= 0 and array[i] > current:
      array[i + 1] = array[i]
      i = i - 1
    array[i + 1] = current
  print(array)
