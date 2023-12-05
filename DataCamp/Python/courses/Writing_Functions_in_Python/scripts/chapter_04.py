# exercise 01

"""
Print the return type

You are debugging a package that you've been working on with your friends. Something weird is happening with the data being returned from one of your functions, but you're not even sure which function is causing the trouble. You know that sometimes bugs can sneak into your code when you are expecting a function to return one thing, and it returns something different. For instance, if you expect a function to return a numpy array, but it returns a list, you can get unexpected behavior. To ensure this is not what is causing the trouble, you decide to write a decorator, print_return_type(), that will print out the type of the variable that gets returned from every call of any function it is decorating.
"""

# steps

"""
    Create a nested function, wrapper(), that will become the new decorated function.
   
    Call the function being decorated.
   
    Return the new decorated function.
"""

# solution

def print_return_type(func):
  # Define wrapper(), the decorated function
  def wrapper(*args, **kwargs):
    # Call the function being decorated
    result = func(*args, **kwargs)
    print('{}() returned type {}'.format(
      func.__name__, type(result)
    ))
    return result
  # Return the decorated function
  return wrapper
  
@print_return_type
def foo(value):
  return value
  
print(foo(42))
print(foo([1, 2, 3]))
print(foo({'a': 42}))

#----------------------------------#

# Conclusion

"""
Righteous return types! Your new decorator helps you examine the results of your functions at runtime. Now you can apply this decorator to every function in the package you are developing and run your scripts. Being able to examine the types of your return values will help you understand what is happening and will hopefully help you find the bug.
"""

# exercise 02

"""
Counter

You're working on a new web app, and you are curious about how many times each of the functions in it gets called. So you decide to write a decorator that adds a counter to each function that you decorate. You could use this information in the future to determine whether there are sections of code that you could remove because they are no longer being used by the app.
"""

# steps

"""
    Call the function being decorated and return the result.
   
    Return the new decorated function.
   
    Decorate foo() with the counter() decorator.
"""

# solution

def counter(func):
  def wrapper(*args, **kwargs):
    wrapper.count += 1
    # Call the function being decorated and return the result
    return func
  wrapper.count = 0
  # Return the new decorated function
  return wrapper

# Decorate foo() with the counter() decorator
@counter
def foo():
  print('calling foo()')
  
foo()
foo()

print('foo() was called {} times.'.format(foo.count))

#----------------------------------#

# Conclusion

"""
Cool counting! Now you can go decorate a bunch of functions with the counter() decorator, let your program run for a while, and then print out how many times each function was called.

It seems a little magical that you can reference the wrapper() function from _inside_ the definition of wrapper() as we do here on line 3. That's just one of the many neat things about functions in Python -- any function, not just decorators.
"""

# exercise 03

"""
Preserving docstrings when decorating functions

Your friend has come to you with a problem. They've written some nifty decorators and added them to the functions in the open-source library they've been working on. However, they were running some tests and discovered that all of the docstrings have mysteriously disappeared from their decorated functions. Show your friend how to preserve docstrings and other metadata when writing decorators.
"""

# steps

"""
Decorate print_sum() with the add_hello() decorator to replicate the issue that your friend saw - that the docstring disappears.
---

    To show your friend that they are printing the wrapper() function's docstring, not the print_sum() docstring, add the following docstring to wrapper():

Print 'hello' and then call the decorated function.

---
def add_hello(func):
  # Add a docstring to wrapper
  def wrapper(*args, **kwargs):
   ' Print 'hello' and then call the decorated function'
    print('Hello')
    return func(*args, **kwargs)
  return wrapper

@add_hello
def print_sum(a, b):
  'Adds two numbers and prints the sum'
  print(a + b)
  
print_sum(10, 20)
print_sum_docstring = print_sum.__doc__
print(print_sum_docstring)
---
Finally, decorate wrapper() so that the metadata from func() is preserved in the new decorated function.
"""

# solution

def add_hello(func):
  def wrapper(*args, **kwargs):
    print('Hello')
    return func(*args, **kwargs)
  return wrapper

# Decorate print_sum() with the add_hello() decorator
@add_hello
def print_sum(a, b):
  """Adds two numbers and prints the sum"""
  print(a + b)
  
print_sum(10, 20)
print_sum_docstring = print_sum.__doc__
print(print_sum_docstring)

#----------------------------------#

# Import the function you need to fix the problem
from functools import wraps

def add_hello(func):
  def wrapper(*args, **kwargs):
    """Print 'hello' and then call the decorated function."""
    print('Hello')
    return func(*args, **kwargs)
  return wrapper
  
@add_hello
def print_sum(a, b):
  """Adds two numbers and prints the sum"""
  print(a + b)
  
