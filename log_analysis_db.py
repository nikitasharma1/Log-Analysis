# Import modules
import psycopg2

# Create variable to store database name
DBNAME = "news"


# Q1. What are the most popular three articles of all time?
# i.e. Which articles have been accessed the most?
def top3_articles():
    # Connect to database
    db = psycopg2.connect(database=DBNAME)
    # Create cursor object
    c = db.cursor()
    # Create query
    query = "SELECT title, article_view_count FROM article_views LIMIT 3;"
    # Execute query
    c.execute(query)
    # Fetch data
    logs = c.fetchall()
    # Close database connection
    db.close()
    # Return data
    return logs


# Q2. Who are the most popular article authors of all time?
# i.e. When you sum up all of the articles each author has written,
# which authors get the most page views?
def top_authors():
    # Connect to database
    db = psycopg2.connect(database=DBNAME)
    # Create cursor object
    c = db.cursor()
    # Create query
    query = """SELECT authors.name,
    SUM(article_views.article_view_count) AS author_view_count
    FROM article_views, authors
    WHERE article_views.author=authors.id
    GROUP BY authors.id
    ORDER BY author_view_count DESC;"""
    # Execute query
    c.execute(query)
    # Fetch data
    logs = c.fetchall()
    # Close database connection
    db.close()
    # Return data
    return logs


# Q3. On which days did more than 1% of requests lead to errors?
def error_gt_1percent():
    # Connect to database
    db = psycopg2.connect(database=DBNAME)
    # Create cursor object
    c = db.cursor()
    # Create query
    query = """SELECT day, error, total_requests
    FROM daywise_status_log
    WHERE error > (0.01 * total_requests)
    ORDER BY day;"""
    # Execute query
    c.execute(query)
    # Fetch data
    logs = c.fetchall()
    # Close database connection
    db.close()
    # Return data
    return logs
