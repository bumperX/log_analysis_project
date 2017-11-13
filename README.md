# Logs Analysis Project
From Udacity [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)

## Description
Logs analysis is a reporting tool that prints out reports (in plain text) based on the data in database. This reporting tool is a Python program using the `psycopg2` module to connect to the database.

## Questions
Here are the questions the reporting tool should answer.

**1. What are the most popular three articles of all time?**
Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

**2. Who are the most popular article authors of all time?**
That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

**3. On which days did more than 1% of requests lead to errors?**
The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. 

## Installation

**1. Install the virtual machine to run in Python.**
* [Python3](http://initd.org/psycopg/docs/install.html) 
* [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
* [Vagrant](https://www.vagrantup.com)

**2. Download the virtual machine configuration**
You can download and unzip this file: [FSND-Virtual-Machine.zip](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip) This will give you a directory called FSND-Virtual-Machine. It may be located inside your Downloads folder.

## Setup
**1. Start the virtual machine**
Inside the vagrant subdirectory, run the command
```sh
$ vagrant up
```
This will cause Vagrant to download the Linux operating system and install it.
This may take quite a while (many minutes) depending on how fast your Internet connection is.When vagrant up is finished running, you will get your shell prompt back. At this point, you can run
```sh
$ vagrant ssh
```
to log in to your newly installed Linux VM.

**2. Download the data**
Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) here. You will need to unzip this file after downloading it. The file inside is called `newsdata.sql`. Put this file into the `vagrant` directory, which is shared with your virtual machine. To load the data, cd into the `vagrant` directory and connect to your installed database server with the command 
```
$ cd /vagrant
$ psql -d news -f newsdata.sql
```

## To run
**1. Explore the data**
Once you have the data loaded into your database, connect to your database using `psql -d news` and explore the tables using the `\dt` and `\d` table commands and select statements.
* `\dt` — display tables — lists the tables that are available in the database.
* `\d` table — (replace table with the name of a table) — shows the database schema for that particular table.

The database includes three tables:
* The `authors` table includes information about the authors of articles.
* The `articles` table includes the articles themselves.
* The `log` table includes one entry for each time a user has accessed the site.

**2. To run**
Download this repository into the `vagrant` directory and execute this program with the command 
```
$ python log_analysis.py
```
