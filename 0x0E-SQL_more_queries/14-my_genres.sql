-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT tg.`name` from `tv_genres` tg JOIN `tv_show_genre` tsg ON tg.`id`=tsg.`genre_id` JOIN `tv_shows` ts ON ts.`id`=tsg.`show_id` WHERE ts.`title`="Dexter" ORDER BY tg.`name`;
