# ls_zoho_billing_products.ProductsApi

All URIs are relative to *https://www.zohoapis.com/billing/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**products_get**](ProductsApi.md#products_get) | **GET** /products | List of all products
[**products_post**](ProductsApi.md#products_post) | **POST** /products | Create a product
[**products_product_id_delete**](ProductsApi.md#products_product_id_delete) | **DELETE** /products/{product_id} | Delete a product
[**products_product_id_get**](ProductsApi.md#products_product_id_get) | **GET** /products/{product_id} | Retrieve a product
[**products_product_id_markasactive_post**](ProductsApi.md#products_product_id_markasactive_post) | **POST** /products/{product_id}/markasactive | Mark as active
[**products_product_id_markasinactive_post**](ProductsApi.md#products_product_id_markasinactive_post) | **POST** /products/{product_id}/markasinactive | Mark as inactive
[**products_product_id_put**](ProductsApi.md#products_product_id_put) | **PUT** /products/{product_id} | Update a product


# **products_get**
> ListOfAllProductsResponse products_get(x_com_zoho_subscriptions_organizationid)

List of all products

List of all created products.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_products
from ls_zoho_billing_products.models.list_of_all_products_response import ListOfAllProductsResponse
from ls_zoho_billing_products.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_products.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_products.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_products.ProductsApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # List of all products
        api_response = api_instance.products_get(x_com_zoho_subscriptions_organizationid)
        print("The response of ProductsApi->products_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**ListOfAllProductsResponse**](ListOfAllProductsResponse.md)

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

# **products_post**
> CreateAProductResponse products_post(x_com_zoho_subscriptions_organizationid, create_a_product_request=create_a_product_request)

Create a product

Create a new product.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_products
from ls_zoho_billing_products.models.create_a_product_request import CreateAProductRequest
from ls_zoho_billing_products.models.create_a_product_response import CreateAProductResponse
from ls_zoho_billing_products.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_products.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_products.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_products.ProductsApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    create_a_product_request = ls_zoho_billing_products.CreateAProductRequest() # CreateAProductRequest |  (optional)

    try:
        # Create a product
        api_response = api_instance.products_post(x_com_zoho_subscriptions_organizationid, create_a_product_request=create_a_product_request)
        print("The response of ProductsApi->products_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **create_a_product_request** | [**CreateAProductRequest**](CreateAProductRequest.md)|  | [optional] 

### Return type

[**CreateAProductResponse**](CreateAProductResponse.md)

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

# **products_product_id_delete**
> DeleteAProductResponse products_product_id_delete(product_id, x_com_zoho_subscriptions_organizationid)

Delete a product

Delete an existing product.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_products
from ls_zoho_billing_products.models.delete_a_product_response import DeleteAProductResponse
from ls_zoho_billing_products.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_products.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_products.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_products.ProductsApi(api_client)
    product_id = '903000000045027' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Delete a product
        api_response = api_instance.products_product_id_delete(product_id, x_com_zoho_subscriptions_organizationid)
        print("The response of ProductsApi->products_product_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_product_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**DeleteAProductResponse**](DeleteAProductResponse.md)

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

# **products_product_id_get**
> RetrieveAProductResponse products_product_id_get(product_id, x_com_zoho_subscriptions_organizationid)

Retrieve a product

Details of an existing product.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_products
from ls_zoho_billing_products.models.retrieve_a_product_response import RetrieveAProductResponse
from ls_zoho_billing_products.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_products.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_products.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_products.ProductsApi(api_client)
    product_id = '903000000045027' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Retrieve a product
        api_response = api_instance.products_product_id_get(product_id, x_com_zoho_subscriptions_organizationid)
        print("The response of ProductsApi->products_product_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_product_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**RetrieveAProductResponse**](RetrieveAProductResponse.md)

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

# **products_product_id_markasactive_post**
> MarkAsActiveResponse products_product_id_markasactive_post(product_id, x_com_zoho_subscriptions_organizationid)

Mark as active

The product has been marked as active.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_products
from ls_zoho_billing_products.models.mark_as_active_response import MarkAsActiveResponse
from ls_zoho_billing_products.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_products.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_products.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_products.ProductsApi(api_client)
    product_id = '903000000045027' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Mark as active
        api_response = api_instance.products_product_id_markasactive_post(product_id, x_com_zoho_subscriptions_organizationid)
        print("The response of ProductsApi->products_product_id_markasactive_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_product_id_markasactive_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | 
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

# **products_product_id_markasinactive_post**
> MarkAsInactiveResponse products_product_id_markasinactive_post(product_id, x_com_zoho_subscriptions_organizationid)

Mark as inactive

The product has been marked as inactive.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_products
from ls_zoho_billing_products.models.mark_as_inactive_response import MarkAsInactiveResponse
from ls_zoho_billing_products.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_products.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_products.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_products.ProductsApi(api_client)
    product_id = '903000000045027' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Mark as inactive
        api_response = api_instance.products_product_id_markasinactive_post(product_id, x_com_zoho_subscriptions_organizationid)
        print("The response of ProductsApi->products_product_id_markasinactive_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_product_id_markasinactive_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | 
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

# **products_product_id_put**
> UpdateAProductResponse products_product_id_put(product_id, x_com_zoho_subscriptions_organizationid, update_a_product_request=update_a_product_request)

Update a product

Update details of an existing product.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_products
from ls_zoho_billing_products.models.update_a_product_request import UpdateAProductRequest
from ls_zoho_billing_products.models.update_a_product_response import UpdateAProductResponse
from ls_zoho_billing_products.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_products.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_products.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_products.ProductsApi(api_client)
    product_id = '903000000045027' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    update_a_product_request = ls_zoho_billing_products.UpdateAProductRequest() # UpdateAProductRequest |  (optional)

    try:
        # Update a product
        api_response = api_instance.products_product_id_put(product_id, x_com_zoho_subscriptions_organizationid, update_a_product_request=update_a_product_request)
        print("The response of ProductsApi->products_product_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_product_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **update_a_product_request** | [**UpdateAProductRequest**](UpdateAProductRequest.md)|  | [optional] 

### Return type

[**UpdateAProductResponse**](UpdateAProductResponse.md)

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

