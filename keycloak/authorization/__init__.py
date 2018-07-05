# -*- coding: utf-8 -*-

import ast
import json

from .permission import Permission
from .policy import Policy
from .role import Role


class Authorization:
    """
    Keycloak Authorization (policies, roles, scopes and resources).

    https://keycloak.gitbooks.io/documentation/authorization_services/index.html

    """

    def __init__(self):
        self._policies = {}

    @property
    def policies(self):
        return self._policies

    @policies.setter
    def policies(self, value):
        self._policies = value

    def load_config(self, data):
        """
        Load policies, roles and permissions (scope/resources).

        :param data: keycloak authorization data (dict)
        :return:
        """
        for pol in data['policies']:
            if pol['type'] == 'role':
                policy = Policy(name=pol['name'],
                                type=pol['type'],
                                logic=pol['logic'],
                                decision_strategy=pol['decisionStrategy'])

                config_roles = json.loads(pol['config']['roles'])
                for role in config_roles:
                    policy.add_role(Role(name=role['id'],
                                         required=role['required']))

                self.policies[policy.name] = policy

            if pol['type'] == 'scope':
                permission = Permission(name=pol['name'],
                                        type=pol['type'],
                                        logic=pol['logic'],
                                        decision_strategy=pol['decisionStrategy'])

                permission.scopes = ast.literal_eval(pol['config']['scopes'])

                for policy_name in ast.literal_eval(pol['config']['applyPolicies']):
                    self.policies[policy_name].add_permission(permission)

            if pol['type'] == 'resource':
                permission = Permission(name=pol['name'],
                                        type=pol['type'],
                                        logic=pol['logic'],
                                        decision_strategy=pol['decisionStrategy'])

                permission.resources = ast.literal_eval(pol['config']['resources'])

                for policy_name in ast.literal_eval(pol['config']['applyPolicies']):
                    self.policies[policy_name].add_permission(permission)
