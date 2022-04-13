from django.contrib import admin


from . models import *

# admin.site.register(NoteForm)
class NotesFormAdmin(admin.ModelAdmin):
    list_display=('id','subject','title','description','date','note','file')
admin.site.register(NoteForm,NotesFormAdmin)


class VideosFormAdmin(admin.ModelAdmin):
    list_display=('id' ,'subject','title','description','date','video','file','link1')
admin.site.register(VideoForm,VideosFormAdmin)


# admin.site.register(edit_userProfile)
class user_editAdmin(admin.ModelAdmin):
    list_display=('id' ,'user_name')
admin.site.register(user_edit,user_editAdmin)

