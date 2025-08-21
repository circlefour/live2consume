import sqlite3

class DB:
    def __init__(self, db_path="vids.db"):
        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor()
    
    def insert_vids(self, vids_data: list[dict], vid_keys=["video_id", "published_at", "title", "description", "channel_title", "channel_id"]):
        clean_vids = [
                {k: vid[k] for k in vid_keys}
                for vid in vids_data
                ]
        self.cur.executemany(
            "insert or ignore into vids (video_id, published_at, title, description, channel_title, channel_id) "
            "values (:video_id, :published_at, :title, :description, :channel_title, :channel_id)",
            clean_vids
        )
        self.conn.commit()

    def get_vid(self, vid_id: str):
        self.cur.execute("select * from vids where video_id = ?", (vid_id,))
        row = self.cur.fetchone()

        if row:
            cols = [col[0] for col in self.cur.description] # gets the names of the db columns
            return dict(zip(cols, row))

        return row # which should be None if it gets here

    # aka mark it as dead
    def kill_vid(self, vid_id: str):
        pass

    def insert_search(self, search_data: dict, keys=["search_str", "published_after", "published_before", "order_by", "region_code", "relevance_lang", "misc_opts", "searched_at"]):
        clean_search = {k: search_data.get(k) for k in keys}

        self.cur.execute("insert or ignore into search (search_str, published_after, published_before, order_by, region_code, relevance_lang, misc_opts, searched_at) values (:search_str, :published_after, :published_before, :order_by, :region_code, :relevance_lang, :misc_opts, :searched_at)", clean_search)
        self.conn.commit()

    def get_search(self, search_id: int):
        pass

    # this one's kinda tricky because the same vid id could have come from multiple search terms
    # it could just return a list of search ids associated with that video id
    def get_search_ids_from_vid(self, vid_id: str):
        pass

    def insert_results(self, results_data: list[dict], keys=["search_id", "video_id", "rank", "style_tag"]):
        # clean each dict to only the keys we care about
        clean_results = [
            {k: res.get(k) for k in keys}
            for res in results_data
        ]

        self.cur.executemany(
            """
            insert or ignore into results (search_id, video_id, rank, style_tag)
            values (:search_id, :video_id, :rank, :style_tag)
            """,
            clean_results
        )
        self.conn.commit()

    # also, if i want to get results, i'd need to get them on a search_id and vid_id
    # but if i get the search ids list, then i can return results that match that list, again in a list of dicts
    def get_results(self, search_id: int, vid_id: str):
        pass

    def close(self):
        self.conn.close()

    # nice to haves
    def modify_vid_data(self, data):
        pass

    def delete_vid(self, id):
        pass
