# Log Analysis Project

To build an internal reporting tool for a newspaper site, that will use information from the database to discover what kind of articles the site's readers like.

## Prerequisites

- Python version **version 2.7.12** or _later_
- PostgreSQL **version 9.5.8** or _later_
- Flask **version 0.12.2** or _later_

## Get Started

- Clone the repository on the local machine

```
$ git clone https://github.com/nikitasharma1/Log-Analysis.git
```

- or_ download the _.zip_ file [here]()
- Download data [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and extract file "newsdata.sql"
- If using vitual environment to run and connect to database, cd into the corresponding directory and move the project folder and "newsdata.sql" i.e. inside this directory
- Run following command to load database

```
$ psql -d news -f <path to "newsdata.sql">
```

- Run following command to connect (if not already) to database **news** (which we have just created)

```
$ psql -d news
```

- Create views by executing the following queries

```
CREATE VIEW article_views AS
SELECT articles.author, articles.id, articles.title, COUNT(*) AS article_view_count
FROM articles, log
WHERE log.path LIKE '%'||articles.slug
GROUP BY articles.id
ORDER BY article_view_count DESC;
```

```
CREATE VIEW daywise_status_log AS
SELECT time::timestamp::date AS day,
SUM(CASE WHEN status='404 NOT FOUND' THEN 1 ELSE 0 END) AS error,
SUM(1) AS total_requests
FROM log
GROUP BY day;
```

- Type ```\q``` and press _Enter_ to exit psql command line utility

- Run script **log_analysis.py**

```
$ python <path to "log_analysis.py">
```

- Connect to server at ```http://localhost:8000``` from the browser

## Acknowledgments

- [Udacity](https://in.udacity.com/course/full-stack-web-developer-nanodegree--nd004/)

## License

This project is licensed under the [MIT](LICENSE.md)  License.
