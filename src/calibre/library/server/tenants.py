#!/usr/bin/env python
# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai

__license__   = 'GPL v3'
__copyright__ = '2010, Kovid Goyal <kovid@kovidgoyal.net>'
__docformat__ = 'restructuredtext en'
__author__ = 'Dan Strohl <dan@strohlfamily.org>'

'''
This module is in support of the multiple library feature (multi-tenancy) and contains various helper classes.
'''

class Tenant():

    def __init__(self, username, password, virtual_lib):
        self.username = username
        self.password = self._encode_password(password)
        self.virtual_lib = virtual_lib

    def _encode_password(self, password):
        pass

    def verify_password(self, password):
        return self.password == self._encode_password(password):

    def __str__(self):
        return '{} [{}]'.format(self.username, self.virtual_lib)


class Tenants():

    def __init__(self):
        self.tenant_dict = {}

    def add_tenant(self, username, password, virtual_lib):
        tmp_tenant = Tenant(username, password, virtual_lib)
        self.tenant_dict[username] = tmp_tenant

    def remove_tenant(self, username):
        del self.tenant_dict[username]

    def update_tenant(self, old_username, username, password, virtual_lib):
        if old_username != username:
            self.remove_tenant(username)
        self.add_tenant(username, password,virtual_lib)

    def list_tenants(self):
        tmp_return = []
        for ten in self.tenant_dict.itervalues():
            tmp_return.append(str(ten))
        return tmp_return

    def __getitem__(self, item):
        return self.tenant_dict[item]
