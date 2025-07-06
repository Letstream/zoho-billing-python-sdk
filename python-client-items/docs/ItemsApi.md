# ls_zoho_billing_items.ItemsApi

All URIs are relative to *https://www.zohoapis.com/billing/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**items_get**](ItemsApi.md#items_get) | **GET** /items | List items
[**items_item_id_active_post**](ItemsApi.md#items_item_id_active_post) | **POST** /items/{item_id}/active | Mark as active
[**items_item_id_delete**](ItemsApi.md#items_item_id_delete) | **DELETE** /items/{item_id} | Delete an item
[**items_item_id_get**](ItemsApi.md#items_item_id_get) | **GET** /items/{item_id} | Retrieve an item
[**items_item_id_inactive_post**](ItemsApi.md#items_item_id_inactive_post) | **POST** /items/{item_id}/inactive | Mark as inactive
[**items_item_id_put**](ItemsApi.md#items_item_id_put) | **PUT** /items/{item_id} | Update an item
[**items_post**](ItemsApi.md#items_post) | **POST** /items | Create an Item


# **items_get**
> ListItemsResponse items_get(x_com_zoho_subscriptions_organizationid, name=name, description=description, rate=rate, tax_id=tax_id, filter_by=filter_by, search_text=search_text, sort_column=sort_column)

List items

Get the list of all active items with pagination.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_items
from ls_zoho_billing_items.models.list_items_response import ListItemsResponse
from ls_zoho_billing_items.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_items.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_items.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_items.ItemsApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    name = 'Hard Drive' # str | Search items by name. <code>Maximum length [100]</code>. Variants: <code>name_startswith</code> and <code>name_contains</code> (optional)
    description = '500GB' # str | Search items by description. <code>Maximum length [100]</code>. Variants: <code>description_startswith</code> and <code>description_contains</code> (optional)
    rate = '120' # str | Search items by rate. Variants: <code>rate_less_than</code>, <code>rate_less_equals</code>, <code>rate_greater_than</code> and <code>rate_greater_equals</code> (optional)
    tax_id = '982000000037049' # str | Search items by tax id. (optional)
    filter_by = '' # str | Filter items by status. Allowed Values: <code>Status.All</code>, <code>Status.Active</code> and <code>Status.Inactive</code> (optional)
    search_text = '' # str | Search items by name or description. <code>Maximum length [100]</code> (optional)
    sort_column = '' # str | Sort items. Allowed Values: <code>name</code>, <code>rate</code> and <code>tax_name</code> (optional)

    try:
        # List items
        api_response = api_instance.items_get(x_com_zoho_subscriptions_organizationid, name=name, description=description, rate=rate, tax_id=tax_id, filter_by=filter_by, search_text=search_text, sort_column=sort_column)
        print("The response of ItemsApi->items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **name** | **str**| Search items by name. &lt;code&gt;Maximum length [100]&lt;/code&gt;. Variants: &lt;code&gt;name_startswith&lt;/code&gt; and &lt;code&gt;name_contains&lt;/code&gt; | [optional] 
 **description** | **str**| Search items by description. &lt;code&gt;Maximum length [100]&lt;/code&gt;. Variants: &lt;code&gt;description_startswith&lt;/code&gt; and &lt;code&gt;description_contains&lt;/code&gt; | [optional] 
 **rate** | **str**| Search items by rate. Variants: &lt;code&gt;rate_less_than&lt;/code&gt;, &lt;code&gt;rate_less_equals&lt;/code&gt;, &lt;code&gt;rate_greater_than&lt;/code&gt; and &lt;code&gt;rate_greater_equals&lt;/code&gt; | [optional] 
 **tax_id** | **str**| Search items by tax id. | [optional] 
 **filter_by** | **str**| Filter items by status. Allowed Values: &lt;code&gt;Status.All&lt;/code&gt;, &lt;code&gt;Status.Active&lt;/code&gt; and &lt;code&gt;Status.Inactive&lt;/code&gt; | [optional] 
 **search_text** | **str**| Search items by name or description. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
 **sort_column** | **str**| Sort items. Allowed Values: &lt;code&gt;name&lt;/code&gt;, &lt;code&gt;rate&lt;/code&gt; and &lt;code&gt;tax_name&lt;/code&gt; | [optional] 

### Return type

[**ListItemsResponse**](ListItemsResponse.md)

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

# **items_item_id_active_post**
> MarkAsActiveResponse items_item_id_active_post(item_id, x_com_zoho_subscriptions_organizationid)

Mark as active

Mark an inactive item as active.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_items
from ls_zoho_billing_items.models.mark_as_active_response import MarkAsActiveResponse
from ls_zoho_billing_items.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_items.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_items.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_items.ItemsApi(api_client)
    item_id = '903000000045027' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Mark as active
        api_response = api_instance.items_item_id_active_post(item_id, x_com_zoho_subscriptions_organizationid)
        print("The response of ItemsApi->items_item_id_active_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->items_item_id_active_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**MarkAsActiveResponse**](MarkAsActiveResponse.md)

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

# **items_item_id_delete**
> DeleteAnItemResponse items_item_id_delete(item_id, x_com_zoho_subscriptions_organizationid)

Delete an item

Delete an existing item. Items that are part of a transaction cannot be deleted.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_items
from ls_zoho_billing_items.models.delete_an_item_response import DeleteAnItemResponse
from ls_zoho_billing_items.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_items.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_items.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_items.ItemsApi(api_client)
    item_id = '903000000045027' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Delete an item
        api_response = api_instance.items_item_id_delete(item_id, x_com_zoho_subscriptions_organizationid)
        print("The response of ItemsApi->items_item_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->items_item_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**DeleteAnItemResponse**](DeleteAnItemResponse.md)

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

# **items_item_id_get**
> RetrieveAnItemResponse items_item_id_get(item_id, x_com_zoho_subscriptions_organizationid)

Retrieve an item

Fetch details of an existing item.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_items
from ls_zoho_billing_items.models.retrieve_an_item_response import RetrieveAnItemResponse
from ls_zoho_billing_items.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_items.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_items.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_items.ItemsApi(api_client)
    item_id = '903000000045027' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Retrieve an item
        api_response = api_instance.items_item_id_get(item_id, x_com_zoho_subscriptions_organizationid)
        print("The response of ItemsApi->items_item_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->items_item_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**RetrieveAnItemResponse**](RetrieveAnItemResponse.md)

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

# **items_item_id_inactive_post**
> MarkAsInactiveResponse items_item_id_inactive_post(item_id, x_com_zoho_subscriptions_organizationid)

Mark as inactive

Mark an active item as inactive.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_items
from ls_zoho_billing_items.models.mark_as_inactive_response import MarkAsInactiveResponse
from ls_zoho_billing_items.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_items.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_items.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_items.ItemsApi(api_client)
    item_id = '903000000045027' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Mark as inactive
        api_response = api_instance.items_item_id_inactive_post(item_id, x_com_zoho_subscriptions_organizationid)
        print("The response of ItemsApi->items_item_id_inactive_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->items_item_id_inactive_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**MarkAsInactiveResponse**](MarkAsInactiveResponse.md)

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

# **items_item_id_put**
> UpdateAnItemResponse items_item_id_put(item_id, x_com_zoho_subscriptions_organizationid, update_an_item_request=update_an_item_request)

Update an item

Update the details of an existing item.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_items
from ls_zoho_billing_items.models.update_an_item_request import UpdateAnItemRequest
from ls_zoho_billing_items.models.update_an_item_response import UpdateAnItemResponse
from ls_zoho_billing_items.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_items.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_items.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_items.ItemsApi(api_client)
    item_id = '903000000045027' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    update_an_item_request = ls_zoho_billing_items.UpdateAnItemRequest() # UpdateAnItemRequest |  (optional)

    try:
        # Update an item
        api_response = api_instance.items_item_id_put(item_id, x_com_zoho_subscriptions_organizationid, update_an_item_request=update_an_item_request)
        print("The response of ItemsApi->items_item_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->items_item_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **update_an_item_request** | [**UpdateAnItemRequest**](UpdateAnItemRequest.md)|  | [optional] 

### Return type

[**UpdateAnItemResponse**](UpdateAnItemResponse.md)

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

# **items_post**
> CreateAnItemResponse items_post(x_com_zoho_subscriptions_organizationid, create_an_item_request=create_an_item_request)

Create an Item

Create a new item.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_items
from ls_zoho_billing_items.models.create_an_item_request import CreateAnItemRequest
from ls_zoho_billing_items.models.create_an_item_response import CreateAnItemResponse
from ls_zoho_billing_items.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_items.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_items.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_items.ItemsApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    create_an_item_request = ls_zoho_billing_items.CreateAnItemRequest() # CreateAnItemRequest |  (optional)

    try:
        # Create an Item
        api_response = api_instance.items_post(x_com_zoho_subscriptions_organizationid, create_an_item_request=create_an_item_request)
        print("The response of ItemsApi->items_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **create_an_item_request** | [**CreateAnItemRequest**](CreateAnItemRequest.md)|  | [optional] 

### Return type

[**CreateAnItemResponse**](CreateAnItemResponse.md)

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

