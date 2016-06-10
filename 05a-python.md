# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

The main difference between lists and tuples is in their mutability. Lists are mutable objects, which means that elements can be appended, removed, or reassigned after the lists are first assigned. Tuples are immutable, so none of these actions are possible after first assignment. There are differences between the two from a data structure standpoint with regard to memory usage. Lists typically use more memory because of the way they grow in size as elements are added. Lists and tuples are similar in that they can be indexed the same way: starting at 0 and ending at n-1.
Tuples will work as keys in dictionaries; lists will not. This is due to the fact that immutable Python objects like tuples support hashing, while mutable objects do not. Dictionaries pair keys to values via hashing. Hashing requires that input values map to the same output values every time. Because mutable objects can be reassigned, their output values can differ, complicating the mapping process.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Lists and sets also differ in their mutability. Sets are immutable and contain unique elements, while lists are mutable can have multiple instances of the same element. Both a list and a set are collections of elements, but lists maintain insertion order while sets do not.
```python
# here is an array of numbers stored in a list
l = [1,3,3,7,9,9,11]

# if you wanted to store the unique elements from the list in a data structure, you would use a set
b = set(l)
print b ~~> {1,3,7,9,11}
```
It takes longer to find an element in a list as a list looks at each element individually while a set uses hashing to determine if it contains an element. 

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

Lambda is an expression used for defining an anonymous function in line. It is shorter to write than a fully defined function, is often used to create a function that only needs to be used once.
```python
# add 3 and 4 together
(lambda x,y: x+y)(3,4) ~~> 7

# unordered list of fruits, both upper and lower case
fruits = ['Pineapple', 'Orange', 'guava', 'peach']

# sorted function returns capitalized words first
sorted(fruits) ~~> ['Orange', 'Pineapple', 'guava', 'peach']

# map a "lower case" function to items before sorting
sorted(fruits, key=lambda fruit: fruit.lower()) ~~> ['guava', 'Orange', 'peach', 'Pineapple']
```
---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

A list comprehension is a way to create a new list from an existing list by imposing conditions on the existing list.

```python
numbers = [1,3,6,7,9]

# create a new list with 3 added to every number
bignumbers = [x+3 for x in numbers]
print bignumbers ~~> [4,6,9,10,12]

# same process using 'map' function
def adder(num):
    return num+3
newnumbers = map(adder, numbers)
print newnumbers ~~> [4,6,9,10,12]

# using 'filter' function to create new list of numbers greater than 5
filtering = [filter(lambda x: x>5, numbers)]
print filtering ~~> [6,7,9]
```
Using a list comprehension is a way to accomplish map or filter with fewer lines of code. With regard to time complexity list comprehension is equivalent to map or filter.
```python
# create a set containing number 3 greater than original number
setbignumbers = {x+3 for x in numbers}
print setbignumbers ~~> {4,6,9,10,12}

# create a dictionary mapping number from original list to number 3 greater
dictbignumbers = {x:x+3 for x in numbers}
print dictbignumbers ~~> {1: 4, 3: 6, 6: 9, 7: 10, 9: 12}
```
---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





