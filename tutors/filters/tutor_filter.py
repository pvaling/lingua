import django_filters

from tutors.models import Tutor, Language, Subject


class TutorFilter(django_filters.FilterSet):

    # price = django_filters.NumberFilter()
    price__gte = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price__lte = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    # languages = django_filters.ModelMultipleChoiceFilter()

    languages = django_filters.ModelMultipleChoiceFilter(
        conjoined=True,
        queryset=Language.objects.all()
    )

    subjects = django_filters.ModelMultipleChoiceFilter(
        conjoined=True,
        queryset=Subject.objects.all()
    )

    class Meta:
        model = Tutor
        fields = ['price__gte', 'price__lte', 'languages', 'subjects']
