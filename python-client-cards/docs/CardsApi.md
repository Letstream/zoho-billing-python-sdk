# ls_zoho_billing_cards.CardsApi

All URIs are relative to *https://www.zohoapis.com/billing/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customers_customer_id_cards_card_id_delete**](CardsApi.md#customers_customer_id_cards_card_id_delete) | **DELETE** /customers/{customer_id}/cards/{card_id} | Delete a credit card
[**customers_customer_id_cards_card_id_get**](CardsApi.md#customers_customer_id_cards_card_id_get) | **GET** /customers/{customer_id}/cards/{card_id} | Retrieve a credit card information
[**customers_customer_id_cards_get**](CardsApi.md#customers_customer_id_cards_get) | **GET** /customers/{customer_id}/cards | List all Active Credit Cards of a Customer


# **customers_customer_id_cards_card_id_delete**
> DeleteACreditCardResponse customers_customer_id_cards_card_id_delete(customer_id, x_com_zoho_subscriptions_organizationid, card_id)

Delete a credit card

Delete an existing credit card.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_cards
from ls_zoho_billing_cards.models.delete_a_credit_card_response import DeleteACreditCardResponse
from ls_zoho_billing_cards.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_cards.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_cards.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_cards.CardsApi(api_client)
    customer_id = '9030000005664' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    card_id = '90300000079226' # str | 

    try:
        # Delete a credit card
        api_response = api_instance.customers_customer_id_cards_card_id_delete(customer_id, x_com_zoho_subscriptions_organizationid, card_id)
        print("The response of CardsApi->customers_customer_id_cards_card_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CardsApi->customers_customer_id_cards_card_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **card_id** | **str**|  | 

### Return type

[**DeleteACreditCardResponse**](DeleteACreditCardResponse.md)

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

# **customers_customer_id_cards_card_id_get**
> RetrieveACreditCardInformationResponse customers_customer_id_cards_card_id_get(customer_id, x_com_zoho_subscriptions_organizationid, card_id)

Retrieve a credit card information

Details of an existing credit card.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_cards
from ls_zoho_billing_cards.models.retrieve_a_credit_card_information_response import RetrieveACreditCardInformationResponse
from ls_zoho_billing_cards.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_cards.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_cards.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_cards.CardsApi(api_client)
    customer_id = '9030000005664' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    card_id = '90300000079226' # str | 

    try:
        # Retrieve a credit card information
        api_response = api_instance.customers_customer_id_cards_card_id_get(customer_id, x_com_zoho_subscriptions_organizationid, card_id)
        print("The response of CardsApi->customers_customer_id_cards_card_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CardsApi->customers_customer_id_cards_card_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **card_id** | **str**|  | 

### Return type

[**RetrieveACreditCardInformationResponse**](RetrieveACreditCardInformationResponse.md)

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

# **customers_customer_id_cards_get**
> ListAllActiveCreditCardsOfACustomerResponse customers_customer_id_cards_get(customer_id, x_com_zoho_subscriptions_organizationid)

List all Active Credit Cards of a Customer

List of all the Active Credit Cards of a Customer.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_cards
from ls_zoho_billing_cards.models.list_all_active_credit_cards_of_a_customer_response import ListAllActiveCreditCardsOfACustomerResponse
from ls_zoho_billing_cards.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_cards.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_cards.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_cards.CardsApi(api_client)
    customer_id = '9030000005664' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # List all Active Credit Cards of a Customer
        api_response = api_instance.customers_customer_id_cards_get(customer_id, x_com_zoho_subscriptions_organizationid)
        print("The response of CardsApi->customers_customer_id_cards_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CardsApi->customers_customer_id_cards_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**ListAllActiveCreditCardsOfACustomerResponse**](ListAllActiveCreditCardsOfACustomerResponse.md)

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

