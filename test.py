from search_string import SearchStringGenerator
from search_options import SearchOptionsGenerator

def test_normalize_weight():
    return

ssg = SearchStringGenerator(['a','b','c','deadbeef'])
print(ssg.get_search_string())

opts = SearchOptionsGenerator()
print(opts.get_options())
