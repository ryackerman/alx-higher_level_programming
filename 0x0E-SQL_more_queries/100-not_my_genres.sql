-- uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT `name` FROM `tv_genres` WHERE `name` NOT IN (SELECT `name` FROM `tv_genres` tg LEFT JOIN `tv_show_genres` tsg ON tg.`id`=tsg.`genre_id` LEFT JOIN `tv_shows` ts ON tsg.`show_id`=ts.`id` WHERE ts.`title`='Dexter') GROUP BY `name` ORDER BY `name` ASC;
