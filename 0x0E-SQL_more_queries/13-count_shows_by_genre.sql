-- Retrieves all genres from the database hbtn_0d_ and counts how many shows are associated with each genre.
-- Output format for each record:
-- Genre of the TV show - Total number of shows associated with this genre
-- Organize the output in descending order based on the count of shows linked to each genre.
-- The name of the database will be provided as a parameter to the MySQL command.
SELECT genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM genres
JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
GROUP BY genres.name
HAVING COUNT(tv_show_genres.show_id) > 0
ORDER BY COUNT(tv_show_genres.show_id) DESC;
