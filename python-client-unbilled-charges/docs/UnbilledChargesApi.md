# ls_zoho_billing_unbilled_charges.UnbilledChargesApi

All URIs are relative to *https://www.zohoapis.com/billing/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**unbilledcharges_unbilled_charge_id_createinvoice_post**](UnbilledChargesApi.md#unbilledcharges_unbilled_charge_id_createinvoice_post) | **POST** /unbilledcharges/{unbilled_charge_id}/createinvoice | Convert unbilled charge to invoice
[**unbilledcharges_unbilled_charge_id_delete**](UnbilledChargesApi.md#unbilledcharges_unbilled_charge_id_delete) | **DELETE** /unbilledcharges/{unbilled_charge_id} | Delete unbilled charge
[**unbilledcharges_unbilled_charge_id_get**](UnbilledChargesApi.md#unbilledcharges_unbilled_charge_id_get) | **GET** /unbilledcharges/{unbilled_charge_id} | Retrieve an unbilled charge


# **unbilledcharges_unbilled_charge_id_createinvoice_post**
> ConvertUnbilledChargeToInvoiceResponse unbilledcharges_unbilled_charge_id_createinvoice_post(unbilled_charge_id, x_com_zoho_subscriptions_organizationid)

Convert unbilled charge to invoice

Convert unbilled charges to an invoice by manual intervention instead of waiting for next renewal.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_unbilled_charges
from ls_zoho_billing_unbilled_charges.models.convert_unbilled_charge_to_invoice_response import ConvertUnbilledChargeToInvoiceResponse
from ls_zoho_billing_unbilled_charges.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_unbilled_charges.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_unbilled_charges.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_unbilled_charges.UnbilledChargesApi(api_client)
    unbilled_charge_id = '90300000079200' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Convert unbilled charge to invoice
        api_response = api_instance.unbilledcharges_unbilled_charge_id_createinvoice_post(unbilled_charge_id, x_com_zoho_subscriptions_organizationid)
        print("The response of UnbilledChargesApi->unbilledcharges_unbilled_charge_id_createinvoice_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnbilledChargesApi->unbilledcharges_unbilled_charge_id_createinvoice_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unbilled_charge_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**ConvertUnbilledChargeToInvoiceResponse**](ConvertUnbilledChargeToInvoiceResponse.md)

### Authorization

[Zoho_Auth](../README.md#Zoho_Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unbilledcharges_unbilled_charge_id_delete**
> DeleteUnbilledChargeResponse unbilledcharges_unbilled_charge_id_delete(unbilled_charge_id, x_com_zoho_subscriptions_organizationid)

Delete unbilled charge

Delete the unbilled charge.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_unbilled_charges
from ls_zoho_billing_unbilled_charges.models.delete_unbilled_charge_response import DeleteUnbilledChargeResponse
from ls_zoho_billing_unbilled_charges.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_unbilled_charges.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_unbilled_charges.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_unbilled_charges.UnbilledChargesApi(api_client)
    unbilled_charge_id = '90300000079200' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Delete unbilled charge
        api_response = api_instance.unbilledcharges_unbilled_charge_id_delete(unbilled_charge_id, x_com_zoho_subscriptions_organizationid)
        print("The response of UnbilledChargesApi->unbilledcharges_unbilled_charge_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnbilledChargesApi->unbilledcharges_unbilled_charge_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unbilled_charge_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**DeleteUnbilledChargeResponse**](DeleteUnbilledChargeResponse.md)

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

# **unbilledcharges_unbilled_charge_id_get**
> RetrieveAnUnbilledChargeResponse unbilledcharges_unbilled_charge_id_get(unbilled_charge_id, x_com_zoho_subscriptions_organizationid)

Retrieve an unbilled charge

Details of an unbilled charge.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_unbilled_charges
from ls_zoho_billing_unbilled_charges.models.retrieve_an_unbilled_charge_response import RetrieveAnUnbilledChargeResponse
from ls_zoho_billing_unbilled_charges.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_unbilled_charges.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_unbilled_charges.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_unbilled_charges.UnbilledChargesApi(api_client)
    unbilled_charge_id = '90300000079200' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Retrieve an unbilled charge
        api_response = api_instance.unbilledcharges_unbilled_charge_id_get(unbilled_charge_id, x_com_zoho_subscriptions_organizationid)
        print("The response of UnbilledChargesApi->unbilledcharges_unbilled_charge_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnbilledChargesApi->unbilledcharges_unbilled_charge_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unbilled_charge_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**RetrieveAnUnbilledChargeResponse**](RetrieveAnUnbilledChargeResponse.md)

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

