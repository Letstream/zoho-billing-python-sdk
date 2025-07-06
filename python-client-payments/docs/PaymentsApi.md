# ls_zoho_billing_payments.PaymentsApi

All URIs are relative to *https://www.zohoapis.com/billing/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payments_payment_id_delete**](PaymentsApi.md#payments_payment_id_delete) | **DELETE** /payments/{payment_id} | Delete a payment
[**payments_payment_id_get**](PaymentsApi.md#payments_payment_id_get) | **GET** /payments/{payment_id} | Retrieve a payment
[**payments_payment_id_put**](PaymentsApi.md#payments_payment_id_put) | **PUT** /payments/{payment_id} | Update a payment
[**payments_post**](PaymentsApi.md#payments_post) | **POST** /payments | Create a payment


# **payments_payment_id_delete**
> DeleteAPaymentResponse payments_payment_id_delete(payment_id, x_com_zoho_subscriptions_organizationid)

Delete a payment

Delete an existing payment.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_payments
from ls_zoho_billing_payments.models.delete_a_payment_response import DeleteAPaymentResponse
from ls_zoho_billing_payments.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_payments.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_payments.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_payments.PaymentsApi(api_client)
    payment_id = '9030000079467' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Delete a payment
        api_response = api_instance.payments_payment_id_delete(payment_id, x_com_zoho_subscriptions_organizationid)
        print("The response of PaymentsApi->payments_payment_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->payments_payment_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**DeleteAPaymentResponse**](DeleteAPaymentResponse.md)

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

# **payments_payment_id_get**
> RetrieveAPaymentResponse payments_payment_id_get(payment_id, x_com_zoho_subscriptions_organizationid)

Retrieve a payment

Details of an existing payment.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_payments
from ls_zoho_billing_payments.models.retrieve_a_payment_response import RetrieveAPaymentResponse
from ls_zoho_billing_payments.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_payments.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_payments.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_payments.PaymentsApi(api_client)
    payment_id = '9030000079467' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Retrieve a payment
        api_response = api_instance.payments_payment_id_get(payment_id, x_com_zoho_subscriptions_organizationid)
        print("The response of PaymentsApi->payments_payment_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->payments_payment_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**RetrieveAPaymentResponse**](RetrieveAPaymentResponse.md)

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

# **payments_payment_id_put**
> UpdateAPaymentResponse payments_payment_id_put(payment_id, x_com_zoho_subscriptions_organizationid, update_a_payment_request=update_a_payment_request)

Update a payment

Update an existing payment information.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_payments
from ls_zoho_billing_payments.models.update_a_payment_request import UpdateAPaymentRequest
from ls_zoho_billing_payments.models.update_a_payment_response import UpdateAPaymentResponse
from ls_zoho_billing_payments.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_payments.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_payments.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_payments.PaymentsApi(api_client)
    payment_id = '9030000079467' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    update_a_payment_request = ls_zoho_billing_payments.UpdateAPaymentRequest() # UpdateAPaymentRequest |  (optional)

    try:
        # Update a payment
        api_response = api_instance.payments_payment_id_put(payment_id, x_com_zoho_subscriptions_organizationid, update_a_payment_request=update_a_payment_request)
        print("The response of PaymentsApi->payments_payment_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->payments_payment_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **update_a_payment_request** | [**UpdateAPaymentRequest**](UpdateAPaymentRequest.md)|  | [optional] 

### Return type

[**UpdateAPaymentResponse**](UpdateAPaymentResponse.md)

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

# **payments_post**
> CreateAPaymentResponse payments_post(x_com_zoho_subscriptions_organizationid, create_a_payment_request=create_a_payment_request)

Create a payment

Create a new payment.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_payments
from ls_zoho_billing_payments.models.create_a_payment_request import CreateAPaymentRequest
from ls_zoho_billing_payments.models.create_a_payment_response import CreateAPaymentResponse
from ls_zoho_billing_payments.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_payments.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_payments.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_payments.PaymentsApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    create_a_payment_request = ls_zoho_billing_payments.CreateAPaymentRequest() # CreateAPaymentRequest |  (optional)

    try:
        # Create a payment
        api_response = api_instance.payments_post(x_com_zoho_subscriptions_organizationid, create_a_payment_request=create_a_payment_request)
        print("The response of PaymentsApi->payments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->payments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **create_a_payment_request** | [**CreateAPaymentRequest**](CreateAPaymentRequest.md)|  | [optional] 

### Return type

[**CreateAPaymentResponse**](CreateAPaymentResponse.md)

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

