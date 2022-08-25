# -*- coding: utf-8 -*-
""" URLs for API version 1 """

from django.urls import path, include
from .. import views

urlpatterns = [
    # ╠════════════╡ Base info ╠═════════════════════════════════════════════════════╡
    path('regions/', include([
        path('<int:pk>', views.v1.RegionsUDCView.as_view(), name='regions-udc'),
        path('', views.v1.RegionsView.as_view(), name='regions-list'),
    ])),
]
