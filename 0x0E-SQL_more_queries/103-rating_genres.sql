-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT `name`, SUM(`tv_show_ratings`.`rate`) 'rating' FROM `tv_genres` tg INNER JOIN `tv_show_genres` tsg ON tg.`id` = tsg.`genre_id` INNER JOIN `tv_show_ratings` tsr ON tsg.`show_id` = tsr.`show_id` GROUP BY `name` ORDER BY rating DESC;
