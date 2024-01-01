from typing import TypeVar
from _collections_abc import Callable
from typing import Concatenate
# 1.4
# 1.

U = TypeVar("U")
def indentity(x: U) -> U:
  return x

# 2.

A = TypeVar("A")
B = TypeVar("B")
C = TypeVar("C")
def compose(f: Callable[[A], B], g: Callable[[B], C])-> Callable[[A],C]:
  return lambda x: g(f(x))

# 3
def add2(x: int)->int:
  return x+2
def add4(x: int)->int:
  return x+4

def appenda(s: str) -> str:
  return s + 'a'
print(add2(add4(2)))
add6 = compose(add2,add4)
print(compose(indentity,add2)(4))
print(compose(appenda,indentity)('matias'))

def memoize(f: Callable[[A], B]) -> Callable[[A], B]:
  memory = {}
  def g(a: A) -> B:
    nonlocal memory
    if a in memory.keys():
      print("in memory")
      return memory[a]
    else:
      print("new value")
      new_value=f(a)
      memory[a]=new_value
      return new_value
  
  return g

@memoize
def factorial(n: int) -> int:
  if n == 1:
    return 1
  else:
    return n*factorial(n-1)



print(factorial(200))
print(factorial(200))
print(factorial(100))
print(factorial(199))

from random import random, seed