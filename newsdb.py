import psycopg2
import datetime

def connect_to_db():
    db = psycopg2.connect(database="news")
    c = db.cursor()
    return db, c

def show_top_articles():
    db, c = connect_to_db()
    query = """create or replace view popular as select articles.title,
            count(log.path) as views from articles join log
            on log.path like '%'||articles.slug group by
            articles.title order by views desc;
            select * from popular order by views desc
            limit 3;
            """
    c.execute(query)
    results = c.fetchall()
    for result in results:
        article = '"' + result[0].title() + '"'
        views = str(result[1]) 
        print(article + ' - ' + views + ' views')

def show_top_authors():
    db, c = connect_to_db()
    query = """select authors.name, sum(popular.views) as views from
               articles join authors on articles.author = authors.id
               join popular on articles.title = popular.title
               group by authors.name order by views desc
            """
    c.execute(query)
    results = c.fetchall()
    for result in results:
        author = result[0]
        views = str(result[1])
        print(author + ' - ' + views + ' views')

def show_error():
    db, c = connect_to_db()
    query = """select to_char(a.time, 'YYYY-MM-DD') as date,
            ( (count(b.status) * 100.0) / (count(a.status)) ) as error
            from log as a left join log as b on a.id = b.id and
            b.status like '404%' group by date having
            ( (count(b.status) * 100.0) / (count(a.status)) ) > 1;
            """
    c.execute(query)
    results = c.fetchall()
    for result in results:
        date = datetime.datetime.strptime(result[0], '%Y-%m-%d')
        error_percent = str(round(result[1], 1)) + '%'
        print(str(date.strftime('%B %d, %Y')) + ' - ' + error_percent)


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
print('Days With Over 1% Reqeust Errors:')
print('=================================')
show_error()
print('')


