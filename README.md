[![PyPI version](https://badge.fury.io/py/py-keycloak.svg)](https://badge.fury.io/py/py-keycloak)
[![Documentation Status](https://readthedocs.org/projects/py-keycloak/badge/?version=latest)](http://py-keycloak.readthedocs.io/en/latest/?badge=latest)
[![GitHub issues](https://img.shields.io/github/issues/c0mpiler/py-keycloak.svg)](https://github.com/c0mpiler/py-keycloak/issues)
[![GitHub license](https://img.shields.io/github/license/c0mpiler/py-keycloak.svg)](https://github.com/c0mpiler/py-keycloak/blob/master/LICENSE)





Python client - Keycloak
====================

For review- see https://github.com/c0mpiler/py-keycloak

**py-keycloak** is a Python package providing access to the Keycloak API.

## Installation

### Via Pypi Package:

``` $ pip install py-keycloak ```

### Manually 

``` $ python setup.py install ```

## Dependencies

py-keycloak depends on:

* Python 3
* [requests](http://docs.python-requests.org/en/master/)
* [python-jose](http://python-jose.readthedocs.io/en/latest/)

### Tests Dependencies

* unittest
* [httmock](https://github.com/patrys/httmock)

## Bug reports

Please report bugs and feature requests at
https://github.com/c0mpiler/py-keycloak/issues

## Documentation

The documentation for py-keycloak is available on [readthedocs](http://py-keycloak.readthedocs.io).

## Usage

```python
from keycloak import KeycloakOpenID as KeyCloak

# Configure client
keycloak = KeyCloak(server_url="http://localhost:8080/auth/",
                    client_id="example_client",
                    realm_name="example_realm",
                    client_secret_key="secret")

# Get WellKnow
config_well_know = keycloak.well_know()

# Get Token
token = keycloak.token("user", "password")

# Get Userinfo
userinfo = keycloak.userinfo(token['access_token'])

# Refresh token
token = keycloak.refresh_token(token['refresh_token'])

# Logout
keycloak.logout(token['refresh_token'])

# Get Certs
certs = keycloak.certs()

# Get RPT (Entitlement)
token = keycloak.token("user", "password")
rpt = keycloak.entitlement(token['access_token'], "resource_id")

# Instropect RPT
token_rpt_info = keycloak.introspect(keycloak.introspect(token['access_token'], rpt=rpt['rpt'],
                                     token_type_hint="requesting_party_token"))

# Introspect Token
token_info = keycloak.introspect(token['access_token']))

# Decode Token
KEYCLOAK_PUBLIC_KEY = "secret"
options = {"verify_signature": True, "verify_aud": True, "exp": True}
token_info = keycloak.decode_token(token['access_token'], key=KEYCLOAK_PUBLIC_KEY, options=options)

# Get permissions by token
token = keycloak.token("user", "password")
keycloak.load_authorization_config("example-authz-config.json")
policies = keycloak.get_policies(token['access_token'], method_token_info='decode', key=KEYCLOAK_PUBLIC_KEY)
permissions = keycloak.get_permissions(token['access_token'], method_token_info='introspect')

# KEYCLOAK ADMIN

from keycloak import KeycloakAdmin

keycloak_admin = KeycloakAdmin(server_url="http://localhost:8080/auth/",
                               username='example-admin',
                               password='secret',
                               realm_name="example_realm",
                               verify=True)

# Add user                       
new_user = keycloak_admin.create_user({"email": "example@example.com",
                    "username": "example@example.com",
                    "enabled": True,
                    "firstName": "Example",
                    "lastName": "Example",
                    "realmRoles": ["user_default", ],
                    "attributes": {"example": "1,2,3,3,"}})    


# Add user and set password                    
new_user = keycloak_admin.create_user({"email": "example@example.com",
                    "username": "example@example.com",
                    "enabled": True,
                    "firstName": "Example",
                    "lastName": "Example",
                    "credentials": [{"value": "secret","type": "password",}],
                    "realmRoles": ["user_default", ],
                    "attributes": {"example": "1,2,3,3,"}})                        

# User counter
count_users = keycloak_admin.users_count()

# Get users Returns a list of users, filtered according to query parameters
users = keycloak_admin.get_users({})

# Get user ID from name
user-id-keycloak = keycloak_admin.get_user_id("example@example.com")

# Get User
user = keycloak_admin.get_user("user-id-keycloak")

# Update User
response = keycloak_admin.update_user(user_id="user-id-keycloak",
                                      payload={'firstName': 'Example Update'})

# Update User Password
response = set_user_password(user_id="user-id-keycloak", password="secret", temporary=True)

# Delete User
response = keycloak_admin.delete_user(user_id="user-id-keycloak")

# Get consents granted by the user
consents = keycloak_admin.consents_user(user_id="user-id-keycloak")

# Send User Action
response = keycloak_admin.send_update_account(user_id="user-id-keycloak",
                                              payload=json.dumps(['UPDATE_PASSWORD']))

# Send Verify Email
response = keycloak_admin.send_verify_email(user_id="user-id-keycloak")

# Get sessions associated with the user
sessions = keycloak_admin.get_sessions(user_id="user-id-keycloak")

# Get themes, social providers, auth providers, and event listeners available on this server
server_info = keycloak_admin.get_server_info()

# Get clients belonging to the realm Returns a list of clients belonging to the realm
clients = keycloak_admin.get_clients()

# Get client - id (not client-id) from client by name
client_id=keycloak_admin.get_client_id("my-client")

# Get representation of the client - id of client (not client-id)
client = keycloak_admin.get_client(client_id="client_id")

# Get all roles for the realm or client
realm_roles = keycloak_admin.get_realm_roles()

# Get all roles for the client
client_roles = keycloak_admin.get_client_roles(client_id="client_id")

# Get client role
role = keycloak_admin.get_client_role(client_id="client_id", role_name="role_name")

# Warning: Deprecated
# Get client role id from name
role_id = keycloak_admin.get_client_role_id(client_id="client_id", role_name="test")

# Create client role
keycloak_admin.create_client_role(client_id, "test")

# Assign client role to user. Note that BOTH role_name and role_id appear to be required.
keycloak_admin.assign_client_role(client_id="client_id", user_id="user_id", role_id="role_id", role_name="test")

# Create new group
group = keycloak_admin.create_group(name="Example Group")

# Get all groups
groups = keycloak_admin.get_groups()

# Get group
group = keycloak_admin.get_group(group_id='group_id')

# Get group by name
group = keycloak_admin.get_group_by_name(name_or_path='group_id', search_in_subgroups=True)

# Function to trigger user sync from provider
sync_users(storage_id="storage_di", action="action")
```
