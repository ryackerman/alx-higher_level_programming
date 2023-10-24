
# 0x14. JavaScript - Web scraping


## Resources

**Read or watch**:

- [Working with JSON data](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)
- [The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran - from Cohort 1 - San Francisco](https://medium.com/@vietkieutie/the-workflow-of-accessing-the-attributes-of-a-simply-created-json-object-82a5b33e2319)
- [request module](https://github.com/request/request)
- [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)
## Learning Objectives

### General

- Why JavaScript programming is amazing
- How to manipulate JSON data
- How to use `request` and fetch API
- How to read and write a file using `fs` module
## Requirements

### Python Scripts

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 20.04 LTS using `node` (version 14.x)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/node`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should be `semistandard` compliant. [Rules of Standard](https://standardjs.com/rules.html) + [semicolons on top](https://github.com/standard/semistandard). Also as reference: [AirBnB style](https://github.com/airbnb/javascript)
- All your files must be executable
- The length of your files will be tested using `wc`
- You are not allowed to use `var`
## More Info

### Install Node 14

```
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

### Install semi-standard

[Documentation](https://github.com/standard/semistandard)
```
$ sudo npm install semistandard --global
```

### Install `request` module and use it

[Documentation](https://github.com/request/request)
```
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```


**Notes:** Request module has been deprecated since February 2020 - the team is considering alternative to replace this module - however, it’s a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry).
## Tasks

    0. Readme
    1. Write me
    2. Status code
    3. Star wars movie title
    4. Star wars Wedge Antilles
    5. Loripsum
    6. How many completed?
## Author

- [ryackerman](https://github.com/ryackerman)
