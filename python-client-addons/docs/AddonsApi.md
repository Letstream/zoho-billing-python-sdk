# ls_zoho_billing_addons.AddonsApi

All URIs are relative to *https://www.zohoapis.com/billing/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addons_addon_code_delete**](AddonsApi.md#addons_addon_code_delete) | **DELETE** /addons/{addon_code} | Delete an addon
[**addons_addon_code_get**](AddonsApi.md#addons_addon_code_get) | **GET** /addons/{addon_code} | Retrieve an addon
[**addons_addon_code_markasactive_post**](AddonsApi.md#addons_addon_code_markasactive_post) | **POST** /addons/{addon_code}/markasactive | Mark as active
[**addons_addon_code_markasinactive_post**](AddonsApi.md#addons_addon_code_markasinactive_post) | **POST** /addons/{addon_code}/markasinactive | Mark as inactive
[**addons_addon_code_put**](AddonsApi.md#addons_addon_code_put) | **PUT** /addons/{addon_code} | Update an addon
[**addons_get**](AddonsApi.md#addons_get) | **GET** /addons | List all addons
[**addons_post**](AddonsApi.md#addons_post) | **POST** /addons | Create an addon


# **addons_addon_code_delete**
> DeleteAnAddonResponse addons_addon_code_delete(addon_code, x_com_zoho_subscriptions_organizationid)

Delete an addon

Delete an existing addon.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_addons
from ls_zoho_billing_addons.models.delete_an_addon_response import DeleteAnAddonResponse
from ls_zoho_billing_addons.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_addons.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_addons.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_addons.AddonsApi(api_client)
    addon_code = 'Email-basic' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Delete an addon
        api_response = api_instance.addons_addon_code_delete(addon_code, x_com_zoho_subscriptions_organizationid)
        print("The response of AddonsApi->addons_addon_code_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddonsApi->addons_addon_code_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_code** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**DeleteAnAddonResponse**](DeleteAnAddonResponse.md)

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

# **addons_addon_code_get**
> RetrieveAnAddonResponse addons_addon_code_get(addon_code, x_com_zoho_subscriptions_organizationid)

Retrieve an addon

Details for an existing Addon.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_addons
from ls_zoho_billing_addons.models.retrieve_an_addon_response import RetrieveAnAddonResponse
from ls_zoho_billing_addons.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_addons.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_addons.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_addons.AddonsApi(api_client)
    addon_code = 'Email-basic' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Retrieve an addon
        api_response = api_instance.addons_addon_code_get(addon_code, x_com_zoho_subscriptions_organizationid)
        print("The response of AddonsApi->addons_addon_code_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddonsApi->addons_addon_code_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_code** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**RetrieveAnAddonResponse**](RetrieveAnAddonResponse.md)

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

# **addons_addon_code_markasactive_post**
> MarkAsActiveResponse addons_addon_code_markasactive_post(addon_code, x_com_zoho_subscriptions_organizationid)

Mark as active

Change status of the addon to <strong>active</strong>.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_addons
from ls_zoho_billing_addons.models.mark_as_active_response import MarkAsActiveResponse
from ls_zoho_billing_addons.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_addons.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_addons.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_addons.AddonsApi(api_client)
    addon_code = 'Email-basic' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Mark as active
        api_response = api_instance.addons_addon_code_markasactive_post(addon_code, x_com_zoho_subscriptions_organizationid)
        print("The response of AddonsApi->addons_addon_code_markasactive_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddonsApi->addons_addon_code_markasactive_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_code** | **str**|  | 
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

# **addons_addon_code_markasinactive_post**
> MarkAsInactiveResponse addons_addon_code_markasinactive_post(addon_code, x_com_zoho_subscriptions_organizationid)

Mark as inactive

Change status of the addon to <strong>inactive</strong>.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_addons
from ls_zoho_billing_addons.models.mark_as_inactive_response import MarkAsInactiveResponse
from ls_zoho_billing_addons.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_addons.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_addons.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_addons.AddonsApi(api_client)
    addon_code = 'Email-basic' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Mark as inactive
        api_response = api_instance.addons_addon_code_markasinactive_post(addon_code, x_com_zoho_subscriptions_organizationid)
        print("The response of AddonsApi->addons_addon_code_markasinactive_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddonsApi->addons_addon_code_markasinactive_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_code** | **str**|  | 
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

# **addons_addon_code_put**
> UpdateAnAddonResponse addons_addon_code_put(addon_code, x_com_zoho_subscriptions_organizationid, update_an_addon_request=update_an_addon_request)

Update an addon

Update details of an existing addon.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_addons
from ls_zoho_billing_addons.models.update_an_addon_request import UpdateAnAddonRequest
from ls_zoho_billing_addons.models.update_an_addon_response import UpdateAnAddonResponse
from ls_zoho_billing_addons.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_addons.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_addons.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_addons.AddonsApi(api_client)
    addon_code = 'Email-basic' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    update_an_addon_request = ls_zoho_billing_addons.UpdateAnAddonRequest() # UpdateAnAddonRequest |  (optional)

    try:
        # Update an addon
        api_response = api_instance.addons_addon_code_put(addon_code, x_com_zoho_subscriptions_organizationid, update_an_addon_request=update_an_addon_request)
        print("The response of AddonsApi->addons_addon_code_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddonsApi->addons_addon_code_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_code** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **update_an_addon_request** | [**UpdateAnAddonRequest**](UpdateAnAddonRequest.md)|  | [optional] 

### Return type

[**UpdateAnAddonResponse**](UpdateAnAddonResponse.md)

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

# **addons_get**
> ListAllAddonsResponse addons_get(x_com_zoho_subscriptions_organizationid, filter_by=filter_by, product_id=product_id)

List all addons

List of all addons.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_addons
from ls_zoho_billing_addons.models.list_all_addons_response import ListAllAddonsResponse
from ls_zoho_billing_addons.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_addons.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_addons.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_addons.AddonsApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    filter_by = 'AddonStatus.All' # str | To list plans based on the Status, use the parameter <code>filter_by</code>. The allowed values for filter_by are AddonStatus.(<code>All</code>, <code>ACTIVE</code>, <code>INACTIVE</code>,<code>ONETIME</code> and <code>RECURRING</code>) (optional)
    product_id = '903000000045027' # str | To list addons of a particular product use the parameter <code>product_id</code>. (optional)

    try:
        # List all addons
        api_response = api_instance.addons_get(x_com_zoho_subscriptions_organizationid, filter_by=filter_by, product_id=product_id)
        print("The response of AddonsApi->addons_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddonsApi->addons_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **filter_by** | **str**| To list plans based on the Status, use the parameter &lt;code&gt;filter_by&lt;/code&gt;. The allowed values for filter_by are AddonStatus.(&lt;code&gt;All&lt;/code&gt;, &lt;code&gt;ACTIVE&lt;/code&gt;, &lt;code&gt;INACTIVE&lt;/code&gt;,&lt;code&gt;ONETIME&lt;/code&gt; and &lt;code&gt;RECURRING&lt;/code&gt;) | [optional] 
 **product_id** | **str**| To list addons of a particular product use the parameter &lt;code&gt;product_id&lt;/code&gt;. | [optional] 

### Return type

[**ListAllAddonsResponse**](ListAllAddonsResponse.md)

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

# **addons_post**
> CreateAnAddonResponse addons_post(x_com_zoho_subscriptions_organizationid, create_an_addon_request=create_an_addon_request)

Create an addon

Create a new addon.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_addons
from ls_zoho_billing_addons.models.create_an_addon_request import CreateAnAddonRequest
from ls_zoho_billing_addons.models.create_an_addon_response import CreateAnAddonResponse
from ls_zoho_billing_addons.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_addons.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_addons.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_addons.AddonsApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    create_an_addon_request = ls_zoho_billing_addons.CreateAnAddonRequest() # CreateAnAddonRequest |  (optional)

    try:
        # Create an addon
        api_response = api_instance.addons_post(x_com_zoho_subscriptions_organizationid, create_an_addon_request=create_an_addon_request)
        print("The response of AddonsApi->addons_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddonsApi->addons_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **create_an_addon_request** | [**CreateAnAddonRequest**](CreateAnAddonRequest.md)|  | [optional] 

### Return type

[**CreateAnAddonResponse**](CreateAnAddonResponse.md)

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

