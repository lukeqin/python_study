#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/03/16 17:43
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : module.py
# @notice ：


# from modules import fibo
#
# fibo.fib(1000)
# print(fibo.fib2(100))
# print(fibo.__name__)
#
# fib = fibo.fib
# fib(1000)


# More on Modules
# from modules.fibo import fib, fib2
# fib(500)

# from modules.fibo import *
# fib(500)

# import modules.fibo as fib
# fib.fib(500)

from modules.fibo import fib as fibonacci
fibonacci(500)


# Executing modules as scripts


# The module search path
'''
>>> sys.path
['', 'C:\\Users\\fsb6077\\AppData\\Local\\Programs\\Python\\Python39\\python39.zip', 'C:\\Users\\fsb6077\\AppData\\Local\\Programs\\
Python\\Python39\\DLLs', 'C:\\Users\\fsb6077\\AppData\\Local\\Programs\\Python\\Python39\\lib', 'C:\\Users\\fsb6077\\AppData\\Local\
\Programs\\Python\\Python39', 'C:\\Users\\fsb6077\\AppData\\Local\\Programs\\Python\\Python39\\lib\\site-packages']
>>>
'''


# Standard modules
'''
>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
>>> sys.ps1 = 'C> '
C> print('Yuck!')
Yuck!
C>

>>> import sys
>>> sys.path.append('/ufs/guido/lib/python')
'''


# The dir() Function
# The built-in function dir() is used to find out which names a module defines. It returns a sorted list of strings:
import sys
import modules.fibo as fibo

print(dir(fibo))
print(dir(sys))

# Without arguments, dir() lists the names you have defined currently:
'''
>>> a = [1, 2, 3, 4, 5]
>>> import fibo
>>> fib = fibo.fib
>>> dir()
['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']
'''


# dir() does not list the names of built-in functions and variables. If you want a list of those, they are defined in the standard module builtins:
import builtins
print(dir(builtins))


# Packages
'''
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
'''

'''
Users of the package can import individual modules from the package, for example:

import sound.effects.echo
This loads the submodule sound.effects.echo. It must be referenced with its full name.

sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
An alternative way of importing the submodule is:

from sound.effects import echo
This also loads the submodule echo, and makes it available without its package prefix, so it can be used as follows:

echo.echofilter(input, output, delay=0.7, atten=4)
Yet another variation is to import the desired function or variable directly:

from sound.effects.echo import echofilter
Again, this loads the submodule echo, but this makes its function echofilter() directly available:

echofilter(input, output, delay=0.7, atten=4)
'''


# import * from package
