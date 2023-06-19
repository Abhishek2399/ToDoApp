from django import template
from ToDoApp.models import Task, StatusMaster
register = template.Library()


@register.filter
def get_val(obj, key):
    return obj.get(key.lower() if type(key) is str else key, f"Key:'{key}' not found in Dict:{obj}")


@register.filter
def get_status(obj, obj_id):
    stat_name = None
    try:
        stat_name = Task.objects.get(pk = obj_id).status.status_name
    except Exception as e:
        pass
    return stat_name


@register.filter
def get_category(obj, obj_id):
    cat_name = None
    try:
        cat_name = Task.objects.get(pk = obj_id).category.category_name
    except Exception as e:
        pass
    return cat_name
