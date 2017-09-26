#!/usr/bin/env python3

# Import modules
import psycopg2

# Create variable to store database name
DBNAME = "news"


def exceute_query(query):
    """Method to execute sql queries"""

    # Connect to database
    db = psycopg2.connect(database=DBNAME)
    # Create cursor object
    c = db.cursor()
    # Execute query
    c.execute(query)
    # Fetch data
    logs = c.fetchall()
    # Close database connection
    db.close()
    # Return data
    return logs


def top3_articles():
    """To find the most popular three articles of all time"""

    # Create query
    query = "SELECT title, article_view_count FROM article_views LIMIT 3;"
    return exceute_query(query)


def top_authors():
    """To find the most popular article authors of all time"""

    # Create query
    query = """SELECT authors.name,
    SUM(article_views.article_view_count) AS author_view_count
    FROM article_views, authors
    WHERE article_views.author=authors.id
    GROUP BY authors.id
    ORDER BY author_view_count DESC;"""
    return exceute_query(query)


def error_gt_1percent():
    """To find days On which more than 1% of requests lead to errors"""

    # Create query
    query = """SELECT day, error, total_requests
    FROM daywise_status_log
    WHERE error > (0.01 * total_requests)
    ORDER BY day;"""
    return exceute_query(query)
