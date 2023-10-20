import pytest

def count(sequence, item):
  count = 0
  for elem in sequence:
    if elem == item:
      count += 1
  return count

def test_count_ints():
  nums = [1, 2, 3, 1, 4, 1]
  assert count(sequence=nums, item=1) == 3

def test_count_strings():
  words = ['hello', 'world', 'hello', 'python']
  assert count(sequence=words, item='hello') == 2
  
if __name__ == '__main__':
  pytest.main()






def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

def test_fact():
    assert fact(0) == 1
    assert fact(1) == 1
    assert fact(5) == 120
    assert fact(10) == 3628800







def list_of_squares(n):
    d=dict()
    for i in range(1,n+1):
        d[i]=i*i
    return d

def test_list_of_squares():
    assert list_of_squares(1) == {1: 1}
    assert list_of_squares(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    assert list_of_squares(10) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}







def vowels(word):
    number_of_vowels = 0
    the_vowels = ["a", "e", "i", "o", "u"]
    for letter in word.lower():
        if letter in the_vowels:
            number_of_vowels += 1
    return number_of_vowels

def test_vowels():
    assert vowels("xyz") == 0
    assert vowels("aeiou") == 5
    assert vowels("AEIOU") == 5
    assert vowels("Hello World") == 3