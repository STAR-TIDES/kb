'''star_tides.services.databases.mongo.schemas.__init__
'''

# Blatantly taken from
# https://marshmallow.readthedocs.io/en/stable/examples.html#inflection-camel-casing-keys.


def camelcase(s) -> str:
    parts = iter(s.split('_'))
    return next(parts) + ''.join(i.title() for i in parts)
