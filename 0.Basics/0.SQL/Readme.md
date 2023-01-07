**SQL**

**Introduction to SQL**

Structure Query Language(SQL) is a database query language used for storing and managing data in Relational DBMS. SQL was the first commercial language introduced for E.F Codd's Relational model of database. Today almost all RDBMS(MySql, Oracle,

Infomix, Sybase, MS Access) use SQL as the standard database query language. SQL is used to perform all types of data operations in RDBMS. SQL Command

SQL defines following ways to manipulate data stored in an RDBMS.

**DDL: Data Definition Language**

This includes changes to the structure of the table like creation of table, altering table, deleting a table etc.

All DDL commands are auto-committed. That means it saves all the changes permanently in the database.

Command    Description ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.001.png)

create:    to create new table or database alter:    for alteration 

truncate:    delete data from table 

drop:    to drop a table 

rename:    to rename a table

**DML: Data Manipulation Language**

DML commands are used for manipulating the data stored in the table and not the table itself.

DML commands are not auto-committed. It means changes are not permanent to database, they can be rolled back. |Command| Description| | --- | ----------- | |insert| to insert a new row| |update| to update existing row| |delete |to delete a row| |merge |merging two rows or two tables|

**TCL: Transaction Control Language**

These commands are to keep a check on other commands and their affect on the database. These commands can annul changes made by other commands by rolling the data back to

its original state. It can also make any temporary change permanent. |Command| Description| | --- | ----------- | |commit| to permanently save| |rollback| to undo change| |savepoint| to save temporarily|

**DCL: Data Control Language**

Data control language are the commands to grant and take back authority from any database user.

**Command Description ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.002.png)**grant grant permission of right revoke take back permission

**DQL: Data Query Language**

Data query language is used to fetch data from tables based on conditions that we can easily apply. 

|Command| Description| | --- | ----------- | |select | retrieve records from one or more table|

**DDL**

**SQL: create command**

*create is a DDL SQL command used to create a table or a database in relational database management system.![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.003.png)*

Creating a Database

To create a database in RDBMS, create command is used. Following is the syntax,

**CREATE**  **DATABASE**  <DB\_NAME>;![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.004.png)

**Example for creating Database**

**CREATE** **DATABASE** **Test**;![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.005.png)

The above command will create a database named Test, which will be an empty schema without any table.

To create tables in this newly created database, we can again use the create command.

**Creating a Table**

create command can also be used to create tables. Now when we create a table, we have to specify the details of the columns of the tables too. We can specify the names and datatypes of various columns in the create command itself.

Following is the syntax,

**CREATE**  **TABLE**  <TABLE\_NAME> ( ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.006.png)

`    `column\_name1 datatype1,     column\_name2 datatype2,     column\_name3 datatype3,     column\_name4 datatype4 );

create table command will tell the database system to create a new table with the given table name and column information.

Example for creating Table

**CREATE** **TABLE** Student( ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.007.png)

`    `student\_id INT,  

`    `**name** VARCHAR(100),      age INT);

The above command will create a new table with name Student in the current database with 3 columns, namely student\_id, name and age. Where the column student\_id will only store integer, name will hold upto 100 characters and age will again store only

integer value.

If you are currently not logged into your database in which you want to create the table then you can also add the database name along with table name, using a dot operator .

For example, if we have a database with name Test and we want to create a table Student in it, then we can do so using the following query:

**CREATE** **TABLE** Test.Student(  ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.008.png)   student\_id INT,  

`    `**name** VARCHAR(100),  

`    `age INT);

**Most commonly used datatypes for Table columns**

Here we have listed some of the most commonly used datatypes used for columns in tables. |Datatype| Use| | --- | ----------- | |INT |used for columns which will store integer values.| |FLOAT | used for columns which will store float values.| |DOUBLE |used for columns which will store float values.| |VARCHAR |used for columns which will be used to store characters and integers, basically a string.| |CHAR |used for columns which will store char values(single character).| |DATE |used for columns which will store date values.| |TEXT |used for columns which will store text which is

generally long in length. For example, if you create a table for storing profile information of a social networking website, then for about me section you can have a column of type TEXT.|

**SQL: ALTER command**

alter command is used for altering the table structure, such as,

