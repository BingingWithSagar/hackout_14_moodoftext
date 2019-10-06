from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.journal,name = 'home'),
    path('entry/',views.journalEntry,name = 'entry'),
    path('logout/',views.logout_view),
    path('psych/',views.psych_view),
    path('single/',views.single_view),
    path('result/',views.result_view),
    path('psychentries/',views.psychentries),
    path('journal/',views.journal),
    path('test/',views.test)


]