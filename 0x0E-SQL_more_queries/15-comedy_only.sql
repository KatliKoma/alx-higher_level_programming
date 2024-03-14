-- Retrieves all Comedy shows from the database hbtn_0d_tvshows.
-- Output format for each record:
-- tv_shows.title
-- Organize the output in ascending order by the show title.
-- The name of the database will be provided as a parameter to the MySQL command.
SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN genres ON tv_show_genres.genre_id = genres.id
WHERE genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
