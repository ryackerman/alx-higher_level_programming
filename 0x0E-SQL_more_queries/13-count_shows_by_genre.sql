-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tg.`name` genre, COUNT(*) number_of_shows FROM `tv_genres` tg JOIN `tv_show_genres` tsg ON tg.`id`=tsg.`genre_id` GROUP BY tg.`name` ORDER BY number_of_shows DESC;