to add a column to existing table ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.009.png)

to rename any existing column 

to change datatype of any column or to modify its size. to drop a column from the table.

**ALTER Command: Add a new Column**

Using ALTER command we can add a column to any existing table. Following is the syntax,

**ALTER** **TABLE** table\_name **ADD**(  ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.010.png)   column\_name datatype);

Here is an Example for this,

**ALTER** **TABLE** student **ADD**(  ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.011.png)   address VARCHAR(200) );

The above command will add a new column address to the table student, which will hold data of type varchar which is nothing but string, of length 200.

**ALTER Command: Add multiple new Columns**

Using ALTER command we can even add multiple new columns to any existing table. Following is the syntax,

**ALTER** **TABLE** table\_name **ADD**(  ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.008.png)   column\_name1 datatype1,      **column**-name2 datatype2,      **column**-name3 datatype3);

Here is an Example for this,

**ALTER** **TABLE** student **ADD**( ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.008.png)

`    `father\_name VARCHAR(60),      mother\_name VARCHAR(60),      dob DATE); 

The above command will add three new columns to the student table

**ALTER Command: Add Column with default value**

ALTER command can add a new column to an existing table with a default value too. The default value is used when no value is inserted in the column. Following is the syntax,

**ALTER** **TABLE** table\_name **ADD**( ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.012.png)

`    `**column**-name1 datatype1 **DEFAULT** some\_value );

Here is an Example for this,

**ALTER** **TABLE** student **ADD**( ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.013.png)

`    `dob DATE **DEFAULT** '01-Jan-99' );

The above command will add a new column with a preset default value to the table student.

**ALTER Command: Modify an existing Column**

ALTER command can also be used to modify data type of any existing column. Following is the syntax,

**ALTER** **TABLE** table\_name **modify**(  ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.014.png)   column\_name datatype 

);

Here is an Example for this,

**ALTER** **TABLE** student **MODIFY**(  ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.015.png)   address varchar(300)); 

Remember we added a new column address in the beginning? The above command will modify the address column of the student table, to now hold upto 300 characters.

**ALTER Command: Rename a Column**

Using ALTER command you can rename an existing column. Following is the syntax,

**ALTER** **TABLE** table\_name **RENAME**  ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.010.png)

`    `old\_column\_name **TO** new\_column\_name;

Here is an example for this,

**ALTER** **TABLE** student **RENAME**  ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.016.png)    address **TO** location; 

The above command will rename address column to location.

**ALTER Command: Drop a Column**

ALTER command can also be used to drop or remove columns. Following is the syntax,

**ALTER** **TABLE** table\_name **DROP**(  ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.010.png)   column\_name);

Here is an example for this,

**ALTER** **TABLE** student **DROP**(  ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.017.png)   address); 

The above command will drop the address column from the table student.

**TRUNCATE  command**

TRUNCATE command removes all the records from a table. But this command will not destroy the table's structure. When we use TRUNCATE command on a table its (auto- increment) primary key is also initialized. Following is its syntax,

TRUNCATE TABLE table\_name Here is an example explaining it,

**TRUNCATE** **TABLE** student;![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.004.png)

The above query will delete all the records from the table student.

In DML commands, we will study about the DELETE command which is also more or less same as the TRUNCATE command. We will also learn about the difference between the two in that tutorial.

**DROP  command**

DROP command completely removes a table from the database. This command will also destroy the table structure and the data stored in it. Following is its syntax,

**DROP** **TABLE** table\_name![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.018.png)

Here is an example explaining it,

**DROP** **TABLE** student;![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.019.png)

The above query will delete the Student table completely. It can also be used on Databases, to delete the complete database. For example, to drop a database,

**DROP** **DATABASE** **Test**;![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.020.png)

The above query will drop the database with name Test from the system.

**RENAME  query**

RENAME command is used to set a new name for any existing table. Following is the syntax,

**RENAME** **TABLE** old\_table\_name **to** new\_table\_name ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.021.png)Here is an example explaining it.

**RENAME** **TABLE** student **to** students\_info;![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.019.png)

The above query will rename the table student to students\_info.

**DML**

Data Manipulation Language (DML) statements are used for managing data in database. DML commands are not auto-committed. It means changes made by DML command are not permanent to database, it can be rolled back.

