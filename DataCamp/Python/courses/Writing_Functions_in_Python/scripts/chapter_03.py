# exercise 01

"""
Building a command line data app

You are building a command line tool that lets a user interactively explore a dataset. We've defined four functions: mean(), std(), minimum(), and maximum() that users can call to analyze their data. Help finish this section of the code so that your users can call any of these functions by typing the function name at the input prompt.

Note: The function get_user_input() in this exercise is a mock version of asking the user to enter a command. It randomly returns one of the four function names. In real life, you would ask for input and wait until the user entered a value.
"""

# steps

"""

    Add the functions std(), minimum(), and maximum() to the function_map dictionary, like we did with mean().
    The name of the function the user wants to call is stored in func_name. Use the dictionary of functions, function_map, to call the chosen function and pass data as an argument.

"""

# solution

# Add the missing function references to the function map
function_map = {
  'mean': mean,
  'std': std,
  'minimum': minimum,
  'maximum': maximum
}

data = load_data()
print(data)

func_name = get_user_input()

# Call the chosen function and pass "data" as an argument
function_map[func_name](data)

#----------------------------------#

# Conclusion

"""
Phenomenal function referencing! By adding the functions to a dictionary, you can select the function based on the user's input. You could have also used a series of if/else statements, but putting them in a dictionary like this is much easier to read and maintain.
"""

# exercise 02

"""
Reviewing your co-worker's code

Your co-worker is asking you to review some code that they've written and give them some tips on how to get it ready for production. You know that having a docstring is considered best practice for maintainable, reusable functions, so as a sanity check you decide to run this has_docstring() function on all of their functions.

def has_docstring(func):
  """#Check to see if the function 
  #`func` has a docstring.

  #Args:
    #func (callable): A function.

  #Returns:
    #bool
  """
  return func.__doc__ is not None

"""

# steps

"""
Call has_docstring() on your co-worker's load_and_plot_data() function.

    Check if the function as_2D() has a docstring.

    Check if the function log_product() has a docstring.

"""

# solution

# Call has_docstring() on the load_and_plot_data() function
ok = has_docstring(load_and_plot_data)

if not ok:
  print("load_and_plot_data() doesn't have a docstring!")
else:
  print("load_and_plot_data() looks ok")

#----------------------------------#

# Call has_docstring() on the as_2D() function
ok = has_docstring(as_2D)

if not ok:
  print("as_2D() doesn't have a docstring!")
else:
  print("as_2D() looks ok")

#----------------------------------#

# Call has_docstring() on the log_product() function
ok = has_docstring(log_product)

if not ok:
  print("log_product() doesn't have a docstring!")
else:
  print("log_product() looks ok")

#----------------------------------#

# Conclusion

"""
Awesome job writing functions as arguments! You have discovered that your co-worker forgot to write a docstring for log_product(). You have learned enough about best practices to tell them how to fix it.

To pass a function as an argument to another function, you had to determine which one you were calling and which one you were referencing. Keeping those straight will be important as we dig deeper into this chapter. From the function names can you think of any other advice you might give your co-worker about their functions?
"""

# exercise 03

"""
Returning functions for a math game

You are building an educational math game where the player enters a math term, and your program returns a function that matches that term. For instance, if the user types "add", your program returns a function that adds two numbers. So far you've only implemented the "add" function. Now you want to include a "subtract" function.
"""

# steps

"""
Define the subtract() function. It should take two arguments and return the first argument minus the second argument.
"""

# solution

def create_math_function(func_name):
  if func_name == 'add':
    def add(a, b):
      return a + b
    return add
  elif func_name == 'subtract':
    # Define the subtract() function
    def  subtract(a, b):
      return a - b
    return subtract
  else:
    print("I don't know that one")
    
add = create_math_function('add')
print('5 + 2 = {}'.format(add(5, 2)))

subtract = create_math_function('subtract')
print('5 - 2 = {}'.format(subtract(5, 2)))

#----------------------------------#

# Conclusion

"""
Nice nested function! Now that you've implemented the subtract() function, you can keep going to include multiply() and divide(). I predict this game is going to be even bigger than Fortnite!

Notice how we assign the return value from create_math_function() to the add and subtract variables in the script. Since create_math_function() returns a function, we can then call _those variables_ as functions.
"""

# exercise 04

