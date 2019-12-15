# Welcome to my ePortfolio

Here is a list of works showing my most exemplary software engineering examples during my academic career in Computer Science

Additionally, I have completed a series of enhancements above and beyond what was required for the original course, in order to showcase my abilities further in several key areas.

## Professional Self-Assessment

This complete ePortfolio highlights my developed skillset at software engineering, my desire for continued learning and professional development, all brought together in this full-stack application I have developed. While the enhancements included in this portfolio specifically focus around software engineering, data structures and algorithms, and database security, there are several other aspects throughout the education I have gained during the computer science program and are also present here.

First and foremost, I really appreciated getting experience during my coursework in a collaborative team environment. It will prove invaluable to have exposure to both working alongside other developers while simultaneously getting exposure to version control in Github, Bitbucket, as well as Eclipse. Peer code reviews were also helpful in seeing code from another person’s perspective which also helps with the next topic of communicating to stakeholders. Granted, I have a lot of professional experience in this area already, but the cumulative result of my experiences has shown the importance of this type of communication. Being able to distill requirements from what stakeholders are asking for is immensely important in the beginning stages of a project. Additionally, being able to walk them through the software you have developed is crucial to finalizing the stages, as well as every step in between. 

Lastly, I have developed an extensive skillset as a developer focusing on data structures and algorithms, software engineering, and databases and security. It is no coincidence these were the three focus areas of my enhancements to my portfolio, and I cover those enhancements in greater detail below. For software engineering, I chose a full-stack application and converted it from Python into Java. This demonstrates a deep understanding of the code and logic used in order to pull it apart and reconstruct it in another language, especially one that involves a lot of use of third-party libraries and interfaces. Secondly, from data structures and algorithms, I focused on putting more nuance into the data that was returned on various searches. This demonstrates a complete understanding of the way the data is structured in order to pull more sophisticated findings and present them to the user. Finally, I turned my attention to databases and security and added a username and password to my MongoDB interface. When initially creating this application, this was one of the big holes I saw in its design, so I was thrilled to have this opportunity to come back and correct this by adding this username and password user authentication. While it may not be enough security alone, it is a great step forward towards making this database more secure.       

In conclusion, I have developed a well-rounded skillset during my time in the computer science program here at SNHU. I have focused specifically on team collaboration, communicating to stakeholders, data structures and algorithms, software engineering principles, databases, and security. I have focused on the three key areas mentioned earlier as I completed three demonstrative enhancements to this portfolio. Next, I will go into detail discussing the 


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
This is, again, a small highlight version of the code changes and the full version can be seen [here](https://github.com/Danny11068/Capstone/blob/master/CS499FinalRESTDannyRandolphEnhancementTwo.py)

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

The third and final enhancement was to convert the client application from Python into Java while maintaning the same usability it had before when interfacing with the PyMongo server side application that runs in tandem with this file. This enhancement can't really be summarized in a small clip of code from before or after as the entire file had to be re-written from scratch. However, I think just how big of a difference it makes can be seen in the initial file setup through the first function, so I will highlight both of those portions here.
Python Version:
```
#!/usr/bin/python
import json
from bson import json_util
import bottle
from bottle import Bottle, route, run, request, abort
import pymongo
from pymongo import MongoClient
import datetime
import pprint

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

# *** CRUD imported operations
def insert_document(document):
    try:
        result=collection.save(document)
    except:
        return False
    return True
```
Java Version
```
package com.snhu.app;

import com.mongodb.BasicDBObject;
import com.mongodb.BulkWriteOperation;
import com.mongodb.BulkWriteResult;
import com.mongodb.Cursor;
import com.mongodb.DB;
import com.mongodb.DBCollection;

import com.mongodb.DBCursor;
import com.mongodb.DBObject;
import com.mongodb.MongoClient;
import com.mongodb.ParallelScanOptions;
import com.mongodb.ServerAddress;
import java.util.List;
import java.util.Set;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.lang.ClassNotFoundException;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;

import static java.util.concurrent.TimeUnit.SECONDS;

public class App {
  
  /* C from CRUD functions for creating a document */
  public static void create_document(BasicDBObject doc) {
    try {
      MongoClient mg = new MongoClient("localhost");
      DB db = mongoClient.getDB("market");
      DBCollection coll = db.getCollection("stocks");
      coll.insert(doc);
    } catch (UnknownHostException e) {
      e.printStackTrace();
    } catch (IOException e) {
      e.printStackTrace();
    } catch (Exception e) {
      e.printStackTrace();
    }
```
As you can see, a great many changes in the nuances of the code are required even though the function from each program simply adds a record to the collection. This final enhancement has affected multiple files. In my github directory, [App.java](https://github.com/Danny11068/Capstone/blob/master/App.java) is the client-side application that runs this, it works with the [pom.xml](https://github.com/Danny11068/Capstone/blob/master/pom.xml) file to point it to the correct places for some of the imports. Once running, it is meant to interface with the [server side script](https://github.com/Danny11068/Capstone/blob/master/CS499FinalRESTDannyRandolphEnhancementTwo.py) in order to actually perform CRUD functions on the Mongo DB I have setup.

### Enhancement Three Narative

This is the enhancement I have been looking forward to the most and wanted to save for last. I began with my CRUD operations which are function I designed in Python using PyMongo to create a set of functions that would perform basic CRUD operations on my Mongo DB. This artifact involves me converting that from Python into a java file. This demonstrates many useful skills of a software engineer. Perhaps most importantly, it demonstrates a clear understanding of the principles of the software to be able to strip it down and recreate all of the functionality in another language. All of the projected course outcomes and objectives were met along with my original outline.

Initially, this task was the most daunting. Despite being proficient in Python, PyMongo is an additional interface which can sometimes be finicky to pick up and get everything working right. I was not looking forward to starting that process over in Java now. Additionally, especially because Python is so unique in its syntax, it can be confusing to copy concepts over and involve a lot of missed semicolons or other minor syntax errors. However, I was pleasantly surprised at how easy the conversion was. Converting my code from Python to Java was pretty seamless and painless, which I predicted would be the easier part. Additionally, I was pleasantly surprised at how easy it was to use the Java driver for Mongo compared to my experience with PyMongo. Perhaps I shouldn’t be as shocked as I was, but many of the exact same names are given to the functions to access, read from, and interface with a mongo DB across the two interfaces and two different languages. Overall this particular artifact came together more easily than I had anticipated, but still served as excellent professional experience that I am sure I will draw on in similar projects throughout my future career in the industry.

## Professional Self-Assessment

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
