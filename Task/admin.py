from django.contrib import admin
from Task.models import Trainee,User,sessionDetails,evaluation
from django.contrib.auth.models import Group
from django.views.decorators.csrf import csrf_exempt
# Register your models here.
class TraineeAdmin(admin.ModelAdmin):
    list_display = ['Full_Name','Age','Qualification']

class sessionAdmin(admin.ModelAdmin):
    list_display =  [ 'tid','Date','session1','session2','session3','session4','description' ]
    list_filter = ['tid','Date']
class evaluationAdmin(admin.ModelAdmin):
    list_display =  [ 'Eid','NamingConvertion','validationUse','exceptionUse','functionalityUse','InternetUsage','UIdesign','AdditionalTask','communication','logicalSkill','debug','coding','TaskCompletion']
    list_filter = ['Eid']
    
admin.site.site_header = 'Cookies Administration'
admin.site.register(Trainee,TraineeAdmin)
admin.site.register(sessionDetails,sessionAdmin)
admin.site.register(evaluation,evaluationAdmin)
admin.site.unregister(Group)