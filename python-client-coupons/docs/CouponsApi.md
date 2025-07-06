# ls_zoho_billing_coupons.CouponsApi

All URIs are relative to *https://www.zohoapis.com/billing/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**coupons_coupon_code_delete**](CouponsApi.md#coupons_coupon_code_delete) | **DELETE** /coupons/{coupon_code} | Delete a coupon
[**coupons_coupon_code_get**](CouponsApi.md#coupons_coupon_code_get) | **GET** /coupons/{coupon_code} | Retrieve a coupon
[**coupons_coupon_code_markasactive_post**](CouponsApi.md#coupons_coupon_code_markasactive_post) | **POST** /coupons/{coupon_code}/markasactive | Mark as active
[**coupons_coupon_code_markasinactive_post**](CouponsApi.md#coupons_coupon_code_markasinactive_post) | **POST** /coupons/{coupon_code}/markasinactive | Mark as inactive
[**coupons_coupon_code_put**](CouponsApi.md#coupons_coupon_code_put) | **PUT** /coupons/{coupon_code} | Update a coupon
[**coupons_get**](CouponsApi.md#coupons_get) | **GET** /coupons | List all coupons
[**coupons_post**](CouponsApi.md#coupons_post) | **POST** /coupons | Create an coupon


# **coupons_coupon_code_delete**
> DeleteACouponResponse coupons_coupon_code_delete(coupon_code, x_com_zoho_subscriptions_organizationid)

Delete a coupon

Delete an existing coupon.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_coupons
from ls_zoho_billing_coupons.models.delete_a_coupon_response import DeleteACouponResponse
from ls_zoho_billing_coupons.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_coupons.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_coupons.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_coupons.CouponsApi(api_client)
    coupon_code = 'THANKSGIVING20' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Delete a coupon
        api_response = api_instance.coupons_coupon_code_delete(coupon_code, x_com_zoho_subscriptions_organizationid)
        print("The response of CouponsApi->coupons_coupon_code_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CouponsApi->coupons_coupon_code_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_code** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**DeleteACouponResponse**](DeleteACouponResponse.md)

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

# **coupons_coupon_code_get**
> RetrieveACouponResponse coupons_coupon_code_get(coupon_code, x_com_zoho_subscriptions_organizationid)

Retrieve a coupon

Details of an existing coupon.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_coupons
from ls_zoho_billing_coupons.models.retrieve_a_coupon_response import RetrieveACouponResponse
from ls_zoho_billing_coupons.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_coupons.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_coupons.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_coupons.CouponsApi(api_client)
    coupon_code = 'THANKSGIVING20' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Retrieve a coupon
        api_response = api_instance.coupons_coupon_code_get(coupon_code, x_com_zoho_subscriptions_organizationid)
        print("The response of CouponsApi->coupons_coupon_code_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CouponsApi->coupons_coupon_code_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_code** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**RetrieveACouponResponse**](RetrieveACouponResponse.md)

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

# **coupons_coupon_code_markasactive_post**
> MarkAsActiveResponse coupons_coupon_code_markasactive_post(coupon_code, x_com_zoho_subscriptions_organizationid)

Mark as active

status of the coupon will be changed to <strong>active</strong>.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_coupons
from ls_zoho_billing_coupons.models.mark_as_active_response import MarkAsActiveResponse
from ls_zoho_billing_coupons.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_coupons.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_coupons.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_coupons.CouponsApi(api_client)
    coupon_code = 'THANKSGIVING20' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Mark as active
        api_response = api_instance.coupons_coupon_code_markasactive_post(coupon_code, x_com_zoho_subscriptions_organizationid)
        print("The response of CouponsApi->coupons_coupon_code_markasactive_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CouponsApi->coupons_coupon_code_markasactive_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_code** | **str**|  | 
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

# **coupons_coupon_code_markasinactive_post**
> MarkAsInactiveResponse coupons_coupon_code_markasinactive_post(coupon_code, x_com_zoho_subscriptions_organizationid)

Mark as inactive

status of the coupon will be changed to <strong>inactive</strong>.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_coupons
from ls_zoho_billing_coupons.models.mark_as_inactive_response import MarkAsInactiveResponse
from ls_zoho_billing_coupons.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_coupons.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_coupons.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_coupons.CouponsApi(api_client)
    coupon_code = 'THANKSGIVING20' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Mark as inactive
        api_response = api_instance.coupons_coupon_code_markasinactive_post(coupon_code, x_com_zoho_subscriptions_organizationid)
        print("The response of CouponsApi->coupons_coupon_code_markasinactive_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CouponsApi->coupons_coupon_code_markasinactive_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_code** | **str**|  | 
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

# **coupons_coupon_code_put**
> UpdateACouponResponse coupons_coupon_code_put(coupon_code, x_com_zoho_subscriptions_organizationid, update_a_coupon_request=update_a_coupon_request)

Update a coupon

Update details of an existing coupon.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_coupons
from ls_zoho_billing_coupons.models.update_a_coupon_request import UpdateACouponRequest
from ls_zoho_billing_coupons.models.update_a_coupon_response import UpdateACouponResponse
from ls_zoho_billing_coupons.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_coupons.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_coupons.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_coupons.CouponsApi(api_client)
    coupon_code = 'THANKSGIVING20' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    update_a_coupon_request = ls_zoho_billing_coupons.UpdateACouponRequest() # UpdateACouponRequest |  (optional)

    try:
        # Update a coupon
        api_response = api_instance.coupons_coupon_code_put(coupon_code, x_com_zoho_subscriptions_organizationid, update_a_coupon_request=update_a_coupon_request)
        print("The response of CouponsApi->coupons_coupon_code_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CouponsApi->coupons_coupon_code_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_code** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **update_a_coupon_request** | [**UpdateACouponRequest**](UpdateACouponRequest.md)|  | [optional] 

### Return type

[**UpdateACouponResponse**](UpdateACouponResponse.md)

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

# **coupons_get**
> ListAllCouponsResponse coupons_get(x_com_zoho_subscriptions_organizationid, filter_by=filter_by, product_id=product_id)

List all coupons

List of all coupons.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_coupons
from ls_zoho_billing_coupons.models.list_all_coupons_response import ListAllCouponsResponse
from ls_zoho_billing_coupons.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_coupons.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_coupons.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_coupons.CouponsApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    filter_by = 'CouponStatus.EXPIRED' # str | To list plans based on the Status, use the parameter <code>filter_by</code>. The allowed values for filter_by are CouponStatus.(<code>All</code>, <code>ACTIVE</code>, <code>INACTIVE</code> and <code>EXPIRED</code>). (optional)
    product_id = '903000000045027' # str | To list Coupons of a particular product use the parameter <code>product_id</code>. (optional)

    try:
        # List all coupons
        api_response = api_instance.coupons_get(x_com_zoho_subscriptions_organizationid, filter_by=filter_by, product_id=product_id)
        print("The response of CouponsApi->coupons_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CouponsApi->coupons_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **filter_by** | **str**| To list plans based on the Status, use the parameter &lt;code&gt;filter_by&lt;/code&gt;. The allowed values for filter_by are CouponStatus.(&lt;code&gt;All&lt;/code&gt;, &lt;code&gt;ACTIVE&lt;/code&gt;, &lt;code&gt;INACTIVE&lt;/code&gt; and &lt;code&gt;EXPIRED&lt;/code&gt;). | [optional] 
 **product_id** | **str**| To list Coupons of a particular product use the parameter &lt;code&gt;product_id&lt;/code&gt;. | [optional] 

### Return type

[**ListAllCouponsResponse**](ListAllCouponsResponse.md)

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

# **coupons_post**
> CreateAnCouponResponse coupons_post(x_com_zoho_subscriptions_organizationid, create_an_coupon_request=create_an_coupon_request)

Create an coupon

Create a new coupon.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_coupons
from ls_zoho_billing_coupons.models.create_an_coupon_request import CreateAnCouponRequest
from ls_zoho_billing_coupons.models.create_an_coupon_response import CreateAnCouponResponse
from ls_zoho_billing_coupons.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_coupons.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_coupons.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_coupons.CouponsApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    create_an_coupon_request = ls_zoho_billing_coupons.CreateAnCouponRequest() # CreateAnCouponRequest |  (optional)

    try:
        # Create an coupon
        api_response = api_instance.coupons_post(x_com_zoho_subscriptions_organizationid, create_an_coupon_request=create_an_coupon_request)
        print("The response of CouponsApi->coupons_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CouponsApi->coupons_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **create_an_coupon_request** | [**CreateAnCouponRequest**](CreateAnCouponRequest.md)|  | [optional] 

### Return type

[**CreateAnCouponResponse**](CreateAnCouponResponse.md)

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

