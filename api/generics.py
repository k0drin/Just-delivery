from rest_framework import generics


class FilterListAPIView(generics.ListAPIView):
    model = None
    filter_field = None
    serializer_class = None

    def get_queryset(self):
        if (
            self.model is None
            or self.serializer_class is None
            or self.filter_field is None
        ):
            raise ValueError(
                "Ensure 'model', 'serializer_class', and 'filter_field' are set."
            )

        filter_value = self.kwargs.get(self.filter_field)
        if filter_value is not None:
            return self.model.objects.filter(**{self.filter_field: filter_value})
        return self.model.objects.all()


__all__ = ["FilterListAPIView"]
