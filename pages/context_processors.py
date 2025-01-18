import yaml
from django.urls import reverse

def page_name_constructor(loader, node):
    name = loader.construct_scalar(node)
    print(name)
    return reverse(name)

yaml.add_constructor('!page_name', page_name_constructor)

def common_context(request):
    with open('i18n/en.yaml', 'r') as file:
        ctx = yaml.safe_load(file)
    return ctx