Talking about the Insert command, whenever we post a Tweet on Twitter, the text is stored in some table, and as we post a new tweet, a new record gets inserted in that table.

**INSERT command**

Insert command is used to insert data into a table. Following is its general syntax,

**INSERT** **INTO** table\_name **VALUES**(data1, data2, ...)![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.019.png)

Lets see an example, Consider a table student with the following fields. s\_id name age

**INSERT** **INTO** student **VALUES**(101, 'Adam', 15);![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.022.png)

The above command will insert a new record into student table. s\_id name age 101 Adam 15

**Insert value into only specific columns**

We can use the INSERT command to insert values for only some specific columns of a row. We can specify the column names along with the values to be inserted like this,

**INSERT** **INTO** student(**id**, **name**) **values**(102, 'Alex');![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.019.png)

The above SQL query will only insert id and name values in the newly inserted record.

**Insert NULL value to a column**

Both the statements below will insert NULL value into age column of the student table.

**INSERT** **INTO** student(**id**, **name**) **values**(102, 'Alex');![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.022.png)

Or,

**INSERT** **INTO** Student **VALUES**(102,'Alex', null);![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.020.png)

The above command will insert only two column values and the other column is set to null. S\_id S\_Name age 101 Adam 15 102 Alex

Insert Default value to a column

**INSERT** **INTO** Student **VALUES**(103,'Chris', **default**)![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.019.png)

|S\_id |S\_Name age| |101 Adam |15| |102 Alex |NULL| |103 chris |14| Suppose the column age in our tabel has a default value of 14.

Also, if you run the below query, it will insert default value into the age column, whatever the default value may be.

**INSERT** **INTO** Student **VALUES**(103,'Chris')![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.005.png)

**UPDATE command**

Let's take an example of a real-world problem. These days, Facebook provides an option for Editing your status update, how do you think it works? Yes, using the Update SQL command.

Let's learn about the syntax and usage of the UPDATE command.

UPDATE command is used to update any record of data in a table. Following is its general syntax,

**UPDATE** table\_name **SET** column\_name = new\_value **WHERE** some\_condition;![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.018.png)

WHERE is used to add a condition to any SQL query, we will soon study about it in ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.016.png)detail.

Lets take a sample table student, student\_id name age 101 Adam 15 102 Alex 103 chris 14

**UPDATE** student **SET** age=18 **WHERE** student\_id=102; ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.005.png)S\_id S\_Name age 101 Adam 15 102 Alex 18 103 chris 14

In the above statement, if we do not use the WHERE clause, then our update query will update age for all the columns of the table to 18. Updating Multiple Columns

We can also update values of multiple columns using a single UPDATE statement.

**UPDATE** student **SET** **name**='Abhi', age=17 **where** s\_id=103; ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.019.png)

The above command will update two columns of the record which has s\_id 103. s\_id name age 101 Adam 15 102 Alex 18 103 Abhi 17

**UPDATE Command: Incrementing Integer Value**

When we have to update any integer value in a table, then we can fetch and update the value in the table in a single statement.

For example, if we have to update the age column of student table every year for every student, then we can simply run the following UPDATE statement to perform the

following operation:

**UPDATE** student **SET** age = age+1; ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.022.png)

As you can see, we have used age = age + 1 to increment the value of age by 1.

NOTE: This style only works for integer values.![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.020.png)

**DELETE command**

When you ask any question in Studytonight's Forum it gets saved into a table. And

using the Delete option, you can even delete a question asked by you. How do you think that works? Yes, using the Delete DML command. DELETE command is used to delete data from a table.

Following is its general syntax, **DELETE** **FROM** table\_name;![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.005.png)

Let's take a sample table student: s\_id name age 101 Adam 15 102 Alex 18 103 Abhi 17 Delete all Records from a Table

**DELETE** **FROM** student;![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.019.png)

The above command will delete all the records from the table student. Delete a particular Record from a Table

In our student table if we want to delete a single record, we can use the WHERE clause to provide a condition in our DELETE statement.

**DELETE** **FROM** student **WHERE** s\_id=103;![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.018.png)

The above command will delete the record where s\_id is 103 from the table student. S\_id S\_Name age 101 Adam 15 102 Alex 18

