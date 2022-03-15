import factory
from takehome.models import Widget


class WidgetFactory(factory.DjangoModelFactory):
    class Meta(object):
        model = Widget

    name = factory.Faker("name")