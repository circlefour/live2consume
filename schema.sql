-- pragma foreign_keys = on;

create table vids (
    video_id        text primary key,
    published_at    text,
    title           text,
    description     text,
    channel_title   text,
    channel_id      text,
    alive           integer default 1   -- videos might get deleted later, or privated, but the data might not be useless depending on what i'm doing
);

create table search (
    id              integer primary key autoincrement,
    search_str      text,
    published_before    text,
    published_after text,
    order_by        text,       -- options like viewCount, date, rating
    region_code     text,
    relevance_lang  text,
    misc_opts       text,       -- might store json as a string with any other possible options
    searched_at     text        -- timestamp when api is called ( matters i guess if stuff gets changed or deleted later )
);

create table results (
    search_id       integer,
    video_id        text,
    rank            integer,    -- where it showed up in the search results for the search term
    style_tag       text,       -- what kind of search term generation was i doing that came up with this result? aka what iteration was this?
    primary key (search_id, video_id),
    foreign key (search_id) references search(id) on delete cascade,
    foreign key (video_id) references vids(video_id) on delete cascade
);
