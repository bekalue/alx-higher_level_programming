-- select show title and genere id from hbtn_0d_tvshows database
SELECT tv_shows.title, tv_show_generes.genere_id
FROM tv_shows
INNER JOIN tv_show_generes
ON tv_shows.id = tv_show_generes.show_id
ORDER BY tv_shows.tittle, tv_show_generes.genre_id ASC;
