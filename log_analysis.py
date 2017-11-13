#!/usr/bin/env python3

import psycopg2

DBNAME = "news"


def article_view_count():
    """
    Create view with the most popular articles
    of all time and their view counts
    """
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    view_query = "create view article_view_count as\
    select title, count(ip) from log, articles\
    where log.path like concat('%', articles.slug, '%')\
    and status like '%OK%'\
    group by title\
    order by count(ip) desc"
    c.execute(view_query)
    db.commit()
    db.close()


def top_3_article():
    """Print out the most popular three articles of all time"""
    try:
        article_view_count()
    except:
        pass
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select * from article_view_count limit 3")
    content = c.fetchall()
    print("What are the most popular three articles of all time?")
    for item in content:
        print("%s -- %d views" % (item[0], item[1]))
    print("\n")
    db.close()


def most_popular_author():
    """Print out the most popular article authors of all time"""
    try:
        article_view_count()
    except:
        pass
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    top_authors = "select name, sum(article_view_count.count)\
    from article_view_count, articles, authors\
    where article_view_count.title = articles.title\
    and authors.id = articles.author\
    group by name\
    order by sum desc"
    c.execute(top_authors)
    content = c.fetchall()
    print("Who are the most popular article authors of all time?")
    for item in content:
        print("%s -- %d views" % (item[0], item[1]))
    print("\n")
    db.close()


def date_status_count():
    """
    Create view with date and the respective count of HTTP status codes
    like error, ok and in total
    """
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    view_query = "create view date_status_count as\
    select time::date as date,\
    sum(case when status like '%OK%' then 1 else 0 end) as success,\
    sum(case when status like '%404%' then 1 else 0 end) as fail,\
    count(*) as total\
    from log group by date"
    c.execute(view_query)
    db.commit()
    db.close()


def top_error_date():
    """Print out the date on which over 1% of requests lead to errors"""
    try:
        date_status_count()
    except:
        pass
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    ratio_query = "select date,\
    (100*fail/total::numeric)::numeric(10,2)::text||'% errors' as ratio\
    from date_status_count\
    where fail::numeric/total > 0.01\
    order by ratio desc"
    c.execute(ratio_query)
    content = c.fetchall()
    print("On which days did more than 1% of requests lead to errors?")
    for item in content:
        print("%s -- %s views" % (item[0], item[1]))
    print("\n")
    db.close()


top_3_article()
most_popular_author()
top_error_date()
