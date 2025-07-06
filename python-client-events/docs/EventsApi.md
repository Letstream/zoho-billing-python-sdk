# ls_zoho_billing_events.EventsApi

All URIs are relative to *https://www.zohoapis.com/billing/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**events_event_id_get**](EventsApi.md#events_event_id_get) | **GET** /events/{event_id} | Retrieve an event
[**events_get**](EventsApi.md#events_get) | **GET** /events | List of events


# **events_event_id_get**
> RetrieveAnEventResponse events_event_id_get(event_id, x_com_zoho_subscriptions_organizationid)

Retrieve an event

Details of an existing event.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_events
from ls_zoho_billing_events.models.retrieve_an_event_response import RetrieveAnEventResponse
from ls_zoho_billing_events.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_events.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_events.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_events.EventsApi(api_client)
    event_id = '90300000005337' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Retrieve an event
        api_response = api_instance.events_event_id_get(event_id, x_com_zoho_subscriptions_organizationid)
        print("The response of EventsApi->events_event_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_event_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**RetrieveAnEventResponse**](RetrieveAnEventResponse.md)

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

# **events_get**
> ListOfEventsResponse events_get(x_com_zoho_subscriptions_organizationid)

List of events

List of all events.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_events
from ls_zoho_billing_events.models.list_of_events_response import ListOfEventsResponse
from ls_zoho_billing_events.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_events.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_events.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_events.EventsApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # List of events
        api_response = api_instance.events_get(x_com_zoho_subscriptions_organizationid)
        print("The response of EventsApi->events_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**ListOfEventsResponse**](ListOfEventsResponse.md)

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