"""
Understanding scope

What four values does this script print?

x = 50

def one():
  x = 10

def two():
  global x
  x = 30

def three():
  x = 100
  print(x)

for func in [one, two, three]:
  func()
  print(x)

"""

# steps

"""
50, 30, 100, 50

10, 30, 30, 30

50, 30, 100, 30 (Answer)

10, 30, 100, 50

50, 50, 50, 50
"""

# solution



#----------------------------------#

# Conclusion

"""
Good job! one() doesn't change the global x, so the first print() statement prints 50.

two() does change the global x so the second print() statement prints 30.

The print() statement inside the function three() is referencing the x value that is local to three(), so it prints 100.

But three() does not change the global x value so the last print() statement prints 30 again.
"""

# exercise 05

"""
Modifying variables outside local scope

Sometimes your functions will need to modify a variable that is outside of the local scope of that function. While it's generally not best practice to do so, it's still good to know how in case you need to do it. Update these functions so they can modify variables that would usually be outside of their scope.
"""

# steps

"""
Add a keyword that lets us update call_count from inside the function.

Add a keyword that lets us modify file_contents from inside save_contents().

Add a keyword to done in check_is_done() so that wait_until_done() eventually stops looping.
"""

# solution

call_count = 0

def my_function():
  # Use a keyword that lets us update call_count 
  global call_count
  call_count += 1
  
  print("You've called my_function() {} times!".format(
    call_count
  ))
  
for _ in range(20):
  my_function()

#----------------------------------#

def read_files():
  file_contents = None
  
  def save_contents(filename):
    # Add a keyword that lets us modify file_contents
    nonlocal file_contents
    if file_contents is None:
      file_contents = []
    with open(filename) as fin:
      file_contents.append(fin.read())
      
  for filename in ['1984.txt', 'MobyDick.txt', 'CatsEye.txt']:
    save_contents(filename)
    
  return file_contents

print('\n'.join(read_files()))

#----------------------------------#

def wait_until_done():
  def check_is_done():
    # Add a keyword so that wait_until_done() 
    # doesn't run forever
    global done
    if random.random() < 0.1:
      done = True
      
  while not done:
    check_is_done()

done = False
wait_until_done()

print('Work done? {}'.format(done))

#----------------------------------#

# Conclusion

"""
Stellar scoping! By adding global done in check_is_done(), you ensure that the done being referenced is the one that was set to False before wait_until_done() was called. Without this keyword, wait_until_done() would loop forever because the done = True in check_is_done() would only be changing a variable that is local to check_is_done(). Understanding what scope your variables are in will help you debug tricky situations like this one.
"""

# exercise 06

"""
Checking for closure

You're teaching your niece how to program in Python, and she is working on returning nested functions. She thinks she has written the code correctly, but she is worried that the returned function won't have the necessary information when called. Show her that all of the nonlocal variables she needs are in the new function's closure.
"""

# steps

"""
Use an attribute of the my_func() function to show that it has a closure that is not None.
---
Show that there are two variables in the closure.
---
Get the values of the variables in the closure so you can show that they are equal to [2, 17], the arguments passed to return_a_func().
"""

# solution

def return_a_func(arg1, arg2):
  def new_func():
    print('arg1 was {}'.format(arg1))
    print('arg2 was {}'.format(arg2))
  return new_func
    
my_func = return_a_func(2, 17)

# Show that my_func()'s closure is not None
print(my_func.__closure__ is not None)

#----------------------------------#

def return_a_func(arg1, arg2):
  def new_func():
    print('arg1 was {}'.format(arg1))
    print('arg2 was {}'.format(arg2))
  return new_func
    
my_func = return_a_func(2, 17)

print(my_func.__closure__ is not None)

# Show that there are two variables in the closure
print(len(my_func.__closure__) == 2)

#----------------------------------#

def return_a_func(arg1, arg2):
  def new_func():
    print('arg1 was {}'.format(arg1))
    print('arg2 was {}'.format(arg2))
  return new_func
    
my_func = return_a_func(2, 17)

print(my_func.__closure__ is not None)
print(len(my_func.__closure__) == 2)

# Get the values of the variables in the closure
closure_values = [
  my_func.__closure__[i].cell_contents for i in range(2)
]
print(closure_values == [2, 17])

#----------------------------------#

