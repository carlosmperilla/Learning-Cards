from rest_framework import filters

class ByAttrFilterBackend(filters.BaseFilterBackend):
    """
    Abstract class by attribute filters.
    """
    class Meta:
        abstract = True

    attrs = []

    def filter_queryset(self, request, queryset, view):
        """
            It iterates over the attributes and filters according to them exactly.
        """

        for attr in self.attrs:
            attr_value = request.query_params.get(attr)
            if attr_value:
                queryset = queryset.filter(**{attr : attr_value})
        return queryset

class ByRangeFilterBackend(filters.BaseFilterBackend):
    """
        Abstract class by range filters.
    """

    class Meta:
        abstract = True
    
    attr = ""
    bottom_limit = 0
    top_limit = 100
    
    def filter_queryset(self, request, queryset, view):
        """
            Filter by range, according to upper and lower limits.
        """

        min_value = request.query_params.get('min_' + self.attr)
        max_value = request.query_params.get('max_' + self.attr)
        if min_value or max_value:
            if min_value is None:
                min_value = self.bottom_limit
            if max_value is None:
                max_value = self.top_limit
            queryset = queryset.filter(**{self.attr + '__range': [min_value, max_value]})
        return queryset
