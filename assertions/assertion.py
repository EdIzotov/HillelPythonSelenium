class Assertion:
    @staticmethod
    def result_contains(data, query):
        for result in data:
            assert query in result.text.lower()
