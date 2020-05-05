from django.contrib import admin
from Booking.models import party,apod,book,p_user,branch,origin,content,price,location
# Register your models here.
admin.site.register(party)
admin.site.register(apod)
admin.site.register(book)
admin.site.register(p_user)
admin.site.register(branch)
admin.site.register(origin)
admin.site.register(content)
admin.site.register(price)
admin.site.register(location)
admin.site.site_header = "Professional Administration"
admin.site.site_title = "Professional Administration"