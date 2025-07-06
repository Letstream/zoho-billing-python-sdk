# ls_zoho_billing_tasks.TasksApi

All URIs are relative to *https://www.zohoapis.com/billing/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projects_project_id_tasks_get**](TasksApi.md#projects_project_id_tasks_get) | **GET** /projects/{project_id}/tasks | List tasks
[**projects_project_id_tasks_post**](TasksApi.md#projects_project_id_tasks_post) | **POST** /projects/{project_id}/tasks | Add a task
[**projects_project_id_tasks_task_id_delete**](TasksApi.md#projects_project_id_tasks_task_id_delete) | **DELETE** /projects/{project_id}/tasks/{task_id} | Delete a Task
[**projects_project_id_tasks_task_id_get**](TasksApi.md#projects_project_id_tasks_task_id_get) | **GET** /projects/{project_id}/tasks/{task_id} | Get a task
[**projects_project_id_tasks_task_id_put**](TasksApi.md#projects_project_id_tasks_task_id_put) | **PUT** /projects/{project_id}/tasks/{task_id} | Update a task


# **projects_project_id_tasks_get**
> ListTasksResponse projects_project_id_tasks_get(project_id, x_com_zoho_subscriptions_organizationid)

List tasks

Get list of all the tasks added to a project.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_tasks
from ls_zoho_billing_tasks.models.list_tasks_response import ListTasksResponse
from ls_zoho_billing_tasks.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_tasks.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_tasks.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_tasks.TasksApi(api_client)
    project_id = '90300000072369' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # List tasks
        api_response = api_instance.projects_project_id_tasks_get(project_id, x_com_zoho_subscriptions_organizationid)
        print("The response of TasksApi->projects_project_id_tasks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->projects_project_id_tasks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**ListTasksResponse**](ListTasksResponse.md)

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

# **projects_project_id_tasks_post**
> AddATaskResponse projects_project_id_tasks_post(project_id, x_com_zoho_subscriptions_organizationid, add_a_task_request=add_a_task_request)

Add a task

Adding a new task to a project.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_tasks
from ls_zoho_billing_tasks.models.add_a_task_request import AddATaskRequest
from ls_zoho_billing_tasks.models.add_a_task_response import AddATaskResponse
from ls_zoho_billing_tasks.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_tasks.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_tasks.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_tasks.TasksApi(api_client)
    project_id = '90300000072369' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    add_a_task_request = ls_zoho_billing_tasks.AddATaskRequest() # AddATaskRequest |  (optional)

    try:
        # Add a task
        api_response = api_instance.projects_project_id_tasks_post(project_id, x_com_zoho_subscriptions_organizationid, add_a_task_request=add_a_task_request)
        print("The response of TasksApi->projects_project_id_tasks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->projects_project_id_tasks_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **add_a_task_request** | [**AddATaskRequest**](AddATaskRequest.md)|  | [optional] 

### Return type

[**AddATaskResponse**](AddATaskResponse.md)

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

# **projects_project_id_tasks_task_id_delete**
> DeleteATaskResponse projects_project_id_tasks_task_id_delete(project_id, x_com_zoho_subscriptions_organizationid, task_id)

Delete a Task

Delete a task added to a project.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_tasks
from ls_zoho_billing_tasks.models.delete_a_task_response import DeleteATaskResponse
from ls_zoho_billing_tasks.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_tasks.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_tasks.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_tasks.TasksApi(api_client)
    project_id = '90300000072369' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    task_id = '90300000072369' # str | 

    try:
        # Delete a Task
        api_response = api_instance.projects_project_id_tasks_task_id_delete(project_id, x_com_zoho_subscriptions_organizationid, task_id)
        print("The response of TasksApi->projects_project_id_tasks_task_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->projects_project_id_tasks_task_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **task_id** | **str**|  | 

### Return type

[**DeleteATaskResponse**](DeleteATaskResponse.md)

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

# **projects_project_id_tasks_task_id_get**
> GetATaskResponse projects_project_id_tasks_task_id_get(project_id, x_com_zoho_subscriptions_organizationid, task_id)

Get a task

Get the details of a task.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_tasks
from ls_zoho_billing_tasks.models.get_a_task_response import GetATaskResponse
from ls_zoho_billing_tasks.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_tasks.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_tasks.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_tasks.TasksApi(api_client)
    project_id = '90300000072369' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    task_id = '90300000072369' # str | 

    try:
        # Get a task
        api_response = api_instance.projects_project_id_tasks_task_id_get(project_id, x_com_zoho_subscriptions_organizationid, task_id)
        print("The response of TasksApi->projects_project_id_tasks_task_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->projects_project_id_tasks_task_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **task_id** | **str**|  | 

### Return type

[**GetATaskResponse**](GetATaskResponse.md)

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

# **projects_project_id_tasks_task_id_put**
> UpdateATaskResponse projects_project_id_tasks_task_id_put(project_id, x_com_zoho_subscriptions_organizationid, task_id, update_a_task_request=update_a_task_request)

Update a task

Update the details of an existing task.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_tasks
from ls_zoho_billing_tasks.models.update_a_task_request import UpdateATaskRequest
from ls_zoho_billing_tasks.models.update_a_task_response import UpdateATaskResponse
from ls_zoho_billing_tasks.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_tasks.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_tasks.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_tasks.TasksApi(api_client)
    project_id = '90300000072369' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    task_id = '90300000072369' # str | 
    update_a_task_request = ls_zoho_billing_tasks.UpdateATaskRequest() # UpdateATaskRequest |  (optional)

    try:
        # Update a task
        api_response = api_instance.projects_project_id_tasks_task_id_put(project_id, x_com_zoho_subscriptions_organizationid, task_id, update_a_task_request=update_a_task_request)
        print("The response of TasksApi->projects_project_id_tasks_task_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->projects_project_id_tasks_task_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **task_id** | **str**|  | 
 **update_a_task_request** | [**UpdateATaskRequest**](UpdateATaskRequest.md)|  | [optional] 

### Return type

[**UpdateATaskResponse**](UpdateATaskResponse.md)

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