# Conclusion

"""
Case closed! Your niece is relieved to see that the values she passed to return_a_func() are still accessible to the new function she returned, even after the program has left the scope of return_a_func().

Values get added to a function's closure in the order they are defined in the enclosing function (in this case, arg1 and then arg2), but only if they are used in the nested function. That is, if return_a_func() took a third argument (e.g., arg3) that wasn't used by new_func(), then it would not be captured in new_func()'s closure.
"""

# exercise 07

"""
Closures keep your values safe

You are still helping your niece understand closures. You have written the function get_new_func() that returns a nested function. The nested function call_func() calls whatever function was passed to get_new_func(). You've also written my_special_function() which simply prints a message that states that you are executing my_special_function().

You want to show your niece that no matter what you do to my_special_function() after passing it to get_new_func(), the new function still mimics the behavior of the original my_special_function() because it is in the new function's closure.
"""

# steps

"""
Show that you still get the original message even if you redefine my_special_function() to only print "hello".

Show that even if you delete my_special_function(), you can still call new_func() without any problems.

Show that you still get the original message even if you overwrite my_special_function() with the new function.
"""

# solution

def my_special_function():
  print('You are running my_special_function()')
  
def get_new_func(func):
  def call_func():
    func()
  return call_func

new_func = get_new_func(my_special_function)

# Redefine my_special_function() to just print "hello"
def my_special_function():
  print('hello')

new_func()

#----------------------------------#

def my_special_function():
  print('You are running my_special_function()')
  
def get_new_func(func):
  def call_func():
    func()
  return call_func

new_func = get_new_func(my_special_function)

# Delete my_special_function()
del(my_special_function)

new_func()

#----------------------------------#

def my_special_function():
  print('You are running my_special_function()')
  
def get_new_func(func):
  def call_func():
    func()
  return call_func

# Overwrite `my_special_function` with the new function
my_special_function = get_new_func(my_special_function)

my_special_function()

#----------------------------------#

# Conclusion

"""
Well done! Your niece feels like she understands closures now. She has seen that you can modify, delete, or overwrite the values needed by the nested function, but the nested function can still access those values because they are stored safely in the function's closure. She even realized that you could run into memory issues if you wound up adding a very large array or object to the closure, and has resolved to keep her eye out for that sort of problem.
"""

# exercise 08

"""
Using decorator syntax

You have written a decorator called print_args that prints out all of the arguments and their values any time a function that it is decorating gets called.
"""

# steps

"""
Decorate my_function() with the print_args() decorator by redefining the my_function variable.
---
Decorate my_function() with the print_args() decorator using decorator syntax.
"""

# solution

def my_function(a, b, c):
  print(a + b + c)

# Decorate my_function() with the print_args() decorator
my_function = print_args(my_function)

my_function(1, 2, 3)

#----------------------------------#

# Decorate my_function() with the print_args() decorator
@print_args
def my_function(a, b, c):
  print(a + b + c)

my_function(1, 2, 3)

#----------------------------------#

# Conclusion

"""
What a delightful decorator! Note that @print_args before the definition of my_function is exactly equivalent to my_function = print_args(my_function). Remember, even though decorators are functions themselves, when you use decorator syntax with the @ symbol you do not include the parentheses after the decorator name.
"""

# exercise 09

"""
Defining a decorator

Your buddy has been working on a decorator that prints a "before" message before the decorated function is called and prints an "after" message after the decorated function is called. They are having trouble remembering how wrapping the decorated function is supposed to work. Help them out by finishing their print_before_and_after() decorator.
"""

# steps

"""
    Call the function being decorated and pass it the positional arguments *args.
    Return the new decorated function.
"""

# solution

def print_before_and_after(func):
  def wrapper(*args):
    print('Before {}'.format(func.__name__))
    # Call the function being decorated with *args
    func(*args)
    print('After {}'.format(func.__name__))
  # Return the nested function
  return wrapper

@print_before_and_after
def multiply(a, b):
  print(a * b)

multiply(5, 10)

#----------------------------------#

# Conclusion

"""

"""

# exercise 10

"""

"""

# steps

"""

"""

# solution



#----------------------------------#

# Conclusion

"""

"""

# exercise 11

"""

"""

# steps

"""

"""

# solution



#----------------------------------#

# Conclusion

"""

"""