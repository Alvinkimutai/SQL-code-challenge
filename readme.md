# Concert Code Challenge #
- Concert code challenge involved writing five different files **band.py**, **venue.py** and **concert.py**. There is also a **test_classes.py** file for running and testing all the python classes. Lastly there is a **mydb.db** which is a relational database for storing the different tables created.
- To perform necessary operations on the database **raw SQL queries** was used in this case.
***

## Running the code ##

- Fork and clone the repository into your local machine
- Open the Repository in Visual Studio Code
- Install **SQLite Viewer** to be able to view the tables in the database
- In the terminal enter the virtual environment though the command **pipenv shell**
- Finally use **nodemon --exec python3 test_classes.py** to run test_classes.py which imports from the three classes. Another suitable command would be **python3 test_classes.py** or press the **run button**
***
## Relationship between the classes ##
> **Band** has many concerts, a **Venue** has many concerts, and a **Concert** belongs to a band and to a venue. **Band-Venue** is a many-to-many relationship.

