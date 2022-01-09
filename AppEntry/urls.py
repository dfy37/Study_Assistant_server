from django.urls import path
from AppEntry import entry

urlpatterns = [
    path('entrysearch', entry.entrySearch),
    path('entrydetail', entry.entryDetail),
    path('addentry', entry.addEntry),
    path('editentry', entry.editEntry),
    path('getentryid', entry.getEntryId),
    path('updateentry', entry.updateEntry),
    path('entrylatexparser', entry.entryLatexParser),
]