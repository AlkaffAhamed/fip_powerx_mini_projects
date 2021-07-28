from org.transcrypt.stubs.browser import *
import random

array = []


def gen_random_int(number, seed):
    result = list(range(number))
    random.shuffle(result, random.seed(seed))
    return result

def generate():
  global array

  number = 10
  seed = 200

  # call gen_random_int() with the given number and seed
  # store it to the global variable array

  array = gen_random_int(number, seed)
  # convert the items into one single string
  # the number should be separated by a comma
  # and a full stop should end the string.

  array_str = ','.join(array) + '.'

  # This line is to placed the string into the HTML
  # under div section with the id called "generate"
  document.getElementById("generate").innerHTML = array_str


def sortnumber1():
  '''	This function is used in Exercise 1.
    The function is called when the sort button is clicked.

    You need to do the following:
      get the list of numbers from the global variable array and
      copy it to a new list
      call your sort function, either bubble sort or insertion sort
      create a string of the sorted numbers and store it in array_str
  '''
  
  global array

  if random.random() < 0.5:
    print("Insertion Sorting...")
    insertion_sort(array)
  else:
    print("Bubble Sorting...")
    bubble_sort(array)
  array_str = ', '.join(array)

  document.getElementById("sorted").innerHTML = array_str

def sortnumber2():
  '''	This function is used in Exercise 2.
    The function is called when the sort button is clicked.

    You need to do the following:
      Get the numbers from a string variable "value".
      Split the string using comma as the separator and convert them to
      a list of numbers
      call your sort function, either bubble sort or insertion sort
      create a string of the sorted numbers and store it in array_str
  '''
  # The following line get the value of the text input called "numbers"
  value = document.getElementsByName("numbers")[0].value

  # Throw alert and stop if nothing in the text input
  if value == "":
    window.alert("Your textbox is empty")
    return

  # Your code should start from here
  # store the final string to the variable array_str
  num_str_arr = value.split(',')
  # Typecast all elements
  numbers = list(map(str_to_num, num_str_arr))

  if random.random() < 0.5:
    print("Insertion Sorting...")
    insertion_sort(numbers)
  else:
    print("Bubble Sorting...")
    bubble_sort(numbers)

  array_str = ', '.join(str(num) for num in numbers)

  document.getElementById("sorted").innerHTML = array_str

def str_to_num(string):
  # Also removes any leading and trailing whitespaces
  if int(string) == float(string):
    return int(string)
  elif float(string):
    return float(string)
  else:
    window.alert("Non number provided")
    return

# Insertion Sort
def insertion_sort(array):
    n = len(array)

    # Outer Loop
    for i in range(1, n):
        # Set Inner Loop strating index = Outer Loop
        j = i
        # Start the Inner Loop
        # Loop must break if decrement j all the way till 0 & if previous element > element j
        while j > 0 and float(array[j]) < float(array[j - 1]):
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1

# Bubble Sort
def bubble_sort(array):
    # count = 0
    n = len(array)
    isSwap = True

    # While loop replaces the outer for loop
    while isSwap:
        isSwap = False
        lastIndex = 0
        # Maintaining j as Inner loop iterator
        for j in range(n - 1):
            # Swap if next element < current element
            #count += 1
            if array[j + 1] < array[j]:
                array[j + 1], array[j] = array[j], array[j + 1]
                isSwap = True  # Swapping happened, so unset flag
                lastIndex = j + 1  # Extract last index + 1 (j + 1) because array is sorted till j+1, not j
        n = lastIndex  # And set as new n for inner loop
