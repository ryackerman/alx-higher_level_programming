
# 0x09. Python - Everything is object




![alt text](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/252/r_208403_QPSN8.jpg)

## Background Context

#### Important notice on intranet checks for Python projects

Now that we understand that everything is an object and have a little bit of knowledge, let’s pause and look a little bit closer at how Python works with different types of objects.

BTW, have you ever modified a variable without knowing it or wanting to? I mean:

```
>>> a = 1
>>> b = a
>>> a = 2
>>> b
1
>>>
```

OK. But what about this?

```
>>> l = [1, 2, 3]
>>> m = l
>>> l[0] = 'x'
>>> m
['x', 2, 3]
>>> 
```

![alt text](https://media.giphy.com/media/wAjfQ9MLUfFjq/giphy.gif)

This project is a little bit different than the usual projects. The first part is only questions about Python’s specificity like “What would be the result of…”. You should **read all documentation first (as usual :))**, then take the time to **think and brainstorm with your peers** about what you think and why. Try to do this without coding anything for a few hours.

Trying examples in the Python interpreter will give you most of the answers without having to think about it. **Don’t go this route.** First read, then think, then brainstorm together. Only then you can test in the interpreter.

It’s important that you truly understand the reasons behind the answers of all those tasks so that you can apply the same logic to other variables and other variable types.

Note that during interviews for Python positions, **you will most likely have to answer to these type of questions.**

All your answers should be only one line in a file. No space before or after the answer.
## Resources

Read or watch:

- [9.10. Objects and values](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#objects-and-values)
- [9.11. Aliasing](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#aliasing)
- [Immutable vs mutable types](https://stackoverflow.com/questions/8056130/immutable-vs-mutable-types)
- [Mutation](http://composingprograms.com/pages/24-mutable-data.html#sequence-objects) (Only this chapter)
- [9.12. Cloning lists](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#cloning-lists)
- [Python tuples: immutable but potentially changing](http://radar.oreilly.com/2014/10/python-tuples-immutable-but-potentially-changing.html)
## General

- Why Python programming is awesome
- What is an object
- What is the difference between a class and an object or instance
- What is the difference between immutable object and mutable object
- What is a reference
- What is an assignment
- What is an alias
- How to know if two variables are identical
- How to know if two variables are linked to the same object
- How to display the variable identifier (which is the memory address in the CPython - implementation)
- What is mutable and immutable
- What are the built-in mutable types
- What are the built-in immutable types
- How does Python pass variables to functions
## Requirements

### Python Scripts

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version `2.8.*`)
- All your files must be executable
- The length of your files will be tested using `wc`

### `.txt` Answer Files

- Only one line
- No Shebang
- All your files should end with a new line
## Tasks

    0. Who am I?
    1. Where are you?
    2. Right count
    3. Right count =
    4. Right count =
    5. Right count =+
    6. Is equal
    7. Is the same
    8. Is really equal
    9. Is really the same
    10. And with a list, is it equal
    11. And with a list, is it the same
    12. And with a list, is it really equal
    13. And with a list, is it really the same
    14. List append
    15. List add
    16. Integer incrementation
    17. List incrementation
    18. List assignation
    19. Copy a list object
    20. Tuple or not?
    21. Tuple or not?
    22. Tuple or not?
    23. Tuple or not?
    24. Who I am?
    25. Tuple or not
    26. Empty is not empty
    27. Still the same?
    28. Same or not?

## Authors

[ryackerman](https://github.com/ryackerman)
