class DB:
    def __init__(self, db_path="vids.db"):
        pass
    
    def insert_vid(self, vid_data: dict):
        pass

    def get_vid(self, vid_id: str):
        pass

    # aka mark it as dead
    def kill_vid(self, vid_id: str):
        pass

    def insert_search(self, search_data: dict):
        pass

    def get_search(self, search_id: int):
        pass

    # this one's kinda tricky because the same vid id could have come from multiple search terms
    # it could just return a list of search ids associated with that video id
    def get_search_ids_from_vid(self, vid_id: str):
        pass

    def insert_results(self, results_data: dict):
        pass

    # also, if i want to get results, i'd need to get them on a search_id and vid_id
    # but if i get the search ids list, then i can return results that match that list, again in a list of dicts
    def get_results(self, search_id: int, vid_id: str):
        pass

    # nice to haves
    def modify_vid_data(self, data):
        pass

    def delete_vid(self, id):
        pass
