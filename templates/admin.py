from django.contrib import admin
from app.models import admin_info,test_info,student_info,exams,courses,subject_list,submitted


class adInfo(admin.ModelAdmin):
    fields = ['fname', 'surname','email','lecture_id','title','ad_type']

admin.site.register(admin_info,adInfo)

admin.site.register(student_info)
admin.site.register(test_info)
admin.site.register(submitted)
admin.site.register(exams)
admin.site.register(courses)
admin.site.register(subject_list)
