# ls_zoho_billing_customers.CustomersApi

All URIs are relative to *https://www.zohoapis.com/billing/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customers_customer_id_delete**](CustomersApi.md#customers_customer_id_delete) | **DELETE** /customers/{customer_id} | Delete a customer
[**customers_customer_id_get**](CustomersApi.md#customers_customer_id_get) | **GET** /customers/{customer_id} | Retrieve a customer
[**customers_customer_id_markasactive_post**](CustomersApi.md#customers_customer_id_markasactive_post) | **POST** /customers/{customer_id}/markasactive | Mark as active
[**customers_customer_id_markasinactive_post**](CustomersApi.md#customers_customer_id_markasinactive_post) | **POST** /customers/{customer_id}/markasinactive | Mark as inactive
[**customers_customer_id_put**](CustomersApi.md#customers_customer_id_put) | **PUT** /customers/{customer_id} | Update a customer
[**customers_get**](CustomersApi.md#customers_get) | **GET** /customers | List all customers
[**customers_post**](CustomersApi.md#customers_post) | **POST** /customers | Create a customer
[**customers_reference_reference_id_get**](CustomersApi.md#customers_reference_reference_id_get) | **GET** /customers/reference/{reference_id} | Retrieve a customer Using CRM Reference
[**transactions_get**](CustomersApi.md#transactions_get) | **GET** /transactions | List of transactions


# **customers_customer_id_delete**
> DeleteACustomerResponse customers_customer_id_delete(customer_id, x_com_zoho_subscriptions_organizationid)

Delete a customer

Delete an existing customer.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_customers
from ls_zoho_billing_customers.models.delete_a_customer_response import DeleteACustomerResponse
from ls_zoho_billing_customers.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_customers.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_customers.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_customers.CustomersApi(api_client)
    customer_id = '903000000000099' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Delete a customer
        api_response = api_instance.customers_customer_id_delete(customer_id, x_com_zoho_subscriptions_organizationid)
        print("The response of CustomersApi->customers_customer_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->customers_customer_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**DeleteACustomerResponse**](DeleteACustomerResponse.md)

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

# **customers_customer_id_get**
> RetrieveACustomerResponse customers_customer_id_get(customer_id, x_com_zoho_subscriptions_organizationid)

Retrieve a customer

Details of an existing customer.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_customers
from ls_zoho_billing_customers.models.retrieve_a_customer_response import RetrieveACustomerResponse
from ls_zoho_billing_customers.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_customers.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_customers.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_customers.CustomersApi(api_client)
    customer_id = '903000000000099' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Retrieve a customer
        api_response = api_instance.customers_customer_id_get(customer_id, x_com_zoho_subscriptions_organizationid)
        print("The response of CustomersApi->customers_customer_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->customers_customer_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**RetrieveACustomerResponse**](RetrieveACustomerResponse.md)

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

# **customers_customer_id_markasactive_post**
> MarkAsActiveResponse customers_customer_id_markasactive_post(customer_id, x_com_zoho_subscriptions_organizationid)

Mark as active

Change status of the customer to <strong>active</strong>.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_customers
from ls_zoho_billing_customers.models.mark_as_active_response import MarkAsActiveResponse
from ls_zoho_billing_customers.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_customers.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_customers.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_customers.CustomersApi(api_client)
    customer_id = '903000000000099' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Mark as active
        api_response = api_instance.customers_customer_id_markasactive_post(customer_id, x_com_zoho_subscriptions_organizationid)
        print("The response of CustomersApi->customers_customer_id_markasactive_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->customers_customer_id_markasactive_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
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

# **customers_customer_id_markasinactive_post**
> MarkAsInactiveResponse customers_customer_id_markasinactive_post(customer_id, x_com_zoho_subscriptions_organizationid)

Mark as inactive

Change status of the customer to <strong>inactive</strong>. A cutomer can be marked as inactive only if there is no active subscription associated with the customer.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_customers
from ls_zoho_billing_customers.models.mark_as_inactive_response import MarkAsInactiveResponse
from ls_zoho_billing_customers.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_customers.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_customers.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_customers.CustomersApi(api_client)
    customer_id = '903000000000099' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Mark as inactive
        api_response = api_instance.customers_customer_id_markasinactive_post(customer_id, x_com_zoho_subscriptions_organizationid)
        print("The response of CustomersApi->customers_customer_id_markasinactive_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->customers_customer_id_markasinactive_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
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

# **customers_customer_id_put**
> UpdateACustomerResponse customers_customer_id_put(customer_id, x_com_zoho_subscriptions_organizationid, update_a_customer_request=update_a_customer_request)

Update a customer

Update details of an existing customer.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_customers
from ls_zoho_billing_customers.models.update_a_customer_request import UpdateACustomerRequest
from ls_zoho_billing_customers.models.update_a_customer_response import UpdateACustomerResponse
from ls_zoho_billing_customers.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_customers.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_customers.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_customers.CustomersApi(api_client)
    customer_id = '903000000000099' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    update_a_customer_request = ls_zoho_billing_customers.UpdateACustomerRequest() # UpdateACustomerRequest |  (optional)

    try:
        # Update a customer
        api_response = api_instance.customers_customer_id_put(customer_id, x_com_zoho_subscriptions_organizationid, update_a_customer_request=update_a_customer_request)
        print("The response of CustomersApi->customers_customer_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->customers_customer_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **update_a_customer_request** | [**UpdateACustomerRequest**](UpdateACustomerRequest.md)|  | [optional] 

### Return type

[**UpdateACustomerResponse**](UpdateACustomerResponse.md)

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

# **customers_get**
> ListAllCustomersResponse customers_get(x_com_zoho_subscriptions_organizationid)

List all customers

List of all customers. You can list customers based on various filter criterias. The allowed values for <code>filter_by</code> are Status.(<code>All</code>, <code>Active</code>, <code>Inactive</code>, <code>Gapps</code>, <code>Crm</code>, <code>NonSubscribers</code>, <code>PortalEnabled</code>, <code>PortalDisabled</code>).

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_customers
from ls_zoho_billing_customers.models.list_all_customers_response import ListAllCustomersResponse
from ls_zoho_billing_customers.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_customers.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_customers.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_customers.CustomersApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # List all customers
        api_response = api_instance.customers_get(x_com_zoho_subscriptions_organizationid)
        print("The response of CustomersApi->customers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->customers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**ListAllCustomersResponse**](ListAllCustomersResponse.md)

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

# **customers_post**
> CreateACustomerResponse customers_post(x_com_zoho_subscriptions_organizationid, create_a_customer_request=create_a_customer_request)

Create a customer

A new customer can a be created separately as well as at the time of creation of a new subscription.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_customers
from ls_zoho_billing_customers.models.create_a_customer_request import CreateACustomerRequest
from ls_zoho_billing_customers.models.create_a_customer_response import CreateACustomerResponse
from ls_zoho_billing_customers.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_customers.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_customers.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_customers.CustomersApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    create_a_customer_request = ls_zoho_billing_customers.CreateACustomerRequest() # CreateACustomerRequest |  (optional)

    try:
        # Create a customer
        api_response = api_instance.customers_post(x_com_zoho_subscriptions_organizationid, create_a_customer_request=create_a_customer_request)
        print("The response of CustomersApi->customers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->customers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **create_a_customer_request** | [**CreateACustomerRequest**](CreateACustomerRequest.md)|  | [optional] 

### Return type

[**CreateACustomerResponse**](CreateACustomerResponse.md)

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

# **customers_reference_reference_id_get**
> RetrieveACustomerUsingCrmReferenceResponse customers_reference_reference_id_get(reference_id, x_com_zoho_subscriptions_organizationid, reference_id_type=reference_id_type)

Retrieve a customer Using CRM Reference

Details of an existing customer using CRM Reference ID. reference_id can be <code> CRM Contact ID </code> (for Contacts only sync) or <code> CRM Account ID </code> (For accounts only and Accounts and its contacts sync). Query param value of <code> reference_id_type </code> must be given accoridngly.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_customers
from ls_zoho_billing_customers.models.retrieve_a_customer_using_crm_reference_response import RetrieveACustomerUsingCrmReferenceResponse
from ls_zoho_billing_customers.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_customers.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_customers.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_customers.CustomersApi(api_client)
    reference_id = '903000000021976' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    reference_id_type = 'CouponStatus.EXPIRED' # str | Possible values are <code> zcrm_account_id </code> and <code>zcrm_contact_id</code>. (optional)

    try:
        # Retrieve a customer Using CRM Reference
        api_response = api_instance.customers_reference_reference_id_get(reference_id, x_com_zoho_subscriptions_organizationid, reference_id_type=reference_id_type)
        print("The response of CustomersApi->customers_reference_reference_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->customers_reference_reference_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **reference_id_type** | **str**| Possible values are &lt;code&gt; zcrm_account_id &lt;/code&gt; and &lt;code&gt;zcrm_contact_id&lt;/code&gt;. | [optional] 

### Return type

[**RetrieveACustomerUsingCrmReferenceResponse**](RetrieveACustomerUsingCrmReferenceResponse.md)

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

# **transactions_get**
> ListOfTransactionsResponse transactions_get(x_com_zoho_subscriptions_organizationid, filter_by=filter_by, customer_id=customer_id)

List of transactions

List of all transactions associated with a particular customer.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_customers
from ls_zoho_billing_customers.models.list_of_transactions_response import ListOfTransactionsResponse
from ls_zoho_billing_customers.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_customers.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_customers.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_customers.CustomersApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    filter_by = 'TransactionType.All' # str | Transactions of particular type can be filtered by passing a param <code>filter_by</code>. The allowed values for filter_by are TransactionType.(<code>All</code>, <code>INVOICE</code>, <code>PAYMENT</code>, <code>CREDIT</code>, <code>REFUND</code>) (optional)
    customer_id = '903000000000099' # str | To list Transactions of a particular customer use the parameter <code>customer_id</code>. (optional)

    try:
        # List of transactions
        api_response = api_instance.transactions_get(x_com_zoho_subscriptions_organizationid, filter_by=filter_by, customer_id=customer_id)
        print("The response of CustomersApi->transactions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->transactions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **filter_by** | **str**| Transactions of particular type can be filtered by passing a param &lt;code&gt;filter_by&lt;/code&gt;. The allowed values for filter_by are TransactionType.(&lt;code&gt;All&lt;/code&gt;, &lt;code&gt;INVOICE&lt;/code&gt;, &lt;code&gt;PAYMENT&lt;/code&gt;, &lt;code&gt;CREDIT&lt;/code&gt;, &lt;code&gt;REFUND&lt;/code&gt;) | [optional] 
 **customer_id** | **str**| To list Transactions of a particular customer use the parameter &lt;code&gt;customer_id&lt;/code&gt;. | [optional] 

### Return type

[**ListOfTransactionsResponse**](ListOfTransactionsResponse.md)

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

