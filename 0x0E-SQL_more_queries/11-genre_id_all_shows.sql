-- lists all shows contained in the database hbtn_0d_tvshows.
select ts.`title`, tsg.`genre_id` from `tv_shows` ts LEFT JOIN `tv_show_genres` tsg ON ts.`id`=tsg.`show_id` order by ts.`title`, tsg.`genre_id`;
