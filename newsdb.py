#!/usr/bin/env python3

import psycopg2
import datetime


def run_db(query):
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute(query)
    return c.fetchall(), db


def show_top_articles():
    query = """select * from popular order by views desc limit 3;"""
    results, db = run_db(query)
    for result in results:
        article = '"' + result[0].title() + '"'
        views = str(result[1])
        print(article + ' - ' + views + ' views')
    db.close()


def show_top_authors():
    query = """select authors.name, sum(popular.views) as views from articles
            join authors on articles.author = authors.id join popular on
            articles.title = popular.title group by authors.name order by
            views desc
            """
    results, db = run_db(query)
    for result in results:
        author = result[0]
        views = str(result[1])
        print(author + ' - ' + views + ' views')
    db.close()


def show_error():
    query = """select time::date as date, ( (sum(case when status =
            '404 NOT FOUND' then 1 else 0 end) * 100.0) / count(*) ) as error
            from log group by date having ( (sum(case when status =
            '404 NOT FOUND' then 1 else 0 end) * 100.0) / count(*) ) > 1;
            """
    results, db = run_db(query)
    for result in results:
        date = result[0]
        error_percent = str(round(result[1], 1)) + '%'
        print(str(date.strftime('%B %d, %Y')) + ' - ' + error_percent)
    db.close()

print('===============')
print('Top 3 Articles:')
print('===============')
show_top_articles()
print('')

print('====================')
print('Top Article Authors:')
print('====================')
show_top_authors()
print('')

print('=================================')
print('Days With Over 1% Request Errors:')
print('=================================')
show_error()
print('')
