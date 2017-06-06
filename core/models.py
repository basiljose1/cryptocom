# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import binascii
import os

from django.db import models

from django.contrib.auth.models import User



class Token(models.Model):
    """
    The user token model.
    """

    user = models.OneToOneField(User, related_name='user_token', on_delete=models.CASCADE)
    key = models.CharField(max_length=20, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "token"
        verbose_name_plural = "tokens"

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super(Token, self).save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(4)).decode()

    def __str__(self):
        return self.key
