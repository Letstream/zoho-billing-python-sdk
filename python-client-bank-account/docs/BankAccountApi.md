# ls_zoho_billing_bank_account.BankAccountApi

All URIs are relative to *https://www.zohoapis.com/billing/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customers_customer_id_bankaccounts_account_id_get**](BankAccountApi.md#customers_customer_id_bankaccounts_account_id_get) | **GET** /customers/{customer_id}/bankaccounts/{account_id} | Retrieve a bank account information


# **customers_customer_id_bankaccounts_account_id_get**
> RetrieveABankAccountInformationResponse customers_customer_id_bankaccounts_account_id_get(customer_id, x_com_zoho_subscriptions_organizationid, account_id)

Retrieve a bank account information

Details of an existing bank account.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_bank_account
from ls_zoho_billing_bank_account.models.retrieve_a_bank_account_information_response import RetrieveABankAccountInformationResponse
from ls_zoho_billing_bank_account.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_bank_account.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_bank_account.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_bank_account.BankAccountApi(api_client)
    customer_id = '9030000005664' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    account_id = '90300000079126' # str | 

    try:
        # Retrieve a bank account information
        api_response = api_instance.customers_customer_id_bankaccounts_account_id_get(customer_id, x_com_zoho_subscriptions_organizationid, account_id)
        print("The response of BankAccountApi->customers_customer_id_bankaccounts_account_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountApi->customers_customer_id_bankaccounts_account_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **account_id** | **str**|  | 

### Return type

[**RetrieveABankAccountInformationResponse**](RetrieveABankAccountInformationResponse.md)

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

