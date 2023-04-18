from django.contrib import admin


from.models import Booking, Departments, Doctors,Contact

# Register your models here.


admin.site.register(Departments)
admin.site.register(Doctors)


class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'p_name', 'p_phone', 'p_email', 'doc_name', 'booking_date', 'booked_on')

admin.site.register(Booking,BookingAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','f_name','l_name', 'email','phone','remark')

admin.site.register(Contact,ContactAdmin)