-- Lists all shows from hbtn_0d_tvshows that are not categorized under the Comedy genre
SELECT tv_shows.title
FROM tv_shows
WHERE NOT EXISTS (
  -- Subquery to identify shows that are linked to the Comedy genre
  SELECT 1
  FROM tv_show_genres
  JOIN genres ON tv_show_genres.genre_id = genres.id
  WHERE genres.name = 'Comedy'
  AND tv_shows.id = tv_show_genres.show_id
)
ORDER BY tv_shows.title ASC;
