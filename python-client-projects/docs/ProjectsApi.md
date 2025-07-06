# ls_zoho_billing_projects.ProjectsApi

All URIs are relative to *https://www.zohoapis.com/billing/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projects_get**](ProjectsApi.md#projects_get) | **GET** /projects | List projects
[**projects_post**](ProjectsApi.md#projects_post) | **POST** /projects | Create a project
[**projects_project_id_active_post**](ProjectsApi.md#projects_project_id_active_post) | **POST** /projects/{project_id}/active | Activate a project
[**projects_project_id_clone_post**](ProjectsApi.md#projects_project_id_clone_post) | **POST** /projects/{project_id}/clone | Clone a project
[**projects_project_id_comments_comment_id_delete**](ProjectsApi.md#projects_project_id_comments_comment_id_delete) | **DELETE** /projects/{project_id}/comments/{comment_id} | Delete comment
[**projects_project_id_comments_get**](ProjectsApi.md#projects_project_id_comments_get) | **GET** /projects/{project_id}/comments | List comments
[**projects_project_id_comments_post**](ProjectsApi.md#projects_project_id_comments_post) | **POST** /projects/{project_id}/comments | Post comment
[**projects_project_id_delete**](ProjectsApi.md#projects_project_id_delete) | **DELETE** /projects/{project_id} | Delete project
[**projects_project_id_get**](ProjectsApi.md#projects_project_id_get) | **GET** /projects/{project_id} | Get a project
[**projects_project_id_inactive_post**](ProjectsApi.md#projects_project_id_inactive_post) | **POST** /projects/{project_id}/inactive | Deactivate a project
[**projects_project_id_invoices_get**](ProjectsApi.md#projects_project_id_invoices_get) | **GET** /projects/{project_id}/invoices | List invoices
[**projects_project_id_put**](ProjectsApi.md#projects_project_id_put) | **PUT** /projects/{project_id} | Update a project
[**projects_project_id_users_get**](ProjectsApi.md#projects_project_id_users_get) | **GET** /projects/{project_id}/users | List Users
[**projects_project_id_users_invite_post**](ProjectsApi.md#projects_project_id_users_invite_post) | **POST** /projects/{project_id}/users/invite | Invite user
[**projects_project_id_users_post**](ProjectsApi.md#projects_project_id_users_post) | **POST** /projects/{project_id}/users | Assign users
[**projects_project_id_users_user_id_delete**](ProjectsApi.md#projects_project_id_users_user_id_delete) | **DELETE** /projects/{project_id}/users/{user_id} | Delete user
[**projects_project_id_users_user_id_get**](ProjectsApi.md#projects_project_id_users_user_id_get) | **GET** /projects/{project_id}/users/{user_id} | Get a User
[**projects_project_id_users_user_id_put**](ProjectsApi.md#projects_project_id_users_user_id_put) | **PUT** /projects/{project_id}/users/{user_id} | Update user


# **projects_get**
> ListProjectsResponse projects_get(x_com_zoho_subscriptions_organizationid, filter_by=filter_by, customer_id=customer_id, sort_column=sort_column)

List projects

List all projects with pagination.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_projects
from ls_zoho_billing_projects.models.list_projects_response import ListProjectsResponse
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
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **filter_by** | **str**| Filter projects by any status. Allowed Values: &lt;code&gt;Status.All&lt;/code&gt;, &lt;code&gt;Status.Active&lt;/code&gt; and &lt;code&gt;Status.Inactive&lt;/code&gt; | [optional] 
 **customer_id** | **str**| Unique ID of the customer. | [optional] 
 **sort_column** | **str**| Sort projects. Allowed Values: &lt;code&gt;project_name&lt;/code&gt;, &lt;code&gt;customer_name&lt;/code&gt;, &lt;code&gt;rate&lt;/code&gt; and &lt;code&gt;created_time&lt;/code&gt; | [optional] 

### Return type

[**ListProjectsResponse**](ListProjectsResponse.md)

### Authorization

[Zoho_Auth](../README.md#Zoho_Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_post**
> CreateAProjectResponse projects_post(x_com_zoho_subscriptions_organizationid, create_a_project_request=create_a_project_request)

Create a project

Create a new project.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_projects
from ls_zoho_billing_projects.models.create_a_project_request import CreateAProjectRequest
from ls_zoho_billing_projects.models.create_a_project_response import CreateAProjectResponse
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
    create_a_project_request = ls_zoho_billing_projects.CreateAProjectRequest() # CreateAProjectRequest |  (optional)

    try:
        # Create a project
        api_response = api_instance.projects_post(x_com_zoho_subscriptions_organizationid, create_a_project_request=create_a_project_request)
        print("The response of ProjectsApi->projects_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **create_a_project_request** | [**CreateAProjectRequest**](CreateAProjectRequest.md)|  | [optional] 

### Return type

[**CreateAProjectResponse**](CreateAProjectResponse.md)

### Authorization

[Zoho_Auth](../README.md#Zoho_Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_active_post**
> ActivateAProjectResponse projects_project_id_active_post(project_id, x_com_zoho_subscriptions_organizationid)

Activate a project

Mark project as active

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_projects
from ls_zoho_billing_projects.models.activate_a_project_response import ActivateAProjectResponse
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
    project_id = '460000000044019' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Activate a project
        api_response = api_instance.projects_project_id_active_post(project_id, x_com_zoho_subscriptions_organizationid)
        print("The response of ProjectsApi->projects_project_id_active_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_project_id_active_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**ActivateAProjectResponse**](ActivateAProjectResponse.md)

### Authorization

[Zoho_Auth](../README.md#Zoho_Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_clone_post**
> CloneAProjectResponse projects_project_id_clone_post(project_id, x_com_zoho_subscriptions_organizationid, clone_a_project_request=clone_a_project_request)

Clone a project

Cloning the settings of an existing project.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_projects
from ls_zoho_billing_projects.models.clone_a_project_request import CloneAProjectRequest
from ls_zoho_billing_projects.models.clone_a_project_response import CloneAProjectResponse
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
    project_id = '460000000044019' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    clone_a_project_request = ls_zoho_billing_projects.CloneAProjectRequest() # CloneAProjectRequest |  (optional)

    try:
        # Clone a project
        api_response = api_instance.projects_project_id_clone_post(project_id, x_com_zoho_subscriptions_organizationid, clone_a_project_request=clone_a_project_request)
        print("The response of ProjectsApi->projects_project_id_clone_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_project_id_clone_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **clone_a_project_request** | [**CloneAProjectRequest**](CloneAProjectRequest.md)|  | [optional] 

### Return type

[**CloneAProjectResponse**](CloneAProjectResponse.md)

### Authorization

[Zoho_Auth](../README.md#Zoho_Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_comments_comment_id_delete**
> DeleteCommentResponse projects_project_id_comments_comment_id_delete(project_id, comment_id, x_com_zoho_subscriptions_organizationid)

Delete comment

Deleting a comment.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_projects
from ls_zoho_billing_projects.models.delete_comment_response import DeleteCommentResponse
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
    project_id = '460000000044019' # str | 
    comment_id = '460000000044027' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Delete comment
        api_response = api_instance.projects_project_id_comments_comment_id_delete(project_id, comment_id, x_com_zoho_subscriptions_organizationid)
        print("The response of ProjectsApi->projects_project_id_comments_comment_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_project_id_comments_comment_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **comment_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**DeleteCommentResponse**](DeleteCommentResponse.md)

### Authorization

[Zoho_Auth](../README.md#Zoho_Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_comments_get**
> ListCommentsResponse projects_project_id_comments_get(project_id, x_com_zoho_subscriptions_organizationid)

List comments

Get comments for a project.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_projects
from ls_zoho_billing_projects.models.list_comments_response import ListCommentsResponse
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
    project_id = '460000000044019' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # List comments
        api_response = api_instance.projects_project_id_comments_get(project_id, x_com_zoho_subscriptions_organizationid)
        print("The response of ProjectsApi->projects_project_id_comments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_project_id_comments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**ListCommentsResponse**](ListCommentsResponse.md)

### Authorization

[Zoho_Auth](../README.md#Zoho_Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_comments_post**
> PostCommentResponse projects_project_id_comments_post(project_id, x_com_zoho_subscriptions_organizationid, post_comment_request=post_comment_request)

Post comment

Post comment to a project.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_projects
from ls_zoho_billing_projects.models.post_comment_request import PostCommentRequest
from ls_zoho_billing_projects.models.post_comment_response import PostCommentResponse
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
    project_id = '460000000044019' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    post_comment_request = ls_zoho_billing_projects.PostCommentRequest() # PostCommentRequest |  (optional)

    try:
        # Post comment
        api_response = api_instance.projects_project_id_comments_post(project_id, x_com_zoho_subscriptions_organizationid, post_comment_request=post_comment_request)
        print("The response of ProjectsApi->projects_project_id_comments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_project_id_comments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **post_comment_request** | [**PostCommentRequest**](PostCommentRequest.md)|  | [optional] 

### Return type

[**PostCommentResponse**](PostCommentResponse.md)

### Authorization

[Zoho_Auth](../README.md#Zoho_Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_delete**
> DeleteProjectResponse projects_project_id_delete(project_id, x_com_zoho_subscriptions_organizationid)

Delete project

Deleting a existing project.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_projects
from ls_zoho_billing_projects.models.delete_project_response import DeleteProjectResponse
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
    project_id = '460000000044019' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Delete project
        api_response = api_instance.projects_project_id_delete(project_id, x_com_zoho_subscriptions_organizationid)
        print("The response of ProjectsApi->projects_project_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_project_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**DeleteProjectResponse**](DeleteProjectResponse.md)

### Authorization

[Zoho_Auth](../README.md#Zoho_Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_get**
> GetAProjectResponse projects_project_id_get(project_id, x_com_zoho_subscriptions_organizationid)

Get a project

Get the details of a project.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_projects
from ls_zoho_billing_projects.models.get_a_project_response import GetAProjectResponse
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
    project_id = '460000000044019' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Get a project
        api_response = api_instance.projects_project_id_get(project_id, x_com_zoho_subscriptions_organizationid)
        print("The response of ProjectsApi->projects_project_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_project_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**GetAProjectResponse**](GetAProjectResponse.md)

### Authorization

[Zoho_Auth](../README.md#Zoho_Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_inactive_post**
> DeactivateAProjectResponse projects_project_id_inactive_post(project_id, x_com_zoho_subscriptions_organizationid)

Deactivate a project

Marking a project as inactive.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_projects
from ls_zoho_billing_projects.models.deactivate_a_project_response import DeactivateAProjectResponse
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
    project_id = '460000000044019' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Deactivate a project
        api_response = api_instance.projects_project_id_inactive_post(project_id, x_com_zoho_subscriptions_organizationid)
        print("The response of ProjectsApi->projects_project_id_inactive_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_project_id_inactive_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**DeactivateAProjectResponse**](DeactivateAProjectResponse.md)

### Authorization

[Zoho_Auth](../README.md#Zoho_Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_invoices_get**
> ListInvoicesResponse projects_project_id_invoices_get(project_id, x_com_zoho_subscriptions_organizationid, sort_column=sort_column)

List invoices

Lists invoices created for this project.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_projects
from ls_zoho_billing_projects.models.list_invoices_response import ListInvoicesResponse
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
    project_id = '460000000044019' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    sort_column = 'created_time' # str | Sort invoices raised. Allowed Values: <code>invoice_number</code>, <code>date</code>, <code>total</code>, <code>balance</code> and <code>created_time</code> (optional)

    try:
        # List invoices
        api_response = api_instance.projects_project_id_invoices_get(project_id, x_com_zoho_subscriptions_organizationid, sort_column=sort_column)
        print("The response of ProjectsApi->projects_project_id_invoices_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_project_id_invoices_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **sort_column** | **str**| Sort invoices raised. Allowed Values: &lt;code&gt;invoice_number&lt;/code&gt;, &lt;code&gt;date&lt;/code&gt;, &lt;code&gt;total&lt;/code&gt;, &lt;code&gt;balance&lt;/code&gt; and &lt;code&gt;created_time&lt;/code&gt; | [optional] 

### Return type

[**ListInvoicesResponse**](ListInvoicesResponse.md)

### Authorization

[Zoho_Auth](../README.md#Zoho_Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_put**
> UpdateAProjectResponse projects_project_id_put(project_id, x_com_zoho_subscriptions_organizationid, update_a_project_request=update_a_project_request)

Update a project

Update details of a project.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_projects
from ls_zoho_billing_projects.models.update_a_project_request import UpdateAProjectRequest
from ls_zoho_billing_projects.models.update_a_project_response import UpdateAProjectResponse
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
    project_id = '460000000044019' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    update_a_project_request = ls_zoho_billing_projects.UpdateAProjectRequest() # UpdateAProjectRequest |  (optional)

    try:
        # Update a project
        api_response = api_instance.projects_project_id_put(project_id, x_com_zoho_subscriptions_organizationid, update_a_project_request=update_a_project_request)
        print("The response of ProjectsApi->projects_project_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_project_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **update_a_project_request** | [**UpdateAProjectRequest**](UpdateAProjectRequest.md)|  | [optional] 

### Return type

[**UpdateAProjectResponse**](UpdateAProjectResponse.md)

### Authorization

[Zoho_Auth](../README.md#Zoho_Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_users_get**
> ListUsersResponse projects_project_id_users_get(project_id, x_com_zoho_subscriptions_organizationid)

List Users

Get list of all users associated to a project.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_projects
from ls_zoho_billing_projects.models.list_users_response import ListUsersResponse
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
    project_id = '460000000044019' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # List Users
        api_response = api_instance.projects_project_id_users_get(project_id, x_com_zoho_subscriptions_organizationid)
        print("The response of ProjectsApi->projects_project_id_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_project_id_users_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**ListUsersResponse**](ListUsersResponse.md)

### Authorization

[Zoho_Auth](../README.md#Zoho_Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_users_invite_post**
> InviteUserResponse projects_project_id_users_invite_post(project_id, x_com_zoho_subscriptions_organizationid, invite_user_request=invite_user_request)

Invite user

Invite a user to the project.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_projects
from ls_zoho_billing_projects.models.invite_user_request import InviteUserRequest
from ls_zoho_billing_projects.models.invite_user_response import InviteUserResponse
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
    project_id = '460000000044019' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    invite_user_request = ls_zoho_billing_projects.InviteUserRequest() # InviteUserRequest |  (optional)

    try:
        # Invite user
        api_response = api_instance.projects_project_id_users_invite_post(project_id, x_com_zoho_subscriptions_organizationid, invite_user_request=invite_user_request)
        print("The response of ProjectsApi->projects_project_id_users_invite_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_project_id_users_invite_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **invite_user_request** | [**InviteUserRequest**](InviteUserRequest.md)|  | [optional] 

### Return type

[**InviteUserResponse**](InviteUserResponse.md)

### Authorization

[Zoho_Auth](../README.md#Zoho_Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_users_post**
> AssignUsersResponse projects_project_id_users_post(project_id, x_com_zoho_subscriptions_organizationid, assign_users_request=assign_users_request)

Assign users

Assign a users to a project.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_projects
from ls_zoho_billing_projects.models.assign_users_request import AssignUsersRequest
from ls_zoho_billing_projects.models.assign_users_response import AssignUsersResponse
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
    project_id = '460000000044019' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    assign_users_request = ls_zoho_billing_projects.AssignUsersRequest() # AssignUsersRequest |  (optional)

    try:
        # Assign users
        api_response = api_instance.projects_project_id_users_post(project_id, x_com_zoho_subscriptions_organizationid, assign_users_request=assign_users_request)
        print("The response of ProjectsApi->projects_project_id_users_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_project_id_users_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **assign_users_request** | [**AssignUsersRequest**](AssignUsersRequest.md)|  | [optional] 

### Return type

[**AssignUsersResponse**](AssignUsersResponse.md)

### Authorization

[Zoho_Auth](../README.md#Zoho_Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_users_user_id_delete**
> DeleteUserResponse projects_project_id_users_user_id_delete(project_id, x_com_zoho_subscriptions_organizationid, user_id)

Delete user

Remove user from a project.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_projects
from ls_zoho_billing_projects.models.delete_user_response import DeleteUserResponse
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
    project_id = '460000000044019' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    user_id = '460000000024003' # str | 

    try:
        # Delete user
        api_response = api_instance.projects_project_id_users_user_id_delete(project_id, x_com_zoho_subscriptions_organizationid, user_id)
        print("The response of ProjectsApi->projects_project_id_users_user_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_project_id_users_user_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **user_id** | **str**|  | 

### Return type

[**DeleteUserResponse**](DeleteUserResponse.md)

### Authorization

[Zoho_Auth](../README.md#Zoho_Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_users_user_id_get**
> GetAUserResponse projects_project_id_users_user_id_get(project_id, x_com_zoho_subscriptions_organizationid, user_id)

Get a User

Get details of a user in project.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_projects
from ls_zoho_billing_projects.models.get_a_user_response import GetAUserResponse
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
    project_id = '460000000044019' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    user_id = '460000000024003' # str | 

    try:
        # Get a User
        api_response = api_instance.projects_project_id_users_user_id_get(project_id, x_com_zoho_subscriptions_organizationid, user_id)
        print("The response of ProjectsApi->projects_project_id_users_user_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_project_id_users_user_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **user_id** | **str**|  | 

### Return type

[**GetAUserResponse**](GetAUserResponse.md)

### Authorization

[Zoho_Auth](../README.md#Zoho_Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_users_user_id_put**
> UpdateUserResponse projects_project_id_users_user_id_put(project_id, x_com_zoho_subscriptions_organizationid, user_id, update_user_request=update_user_request)

Update user

Update details of a user.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_projects
from ls_zoho_billing_projects.models.update_user_request import UpdateUserRequest
from ls_zoho_billing_projects.models.update_user_response import UpdateUserResponse
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
    project_id = '460000000044019' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    user_id = '460000000024003' # str | 
    update_user_request = ls_zoho_billing_projects.UpdateUserRequest() # UpdateUserRequest |  (optional)

    try:
        # Update user
        api_response = api_instance.projects_project_id_users_user_id_put(project_id, x_com_zoho_subscriptions_organizationid, user_id, update_user_request=update_user_request)
        print("The response of ProjectsApi->projects_project_id_users_user_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_project_id_users_user_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **user_id** | **str**|  | 
 **update_user_request** | [**UpdateUserRequest**](UpdateUserRequest.md)|  | [optional] 

### Return type

[**UpdateUserResponse**](UpdateUserResponse.md)

### Authorization

[Zoho_Auth](../README.md#Zoho_Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