**Isn't DELETE same as TRUNCATE**

TRUNCATE command is different from DELETE command. The delete command will delete all the rows from a table whereas truncate command not only deletes all the records stored in the table, but it also re-initializes the table(like a newly created table).

For eg: If you have a table with 10 rows and an auto\_increment primary key, and if you use DELETE command to delete all the rows, it will delete all the rows, but will not re-initialize the primary key, hence if you will insert any row after using the DELETE command, the auto\_increment primary key will start from 11. But in case of TRUNCATE command, primary key is re-initialized, and it will again start from 1.

**TCL**

Transaction Control Language(TCL) commands are used to manage transactions in the database. These are used to manage the changes made to the data in a table by DML statements. It also allows statements to be grouped together into logical transactions.

**COMMIT command**

COMMIT command is used to permanently save any transaction into the database.

When we use any DML command like INSERT, UPDATE or DELETE, the changes made by these commands are not permanent, until the current session is closed, the changes made by these commands can be rolled back.

To avoid that, we use the COMMIT command to mark the changes as permanent. Following is commit command's syntax,

**COMMI T**;![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.019.png)

**ROLLBACK command**

This command restores the database to last commited state. It is also used with SAVEPOINT command to jump to a savepoint in an ongoing transaction.

If we have used the UPDATE command to make some changes into the database, and realise that those changes were not required, then we can use the ROLLBACK command to rollback those changes, if they were not commited using the COMMIT command.

Following is rollback command's syntax, ROLLBACK TO savepoint\_name;

**SAVEPOINT command**

SAVEPOINT command is used to temporarily save a transaction so that you can rollback to that point whenever required.

Following is savepoint command's syntax,

**SAVEPOINT** savepoint\_name;![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.018.png)

In short, using this command we can name the different states of our data in any table and then rollback to that state using the ROLLBACK command whenever required. Using Savepoint and Rollback

Following is the table class,

id  name 1 ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.009.png)  Abhi 2   Adam 4   Alex

Lets use some SQL queries on the above table and see the results.

**INSERT** **INTO** **class** **VALUES**(5, 'Rahul'); ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.023.png)

**COMMI T**; 

**UPDATE** **class** **SET** **name** = 'Abhijit' **WHERE** **id** = '5'; 

**SAVEPOINT** A; 

**INSERT** **INTO** **class** **VALUES**(6, 'Chris'); 

**SAVEPOINT** B; 

**INSERT** **INTO** **class** **VALUES**(7, 'Bravo'); 

**SAVEPOINT** C; 

**SELECT** \* **FROM** **class**;

NOTE: SELECT statement is used to show the data stored in the table. The resultant table will look like,

id  name ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.024.png)

1   Abhi 2   Adam 4   Alex 

5   Abhijit 6   Chris 7   Bravo

Now let's use the ROLLBACK command to roll back the state of data to the savepoint B.

**ROLLBACK** **TO** B; ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.011.png)

**SELECT** \* **FROM** **class**;

Now our class table will look like, id ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.025.png) name 

1   Abhi 

2   Adam 

4   Alex 

5   Abhijit 

6   Chris

Now let's again use the ROLLBACK command to roll back the state of data to the savepoint A

**ROLLBACK**  **TO**  A;![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.019.png)

**SELECT** \* **FROM** **class**; ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.026.png)Now the table will look like,

id  name ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.027.png)

1   Abhi 2   Adam 4   Alex 5   Abhijit

So now you know how the commands COMMIT, ROLLBACK and SAVEPOINT works.

**DCL**

Data Control Language(DCL) is used to control privileges in Database. To perform any operation in the database, such as for creating tables, sequences or views, a user needs privileges. Privileges are of two types,

System: This includes permissions for creating session, table, etc and all types of ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.008.png)other system privileges. 

Object: This includes permissions for any command or query to perform any operation on the database tables.

In DCL we have two commands,

GRANT: Used to provide any user access privileges or other priviliges for the ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.028.png)database. 

REVOKE: Used to take back permissions from any user.

Allow a User to create session

When we create a user in SQL, it is not even allowed to login and create a session until and unless proper permissions/priviliges are granted to the user.

Following command can be used to grant the session creating priviliges.

GRANT CREATE SESSION TO username;

