# ls_zoho_billing_plans.PlansApi

All URIs are relative to *https://www.zohoapis.com/billing/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**plans_get**](PlansApi.md#plans_get) | **GET** /plans | List all plans
[**plans_plan_code_delete**](PlansApi.md#plans_plan_code_delete) | **DELETE** /plans/{plan_code} | Delete a plan
[**plans_plan_code_get**](PlansApi.md#plans_plan_code_get) | **GET** /plans/{plan_code} | Retrieve a plan
[**plans_plan_code_markasactive_post**](PlansApi.md#plans_plan_code_markasactive_post) | **POST** /plans/{plan_code}/markasactive | Mark as active
[**plans_plan_code_markasinactive_post**](PlansApi.md#plans_plan_code_markasinactive_post) | **POST** /plans/{plan_code}/markasinactive | Mark as inactive
[**plans_plan_code_put**](PlansApi.md#plans_plan_code_put) | **PUT** /plans/{plan_code} | Update a plan
[**plans_post**](PlansApi.md#plans_post) | **POST** /plans | Create a plan


# **plans_get**
> ListAllPlansResponse plans_get(x_com_zoho_subscriptions_organizationid, filter_by=filter_by, product_id=product_id)

List all plans

List of all plans created.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_plans
from ls_zoho_billing_plans.models.list_all_plans_response import ListAllPlansResponse
from ls_zoho_billing_plans.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_plans.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_plans.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_plans.PlansApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    filter_by = 'PlanStatus.ACTIVE' # str | To list plans based on the Status, use the parameter <code>filter_by</code>. The allowed values for filter_by are PlanStatus.(<code>All</code>, <code>ACTIVE</code> and <code>INACTIVE</code>). (optional)
    product_id = '903000000045027' # str | To list plans of a particular product use the parameter <code>product_id</code>.  (optional)

    try:
        # List all plans
        api_response = api_instance.plans_get(x_com_zoho_subscriptions_organizationid, filter_by=filter_by, product_id=product_id)
        print("The response of PlansApi->plans_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlansApi->plans_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **filter_by** | **str**| To list plans based on the Status, use the parameter &lt;code&gt;filter_by&lt;/code&gt;. The allowed values for filter_by are PlanStatus.(&lt;code&gt;All&lt;/code&gt;, &lt;code&gt;ACTIVE&lt;/code&gt; and &lt;code&gt;INACTIVE&lt;/code&gt;). | [optional] 
 **product_id** | **str**| To list plans of a particular product use the parameter &lt;code&gt;product_id&lt;/code&gt;.  | [optional] 

### Return type

[**ListAllPlansResponse**](ListAllPlansResponse.md)

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

# **plans_plan_code_delete**
> DeleteAPlanResponse plans_plan_code_delete(plan_code, x_com_zoho_subscriptions_organizationid)

Delete a plan

Delete an existing plan. A plan can only be deleted if it has no transactions associated with it.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_plans
from ls_zoho_billing_plans.models.delete_a_plan_response import DeleteAPlanResponse
from ls_zoho_billing_plans.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_plans.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_plans.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_plans.PlansApi(api_client)
    plan_code = 'basic-monthly' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Delete a plan
        api_response = api_instance.plans_plan_code_delete(plan_code, x_com_zoho_subscriptions_organizationid)
        print("The response of PlansApi->plans_plan_code_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlansApi->plans_plan_code_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_code** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**DeleteAPlanResponse**](DeleteAPlanResponse.md)

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

# **plans_plan_code_get**
> RetrieveAPlanResponse plans_plan_code_get(plan_code, x_com_zoho_subscriptions_organizationid)

Retrieve a plan

Retrieve details of an existing plan.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_plans
from ls_zoho_billing_plans.models.retrieve_a_plan_response import RetrieveAPlanResponse
from ls_zoho_billing_plans.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_plans.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_plans.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_plans.PlansApi(api_client)
    plan_code = 'basic-monthly' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Retrieve a plan
        api_response = api_instance.plans_plan_code_get(plan_code, x_com_zoho_subscriptions_organizationid)
        print("The response of PlansApi->plans_plan_code_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlansApi->plans_plan_code_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_code** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**RetrieveAPlanResponse**](RetrieveAPlanResponse.md)

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

# **plans_plan_code_markasactive_post**
> MarkAsActiveResponse plans_plan_code_markasactive_post(plan_code, x_com_zoho_subscriptions_organizationid)

Mark as active

Change the status of the plan to <strong>active</strong>.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_plans
from ls_zoho_billing_plans.models.mark_as_active_response import MarkAsActiveResponse
from ls_zoho_billing_plans.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_plans.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_plans.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_plans.PlansApi(api_client)
    plan_code = 'basic-monthly' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Mark as active
        api_response = api_instance.plans_plan_code_markasactive_post(plan_code, x_com_zoho_subscriptions_organizationid)
        print("The response of PlansApi->plans_plan_code_markasactive_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlansApi->plans_plan_code_markasactive_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_code** | **str**|  | 
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

# **plans_plan_code_markasinactive_post**
> MarkAsInactiveResponse plans_plan_code_markasinactive_post(plan_code, x_com_zoho_subscriptions_organizationid)

Mark as inactive

Change the status of the plan to <strong>inactive</strong>.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_plans
from ls_zoho_billing_plans.models.mark_as_inactive_response import MarkAsInactiveResponse
from ls_zoho_billing_plans.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_plans.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_plans.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_plans.PlansApi(api_client)
    plan_code = 'basic-monthly' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Mark as inactive
        api_response = api_instance.plans_plan_code_markasinactive_post(plan_code, x_com_zoho_subscriptions_organizationid)
        print("The response of PlansApi->plans_plan_code_markasinactive_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlansApi->plans_plan_code_markasinactive_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_code** | **str**|  | 
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

# **plans_plan_code_put**
> UpdateAPlanResponse plans_plan_code_put(plan_code, x_com_zoho_subscriptions_organizationid, update_a_plan_request=update_a_plan_request)

Update a plan

Update details of an existing plan.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_plans
from ls_zoho_billing_plans.models.update_a_plan_request import UpdateAPlanRequest
from ls_zoho_billing_plans.models.update_a_plan_response import UpdateAPlanResponse
from ls_zoho_billing_plans.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_plans.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_plans.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_plans.PlansApi(api_client)
    plan_code = 'basic-monthly' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    update_a_plan_request = ls_zoho_billing_plans.UpdateAPlanRequest() # UpdateAPlanRequest |  (optional)

    try:
        # Update a plan
        api_response = api_instance.plans_plan_code_put(plan_code, x_com_zoho_subscriptions_organizationid, update_a_plan_request=update_a_plan_request)
        print("The response of PlansApi->plans_plan_code_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlansApi->plans_plan_code_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_code** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **update_a_plan_request** | [**UpdateAPlanRequest**](UpdateAPlanRequest.md)|  | [optional] 

### Return type

[**UpdateAPlanResponse**](UpdateAPlanResponse.md)

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

# **plans_post**
> CreateAPlanResponse plans_post(x_com_zoho_subscriptions_organizationid, create_a_plan_request=create_a_plan_request)

Create a plan

Create a new plan.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_plans
from ls_zoho_billing_plans.models.create_a_plan_request import CreateAPlanRequest
from ls_zoho_billing_plans.models.create_a_plan_response import CreateAPlanResponse
from ls_zoho_billing_plans.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_plans.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_plans.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_plans.PlansApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    create_a_plan_request = ls_zoho_billing_plans.CreateAPlanRequest() # CreateAPlanRequest |  (optional)

    try:
        # Create a plan
        api_response = api_instance.plans_post(x_com_zoho_subscriptions_organizationid, create_a_plan_request=create_a_plan_request)
        print("The response of PlansApi->plans_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlansApi->plans_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **create_a_plan_request** | [**CreateAPlanRequest**](CreateAPlanRequest.md)|  | [optional] 

### Return type

[**CreateAPlanResponse**](CreateAPlanResponse.md)

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

