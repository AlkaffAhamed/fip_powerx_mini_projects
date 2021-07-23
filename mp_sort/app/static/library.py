from org.transcrypt.stubs.browser import *
import random

array = []

def gen_random_int(number, seed):
  pass

def generate():
  global array

  number = 10
  seed = 200

  # call gen_random_int() with the given number and seed
  # store it to the global variable array
  pass

  array = None
  # convert the items into one single string
  # the number should be separated by a comma
  # and a full stop should end the string.
  pass

  array_str = None

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
  pass

  array_str = None

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
  sort_arr(numbers)

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

def sort_arr(arr):
  # Sort by Insertion Sort
  n = len(arr)
  for outer_index in range(1, n):
    inner_index = outer_index
    temp = arr[inner_index]
    while (inner_index > 0 and temp < arr[inner_index - 1]):
      # Number at inner index is smaller than previous number on the left
      # Move previous number to inner index
      arr[inner_index] = arr[inner_index - 1]
      # Update inner index
      inner_index -= 1
    # Inner index now at lowest value satisfying loop condition
    # Swap positions
    arr[inner_index] = temp