print_sum(10, 20)
print_sum_docstring = print_sum.__doc__
print(print_sum_docstring)

#----------------------------------#

from functools import wraps

def add_hello(func):
  # Decorate wrapper() so that it keeps func()'s metadata
  @wraps(func)
  def wrapper(*args, **kwargs):
    """Print 'hello' and then call the decorated function."""
    print('Hello')
    return func(*args, **kwargs)
  return wrapper
  
@add_hello
def print_sum(a, b):
  """Adds two numbers and prints the sum"""
  print(a + b)
  
print_sum(10, 20)
print_sum_docstring = print_sum.__doc__
print(print_sum_docstring)

#----------------------------------#

# Conclusion

"""
That's a wrap! Your friend was concerned that they couldn't print the docstrings of their functions. They now realize that the strange behavior they were seeing was caused by the fact that they were accidentally printing the wrapper() docstring instead of the docstring of the original function. After adding @wraps(func) to all of their decorators, they see that the docstrings are back where they expect them to be.
"""

# exercise 04

"""
Measuring decorator overhead

Your boss wrote a decorator called check_everything() that they think is amazing, and they are insisting you use it on your function. However, you've noticed that when you use it to decorate your functions, it makes them run much slower. You need to convince your boss that the decorator is adding too much processing time to your function. To do this, you are going to measure how long the decorated function takes to run and compare it to how long the undecorated function would have taken to run. This is the decorator in question:

def check_everything(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    check_inputs(*args, **kwargs)
    result = func(*args, **kwargs)
    check_outputs(result)
    return result
  return wrapper

"""

# steps

"""
Call the original function instead of the decorated version by using an attribute of the function that the wraps() statement in your boss's decorator added to the decorated function.
"""

# solution

@check_everything
def duplicate(my_list):
  """Return a new list that repeats the input twice"""
  return my_list + my_list

t_start = time.time()
duplicated_list = duplicate(list(range(50)))
t_end = time.time()
decorated_time = t_end - t_start

t_start = time.time()
# Call the original function instead of the decorated one
duplicated_list = duplicate.__wrapped__(list(range(50)))
t_end = time.time()
undecorated_time = t_end - t_start

print('Decorated time: {:.5f}s'.format(decorated_time))
print('Undecorated time: {:.5f}s'.format(undecorated_time))

#----------------------------------#

# Conclusion

"""
Wow! Your function ran approximately 10,000 times faster without your boss's decorator. At least they were smart enough to add @wraps(func) to the nested wrapper() function so that you were able to access the original function. You should show them the results of this test. Be sure to ask for a raise while you're at it!
"""

# exercise 05

"""
Run_n_times()

In the video exercise, I showed you an example of a decorator that takes an argument: run_n_times(). The code for that decorator is repeated below to remind you how it works. Practice different ways of applying the decorator to the function print_sum(). Then I'll show you a funny prank you can play on your co-workers.

def run_n_times(n):
  'Define and return a decorator'
  def decorator(func):
    def wrapper(*args, **kwargs):
      for i in range(n):
        func(*args, **kwargs)
    return wrapper
  return decorator

"""

# steps

"""
Add the run_n_times() decorator to print_sum() using decorator syntax so that print_sum() runs 10 times.

Use run_n_times() to create a decorator run_five_times() that will run any function five times.

Here's the prank: use run_n_times() to modify the built-in print() function so that it always prints 20 times!
"""

# solution

# Make print_sum() run 10 times with the run_n_times() decorator
@run_n_times(10)
def print_sum(a, b):
  print(a + b)
  
print_sum(15, 20)

#----------------------------------#

# Use run_n_times() to create the run_five_times() decorator
run_five_times = run_n_times(5)

@run_five_times
def print_sum(a, b):
  print(a + b)
  
print_sum(4, 100)

#----------------------------------#

# Modify the print() function to always run 20 times
print = run_n_times(20)(print)

print('What is happening?!?!')

#----------------------------------#

# Conclusion

"""
Good job!
Good job!
Good job!

You've become an expert at using decorators. Notice how when you use decorator syntax for a decorator that takes arguments, you need to call the decorator by adding parentheses, but you don't add parenthesis for decorators that don't take arguments.

_Warning: overwriting commonly used functions is probably not a great idea, so think twice before using these powers for evil._
"""

# exercise 06

"""
HTML Generator

You are writing a script that generates HTML for a webpage on the fly. So far, you have written two decorators that will add bold or italics tags to any function that returns a string. You notice, however, that these two decorators look very similar. Instead of writing a bunch of other similar looking decorators, you want to create one decorator, html(), that can take any pair of opening and closing tags.

def bold(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    msg = func(*args, **kwargs)
    return '<b>{}</b>'.format(msg)
  return wrapper

def italics(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    msg = func(*args, **kwargs)
    return '<i>{}</i>'.format(msg)
  return wrapper

"""

