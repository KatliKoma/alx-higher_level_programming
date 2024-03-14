-- Retrieves all genres associated with the show Dexter.
-- Output format for each record:
-- tv_genres.name
-- Organize the output in ascending order by the genre name.
-- The name of the database will be provided as a parameter to the MySQL command.
SELECT genres.name
FROM genres
JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter'
ORDER BY genres.name ASC;