Allow a User to create table

To allow a user to create tables in the database, we can use the below command, GRANT CREATE TABLE TO username;

Provide user with space on tablespace to store table

Allowing a user to create table is not enough to start storing data in that table. We also must provide the user with priviliges to use the available tablespace for their table and data.

ALTER USER username QUOTA UNLIMITED ON SYSTEM;

The above command will alter the user details and will provide it access to unlimited tablespace on system.

NOTE: Generally unlimited quota is provided to Admin users. ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.022.png)Grant all privilege to a User

sysdba is a set of priviliges which has all the permissions in it. So if we want to provide all the privileges to any user, we can simply grant them the sysdba permission.

**GRANT** **sysdba** **TO** username ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.021.png)Grant permission to create any table

Sometimes user is restricted from creating come tables with names which are reserved for system tables. But we can grant privileges to a user to create any table using the below command,

**GRANT** **CREATE** **ANY** **TABLE** **TO** username ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.005.png)Grant permission to drop any table

As the title suggests, if you want to allow user to drop any table from the database, then grant this privilege to the user,

**GRANT** **DROP** **ANY** **TABLE** **TO** username![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.019.png)

To take back Permissions

And, if you want to take back the privileges from any user, use the REVOKE command.

**REVOKE**  **CREATE**  **TABLE**  **FROM**  us er name![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.026.png)

**DQL: Data Query Language nad conditions**

**SELECT SQL Query**

SELECT query is used to retrieve data from a table. It is the most used SQL query. We can retrieve complete table data, or partial by specifying conditions using the WHERE clause. Syntax of SELECT query

SELECT query is used to retieve records from a table. We can specify the names of the columns which we want in the resultset.

**SELECT**  ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.029.png)

`    `column\_name1,      column\_name2,      column\_name3,      ... 

`    `column\_nameN  

`    `**FROM** table\_name;

Time for an Example

Consider the following student table,

s\_id    name    age address ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.030.png)101 Adam    15  Chennai 102 Alex    18  Delhi 

103 Abhi    17  Banglore 104 Ankit   22  Mumbai

**SELECT** s\_id, **name**, age **FROM** student;![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.026.png)

The above query will fetch information of s\_id, name and age columns of the student table and display them,

s\_id    name    age ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.031.png)101 Adam    15 

102 Alex    18 

103 Abhi    17 

104 Ankit   22

As you can see the data from address column is absent, because we did not specif it in our SELECT query. Select all records from a table

A special character asterisk \* is used to address all the data(belonging to all columns) in a query. SELECT statement uses \* character to retrieve all records from a table, for all the columns.

**SELECT** \* **FROM** student;![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.032.png)

The above query will show all the records of student table, that means it will show complete dataset of the table.

s\_id    name    age address ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.033.png)101 Adam    15  Chennai 102 Alex    18  Delhi 

103 Abhi    17  Banglore 104 Ankit   22  Mumbai

Select a particular record based on a condition We can use the WHERE clause to set a condition,

**SELECT** \* **FROM** student **WHERE** **name** = 'Abhi';![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.019.png)

The above query will return the following result,

103 Abhi    17  Rohtak![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.022.png)

Performing Simple Calculations using SELECT Query Consider the following employee table.

eid name    age salary ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.034.png)101 Adam    26  5000 102 Ricky   42  8000 103 Abhi    25  10000 ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.035.png)104 Rohan   22  5000

Here is our SELECT query,

**SELECT** eid, **name**, salary+3000  **FROM** employee;![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.019.png)

The above command will display a new column in the result, with 3000 added into existing salaries of the employees.

eid name    salary+3000 ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.031.png)101 Adam    8000 

102 Ricky   11000 

103 Abhi    13000 104 Rohan   8000

So you can also perform simple mathematical operations on the data too using the SELECT query to fetch data from table.

Using the WHERE SQL clause

WHERE clause is used to specify/apply any condition while retrieving, updating or deleting data from a table. This clause is used mostly with SELECT, UPDATE and DELETEquery.

When we specify a condition using the WHERE clause then the query executes only for those records for which the condition specified by the WHERE clause is true. Syntax for WHERE clause

Here is how you can use the WHERE clause with a DELETE statement, or any other statement,

