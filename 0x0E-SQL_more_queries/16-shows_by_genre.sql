/*
List all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
If a show doesn’t have a genre, display NULL in the genre column.
*/
SELECT TV_SHOWS.TITLE, IFNULL(TV_GENRES.NAME, 'NULL') AS NAME
FROM TV_SHOWS
LEFT JOIN TV_SHOW_GENRES ON TV_SHOWS.ID = TV_SHOW_GENRES.TV_SHOW_ID
LEFT JOIN TV_GENRES ON TV_SHOW_GENRES.TV_GENRE_ID = TV_GENRES.ID
ORDER BY TV_SHOWS.TITLE ASC, TV_GENRES.NAME ASC;
