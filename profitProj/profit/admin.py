from django.contrib import admin
from profit.models import Category,SubCat,Goal,FitUser,Activity,WeightLog,Suggestions,Session,SessionActivity

class SearchActivity(admin.ModelAdmin):
    search_fields = ['user__name','subcat__name']

class SearchWeightLog(admin.ModelAdmin):
    search_fields = ['user__name']


admin.site.register(Category)
admin.site.register(SubCat)
admin.site.register(Goal)
admin.site.register(FitUser)
admin.site.register(Activity,SearchActivity)
admin.site.register(WeightLog,SearchWeightLog)
admin.site.register(Suggestions)
admin.site.register(Session)
admin.site.register(SessionActivity)