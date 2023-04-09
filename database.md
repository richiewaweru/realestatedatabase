# Real Estate Head Office
## Overview

The database application implement a database for a real estate company.It has the following components:<br>
1. Sellers Table
```
Record the relevant sellers detail such as sellerid,name,email and  number.
```
2. Houses Table
```
Records relevant houses details.
```
3. Sales table

```
Records relevant details pertaining sales.
```
4. Agents table

```
Records relevant details pertaining agents.
```


5. Offices table
```
Records relevant details pertaining offices.
```
6. Agentoffices table

```
Records relevant details pertaining agents and their office allocation.Each agent is assigned to one office which they may share with other agents.
```


### Execution (Python)

The following are the commands for running my files.

These are the recommended commands for macOS:
```bash
python -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python create.py
python insert_data.py
python query_data.py

```

Recommended commands for Windows:
```cmd
python -m venv venv
venv\Scripts\activate.bat
pip3 install -r requirements.txt
python create.py
python insert_data.py
python query_data.py
```

#### Execution for testing

These are the recommended commands for macOS:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python tests.py
```

Recommended commands for Windows:
```cmd
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
python tests.py
```
<hr>

## data normalization, indices, and transactions.<br>

I have appled data normalization as follows:

First Normal Form (1NF):<br>
Every table in a database should has a primary key and that each column in the table contains atomic values.

Second Normal Form (2NF):<br>

The columns in my tables are dependent the entire primary key.

Third Normal Form (3NF):<br>
All my columns in my tables are dependent only on the primary key, and not on other columns thus no transitive dependency.

### Indices
I have created indexes by setting the Index option=True for columns that are have been used most during the queries for faster querying.

### Transactions

I have used SQLAlchemy's Session object to create tables,insert data into the tables using session.add and session.commit to complete the transactions.This ensures that the transactions are completed.

## AI use
I have used Chatgpt to populate the test data for me and leads on how to use the faker library.