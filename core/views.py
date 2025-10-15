# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import matplotlib
matplotlib.use('Agg')  # use non-GUI backend
import matplotlib.pyplot as plt
import io
from .models import Project, Invoice
from django.utils import timezone
from datetime import date, timedelta

def home(request):
    return render(request, "core/home.html")

def dashboard_plot(request):
    # Example: jobs completed per month (last 6 months)
    today = date.today()
    months = []
    counts = []
    for i in range(5, -1, -1):
        m = (today.replace(day=1) - timedelta(days=30*i)).strftime("%b %Y")
        months.append(m)
        # simple count of completed projects whose end_date month matches
        start = (today.replace(day=1) - timedelta(days=30*(i+1))) + timedelta(days=1)
        end = (today.replace(day=1) - timedelta(days=30*i))
        cnt = Project.objects.filter(completed=True, end_date__range=(start, end)).count()
        counts.append(cnt)

    fig, ax = plt.subplots()
    ax.plot(months, counts, marker='o')
    ax.set_title("Completed Jobs (last 6 months)")
    ax.set_xlabel("Month")
    ax.set_ylabel("Jobs Completed")
    plt.tight_layout()

    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    return HttpResponse(buf.getvalue(), content_type="image/png")
