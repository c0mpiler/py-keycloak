# -*- coding: utf-8 -*-

class Role:
    """
    Roles identify a type or category of user. Admin, user,
    manager, and employee are all typical roles that may exist in an organization.

    https://keycloak.gitbooks.io/documentation/server_admin/topics/roles.html

    """

    def __init__(self, name, required=False):
        self.name = name
        self.required = required

    @property
    def get_name(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        return NotImplemented
