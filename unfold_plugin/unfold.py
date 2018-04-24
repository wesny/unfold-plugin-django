# -*- encoding: utf-8 -*-
# Unfold Django Plugin v0.1.0
# Unfold payment plugins to support payments in Django backends
# Copyright © 2018, Sweyn Venderbush.
# See /LICENSE for licensing information.

"""
INSERT MODULE DESCRIPTION HERE.

:Copyright: © 2018, Sweyn Venderbush.
:License: BSD (see /LICENSE).
"""
from django.shortcuts import redirect
from django.conf import settings
import requests


_auth_key = settings.UNFOLD_AUTH_KEY
_auth_username = settings.UNFOLD_AUTH_USERNAME

#HOST_URL = "http://localhost:8000"
HOST_URL = "https://unfoldapp.herokuapp.com"

def unfold_required(get_article_attributes):

    def decorator(f):

        def real_decorator(request, *args, **kwargs):
            attribs = get_article_attributes(request, *args, **kwargs)
            attribs['url'] = request.build_absolute_uri()
            attribs['price'] = str(attribs['price'])
            register_article(_auth_key, attribs)
            username = request.session.get('unfold_user')
            token = request.GET.get('token')
            if token:
                valid, username = validate_token(_auth_key, token)
                if valid:
                    request.session['unfold_user'] = username
            if not username or not has_purchased(_auth_key, username, attribs['external_id']):
                return redirect(HOST_URL + "/purchase?id=" + str(attribs['external_id']) + "&publisher=" + _auth_username)
            else:
                return f(request, *args, **kwargs)

        return real_decorator

    return decorator

def validate_token(auth_key, token):
    headers ={'Authorization': 'JWT ' + auth_key}
    try:
        r = requests.get(HOST_URL + "/api/validate-token", headers=headers, params={"token": token})
        r.raise_for_status()
        print(r.json())
        if r.json()['valid'] == False:
            return False, None
        return r.json()['valid'], r.json()['username']
    except Exception as e:
        if e.response.status_code == 401:
            raise requests.exceptions.HTTPError('Authentication key is invalid')
        else:
            return False, None

def has_purchased(auth_key, username, id):
    headers ={'Authorization': 'JWT ' + auth_key}
    data = {
        "username": username,
        "id": id
    }
    try:
        r = requests.get(HOST_URL + "/api/has-access", headers=headers, params=data)
        r.raise_for_status()
        return r.json()['result']
    except Exception as e:
        if e.response.status_code == 401:
            raise requests.exceptions.HTTPError('Authentication key is invalid')
        else:
            return False

def register_article(auth_key, attribs):
    headers ={'Authorization': 'JWT ' + auth_key}
    try:
        r = requests.post(HOST_URL + "/api/articles", headers=headers, data=attribs)
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 401:
            raise requests.exceptions.HTTPError('Authentication key is invalid')
        raise requests.exceptions.HTTPError('An error occurred while an article was trying to be registered')

