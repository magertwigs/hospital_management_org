from django.contrib import admin
from hospitalapp.models import Users,Product,Member,Contact,ImageModel

# Register your models here.
admin.site.register(Users)
admin.site.register(Product)
admin.site.register(Member)
admin.site.register(Contact)
admin.site.register(ImageModel)
