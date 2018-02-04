# cp.py

from datetime import datetime


def my_cp(request):
    ctx = {
        "actual_date": datetime.now()
    }
    return ctx
