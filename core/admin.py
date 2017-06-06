# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from core.models import Token
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(Token)