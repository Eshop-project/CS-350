from django.contrib import admin


from .models import NewUser

#admin.site.unregister(NewUser)
admin.site.register(NewUser)

