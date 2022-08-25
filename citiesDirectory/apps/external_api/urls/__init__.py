# -*- coding: utf-8 -*-

"""
URLs
"""

__all__ = [
    'urlpatterns',
]

from django.urls import path, include

from citiesDirectory.apps.external_api.urls import v1

urlpatterns = [
    path('v1/', include(('citiesDirectory.apps.external_api.urls.v1', 'citiesDirectory.apps.external_api'),
                        namespace='v1')
         ),
]
