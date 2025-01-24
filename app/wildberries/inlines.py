from django.contrib.admin import StackedInline
from .models import User_Request_History


class HistoryInline(StackedInline):
    model=User_Request_History
    extra=0