**DELETE** **FROM** table\_name **WHERE** [condition];![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.026.png)

The WHERE clause is used at the end of any SQL query, to specify a condition for execution. Time for an Example

Consider a table student,

s\_id    name    age address ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.031.png)101 Adam    15  Chennai 102 Alex    18  Delhi 

103 Abhi    17  Banglore 104 Ankit   22  Mumbai

Now we will use the SELECT statement to display data of the table, based on a condition, which we will add to our SELECT query using WHERE clause.

Let's write a simple SQL query to display the record for student with s\_id as 101.

**SELECT** s\_id,  ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.030.png)

`    `**name**,  

`    `age,  

`    `address  

`    `**FROM** student **WHERE** s\_id = 101;

Following will be the result of the above query. s\_id name age address 101 Adam 15 Noida Applying condition on Text Fields

In the above example we have applied a condition to an integer value field, but what

if we want to apply the condition on name field. In that case we must enclose the

value in single quote ' '. Some databases even accept double quotes, but single quotes is accepted by all.

**SELECT** s\_id,  ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.030.png)

`    `**name**,  

`    `age,  

`    `address  

`    `**FROM** student **WHERE** **name** = 'Adam';

Following will be the result of the above query.

s\_id    name    age address ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.036.png)

101 Adam    15  Noida 

Operators for WHERE clause condition

Following is a list of operators that can be used while specifying the WHERE clause condition.

Operator    Description = ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.037.png)  Equal to !=  Not Equal to <   Less than >   Greater than <=  Less than or Equal to 

\>=  Greate than or Equal to 

BETWEEN Between a specified range of values 

LIKE    This is used to search for a pattern in value. IN  In a given set of values

**DISTINCT keyword**

The distinct keyword is used with SELECT statement to retrieve unique values from the table. Distinct removes all the duplicate records while retrieving records from any table in the database. Syntax for DISTINCT Keyword

**SELECT** **DISTINCT** **column**-**name** **FROM** **table**-**name**; ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.022.png)Example using DISTINCT Keyword

Consider the following Emp table. As you can see in the table below, there is employee name, along with employee salary and age.

In the table below, multiple employees have the same salary, so we will be using DISTINCT keyword to list down distinct salary amount, that is currently being paid to the employees.

401 Anu 22  5000 ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.038.png)

402 Shane   29  8000 403 Rohan   34  10000 404 Scott   44  10000 ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.039.png)405 Tiger   35  8000

**SELECT** **DISTINCT** salary **FROM** Emp;![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.019.png)

The above query will return only the unique salary from Emp table.

5000 ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.040.png)8000 10000

**AND operator**

Example of AND operator

Consider the following Emp table

401 Anu 22  5000 ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.041.png)

402 Shane   29  8000 403 Rohan   34  12000 404 Scott   44  10000 405 Tiger   35  9000

**SELECT** \* **FROM** Emp **WHERE** salary < 10000 **AND** age > 25![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.022.png)

The above query will return records where salary is less than 10000 and age greater than 25. Hope you get the concept here. We have used the AND operator to specify two conditions with WHERE clause.

402 Shane   29  8000 ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.042.png)405 Tiger   35  9000

AND operator is used to set multiple conditions with the WHERE clause, alongside, SELECT, UPDATE or DELETE SQL queries.

**OR operator**

OR operator is also used to combine multiple conditions with WHERE clause. The only difference between AND and OR is their behaviour.

Example of OR operator

Consider the following Emp table

401 Anu 22  5000 ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.027.png)

402 Shane   29  8000 403 Rohan   34  12000 404 Scott   44  10000 405 Tiger   35  9000

**SELECT** \* **FROM** Emp **WHERE** salary > 10000 **OR** age > 25![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.022.png)

The above query will return records where either salary is greater than 10000 or age is greater than 25. 402 Shane 29 8000 403 Rohan 34 12000 404 Scott 44 10000 405 Tiger 35 9000

**SQL LIKE clause**

LIKE clause is used in the condition in SQL query with the WHERE clause. LIKE clause compares data with an expression using wildcard operators to match pattern given in the condition. Wildcard operators

There are two wildcard operators that are used in LIKE clause.

Percent sign %: represents zero, one or more than one character. ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.010.png)Underscore sign \_: represents only a single character.

