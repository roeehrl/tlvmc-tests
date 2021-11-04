"""Lab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from Beryllium import views
from Beryllium.views import patientsView, testersView, WellExcel, getWellsJSON, saveWellsJSON, isWellActive, getSecJSON, exportDoc, dashboard, changeType


urlpatterns = [
    path('Beryllium/admin/', admin.site.urls),
    path('Beryllium/BeTest/<int:id>/', views.BeTestView.as_view(), name='BeTest'),
    path('Beryllium/TestView/<int:id>/', views.TestViewView.as_view(), name='ResultViewt'),
    path('Beryllium/TestCalc/<int:id>', views.TestCalc.as_view()),
    path('Beryllium/testers', testersView),
    path('Beryllium/patients', patientsView),

    path('Beryllium/WellExcel/<int:id>', WellExcel),
    path('Beryllium/WellsJSON/<int:id>', getWellsJSON),
    path('Beryllium/saveWellsJSON/',saveWellsJSON),
    path('Beryllium/isWellActive/<int:id>',isWellActive),
    path('Beryllium/getSecJSON/<int:id>/<int:num>/<sec>',getSecJSON),
    path('Beryllium/Export/<int:id>',exportDoc),
    path('Beryllium/dashboard',views.dashboard.as_view()),
    path('dashboard',views.dashboard.as_view()),
    path('session/<type>', changeType),


    url(r'^WellPartial_view/(?P<arg2>\w+)/$',
    views.WellPartialView.as_view(),
    name='WellPartial_view'),
    path('Beryllium/WellPartial_view/<int:id>',
    views.WellPartialView.as_view(),
    name='WellPartial_view'),
  
]
