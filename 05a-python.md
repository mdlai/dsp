# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are similar because they are a sequence of values.  Lists are different from tuples because tuples are immutable and lists are not.  As a result, tuples will work in dictionaries but lists will not.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets are both sequence of values.  A list is different from a set because it can have multiple repeating values.  The list also preserves order.  The performance of a set is better for finding an element because it uses as hashtable.  This allows an element in a set to have a known location based on its value.<br/>
`a = [1,2,3,4,3]`
set: `set(a) -->
set([1,2,3,4])`
list: `list(a) -->
[1,2,3,4,3]`

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Python's `lambda` creates a function without explicitly defining the function.  It's useful for functions that aren't used repeatedly.  <br/> `sorted([3,5,1,2,4], key = lambda x: -x)`

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are like creating sets in mathematics.  In mathematics someone could write `S = {0*0, 1*1, 2*2, ... 9*9}` and the equivalent list comprehension would be `[x**2 for x in range(0,10)]`. <br/>Using map it would equivalently be `map(lambda x:x**2, range(0,10))`.  <br/><br/>Maps seem better for iterating multiple lists simultaneously for example `map(lambda x,y: x+y, [1,2,3],[4,5,6])` could be written as `[[1,2,3][j]+[4,5,6][j] for j in range(0,3)]` <br/><br/>`filter(lambda x: x > 2, range(0,5))` is equivalent to `[x for x in range(0,5) if x > 2]`  Filter and lambda seem identical.<br/><br/>set comprehension: `{x for x in range(0,10)}`<br/>dictionary comprehension: `{x:y for (x,y) in enumerate(range(1,11))}`



---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 Days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 Days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 Days

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
