#! /usr/bin/env python
# "Database code" for the DB Forum.


from flask import Flask, url_for, request, redirect
import math
import psycopg2

DBNAME = "news"


def get_posts():
    """Return all posts from the 'database', most recent first."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()

    """query to display What are the most popular three articles of all time"""
    sql_query = """select SUBSTR(log.path,10,LENGTH(path)) as art,
                    count(path) as cnt from log  where  path!='/' group by
                    path order by cnt desc limit 3;"""
    c.execute(sql_query)
    output = "The 3 most popular articles of all time are:\n"
    print output
    data = c.fetchall()

    for row in data:
        mylist = []
        mylist.append('"')
        mylist.append(row[0])
        mylist.append('-')
        mylist.append('"')
        mylist.append(str(row[1]))
        mylist.append(' views')
        s = ''.join(mylist)
        print s
        """query to display most popular article authors of all time"""

        sql_query1 = """select name,count(path) as total from log join
                        logs_analysis on logs_analysis.slug=SUBSTR(path,10,
                        LENGTH(path)) GROUP BY logs_analysis.name
                        ORDER BY total DESC;"""
    c.execute(sql_query1)
    print "\nthe most popular article authors of all time are: \n"
    authors = c.fetchall()

    for row in authors:
        mylist = []
        mylist.append('"')
        mylist.append(row[0])
        mylist.append('-')
        mylist.append('"')
        mylist.append(str(row[1]))
        mylist.append(' views')
        s = ''.join(mylist)
        print s

        """query for which days did more than 1% of requests lead to errors?"""

        sql_query2 = """select status.date1,status_404.status_count*100.0 / status.status_count
                        as percentage from status_404 join status on status_404
                        .date1= status.date1 order by percentage
                        desc limit 1;"""
    c.execute(sql_query2)
    print "\nDay with more than 1% of request that lead to an error is on: \n"
    status = c.fetchall()

    for row in status:
        mylist = []
        mylist.append(str(row[0]))
        mylist.append('-')
        mylist.append(str(math.ceil(row[1]*100)/100))
        mylist.append('%')
        s = ''.join(mylist)
        print s
        """closing database connection"""
        db.close()

get_posts()
