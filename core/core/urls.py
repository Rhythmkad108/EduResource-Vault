"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from home.views import *

urlpatterns = [
    path("home/", homePage, name="home"),
    # Sem 1
    path("home/sem1/", sem1Page, name="sem1"),
    path("home/sem1/ed", edPage, name="ed"),
    path("home/sem1/ieee", ieeePage, name="ieee"),
    path("home/sem1/computing", computingPage, name="computing"),
    path("home/sem1/calculus", calculusPage, name="calculus"),
    path("home/sem1/chem", chemPage, name="chem"),
    # Sem 2
    path("home/sem2/", sem2Page, name="sem2"),
    path("home/sem2/evs1", evs1Page, name="evs1"),
    path("home/sem2/evs2", evs2Page, name="evs2"),
    path("home/sem2/physics", physicsPage, name="physics"),
    path("home/sem2/manuf", manufPage, name="manuf"),
    path("home/sem2/mecha", mechaPage, name="mecha"),
    path("home/sem2/english", englishPage, name="english"),
    path("home/sem2/prob", probPage, name="probability"),
    # Sem 3
    path("home/sem3/", sem3Page, name="sem3"),
    path("home/sem3/aiml/", aimlPage, name="aiml"),
    path("home/sem3/dscs/", dscsPage, name="dscs"),
    path("home/sem3/cao/", caoPage, name="cao"),
    path("home/sem3/dsa/", dsaPage, name="dsa"),
    path("home/sem3/ot/", otPage, name="ot"),
    # Sem4
    path("home/sem4/", sem4Page, name="sem4"),
    path("home/sem4/cn/", cnPage, name="cn"),
    path("home/sem4/os/", osPage, name="os"),
    path("home/sem4/ada/", adaPage, name="ada"),
    path("home/sem4/psycho/", psychoPage, name="psycho"),
    path("home/sem4/fin/", finPage, name="fin"),
    # Sem 5
    path("home/sem5/", sem5Page, name="sem5"),
    path("home/sem5/se/", sePage, name="se"),
    path("home/sem5/sc/", scPage, name="sc"),
    path("home/sem5/toc/", tocPage, name="toc"),
    path("home/sem5/ml/", mlPage, name="ml"),
    path("home/sem5/wirc/", wircPage, name="wirc"),
    # Sem 6
    path("home/sem6/", sem6Page, name="sem6"),
    # Sem 7
    path("home/sem7/", sem7Page, name="sem7"),
    # Sem 8
    path("home/sem8/", sem8Page, name="sem8"),
    # ------
    path("", loginPage, name="login"),
    path("register/", registerPage, name="register"),
    path("logout/", logoutPage, name="logout"),
    path("admin/", admin.site.urls),
    path(
        "api/courses/<int:sem_no>/<str:course_name>/",
        get_course_info,
        name="get_course_info",
    ),
    path(
        "update_material_status/", update_material_status, name="update_material_status"
    ),
    path("crawler/", crawlerPage, name="crawler"),
]
