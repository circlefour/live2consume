import random
import datetime
from dateutil.relativedelta import relativedelta

# all of these can be empty / this object does not need to be created to make a search. and even if it is, not all of these options need to be specified. i could optionally have them be null and check for that in main before calling the api

ORDER_OPTIONS = ['viewCount', 'date', 'rating']
REGIONS = ['CA', 'US', 'IN', 'JP']
LANGUAGES = ['en', 'es', 'fr']

MIN_DATE = datetime.datetime(2005, 4, 23, 0, 0, 0, tzinfo=datetime.timezone.utc)
MAX_DATE = datetime.datetime.now(datetime.timezone.utc)

MIN_BEFORE = MIN_DATE + relativedelta(years=1)

# FIXME i also want to be able to choose which specific options i want. don't i? nah i personally don't, i wonder if i will in the future, but i guess that's a future problem then.
class SearchOptionsGenerator:
    # none probability is going to be a dict that contains the probability of each option picked being None or not
    # right now i'm not going to include the none probability piece, i'm just going to let it choose a random choice, including None in those choices
    def __init__(self, none_p={}):
        self.publishedBefore = None
        self.publishedAfter = None

    def get_rand_date_range(self, max_date=MAX_DATE, min_date=MIN_BEFORE):
        # TODO: sanitize input (make sure timezone is correct, and format is valid, etc)
        delta_seconds = int((max_date - min_date).total_seconds())
        rand_addition = random.randint(0, delta_seconds)

        published_before = max_date - relativedelta(seconds=rand_addition)

        # getting a random publishedAfter
        delta_seconds = int((published_before - relativedelta(days=1) - min_date).total_seconds())
        rand_addition = random.randint(0, delta_seconds)

        published_after = published_before + relativedelta(seconds=rand_addition)

        return published_after, published_before

    # FIXME published before and published after could also be None too, depending on if it should even be used as an option or not
    def get_options(self):
        # reminder : right now i'm not going to include the none probability piece, i'm just going to let it choose a random choice, including None in those choices
        published_after, published_before = self.get_rand_date_range()
        return {
                "order_by": random.choice([None] + ORDER_OPTIONS),
                'region_code': random.choice([None] + REGIONS),
                'relevance_lang': random.choice([None] + LANGUAGES),
                'published_before': random.choice([None, published_before.isoformat()]),
                'published_after': published_after.isoformat(), # in main, only check if before is none to determine if i'm going to actually input date (for now)
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
