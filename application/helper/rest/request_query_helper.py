import re

def model_to_dict(model_obj, exclude_column_names=None, extra_fields=None):

    d = {}

    for column in model_obj.__table__.columns:
        if exclude_column_names is not None \
                and column.name in exclude_column_names:
            continue
        d[to_camelcase(column.name)] = getattr(model_obj, column.name)

    if extra_fields is not None:
        d.update(extra_fields)

    return d

def to_camelcase(s):
    return re.sub(r'(?!^)_([a-zA-Z])', lambda m: m.group(1).upper(), s)


def to_snakecase(s):
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s).lower()

def model_to_dict_params(model_obj, *args):
    d = {}
    model_dict = model_to_dict(model_obj)
    for arg in args:
        if model_dict[arg] is not None:
            d[arg] = model_dict[arg]
    return d


