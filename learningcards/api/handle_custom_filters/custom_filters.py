from .abstract_custom_filters import (
                                        ByAttrFilterBackend,
                                        ByRangeFilterBackend
                                     )


class ByKitAttrFilterBackend(ByAttrFilterBackend):
    """
    Filter by kit attributes.
    """

    attrs = ['name', 'foreign_language', 'native_language', 'successful']


class BySuccessfulRangeFilterBackend(ByRangeFilterBackend):
    """
    Filter by successful range.
    """

    attr = "successful"


class ByCardAttrFilterBackend(ByAttrFilterBackend):
    """
    Filter by card attributes.
    """

    attrs = ['foreign_word', 'native_word', 'hits', 'mistakes', 'success']


class ByHitsRangeFilterBackend(ByRangeFilterBackend):
    """
    Filter by hits range.
    """

    attr = "hits"
    top_limit = 99999999


class ByMistakesRangeFilterBackend(ByRangeFilterBackend):
    """
    Filter by mistakes range.
    """

    attr = "mistakes"
    top_limit = 99999999


class BySuccessRangeFilterBackend(ByRangeFilterBackend):
    """
    Filter by success range.
    """

    attr = "success"