from import_export import resources
from .models import Teacher

class PersonResource(resources.ModelResource):
    class Meta:
        model = Teacher