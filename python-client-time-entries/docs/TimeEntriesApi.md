# ls_zoho_billing_time_entries.TimeEntriesApi

All URIs are relative to *https://www.zohoapis.com/billing/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projects_timeentries_delete**](TimeEntriesApi.md#projects_timeentries_delete) | **DELETE** /projects/timeentries | Delete time entries
[**projects_timeentries_get**](TimeEntriesApi.md#projects_timeentries_get) | **GET** /projects/timeentries | List time entries.
[**projects_timeentries_post**](TimeEntriesApi.md#projects_timeentries_post) | **POST** /projects/timeentries | Log time entries
[**projects_timeentries_runningtimer_me_get**](TimeEntriesApi.md#projects_timeentries_runningtimer_me_get) | **GET** /projects/timeentries/runningtimer/me | Get timer
[**projects_timeentries_time_entry_id_delete**](TimeEntriesApi.md#projects_timeentries_time_entry_id_delete) | **DELETE** /projects/timeentries/{time_entry_id} | Delete time entry
[**projects_timeentries_time_entry_id_get**](TimeEntriesApi.md#projects_timeentries_time_entry_id_get) | **GET** /projects/timeentries/{time_entry_id} | Get a time entry
[**projects_timeentries_time_entry_id_put**](TimeEntriesApi.md#projects_timeentries_time_entry_id_put) | **PUT** /projects/timeentries/{time_entry_id} | Update time entry
[**projects_timeentries_time_entry_id_timer_start_post**](TimeEntriesApi.md#projects_timeentries_time_entry_id_timer_start_post) | **POST** /projects/timeentries/{time_entry_id}/timer/start | Start timer
[**projects_timeentries_timer_stop_post**](TimeEntriesApi.md#projects_timeentries_timer_stop_post) | **POST** /projects/timeentries/timer/stop | Stop timer


# **projects_timeentries_delete**
> DeleteTimeEntriesResponse projects_timeentries_delete(x_com_zoho_subscriptions_organizationid)

Delete time entries

Deleting time entries.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_time_entries
from ls_zoho_billing_time_entries.models.delete_time_entries_response import DeleteTimeEntriesResponse
from ls_zoho_billing_time_entries.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_time_entries.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_time_entries.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_time_entries.TimeEntriesApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Delete time entries
        api_response = api_instance.projects_timeentries_delete(x_com_zoho_subscriptions_organizationid)
        print("The response of TimeEntriesApi->projects_timeentries_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeEntriesApi->projects_timeentries_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**DeleteTimeEntriesResponse**](DeleteTimeEntriesResponse.md)

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

# **projects_timeentries_get**
> ListTimeEntriesResponse projects_timeentries_get(x_com_zoho_subscriptions_organizationid, from_date=from_date, to_date=to_date, filter_by=filter_by, project_id=project_id, user_id=user_id, sort_column=sort_column)

List time entries.

List all time entries with pagination.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_time_entries
from ls_zoho_billing_time_entries.models.list_time_entries_response import ListTimeEntriesResponse
from ls_zoho_billing_time_entries.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_time_entries.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_time_entries.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_time_entries.TimeEntriesApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    from_date = '2013-09-17' # str | Date from which the time entries logged to be fetched (optional)
    to_date = '2013-10-17' # str | Date up to which the time entries logged to be fetched (optional)
    filter_by = 'Status.Unbilled' # str | Filter time entries by date and status. Allowed Values: <code>Date.All</code>, <code>Date.Today</code>, <code>Date.ThisWeek</code>, <code>Date.ThisMonth</code>, <code>Date.ThisQuarter</code>, <code>Date.ThisYear</code>, <code>Date.PreviousDay</code>, <code>Date.PreviousWeek</code>, <code>Date.PreviousMonth</code>, <code>Date.PreviousQuarter</code>, <code>Date.PreviousYear</code>, <code>Date.CustomDate</code>, <code>Status.Unbilled</code> and <code>Status.Invoiced</code> (optional)
    project_id = '460000000044019' # str | Unique ID of the project (optional)
    user_id = '460000000024003' # str | Unique ID of the user of timesheet. (optional)
    sort_column = 'customer_name' # str | Sort time entries. Allowed Values: <code>project_name</code>, <code>task_name</code>, <code>user_name</code>, <code>log_date</code>, <code>timer_started_at</code> and <code>customer_name</code> (optional)

    try:
        # List time entries.
        api_response = api_instance.projects_timeentries_get(x_com_zoho_subscriptions_organizationid, from_date=from_date, to_date=to_date, filter_by=filter_by, project_id=project_id, user_id=user_id, sort_column=sort_column)
        print("The response of TimeEntriesApi->projects_timeentries_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeEntriesApi->projects_timeentries_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **from_date** | **str**| Date from which the time entries logged to be fetched | [optional] 
 **to_date** | **str**| Date up to which the time entries logged to be fetched | [optional] 
 **filter_by** | **str**| Filter time entries by date and status. Allowed Values: &lt;code&gt;Date.All&lt;/code&gt;, &lt;code&gt;Date.Today&lt;/code&gt;, &lt;code&gt;Date.ThisWeek&lt;/code&gt;, &lt;code&gt;Date.ThisMonth&lt;/code&gt;, &lt;code&gt;Date.ThisQuarter&lt;/code&gt;, &lt;code&gt;Date.ThisYear&lt;/code&gt;, &lt;code&gt;Date.PreviousDay&lt;/code&gt;, &lt;code&gt;Date.PreviousWeek&lt;/code&gt;, &lt;code&gt;Date.PreviousMonth&lt;/code&gt;, &lt;code&gt;Date.PreviousQuarter&lt;/code&gt;, &lt;code&gt;Date.PreviousYear&lt;/code&gt;, &lt;code&gt;Date.CustomDate&lt;/code&gt;, &lt;code&gt;Status.Unbilled&lt;/code&gt; and &lt;code&gt;Status.Invoiced&lt;/code&gt; | [optional] 
 **project_id** | **str**| Unique ID of the project | [optional] 
 **user_id** | **str**| Unique ID of the user of timesheet. | [optional] 
 **sort_column** | **str**| Sort time entries. Allowed Values: &lt;code&gt;project_name&lt;/code&gt;, &lt;code&gt;task_name&lt;/code&gt;, &lt;code&gt;user_name&lt;/code&gt;, &lt;code&gt;log_date&lt;/code&gt;, &lt;code&gt;timer_started_at&lt;/code&gt; and &lt;code&gt;customer_name&lt;/code&gt; | [optional] 

### Return type

[**ListTimeEntriesResponse**](ListTimeEntriesResponse.md)

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

# **projects_timeentries_post**
> LogTimeEntriesResponse projects_timeentries_post(x_com_zoho_subscriptions_organizationid, log_time_entries_request=log_time_entries_request)

Log time entries

Logging time entries.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_time_entries
from ls_zoho_billing_time_entries.models.log_time_entries_request import LogTimeEntriesRequest
from ls_zoho_billing_time_entries.models.log_time_entries_response import LogTimeEntriesResponse
from ls_zoho_billing_time_entries.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_time_entries.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_time_entries.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_time_entries.TimeEntriesApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    log_time_entries_request = ls_zoho_billing_time_entries.LogTimeEntriesRequest() # LogTimeEntriesRequest |  (optional)

    try:
        # Log time entries
        api_response = api_instance.projects_timeentries_post(x_com_zoho_subscriptions_organizationid, log_time_entries_request=log_time_entries_request)
        print("The response of TimeEntriesApi->projects_timeentries_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeEntriesApi->projects_timeentries_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **log_time_entries_request** | [**LogTimeEntriesRequest**](LogTimeEntriesRequest.md)|  | [optional] 

### Return type

[**LogTimeEntriesResponse**](LogTimeEntriesResponse.md)

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

# **projects_timeentries_runningtimer_me_get**
> GetTimerResponse projects_timeentries_runningtimer_me_get(x_com_zoho_subscriptions_organizationid)

Get timer

Get current running timer.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_time_entries
from ls_zoho_billing_time_entries.models.get_timer_response import GetTimerResponse
from ls_zoho_billing_time_entries.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_time_entries.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_time_entries.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_time_entries.TimeEntriesApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Get timer
        api_response = api_instance.projects_timeentries_runningtimer_me_get(x_com_zoho_subscriptions_organizationid)
        print("The response of TimeEntriesApi->projects_timeentries_runningtimer_me_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeEntriesApi->projects_timeentries_runningtimer_me_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**GetTimerResponse**](GetTimerResponse.md)

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

# **projects_timeentries_time_entry_id_delete**
> DeleteTimeEntryResponse projects_timeentries_time_entry_id_delete(time_entry_id, x_com_zoho_subscriptions_organizationid)

Delete time entry

Deleting a logged time entry.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_time_entries
from ls_zoho_billing_time_entries.models.delete_time_entry_response import DeleteTimeEntryResponse
from ls_zoho_billing_time_entries.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_time_entries.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_time_entries.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_time_entries.TimeEntriesApi(api_client)
    time_entry_id = '460000000044021' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Delete time entry
        api_response = api_instance.projects_timeentries_time_entry_id_delete(time_entry_id, x_com_zoho_subscriptions_organizationid)
        print("The response of TimeEntriesApi->projects_timeentries_time_entry_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeEntriesApi->projects_timeentries_time_entry_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_entry_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**DeleteTimeEntryResponse**](DeleteTimeEntryResponse.md)

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

# **projects_timeentries_time_entry_id_get**
> GetATimeEntryResponse projects_timeentries_time_entry_id_get(time_entry_id, x_com_zoho_subscriptions_organizationid)

Get a time entry

Get details of a time entry.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_time_entries
from ls_zoho_billing_time_entries.models.get_a_time_entry_response import GetATimeEntryResponse
from ls_zoho_billing_time_entries.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_time_entries.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_time_entries.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_time_entries.TimeEntriesApi(api_client)
    time_entry_id = '460000000044021' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Get a time entry
        api_response = api_instance.projects_timeentries_time_entry_id_get(time_entry_id, x_com_zoho_subscriptions_organizationid)
        print("The response of TimeEntriesApi->projects_timeentries_time_entry_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeEntriesApi->projects_timeentries_time_entry_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_entry_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**GetATimeEntryResponse**](GetATimeEntryResponse.md)

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

# **projects_timeentries_time_entry_id_put**
> UpdateTimeEntryResponse projects_timeentries_time_entry_id_put(time_entry_id, x_com_zoho_subscriptions_organizationid, update_time_entry_request=update_time_entry_request)

Update time entry

Update logged time entry.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_time_entries
from ls_zoho_billing_time_entries.models.update_time_entry_request import UpdateTimeEntryRequest
from ls_zoho_billing_time_entries.models.update_time_entry_response import UpdateTimeEntryResponse
from ls_zoho_billing_time_entries.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_time_entries.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_time_entries.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_time_entries.TimeEntriesApi(api_client)
    time_entry_id = '460000000044021' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    update_time_entry_request = ls_zoho_billing_time_entries.UpdateTimeEntryRequest() # UpdateTimeEntryRequest |  (optional)

    try:
        # Update time entry
        api_response = api_instance.projects_timeentries_time_entry_id_put(time_entry_id, x_com_zoho_subscriptions_organizationid, update_time_entry_request=update_time_entry_request)
        print("The response of TimeEntriesApi->projects_timeentries_time_entry_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeEntriesApi->projects_timeentries_time_entry_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_entry_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **update_time_entry_request** | [**UpdateTimeEntryRequest**](UpdateTimeEntryRequest.md)|  | [optional] 

### Return type

[**UpdateTimeEntryResponse**](UpdateTimeEntryResponse.md)

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

# **projects_timeentries_time_entry_id_timer_start_post**
> StartTimerResponse projects_timeentries_time_entry_id_timer_start_post(time_entry_id, x_com_zoho_subscriptions_organizationid)

Start timer

Start tracking time spent.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_time_entries
from ls_zoho_billing_time_entries.models.start_timer_response import StartTimerResponse
from ls_zoho_billing_time_entries.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_time_entries.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_time_entries.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_time_entries.TimeEntriesApi(api_client)
    time_entry_id = '460000000044021' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Start timer
        api_response = api_instance.projects_timeentries_time_entry_id_timer_start_post(time_entry_id, x_com_zoho_subscriptions_organizationid)
        print("The response of TimeEntriesApi->projects_timeentries_time_entry_id_timer_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeEntriesApi->projects_timeentries_time_entry_id_timer_start_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_entry_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**StartTimerResponse**](StartTimerResponse.md)

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

# **projects_timeentries_timer_stop_post**
> StopTimerResponse projects_timeentries_timer_stop_post(x_com_zoho_subscriptions_organizationid)

Stop timer

Stop tracking time, say taking a break or leaving.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_time_entries
from ls_zoho_billing_time_entries.models.stop_timer_response import StopTimerResponse
from ls_zoho_billing_time_entries.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_time_entries.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_time_entries.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_time_entries.TimeEntriesApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Stop timer
        api_response = api_instance.projects_timeentries_timer_stop_post(x_com_zoho_subscriptions_organizationid)
        print("The response of TimeEntriesApi->projects_timeentries_timer_stop_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeEntriesApi->projects_timeentries_timer_stop_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**StopTimerResponse**](StopTimerResponse.md)

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

