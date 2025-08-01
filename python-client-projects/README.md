# ls_zoho_billing_projects
A project is a series of tasks performed over a period of time, to achieve certain targets. There can be many number of people working on a single project and a project may consist of single or multiple tasks. A project is billed and charged upon a customer whom the project was taken up for.<br><br><b>Possible error codes: </b><br><table><thead><tr><th>Error Code</th><th>Message</th></tr></thead><tbody><tr><td><span style=\"color:#FF0000;\"> 1002</span></td><td>Project does not exists</td></tr><tr><td><span style=\"color:#FF0000;\"> 20004</span></td><td>Please ensure that the amount is not negative</td></tr><tr><td><span style=\"color:#FF0000;\"> 20077</span></td><td>Expense has been recorded for this project. Hence, it cannot be deleted</td></tr></tbody></table></tbody></table>

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Generator version: 7.14.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.9+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import ls_zoho_billing_projects
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import ls_zoho_billing_projects
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import ls_zoho_billing_projects
from ls_zoho_billing_projects.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_projects.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]


# Enter a context with an instance of the API client
with ls_zoho_billing_projects.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_projects.ProjectsApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    filter_by = 'Status.All' # str | Filter projects by any status. Allowed Values: <code>Status.All</code>, <code>Status.Active</code> and <code>Status.Inactive</code> (optional)
    customer_id = '460000000044001' # str | Unique ID of the customer. (optional)
    sort_column = 'created_time' # str | Sort projects. Allowed Values: <code>project_name</code>, <code>customer_name</code>, <code>rate</code> and <code>created_time</code> (optional)

    try:
        # List projects
        api_response = api_instance.projects_get(x_com_zoho_subscriptions_organizationid, filter_by=filter_by, customer_id=customer_id, sort_column=sort_column)
        print("The response of ProjectsApi->projects_get:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->projects_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://www.zohoapis.com/billing/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ProjectsApi* | [**projects_get**](docs/ProjectsApi.md#projects_get) | **GET** /projects | List projects
*ProjectsApi* | [**projects_post**](docs/ProjectsApi.md#projects_post) | **POST** /projects | Create a project
*ProjectsApi* | [**projects_project_id_active_post**](docs/ProjectsApi.md#projects_project_id_active_post) | **POST** /projects/{project_id}/active | Activate a project
*ProjectsApi* | [**projects_project_id_clone_post**](docs/ProjectsApi.md#projects_project_id_clone_post) | **POST** /projects/{project_id}/clone | Clone a project
*ProjectsApi* | [**projects_project_id_comments_comment_id_delete**](docs/ProjectsApi.md#projects_project_id_comments_comment_id_delete) | **DELETE** /projects/{project_id}/comments/{comment_id} | Delete comment
*ProjectsApi* | [**projects_project_id_comments_get**](docs/ProjectsApi.md#projects_project_id_comments_get) | **GET** /projects/{project_id}/comments | List comments
*ProjectsApi* | [**projects_project_id_comments_post**](docs/ProjectsApi.md#projects_project_id_comments_post) | **POST** /projects/{project_id}/comments | Post comment
*ProjectsApi* | [**projects_project_id_delete**](docs/ProjectsApi.md#projects_project_id_delete) | **DELETE** /projects/{project_id} | Delete project
*ProjectsApi* | [**projects_project_id_get**](docs/ProjectsApi.md#projects_project_id_get) | **GET** /projects/{project_id} | Get a project
*ProjectsApi* | [**projects_project_id_inactive_post**](docs/ProjectsApi.md#projects_project_id_inactive_post) | **POST** /projects/{project_id}/inactive | Deactivate a project
*ProjectsApi* | [**projects_project_id_invoices_get**](docs/ProjectsApi.md#projects_project_id_invoices_get) | **GET** /projects/{project_id}/invoices | List invoices
*ProjectsApi* | [**projects_project_id_put**](docs/ProjectsApi.md#projects_project_id_put) | **PUT** /projects/{project_id} | Update a project
*ProjectsApi* | [**projects_project_id_users_get**](docs/ProjectsApi.md#projects_project_id_users_get) | **GET** /projects/{project_id}/users | List Users
*ProjectsApi* | [**projects_project_id_users_invite_post**](docs/ProjectsApi.md#projects_project_id_users_invite_post) | **POST** /projects/{project_id}/users/invite | Invite user
*ProjectsApi* | [**projects_project_id_users_post**](docs/ProjectsApi.md#projects_project_id_users_post) | **POST** /projects/{project_id}/users | Assign users
*ProjectsApi* | [**projects_project_id_users_user_id_delete**](docs/ProjectsApi.md#projects_project_id_users_user_id_delete) | **DELETE** /projects/{project_id}/users/{user_id} | Delete user
*ProjectsApi* | [**projects_project_id_users_user_id_get**](docs/ProjectsApi.md#projects_project_id_users_user_id_get) | **GET** /projects/{project_id}/users/{user_id} | Get a User
*ProjectsApi* | [**projects_project_id_users_user_id_put**](docs/ProjectsApi.md#projects_project_id_users_user_id_put) | **PUT** /projects/{project_id}/users/{user_id} | Update user


## Documentation For Models

 - [ActivateAProjectResponse](docs/ActivateAProjectResponse.md)
 - [AssignUsersRequest](docs/AssignUsersRequest.md)
 - [AssignUsersResponse](docs/AssignUsersResponse.md)
 - [AssignUsersResponseUsersInner](docs/AssignUsersResponseUsersInner.md)
 - [CloneAProjectRequest](docs/CloneAProjectRequest.md)
 - [CloneAProjectResponse](docs/CloneAProjectResponse.md)
 - [CreateAProjectRequest](docs/CreateAProjectRequest.md)
 - [CreateAProjectRequestTasksInner](docs/CreateAProjectRequestTasksInner.md)
 - [CreateAProjectRequestUsersInner](docs/CreateAProjectRequestUsersInner.md)
 - [CreateAProjectResponse](docs/CreateAProjectResponse.md)
 - [DeactivateAProjectResponse](docs/DeactivateAProjectResponse.md)
 - [DeleteCommentResponse](docs/DeleteCommentResponse.md)
 - [DeleteProjectResponse](docs/DeleteProjectResponse.md)
 - [DeleteUserResponse](docs/DeleteUserResponse.md)
 - [GetAProjectResponse](docs/GetAProjectResponse.md)
 - [GetAProjectResponseProject](docs/GetAProjectResponseProject.md)
 - [GetAUserResponse](docs/GetAUserResponse.md)
 - [GetAUserResponseUsers](docs/GetAUserResponseUsers.md)
 - [InviteUserRequest](docs/InviteUserRequest.md)
 - [InviteUserResponse](docs/InviteUserResponse.md)
 - [InviteUserResponseUsersInner](docs/InviteUserResponseUsersInner.md)
 - [ListCommentsResponse](docs/ListCommentsResponse.md)
 - [ListCommentsResponseCommentsInner](docs/ListCommentsResponseCommentsInner.md)
 - [ListInvoicesResponse](docs/ListInvoicesResponse.md)
 - [ListInvoicesResponseInvoicesInner](docs/ListInvoicesResponseInvoicesInner.md)
 - [ListProjectsResponse](docs/ListProjectsResponse.md)
 - [ListProjectsResponseProjectsInner](docs/ListProjectsResponseProjectsInner.md)
 - [ListUsersResponse](docs/ListUsersResponse.md)
 - [PostCommentRequest](docs/PostCommentRequest.md)
 - [PostCommentResponse](docs/PostCommentResponse.md)
 - [PostCommentResponseCommentsInner](docs/PostCommentResponseCommentsInner.md)
 - [ProjectResponse](docs/ProjectResponse.md)
 - [ProjectResponseTasksInner](docs/ProjectResponseTasksInner.md)
 - [ProjectResponseUsersInner](docs/ProjectResponseUsersInner.md)
 - [UpdateAProjectRequest](docs/UpdateAProjectRequest.md)
 - [UpdateAProjectResponse](docs/UpdateAProjectResponse.md)
 - [UpdateAProjectResponseProject](docs/UpdateAProjectResponseProject.md)
 - [UpdateUserRequest](docs/UpdateUserRequest.md)
 - [UpdateUserResponse](docs/UpdateUserResponse.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="Zoho_Auth"></a>
### Zoho_Auth

- **Type**: OAuth
- **Flow**: implicit
- **Authorization URL**: https://accounts.zoho.com/oauth/v2/auth
- **Scopes**: 
 - **ZohoSubscriptions.projects.CREATE**: Create Projects
 - **ZohoSubscriptions.projects.UPDATE**: Update Projects
 - **ZohoSubscriptions.projects.READ**: Read Projects
 - **ZohoSubscriptions.projects.DELETE**: Delete Projects


## Author




