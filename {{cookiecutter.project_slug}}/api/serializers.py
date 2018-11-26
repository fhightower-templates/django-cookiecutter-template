#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from rest_framework import serializers

from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    """."""
    class Meta:
        model = User
        fields = ('groups', 'username')
