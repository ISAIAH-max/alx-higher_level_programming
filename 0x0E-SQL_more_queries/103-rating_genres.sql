-- Import the database dump from hbtn_0d_tvshows_rate to your MySQL server: download (same as 102-rating_shows.sql)
-- Write a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_genres.name - rating sum
-- Results must be sorted in descending order by their rating
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command.
SELECT a.name, SUM(c.rate) AS rating
FROM tv_genres AS a
JOIN tv_show_genres AS b
ON a.id = b.genre_id
JOIN tv_show_ratings AS c
ON b.show_id = c.show_id
GROUP BY a.name
ORDER BY rating DESC;
