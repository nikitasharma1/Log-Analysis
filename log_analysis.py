#!/usr/bin/env python3

# Import Modules
from flask import Flask, url_for, render_template
from log_analysis_db import top3_articles, top_authors, error_gt_1percent

# Create Flask object
app = Flask(__name__)

# Create variable to store database name
DBNAME = "news"


# Bind url "host:port/" to function "main"
@app.route("/", methods=["GET"])
def main(database=DBNAME):
    """Insert data into template,
    Render template"""

    # Get data
    # (i.e. top 3 articles, top authors and
    # day with error requests > one percent)
    # returned by methods in "log_analysis_db.py"
    article_logs = top3_articles(database)
    author_logs = top_authors(database)
    error_logs = error_gt_1percent(database)

    # render template "log_analysis.html"
    # inserted with fetched data
    return render_template("log_analysis.html",
                           article_logs=article_logs,
                           author_logs=author_logs,
                           error_logs=error_logs)


# If run as script (i.e. via interpreter),
if __name__ == "__main__":
    # Run server at port 8000
    app.run(host='0.0.0.0', port=8000)
