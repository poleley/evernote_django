"""evernote_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from evernote import views
from evernote.views import RegisterUser, LoginUser, MainView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('evernote/main', views.show_main, name='main_page'),
    path('evernote/main', MainView.as_view(), name='main_page'),
    path('evernote/main/<int:idnote>', views.deletenote_page, name='delete-note_page'),
    path('evernote', views.landing, name='landing_page'),
    path('evernote/registration', RegisterUser.as_view(), name='registration_page'),
    path('evernote/login', LoginUser.as_view(), name='login_page'),
    path('evernote/logout', views.logout_user, name='logout'),
    path('evernote/add-note', views.new_note, name='add-note_page'),
    path('evernote/add-tag/<int:idnote>', views.new_tag, name='add-tag_page'),
    path('evernote/download-file/<int:idnote>', views.download_file, name='download-file_page'),
]