# steps

"""
Return the decorator and the decorated function from the correct places in the new html() decorator.

Use the html() decorator to wrap the return value of hello() in the strings <b> and </b> (the HTML tags that mean "bold").

Use html() to wrap the return value of goodbye() in the strings <i> and </i> (the HTML tags that mean "italics").

Use html() to wrap hello_goodbye() in a DIV, which is done by adding the strings <div> and </div> tags around a string.
"""

# solution

def html(open_tag, close_tag):
  def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
      msg = func(*args, **kwargs)
      return '{}{}{}'.format(open_tag, msg, close_tag)
    # Return the decorated function
    return wrapper
  # Return the decorator
  return decorator

#----------------------------------#

# Make hello() return bolded text
@html('<b>', '</b>')
def hello(name):
  return 'Hello {}!'.format(name)
  
print(hello('Alice'))

#----------------------------------#

# Make goodbye() return italicized text
@html('<i>', '</i>')
def goodbye(name):
  return 'Goodbye {}.'.format(name)
  
print(goodbye('Alice'))

#----------------------------------#

# Wrap the result of hello_goodbye() in <div> and </div>
@html('<div>', '</div>')
def hello_goodbye(name):
  return '\n{}\n{}\n'.format(hello(name), goodbye(name))
  
print(hello_goodbye('Alice'))

#----------------------------------#

# Conclusion

"""
That's some HTML hotness! With the new html() decorator you can focus on writing simple functions that return the information you want to display on the webpage and let the decorator take care of wrapping them in the appropriate HTML tags.
"""

# exercise 07

"""
Tag your functions

Tagging something means that you have given that thing one or more strings that act as labels. For instance, we often tag emails or photos so that we can search for them later. You've decided to write a decorator that will let you tag your functions with an arbitrary list of tags. You could use these tags for many things:

    Adding information about who has worked on the function, so a user can look up who to ask if they run into trouble using it.
    Labeling functions as "experimental" so that users know that the inputs and outputs might change in the future.
    Marking any functions that you plan to remove in a future version of the code.
    Etc.

"""

# steps

"""
Define a new decorator, named decorator(), to return.

Ensure the decorated function keeps its metadata.

Call the function being decorated and return the result.

Return the new decorator.
"""

# solution

def tag(*tags):
  # Define a new decorator, named "decorator", to return
  def decorator(func):
    # Ensure the decorated function keeps its metadata
    @wraps(func)
    def wrapper(*args, **kwargs):
      # Call the function being decorated and return the result
      return func(*args, **kwargs)
    wrapper.tags = tags
    return wrapper
  # Return the new decorator
  return decorator

@tag('test', 'this is a tag')
def foo():
  pass

print(foo.tags)

#----------------------------------#

# Conclusion

"""
Terrific tagging! With this new decorator, you can do some really interesting things. For instance, you could tag a bunch of image transforming functions, and then write code that searches for all of the functions that transform images and apply them, one after the other, on a given input image. What other neat uses can you come up with for this decorator?
"""

# exercise 08

"""
Check the return type

Python's flexibility around data types is usually cited as one of the benefits of the language. It can sometimes cause problems though if incorrect data types go unnoticed. You've decided that in order to ensure your code is doing exactly what you want it to do, you will explicitly check the return types in all of your functions and make sure they're returning what you expect. To do that, you are going to create a decorator that checks if the return type of the decorated function is correct.

Note: assert is a keyword that you can use to test whether something is true. If you type assert condition and condition is True, this function doesn't do anything. If condition is False, this function raises an error. The type of error that it raises is called an AssertionError.
"""

# steps

"""
Start by completing the returns_dict() decorator so that it raises an AssertionError if the return type of the decorated function is not a dictionary.
---
Now complete the returns() decorator, which takes the expected return type as an argument.
"""

# solution

def returns_dict(func):
  # Complete the returns_dict() decorator
  def wrapper(*args, **kwargs):
    result = func(*args, **kwargs)
    assert type(result) == dict
    return result
  return wrapper
  
@returns_dict
def foo(value):
  return value

try:
  print(foo([1,2,3]))
except AssertionError:
  print('foo() did not return a dict!')
  

#----------------------------------#

def returns(return_type):
  # Complete the returns() decorator
  def decorator(func):
    def wrapper(*args, **kwargs):
      result = func(*args, **kwargs)
      assert type(result) == return_type
      return result
    return wrapper
  return decorator
  
@returns(dict)
def foo(value):
  return value

try:
  print(foo([1,2,3]))
except AssertionError:
  print('foo() did not return a dict!')

#----------------------------------#

# Conclusion

"""

"""