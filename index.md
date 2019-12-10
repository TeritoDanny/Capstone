# Welcome to my ePortfolio

Here is a list of works showing my most exemplary software engineering examples during my academic career in Computer Science

Additionally, I have completed a series of enhancements above and beyond what was required for the original course, in order to showcase my abilities further in several key areas.

## Code Review

Here is a link to my video code review where I go through these projects, in the video I identify the need to make the following enhancements:

- Algorithms and Data Structures: expand upon the stock report returned, making it more complex and more professional in appearance

- Databases: Make the database more secure by adding a username/password requirement to access the DB

- Software Engineering: Convert the project from Python into Java which will relay a variety of software development skills

## Enhancement One - Databases
Here we will make the first enhancement which involves adding the username and password to the database.
First, here is the original code setting up the databse connection:
```
connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']
```
This enhancement occured in two primary steps, excluding the backend changes to the database itself, which are not highlighted in this portfolio. First, we need to capture a username and password from the user. Secondly, we need to pass this info during the database connection setup. These two steps are shown in the code snippets below:

```def main():
  
    useName = input("Username:")
    passW = input("Password:")
    authenticate_user(useName,passW)
```

```
# setup database connection with user authentication details
def authenticate_user(name,pw):
    try:
        connection = MongoClient('localhost', 27017, username=useName, password=passW)
        db = connection['market']
        collection = db['stocks']
    except:
        return False
    return True
```

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/TeritoDanny/Capstone/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
