from app.google_search import GoogleSearch
from assertions.assertion import Assertion


def test_google_search():
    query = 'toyota'
    google_search_result = GoogleSearch.get(query)
    Assertion.result_contains(google_search_result, query)
