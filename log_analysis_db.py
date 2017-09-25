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
	query = "select title, article_view_count from article_views limit 3;"
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
	query = """select authors.name, sum(article_views.article_view_count)
	as author_view_count from article_views, authors
	where article_views.author=authors.id
	group by authors.id
	order by author_view_count desc;"""
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
	query = """select day, error, total_requests from daywise_status_log
	where error > (0.01 * total_requests)
	order by day;"""
	# Execute query
	c.execute(query)
	# Fetch data
	logs = c.fetchall()
	# Close database connection
	db.close()
	# Return data
	return logs
