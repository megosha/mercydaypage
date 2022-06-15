from django import template
from django.core.cache import cache
from indexpage.models import Settings
from string import Formatter

register = template.Library()


def get_settings(params:list):
    params_from_cache = [cache.get(i) for i in params]
    if all(params_from_cache):
        return {p: params_from_cache[idx] for idx, p in enumerate(params)}
    params_from_db = Settings.objects.filter().values(*params).first()
    for index, p in enumerate(params):
        cache.set(p,params_from_db[p])
    return params_from_db

@register.filter()
def str_custom(address_from_db:str):
    params = [p for _,p,_,_ in Formatter().parse(address_from_db) if p]
    if not params:
        return address_from_db
    params_from_db = get_settings(params)
    return address_from_db.format(**params_from_db)
