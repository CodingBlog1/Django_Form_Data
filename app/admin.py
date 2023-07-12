from django.contrib import admin
from app.models import Member
# Register your models here.
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('mid','mname','memail','mnumber')