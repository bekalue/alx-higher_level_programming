-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_shows.title, tv_genres.name ASC;