Example of LIKE clause

Consider the following Student table. ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.043.png)s\_id    s\_Name  age 

101 Adam    15 

102 Alex    18 

103 Abhi    17

**SELECT** \* **FROM** Student **WHERE** s\_name **LIKE** 'A%';![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.018.png)

The above query will return all records where s\_name starts with character 'A'.

s\_id    s\_Name  age ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.030.png)101 Adam    15 102 Alex    18 

103 Abhi    17 Using \_ and %

**SELECT** \* **FROM** Student **WHERE** s\_name **LIKE** '\_d%';![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.026.png)

The above query will return all records from Student table where s\_name contain 'd' as second character. s\_id s\_Name age 101 Adam 15 Using % only

**SELECT** \* **FROM** Student **WHERE** s\_name **LIKE** '%x';![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.005.png)

The above query will return all records from Student table where s\_name contain 'x' as last character.

s\_id    s\_Name  age ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.042.png)102 Alex    18

**SQL ORDER BY Clause**

Order by clause is used with SELECT statement for arranging retrieved data in sorted order. The Order by clause by default sorts the retrieved data in ascending order. To sort the data in descending order DESC keyword is used with Order by clause. Syntax of Order By

**SELECT** **column**-**list**|\* **FROM** **table**-**name** **ORDER** **BY** **ASC** | **DESC**; ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.019.png)Using default Order by

Consider the following Emp table,

eid name    age salary ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.044.png)401 Anu 22  9000 

402 Shane   29  8000 403 Rohan   34  6000 404 Scott   44  10000 405 Tiger   35  8000

**SELECT** \* **FROM** Emp **ORDER** **BY** salary; ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.005.png)The above query will return the resultant data in **ascending order** of the salary.

eid name    age salary ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.045.png)403 Rohan   34  6000 402 Shane   29  8000 405 Tiger   35  8000 401 Anu 22  9000 

404 Scott   44  10000 Using Order by DESC

Consider the Emp table described above,

**SELECT** \* **FROM** Emp **ORDER** **BY** salary **DESC**;![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.020.png)

The above query will return the resultant data in descending order of the salary.

eid name    age salary ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.046.png)404 Scott   44  10000 401 Anu 22  9000 

405 Tiger   35  8000 402 Shane   29  8000 403 Rohan   34  6000

**Example for sorting by multiple columns**

` `**SELECT** \* **FROM** Customers ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.042.png)

**ORDER** **BY** Country **ASC**, CustomerName **DESC**; 

**SQL GROUP BY Statement**

The GROUP BY statement groups rows that have the same values into summary rows, like "find the number of customers in each country".

The GROUP BY statement is often used with aggregate functions (COUNT, MAX, MIN, SUM, AVG) to group the result-set by one or more columns.

It takes several rows and turns them into one row. Because of this, it has to know what to ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.047.png)do with all the combined rows where there have different values for some 

columns (fields).![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.048.png)

**SELECT** column\_name(s) ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.043.png)**FROM** table\_name 

**WHERE** condition 

**GROUP** **BY** column\_name(s) **ORDER** **BY** column\_name(s); 

**SQL GROUP BY Examples**

The following SQL statement lists the number of customers in each country:

**SELECT** **COUNT**(CustomerID), Country ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.012.png)**FROM** Customers 

**GROUP** **BY** Country;

SQL statement lists the number of customers in each country, sorted high to low:

**SELECT** **COUNT**(CustomerID), Country ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.049.png)**FROM** Customers 

**GROUP** **BY** Country 

**ORDER** **BY** **COUNT**(CustomerID) **DESC**;

**SQL HAVING Clause**

**The HAVING clause was added to SQL because the WHERE keyword could not be used with aggregate functions.**

**HAVING Syntax**

**SELECT** column\_name(s) ![](Aspose.Words.a2b64e81-447e-449a-9b32-0251060414b3.050.png)**FROM** table\_name 

**WHERE** condition 

**GROUP** **BY** column\_name(s) **HAVING** condition 

**ORDER** **BY** column\_name(s); 

**Advanced SQL**

* Agregate functions?
* Joins function

Top interview questions 

* https://artoftesting.com/sql-queries-for-interview#SQL_Query_Interview_Questions_for_Experienced