
================================
ZenPacks.community.ZenODBC
================================

About
=====

This Functionality ZenPack provides a new **ODBC** data source, and allows you 
to access a number of different RDBMSes.

Requirements
============

Zenoss
------

You must first have, or install, Zenoss 2.5.2 or later. This ZenPack was tested 
against Zenoss 2.5.2 and Zenoss 3.2. You can download the free Core version of 
Zenoss from http://community.zenoss.org/community/download

ZenPacks
--------

You must first install `SQLDataSource ZenPack <http://community.zenoss.org/docs/DOC-5913>`_.


Installation
============

Normal Installation (packaged egg)
----------------------------------

Download the `ZenODBC ZenPack <http://community.zenoss.org/docs/DOC-3440>`_. 
Copy this file to your Zenoss server and run the following commands as the zenoss 
user.

    ::

        zenpack --install ZenPacks.community.ZenODBC-4.0.egg
        zenoss restart

Developer Installation (link mode)
----------------------------------

If you wish to further develop and possibly contribute back to the ZenODBC 
ZenPack you should clone the git `repository <https://github.com/epuzanov/ZenPacks.community.ZenODBC>`_, 
then install the ZenPack in developer mode using the following commands.

    ::

        git clone git://github.com/epuzanov/ZenPacks.community.ZenODBC.git
        zenpack --link --install ZenPacks.community.ZenODBC
        zenoss restart


Usage
=====

Connection String
-----------------
ODBC connection string format

Example:

    ::

        driver={MySQL};server=localhost;database=somedb;uid=user;pwd=pwd

Columns name to Data Points name mapping
----------------------------------------
use SQL Aliases Syntax for columns names to set the same name as Data Poins 
names.

Example query which returned values for **dataSize**, **indexSize** and 
**sizeUsed** Data Points:

    ::

        SELECT sum(data_length) as dataSize, sum(index_length) as indexSize, sum( data_length + index_length ) as sizeUsed FROM TABLES WHERE table_schema='mysql' GROUP BY table_schema

Queue sorting (join multiple queries in single query)
-----------------------------------------------------
WHERE statement will be removed from SQL Query and used as key by results parsing.

Example:
We have 3 databases ('events', 'information_schema' and 'mysql') and we need 
collect data and idx size of every database.

DataSource Query for '**events**':

    ::

        SELECT sum(data_length) as dataSize, sum(index_length) as indexSize, sum( data_length + index_length ) as sizeUsed FROM TABLES WHERE table_schema='events' GROUP BY table_schema

DataSource Query for '**mysql**':

    ::

         SELECT sum(data_length) as dataSize, sum(index_length) as indexSize, sum( data_length + index_length ) as sizeUsed FROM TABLES WHERE table_schema='mysql' GROUP BY table_schema

DataSource Query for '**information_schema**':

    ::

         SELECT sum(data_length) as dataSize, sum(index_length) as indexSize, sum( data_length + index_length ) as sizeUsed FROM TABLES WHERE table_schema=' information_schema' GROUP BY table_schema

As result 3 queries will be replaced by single query:

    ::

        SELECT sum(data_length) as dataSize, sum(index_length) as indexSize, sum( data_length + index_length ) as sizeUsed,table_schema FROM TABLES GROUP BY table_schema

Data Point Aliases formulas
---------------------------
before be saved in RRD, values will be evaluated by **REVERSED** alias.formula

- supported operations: **+, -, *, /**
- tales variables: now, here

Example:

alias.formula = **"100,/,1,-"** replaced by **REVERSED** formula **"1,+,100,*"**

Why alias.formula must be reversed?

- raw data: **100** -> **"100,100,/,1,-"** -> RRD: **0** -> **"0,100,/,1,-"** ->Report: **-1** - FALSE!
- raw data: **100** -> **"100,1,+,100,*"** -> RRD: **10100** -> **"10100,100,/,1,-"** ->Report: **100** - TRUE!

Dictionary as Data Point Aliases formula
----------------------------------------
before be saved in RRD, values will be evaluated

Example:

    ::

        "Unknown":0,"Other":1,"OK":2,"Warning":3,"Error":4

Agregation functions support for multiline results
--------------------------------------------------
Agregation functions **avg**, **count**, **sum**, **min**, **max**, **first**, 
**last** are supported for data points with multiline result. If query returned 
multiple values for single Data Point, than zenperfsql datemon used **avg** 
function by default. If another function must be used, than add **_function** 
to the data points name.

Example:

- **dataSize_max** - will write in to RRD file maximal dataSize value
