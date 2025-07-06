# ls_zoho_billing_hosted_pages.HostedPagesApi

All URIs are relative to *https://www.zohoapis.com/billing/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hostedpages_addpaymentmethod_post**](HostedPagesApi.md#hostedpages_addpaymentmethod_post) | **POST** /hostedpages/addpaymentmethod | Associate a Payment method for a customer
[**hostedpages_buyonetimeaddon_post**](HostedPagesApi.md#hostedpages_buyonetimeaddon_post) | **POST** /hostedpages/buyonetimeaddon | Buy one-time addon for a subscription
[**hostedpages_get**](HostedPagesApi.md#hostedpages_get) | **GET** /hostedpages | List of HostedPages
[**hostedpages_hostedpage_id_get**](HostedPagesApi.md#hostedpages_hostedpage_id_get) | **GET** /hostedpages/{hostedpage_id} | Retrieve a hosted page
[**hostedpages_invoicepayment_post**](HostedPagesApi.md#hostedpages_invoicepayment_post) | **POST** /hostedpages/invoicepayment | Record a Invoice Payment
[**hostedpages_newsubscription_post**](HostedPagesApi.md#hostedpages_newsubscription_post) | **POST** /hostedpages/newsubscription | Create a subscription
[**hostedpages_updatecard_post**](HostedPagesApi.md#hostedpages_updatecard_post) | **POST** /hostedpages/updatecard | Update card for a subscription
[**hostedpages_updatepaymentmethod_post**](HostedPagesApi.md#hostedpages_updatepaymentmethod_post) | **POST** /hostedpages/updatepaymentmethod | Update customer payment details
[**hostedpages_updatesubscription_post**](HostedPagesApi.md#hostedpages_updatesubscription_post) | **POST** /hostedpages/updatesubscription | Update a subscription


# **hostedpages_addpaymentmethod_post**
> AddPaymentMethodForACustomerResponse hostedpages_addpaymentmethod_post(x_com_zoho_subscriptions_organizationid, add_payment_method_for_a_customer_request=add_payment_method_for_a_customer_request)

Associate a Payment method for a customer

Add payment method for a customer

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_hosted_pages
from ls_zoho_billing_hosted_pages.models.add_payment_method_for_a_customer_request import AddPaymentMethodForACustomerRequest
from ls_zoho_billing_hosted_pages.models.add_payment_method_for_a_customer_response import AddPaymentMethodForACustomerResponse
from ls_zoho_billing_hosted_pages.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_hosted_pages.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_hosted_pages.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_hosted_pages.HostedPagesApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    add_payment_method_for_a_customer_request = ls_zoho_billing_hosted_pages.AddPaymentMethodForACustomerRequest() # AddPaymentMethodForACustomerRequest |  (optional)

    try:
        # Associate a Payment method for a customer
        api_response = api_instance.hostedpages_addpaymentmethod_post(x_com_zoho_subscriptions_organizationid, add_payment_method_for_a_customer_request=add_payment_method_for_a_customer_request)
        print("The response of HostedPagesApi->hostedpages_addpaymentmethod_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostedPagesApi->hostedpages_addpaymentmethod_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **add_payment_method_for_a_customer_request** | [**AddPaymentMethodForACustomerRequest**](AddPaymentMethodForACustomerRequest.md)|  | [optional] 

### Return type

[**AddPaymentMethodForACustomerResponse**](AddPaymentMethodForACustomerResponse.md)

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

# **hostedpages_buyonetimeaddon_post**
> BuyOneTimeAddonForASubscriptionResponse hostedpages_buyonetimeaddon_post(x_com_zoho_subscriptions_organizationid, buy_one_time_addon_for_a_subscription_request=buy_one_time_addon_for_a_subscription_request)

Buy one-time addon for a subscription

Create hosted page for buying a one-time addon for a subscription.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_hosted_pages
from ls_zoho_billing_hosted_pages.models.buy_one_time_addon_for_a_subscription_request import BuyOneTimeAddonForASubscriptionRequest
from ls_zoho_billing_hosted_pages.models.buy_one_time_addon_for_a_subscription_response import BuyOneTimeAddonForASubscriptionResponse
from ls_zoho_billing_hosted_pages.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_hosted_pages.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_hosted_pages.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_hosted_pages.HostedPagesApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    buy_one_time_addon_for_a_subscription_request = ls_zoho_billing_hosted_pages.BuyOneTimeAddonForASubscriptionRequest() # BuyOneTimeAddonForASubscriptionRequest |  (optional)

    try:
        # Buy one-time addon for a subscription
        api_response = api_instance.hostedpages_buyonetimeaddon_post(x_com_zoho_subscriptions_organizationid, buy_one_time_addon_for_a_subscription_request=buy_one_time_addon_for_a_subscription_request)
        print("The response of HostedPagesApi->hostedpages_buyonetimeaddon_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostedPagesApi->hostedpages_buyonetimeaddon_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **buy_one_time_addon_for_a_subscription_request** | [**BuyOneTimeAddonForASubscriptionRequest**](BuyOneTimeAddonForASubscriptionRequest.md)|  | [optional] 

### Return type

[**BuyOneTimeAddonForASubscriptionResponse**](BuyOneTimeAddonForASubscriptionResponse.md)

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

# **hostedpages_get**
> ListOfHostedpagesResponse hostedpages_get(x_com_zoho_subscriptions_organizationid)

List of HostedPages

Retrieve the list of all hosted pages.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_hosted_pages
from ls_zoho_billing_hosted_pages.models.list_of_hostedpages_response import ListOfHostedpagesResponse
from ls_zoho_billing_hosted_pages.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_hosted_pages.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_hosted_pages.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_hosted_pages.HostedPagesApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # List of HostedPages
        api_response = api_instance.hostedpages_get(x_com_zoho_subscriptions_organizationid)
        print("The response of HostedPagesApi->hostedpages_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostedPagesApi->hostedpages_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**ListOfHostedpagesResponse**](ListOfHostedpagesResponse.md)

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

# **hostedpages_hostedpage_id_get**
> RetrieveAHostedPageResponse hostedpages_hostedpage_id_get(hostedpage_id, x_com_zoho_subscriptions_organizationid)

Retrieve a hosted page

Details of a specific hosted page. The <code>data</code> field will be populated with the subscription details in case of successfull subscription via Hostedpage. In case of fresh hosted pages the <code>data</code> field will be empty.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_hosted_pages
from ls_zoho_billing_hosted_pages.models.retrieve_a_hosted_page_response import RetrieveAHostedPageResponse
from ls_zoho_billing_hosted_pages.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_hosted_pages.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_hosted_pages.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_hosted_pages.HostedPagesApi(api_client)
    hostedpage_id = '8c589071e7e26a8d28e8af081c373fb00bd6dc5366fd129eefd5c61c569da526' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Retrieve a hosted page
        api_response = api_instance.hostedpages_hostedpage_id_get(hostedpage_id, x_com_zoho_subscriptions_organizationid)
        print("The response of HostedPagesApi->hostedpages_hostedpage_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostedPagesApi->hostedpages_hostedpage_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostedpage_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**RetrieveAHostedPageResponse**](RetrieveAHostedPageResponse.md)

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

# **hostedpages_invoicepayment_post**
> RecordInvoicePaymentForASubscriptionResponse hostedpages_invoicepayment_post(x_com_zoho_subscriptions_organizationid, record_invoice_payment_for_a_subscription_request=record_invoice_payment_for_a_subscription_request)

Record a Invoice Payment

Create a Hosted page for recording a Invoice payment for a subscription

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_hosted_pages
from ls_zoho_billing_hosted_pages.models.record_invoice_payment_for_a_subscription_request import RecordInvoicePaymentForASubscriptionRequest
from ls_zoho_billing_hosted_pages.models.record_invoice_payment_for_a_subscription_response import RecordInvoicePaymentForASubscriptionResponse
from ls_zoho_billing_hosted_pages.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_hosted_pages.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_hosted_pages.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_hosted_pages.HostedPagesApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    record_invoice_payment_for_a_subscription_request = ls_zoho_billing_hosted_pages.RecordInvoicePaymentForASubscriptionRequest() # RecordInvoicePaymentForASubscriptionRequest |  (optional)

    try:
        # Record a Invoice Payment
        api_response = api_instance.hostedpages_invoicepayment_post(x_com_zoho_subscriptions_organizationid, record_invoice_payment_for_a_subscription_request=record_invoice_payment_for_a_subscription_request)
        print("The response of HostedPagesApi->hostedpages_invoicepayment_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostedPagesApi->hostedpages_invoicepayment_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **record_invoice_payment_for_a_subscription_request** | [**RecordInvoicePaymentForASubscriptionRequest**](RecordInvoicePaymentForASubscriptionRequest.md)|  | [optional] 

### Return type

[**RecordInvoicePaymentForASubscriptionResponse**](RecordInvoicePaymentForASubscriptionResponse.md)

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

# **hostedpages_newsubscription_post**
> CreateASubscriptionResponse hostedpages_newsubscription_post(x_com_zoho_subscriptions_organizationid, create_a_subscription_request=create_a_subscription_request)

Create a subscription

Create a hosted page for a new subscription. To create a subscription for a new customer, you have to pass the customer object. To create a subscription for a existing customer pass the customer_id of that customer.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_hosted_pages
from ls_zoho_billing_hosted_pages.models.create_a_subscription_request import CreateASubscriptionRequest
from ls_zoho_billing_hosted_pages.models.create_a_subscription_response import CreateASubscriptionResponse
from ls_zoho_billing_hosted_pages.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_hosted_pages.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_hosted_pages.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_hosted_pages.HostedPagesApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    create_a_subscription_request = ls_zoho_billing_hosted_pages.CreateASubscriptionRequest() # CreateASubscriptionRequest |  (optional)

    try:
        # Create a subscription
        api_response = api_instance.hostedpages_newsubscription_post(x_com_zoho_subscriptions_organizationid, create_a_subscription_request=create_a_subscription_request)
        print("The response of HostedPagesApi->hostedpages_newsubscription_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostedPagesApi->hostedpages_newsubscription_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **create_a_subscription_request** | [**CreateASubscriptionRequest**](CreateASubscriptionRequest.md)|  | [optional] 

### Return type

[**CreateASubscriptionResponse**](CreateASubscriptionResponse.md)

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

# **hostedpages_updatecard_post**
> UpdateCardForASubscriptionResponse hostedpages_updatecard_post(x_com_zoho_subscriptions_organizationid, update_card_for_a_subscription_request=update_card_for_a_subscription_request)

Update card for a subscription

Create hosted page for updating card information for a subscription.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_hosted_pages
from ls_zoho_billing_hosted_pages.models.update_card_for_a_subscription_request import UpdateCardForASubscriptionRequest
from ls_zoho_billing_hosted_pages.models.update_card_for_a_subscription_response import UpdateCardForASubscriptionResponse
from ls_zoho_billing_hosted_pages.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_hosted_pages.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_hosted_pages.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_hosted_pages.HostedPagesApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    update_card_for_a_subscription_request = ls_zoho_billing_hosted_pages.UpdateCardForASubscriptionRequest() # UpdateCardForASubscriptionRequest |  (optional)

    try:
        # Update card for a subscription
        api_response = api_instance.hostedpages_updatecard_post(x_com_zoho_subscriptions_organizationid, update_card_for_a_subscription_request=update_card_for_a_subscription_request)
        print("The response of HostedPagesApi->hostedpages_updatecard_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostedPagesApi->hostedpages_updatecard_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **update_card_for_a_subscription_request** | [**UpdateCardForASubscriptionRequest**](UpdateCardForASubscriptionRequest.md)|  | [optional] 

### Return type

[**UpdateCardForASubscriptionResponse**](UpdateCardForASubscriptionResponse.md)

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

# **hostedpages_updatepaymentmethod_post**
> UpdatePaymentMethodResponse hostedpages_updatepaymentmethod_post(x_com_zoho_subscriptions_organizationid, update_payment_method_request=update_payment_method_request)

Update customer payment details

Create a Hosted Payment Page to update customers card, bank account (ACH) or PayPal details

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_hosted_pages
from ls_zoho_billing_hosted_pages.models.update_payment_method_request import UpdatePaymentMethodRequest
from ls_zoho_billing_hosted_pages.models.update_payment_method_response import UpdatePaymentMethodResponse
from ls_zoho_billing_hosted_pages.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_hosted_pages.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_hosted_pages.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_hosted_pages.HostedPagesApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    update_payment_method_request = ls_zoho_billing_hosted_pages.UpdatePaymentMethodRequest() # UpdatePaymentMethodRequest |  (optional)

    try:
        # Update customer payment details
        api_response = api_instance.hostedpages_updatepaymentmethod_post(x_com_zoho_subscriptions_organizationid, update_payment_method_request=update_payment_method_request)
        print("The response of HostedPagesApi->hostedpages_updatepaymentmethod_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostedPagesApi->hostedpages_updatepaymentmethod_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **update_payment_method_request** | [**UpdatePaymentMethodRequest**](UpdatePaymentMethodRequest.md)|  | [optional] 

### Return type

[**UpdatePaymentMethodResponse**](UpdatePaymentMethodResponse.md)

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

# **hostedpages_updatesubscription_post**
> UpdateASubscriptionResponse hostedpages_updatesubscription_post(x_com_zoho_subscriptions_organizationid, update_a_subscription_request=update_a_subscription_request)

Update a subscription

Create a hosted page for a updating a subscription.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_hosted_pages
from ls_zoho_billing_hosted_pages.models.update_a_subscription_request import UpdateASubscriptionRequest
from ls_zoho_billing_hosted_pages.models.update_a_subscription_response import UpdateASubscriptionResponse
from ls_zoho_billing_hosted_pages.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_hosted_pages.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_hosted_pages.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_hosted_pages.HostedPagesApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    update_a_subscription_request = ls_zoho_billing_hosted_pages.UpdateASubscriptionRequest() # UpdateASubscriptionRequest |  (optional)

    try:
        # Update a subscription
        api_response = api_instance.hostedpages_updatesubscription_post(x_com_zoho_subscriptions_organizationid, update_a_subscription_request=update_a_subscription_request)
        print("The response of HostedPagesApi->hostedpages_updatesubscription_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostedPagesApi->hostedpages_updatesubscription_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **update_a_subscription_request** | [**UpdateASubscriptionRequest**](UpdateASubscriptionRequest.md)|  | [optional] 

### Return type

[**UpdateASubscriptionResponse**](UpdateASubscriptionResponse.md)

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

