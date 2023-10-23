-- lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT `title`, SUM(`tv_show_ratings`.`rate`) 'rating' FROM `tv_shows` ts LEFT JOIN `tv_show_ratings` tsr ON tsr.`show_id` = ts.`id` GROUP BY `title` ORDER BY rating DESC;
