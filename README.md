# Log Analysis Project

The purpose of this project is to build an internal reporting tool for a newspaper site, that will use information from the database to discover what kind of articles the site's readers like.

The project currently answers the following questions:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Prerequisites

- Python version **version 2.7.12** or _later_
- PostgreSQL **version 9.5.8** or _later_
- Flask **version 0.12.2** or _later_

## Get Started

- Clone the repository on the local machine

```
$ git clone https://github.com/nikitasharma1/Log-Analysis.git
```

- or_ download the _.zip_ file [here](https://github.com/nikitasharma1/Log-Analysis/archive/master.zip)
- Download data [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and extract file **newsdata.sql**
- If using vitual environment to run and connect to database, cd into the corresponding directory and move the project folder and "newsdata.sql" inside this directory
- Create database **news**

```
$ createdb news
```

- Load data from **newsdata.sql** into **news**

```
$ psql -d news -f <path to "newsdata.sql">
```

- Create views from **create_views.sql**

```
$ psql -d news -f <path to "create_views.sql">
```

- To check if database and corresponding views have been created,
    - Enter command line utility by typing ```psql```
    - Type ```\list``` or ```\l``` to view the list of databases
    - Type ```\c news``` to connect to database **news**
    - Type ```\d``` to view list of tables, views and sequences. It should have:
        - 3 Tables: authors, articles, log
        - 3 Sequences: authors_id_seq, articles_id_seq, log_id_seq
        - 2 Views: article_views, daywise_status_log

- Type ```\q``` to exit psql command line utility
- Run script **log_analysis.py**

```
$ python <path to "log_analysis.py">
```

- Connect to server at ```http://localhost:8000``` from the browser

## Acknowledgments

- [Udacity](https://in.udacity.com/course/full-stack-web-developer-nanodegree--nd004/)

## License

This project is licensed under the [MIT](LICENSE.md)  License.
