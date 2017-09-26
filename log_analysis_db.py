#!/usr/bin/env python3

# Import modules
import psycopg2


def connect(database):
    """Connect to database,
    return connection and cursor objects"""

    try:
        # Connect to database
        db = psycopg2.connect(database="%s" % database)
        # Create cursor object
        c = db.cursor()
        # Return connection and database objects
        return db, c
    except psycopg2.Error as e:
        print("Unable to connect to database", database)
        print(e)


def exceute_query(query, database):
    """Execute sql queries"""

    db, c = connect(database)
    # Execute query
    c.execute(query)
    # Fetch data
    logs = c.fetchall()
    # Close database connection
    db.close()
    # Return data
    return logs


def top3_articles(database):
    """Find the most popular three articles of all time"""

    # Create query
    query = "SELECT title, article_view_count FROM article_views LIMIT 3;"
    try:
        return exceute_query(query, database)
    except (Exception, psycopg2.DatabaseError) as e:
        print("Unable execute query", query)
        print(e)


def top_authors(database):
    """Find the most popular article authors of all time"""

    # Create query
    query = """SELECT authors.name,
    SUM(article_views.article_view_count) AS author_view_count
    FROM article_views, authors
    WHERE article_views.author=authors.id
    GROUP BY authors.id
    ORDER BY author_view_count DESC;"""
    try:
        return exceute_query(query, database)
    except (Exception, psycopg2.DatabaseError) as e:
        print("Unable execute query", query)
        print(e)


def error_gt_1percent(database):
    """Find days On which more than 1% of requests lead to errors"""

    # Create query
    query = """SELECT day, error, total_requests,
    (CAST(error AS float)/CAST(total_requests AS float)) * 100
    AS error_percentage
    FROM daywise_status_log
    WHERE error > (0.01 * total_requests)
    ORDER BY day;"""
    try:
        return exceute_query(query, database)
    except (Exception, psycopg2.DatabaseError) as e:
        print("Unable execute query", query)
        print(e)
