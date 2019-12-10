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

```
def main():
  
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
This is the quick version highlighting the most important pieces of code, to see the final code in its full version please reference the file [CS499FinalCRUDDannyRandolphEnhancementOne.py](https://github.com/Danny11068/Capstone/blob/master/CS499FinalCRUDDannyRandolphEnhancementOne.py) in the github directory for this project.

### Enhancement One Narrative

To begin, I started with my full-stack API that was created in client/server development class CS340. It was created a few months ago and is fully functional but devoid of any sort of security protections whatsoever, and the database is completely open to be accessed by anyone. It is an exemplary example of my skills at full-stack development and is, in fact, the project I am most proud of and I feel demonstrates real-world industry skills the best. This enhancement to add security to the software accomplishes two main goals. First, it meets the course objects planned with this enhancement and keeps me on track for full outcome coverage. Secondly, it really makes this artifact shine as it is included in my ePortfolio as a fully functional API that could very reasonably be used in a real-world scenario. 

This first enhancement was quite a fun and challenging learning exercise. The enhancement completed was to add a username and login to the database connection so that our data could be secure and not just have an open database that anyone could access. This required a good amount of learning and research into how to use the right functions from PyMongo framework in order to pass username and password to the database connection. Additionally, the program had to be modified to include this information as previously the database connection was setup immediately after the import statements. Now, it has to get the user to provide a username and password first, and then setup the database connection which is now being done inside the main method. The main method then sends the information to a newly created function authenticate_user in order to create the DB connection and successfully verify login credentials. Additionally, I chose to send this to a new function rather than just build it inside the main method, so that the code can be wrapped in a try block and return a False value if there is an error and additionally it can be called again with new credentials in the future, whereas if it was hardcoded in the main function this would not be possible.

While not demonstrated directly in the provided code, this project also involved a lot of learning on the backend mongo setup in order to change it to a secured database. Additionally, this involved learning how to create and maintain a table of usernames and passwords that the database would accept. Lastly, I also learned to change the default address and port in accordance with best practices from the industry on establishing a secure database.

In conclusion, a good deal of changes was made on both the front end as well as the back end of this full-stack project in order to add an invaluable layer of security to our database. This enhancement accomplished both of the course objectives I planned for enhancement one. First, it demonstrates my ability to design and implement solutions to solve a problem, like database security, within acceptable constraints as far as trade offs and design choices. Secondly, it demonstrates a security mindset and anticipates adversarial exploits and aims to help reduce the risk. This ensures the portfolio is on track with the original outline in order to ensure I achieve all course outcomes. However, there are a few immediate changes that would be next steps if this were a real environment and I wanted to touch on those here. First, retrieving username and password from the user is setup in the only python file with a main method, however, there are other files in this full-stack project and I would create a way for all of those files to use the provided name and password rather than have to ask the user every time we move to a different portion. Secondly, while username and password help make the database much more secure than it was, the next step would be to add SSL and security certificates to the process to add an additional layer of security. With the combination of user authentication and SSL/security certificates I believe we would have successfully created a full-stack API that is sufficiently secure by the current standards of best practices in this industry.

## Enhancement Two - Data Structures and Algorithms

This second enhancement's primary goal was to take a group of functions that were created for academic purposes and generaly only required to return a specific field, and make them more professional by developing a set of uniform fields to include in every result, making them look and feel more professional as well as bring uniformity to the user experience and ensure a pleasant interaction with the application. For this purpose I identified 4 key fields to include in every function Ticker, Price, Sector, and Industry. These were changed to match all of the fields, but I highlight one primary example below:

Old function
```
# stockReport/list
@route('/stockReport/<list>', method='GET')
def stockReport(list):
    projection = {"Ticker" : 1, "50-Day Simple Moving Average": 1, "_id": 0}
    myDoc = {"Ticker": list}
    result = read_documentProjection(myDoc, projection)
    return json.loads(json.dumps(result, indent=4, default=json_util.default))
```

New Function
```
# stockReport/list
@route('/stockReport/<list>', method='GET')
def stockReport(list):
    projection = {"Ticker" : 1, "Sector" : 1, "Industry" : 1, "Performance (YTD)" : 1, "Price" : 1, "50-Day Simple Moving Average": 1, "Shares Float": 1, "_id": 0}
    myDoc = {"Ticker": list}
    result = read_documentProjection(myDoc, projection)
    return json.loads(json.dumps(result, indent=4, default=json_util.default))
```

### Enhancement Two Narrative

To begin, I started with my full-stack API from CS340 class, client and server development. It was created a few months ago and is fully functional but I felt strongly there was an opportunity to expand the stock report function to return something much more interesting, as well as demonstrate a real-world output, by enhancing the query and the projection it returns. I was proud of this project at the time, and still am, but I see a unique opportunity in really showcases how closely this can reflect real-world scenarios by developing the queries an algorithms a little more here.

	This second enhancement is to alter a few things with the algorithms and primarily the data structure that is returned to the user as well. First, all of this is using a stock market database and I want the information to be the same no matter what query we are running. For that I have selected the Ticker, the Sector, the Industry, Performance, and Price. I am going to make sure that all of my stock-analysis queries report these 5 pieces of information and in the same order consistently. If there is anything specific to a particular category, it will be included in addition to these categories. The only exception will be the one search that returns anything greater than a certain 50-day average as that one returns too many results and causing it to return 6 times as many fields just made it harder to read and didn’t feel as an improvement. On a logical level, this appeared to be more complex than it really needs to be. After getting into the code, Python, or PyMongo more accurately, provides a strong tool for this already in the form of a Projection variable. The projection variable can be used to specify what data is returned and how you want to see it. Once I have build this projection variable once, it can be used repeatedly to provide this extensive, uniform feedback we are looking for. I have provided a key before and after example below:
 
```
# stockReport/list
@route('/stockReport/<list>', method='GET')
def stockReport(list):
    projection = {"Ticker" : 1, "50-Day Simple Moving Average": 1, "_id": 0}
    myDoc = {"Ticker": list}
    result = read_documentProjection(myDoc, projection)
    return json.loads(json.dumps(result, indent=4, default=json_util.default))
```
 
Which I have altered to include a projection variable based on the data above and now looks like this:

```
# stockReport/list
@route('/stockReport/<list>', method='GET')
def stockReport(list):
    projection = {"Ticker" : 1, "Sector" : 1, "Industry" : 1, "Performance (YTD)" : 1, "Price" : 1, "50-Day Simple Moving Average": 1, "Shares Float": 1, "_id": 0}
    myDoc = {"Ticker": list}
    result = read_documentProjection(myDoc, projection)
    return json.loads(json.dumps(result, indent=4, default=json_util.default))
```

Overall, we can see this is much more information but professionally displayed and the results will be uniform no matter how many different stock reports the user pulls they will be used to seeing the same data variables throughout the entirety of this application. These changes highlight two important course objectives. First, the uniformaty that I am aiming to bring to this project with these changes provides broader usability for a multitude of different users. It makes the system more accessaple to a diverse audience in order to support organizational decision making. Secondly, it brings a professional quality to the function that we created for academic purposes but could really be used beyond that now that we have added some polish and complexity to the situation. With both of these goals complete, this portfolio is on track with the original plan to meet all course objectives.

## Enhancement Three - Software Engineering

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
