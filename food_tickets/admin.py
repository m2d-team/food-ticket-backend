from django.contrib import admin
from django.shortcuts import render

from .forms import UploadExcelForm
from .models import Student, FoodAccessLog, FoodTicket


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'full_name', 'date_of_birth', 'grade', 'secret_code', 'telegram_account', 'has_food_right',
    ]
    search_fields = ('full_name', 'telegram_account')
    sortable_by = ('has_food_right',)

    def upload_excel(self, request, queryset):
        # TODO: add docstring
        """"""
        if request.POST:
            # return HttpResponseRedirect(request.get_full_path())
            pass

        else:
            form = UploadExcelForm()
            return render(
                request, "food_tickets/upload_excel.html", {'form': form, 'title': u'Broadcast message'}
            )



@admin.register(FoodTicket)
class FoodTicketAdmin(admin.ModelAdmin):
    list_display = [
        'owner', 'ticket_sponsor', 'date_usable_at', 'type', 'time_created_at'
    ]
    search_fields = ('owner', 'ticket_sponsor')
    sortable_by = ('ticket_sponsor', 'owner', 'date_usable_at', 'type', 'time_created_at')


@admin.register(FoodAccessLog)
class FoodAccessLogAdmin(admin.ModelAdmin):
    list_display = [
        'datetime_created', 'eater', 'food_ticket',
    ]
    sortable_by = ('time',)
    search_fields = ('food_ticket',)
