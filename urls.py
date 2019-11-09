"""cafeEcomerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  re_path('', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  re_path('', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.urls import include, re_path
	2. Add a URL to urlpatterns:  re_path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path

from core import views as views_core
from catalog import views as views_cat

urlpatterns = [
	re_path(r'^$', views_core.inicial, name='inicial'),

	re_path(r'^home/$', views_core.index, name='home'),

	re_path(r'^produtos/(?P<slug>[\w_-]+)/',views_core.index_tipo, name="tipo"),

	re_path(r'^carrinho/$', views_core.carrinho, name='carrinho'),

	re_path(r'^busca/$', views_core.busca, name='busca'),

	re_path(r'^cadastro/$', views_core.cadastro, name='cadastro'),

	re_path(r'^login/$', views_core.login, name='login'),

	re_path(r'^produtora/$', views_core.produtora, name='produtora'),

	re_path(r'^cartao/$', views_core.cartao, name='cartao'),

	re_path(r'^admin/', admin.site.urls),

]
