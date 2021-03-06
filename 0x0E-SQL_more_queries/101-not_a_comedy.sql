-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 100-not_my_genres.sql)
-- Write a script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use a maximum of two SELECT statement
-- The database name will be passed as an argument of the mysql command.
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.title NOT IN
      (SELECT a.title
      FROM tv_shows AS a
      JOIN tv_show_genres AS b
      ON a.id = b.show_id
      JOIN tv_genres AS c
      ON b.genre_id = c.id
      WHERE c.name = 'Comedy')
ORDER BY tv_shows.title ASC;
