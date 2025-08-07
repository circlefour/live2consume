import random
import datetime

# all of these can be empty / this object does not need to be created to make a search. and even if it is, not all of these options need to be specified. i could optionally have them be null and check for that in main before calling the api

ORDER_OPTIONS = ['viewCount', 'date', 'rating', None]
REGIONS = ['CA', 'US', 'IN', 'JP', None]
LANGUAGES = ['en', 'es', 'fr', None]

class SearchOptionsGenerator:
    def __init__(self, none_p={}):
        self.now = datetime.datetime.now()
        self.none_p = none_p

    def get_rand_time_range(self):
        # FIXME : def don't want end being now. also, don't really want self.now being now. want to pick a time range. maybe i just send it in?
        end = self.now
        start = end - datetime.datetime.now()
        return start.isoformat(), end.isoformat()

    def get_options(self):
        published_after, published_before = self.random_time_range()
        return {
                "order_by": random.choice(ORDER_OPTIONS),
                'region_code': random.choice(REGIONS),
                'relevance_lang': random.choice(LANGUAGES),
                'published_before': published_before,
                'published_after': published_after,
                }

# tryna handle any float value given as probability weight with grace. tryna ensure negative probabilities are treated as penalties. tryna make all values good values
def normalize_weight(p, min_threshold=1e-4):
    penalty = True if p < 0.0 else False
    while abs(p) > 1:
        p /= 10
    p = 0.0 if abs(p) < min_threshold else abs(p)
    return 1 - p if penalty else p

# helper / random chooser
def weighted_random_choice(options, none_p=0.5):
    weights = [none_p] + [(1 - none_p) / len(options)] * len(options)
    return random.choices([None] + options, weights=weights, k=1)
