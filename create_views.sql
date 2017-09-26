CREATE VIEW article_views AS
SELECT articles.author, articles.id, articles.title, COUNT(*) AS article_view_count
FROM articles, log
WHERE log.path='/article/'||articles.slug
GROUP BY articles.id
ORDER BY article_view_count DESC;

CREATE VIEW daywise_status_log AS
SELECT time::timestamp::date AS day,
SUM(CASE WHEN status='404 NOT FOUND' THEN 1 ELSE 0 END) AS error,
SUM(1) AS total_requests
FROM log
GROUP BY day;