from django.contrib import admin

# Register your models here.
from .models import Post

admin.site.register(Post)

from .models import kid

admin.site.register(kid)


from .models import men

admin.site.register(men)

from .models import women

admin.site.register(women)