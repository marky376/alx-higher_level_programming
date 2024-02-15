-- Import the database dump from hbtn_0d_tvshows

SELECT genre AS genre,
       COUNT(tv_shows.id) AS number_of_shows
FROM genres
JOIN tv_shows_genres ON genres.id = tv_shows_genres.genre_id
JOIN tv_shows ON tv_shows.id = tv_shows_genres.tv_show_id
GROUP BY genre
ORDER BY number_of_shows DESC;
