-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tg.`name`, COUNT(*) nOfShows FROM `tv_genres` tg JOIN `tv_show_genres` tsg ON tg.`id`=tsg.`genre.id` GROUP BY tg.`name` ORDER BY nOfShows DESC;
