# CMSC447IndividualAssignment
Author: Sean Elia

This Repository contains files to add to a python virtual library in order to set up the project
These need to be downloaded for the project to function:
- python 3+
- mySQL (and preferably mySQL Workbench)

The following libraries (and any they are dependant on) must be added to the virtual environment using pip:
- flask
- react
- mysql.connector
- pandas

Files that must be added to the virtual environment (assume venv was named *myVenv*):
(Note: repository contains some unnecesary files, however these are the only files that need to be added)

*myVenv*:
- app.py
- create.sql
- drop.sql
- populate.sql
- config.txt
- *Templates*:
    - edit.html
    - home.html
    - view.html

How to set up the Database portion:
- Using mySQL Workbench, host a Database and run the included files *create.sql* then *populate.sql* on the server to initialize the table
    - If not using mySQL Workbench, then create the server and copy the scripts into a comand line
- Update the contents of *config.txt* to contain the name of your Database, the username and pasword, and the IP address/port it is connected to
    - Ensure that each data field listed below is on a seperate line of the file and formated as "< data field >: < value specific to your database >":
        - dbName        (The name you assined to the Database server as a whole)
        - dbIP          (The IP address the Database can be accessed at)
        - dbPort        (Which port the Database must be accessed from)
        - dbUser        (The username to access your Database)
        - dbPass        (The password to access your Database)
    - The order of these data fields is irrelavent, however the format and inclusion of each is very important