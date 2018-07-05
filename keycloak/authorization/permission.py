# -*- coding: utf-8 -*-

class Permission:
    """
    Consider this simple and very common permission:

    A permission associates the object being protected with the policies that must be evaluated to determine whether access is granted.

    X CAN DO Y ON RESOURCE Z

    where …
        X represents one or more users, roles, or groups, or a combination of them. You can
        also use claims and context here.
        Y represents an action to be performed, for example, write, view, and so on.
        Z represents a protected resource, for example, "/accounts".

    https://keycloak.gitbooks.io/documentation/authorization_services/topics/permission/overview.html

    """

    def __init__(self, name, type, logic, decision_strategy):
        self._name = name
        self._type = type
        self._logic = logic
        self._decision_strategy = decision_strategy
        self._resources = []
        self._scopes = []

    def __repr__(self):
        return "<Permission: %s (%s)>" % (self.name, self.type)

    def __str__(self):
        return "Permission: %s (%s)" % (self.name, self.type)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def logic(self):
        return self._logic

    @logic.setter
    def logic(self, value):
        self._logic = value

    @property
    def decision_strategy(self):
        return self._decision_strategy

    @decision_strategy.setter
    def decision_strategy(self, value):
        self._decision_strategy = value

    @property
    def resources(self):
        return self._resources

    @resources.setter
    def resources(self, value):
        self._resources = value

    @property
    def scopes(self):
        return self._scopes

    @scopes.setter
    def scopes(self, value):
        self._scopes = value
