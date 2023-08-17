-- lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT `title` FROM `tv_shows` ts LEFT JOIN `tv_show_genres` tsg ON ts.`id`=tsg.`show_id` LEFT JOIN `tv_genres` tg ON tsg.`genre_id`=tg.`id` WHERE tg.`name`='Comedy' GROUP BY `title` ORDER BY `title` ASC;
