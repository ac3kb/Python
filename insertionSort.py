#insertion sort

data = [31, 41, 59, 26, 41, 58, 27, 35, 70, 40]

#decreasing order
def insertionSort(array): 
  for j in range(1, len(array)):             #j is the current val and starts at the second index
    current = array[j]                       #current holds the value at the second index / j
    i = j - 1                                # i is the index previous to j / current value
    while i >= 0 and array[i] > current:     #loop only runs when i is not < 0 and the value of i / previous value is larger than the current value
      array[i + 1] = array[i]                #set the value at the index of current to value of the previous index
      i = i - 1                         #move the index of i one index down from its already prev position. this will stop the loop since array[i - 1] will be !> current
    array[i + 1] = current                   #set the value of the index previous to our current value equal to the current value 
  print(array)
