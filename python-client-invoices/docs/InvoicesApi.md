# ls_zoho_billing_invoices.InvoicesApi

All URIs are relative to *https://www.zohoapis.com/billing/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invoice_invoice_id_customfields_put**](InvoicesApi.md#invoice_invoice_id_customfields_put) | **PUT** /invoice/{invoice_id}/customfields | Update custom field in existing invoices
[**invoices_get**](InvoicesApi.md#invoices_get) | **GET** /invoices | List all invoices
[**invoices_invoice_id_address_put**](InvoicesApi.md#invoices_invoice_id_address_put) | **PUT** /invoices/{invoice_id}/address | Update address
[**invoices_invoice_id_attachment_post**](InvoicesApi.md#invoices_invoice_id_attachment_post) | **POST** /invoices/{invoice_id}/attachment | Add attachment to an invoice
[**invoices_invoice_id_cancelwriteoff_post**](InvoicesApi.md#invoices_invoice_id_cancelwriteoff_post) | **POST** /invoices/{invoice_id}/cancelwriteoff | Cancel write off
[**invoices_invoice_id_collect_post**](InvoicesApi.md#invoices_invoice_id_collect_post) | **POST** /invoices/{invoice_id}/collect | Collect charge via bank account / credit card
[**invoices_invoice_id_converttoopen_post**](InvoicesApi.md#invoices_invoice_id_converttoopen_post) | **POST** /invoices/{invoice_id}/converttoopen | Convert to open
[**invoices_invoice_id_credits_post**](InvoicesApi.md#invoices_invoice_id_credits_post) | **POST** /invoices/{invoice_id}/credits | Apply Multiple Credits to Invoice
[**invoices_invoice_id_customfields_post**](InvoicesApi.md#invoices_invoice_id_customfields_post) | **POST** /invoices/{invoice_id}/customfields | Update Custom Fields
[**invoices_invoice_id_delete**](InvoicesApi.md#invoices_invoice_id_delete) | **DELETE** /invoices/{invoice_id} | Delete an invoice
[**invoices_invoice_id_email_post**](InvoicesApi.md#invoices_invoice_id_email_post) | **POST** /invoices/{invoice_id}/email | Email an invoice
[**invoices_invoice_id_get**](InvoicesApi.md#invoices_invoice_id_get) | **GET** /invoices/{invoice_id} | Retrieve an invoice
[**invoices_invoice_id_lineitems_item_id_delete**](InvoicesApi.md#invoices_invoice_id_lineitems_item_id_delete) | **DELETE** /invoices/{invoice_id}/lineitems/{item_id} | Delete items from a pending invoice
[**invoices_invoice_id_lineitems_post**](InvoicesApi.md#invoices_invoice_id_lineitems_post) | **POST** /invoices/{invoice_id}/lineitems | Add items to a pending invoice
[**invoices_invoice_id_put**](InvoicesApi.md#invoices_invoice_id_put) | **PUT** /invoices/{invoice_id} | Update an invoice
[**invoices_invoice_id_void_post**](InvoicesApi.md#invoices_invoice_id_void_post) | **POST** /invoices/{invoice_id}/void | Void an invoice
[**invoices_invoice_id_writeoff_post**](InvoicesApi.md#invoices_invoice_id_writeoff_post) | **POST** /invoices/{invoice_id}/writeoff | Write off
[**invoices_post**](InvoicesApi.md#invoices_post) | **POST** /invoices | Create an invoice


# **invoice_invoice_id_customfields_put**
> UpdateAnInvoiceCustomfieldResponse invoice_invoice_id_customfields_put(invoice_id, x_com_zoho_subscriptions_organizationid, custom_fields_update_inner=custom_fields_update_inner)

Update custom field in existing invoices

Update the value of the custom field in existing invoices.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_invoices
from ls_zoho_billing_invoices.models.custom_fields_update_inner import CustomFieldsUpdateInner
from ls_zoho_billing_invoices.models.update_an_invoice_customfield_response import UpdateAnInvoiceCustomfieldResponse
from ls_zoho_billing_invoices.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_invoices.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_invoices.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_invoices.InvoicesApi(api_client)
    invoice_id = '982000000567114' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    custom_fields_update_inner = [ls_zoho_billing_invoices.CustomFieldsUpdateInner()] # List[CustomFieldsUpdateInner] |  (optional)

    try:
        # Update custom field in existing invoices
        api_response = api_instance.invoice_invoice_id_customfields_put(invoice_id, x_com_zoho_subscriptions_organizationid, custom_fields_update_inner=custom_fields_update_inner)
        print("The response of InvoicesApi->invoice_invoice_id_customfields_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoice_invoice_id_customfields_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **custom_fields_update_inner** | [**List[CustomFieldsUpdateInner]**](CustomFieldsUpdateInner.md)|  | [optional] 

### Return type

[**UpdateAnInvoiceCustomfieldResponse**](UpdateAnInvoiceCustomfieldResponse.md)

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

# **invoices_get**
> ListAllInvoicesResponse invoices_get(x_com_zoho_subscriptions_organizationid, filter_by=filter_by)

List all invoices

List of all invoices. <br><br> To list invoices for a particular subscription or customer append a param as <code>subscription_id={subscription_id}</code> or <code>customer_id={customer_id}</code>.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_invoices
from ls_zoho_billing_invoices.models.list_all_invoices_response import ListAllInvoicesResponse
from ls_zoho_billing_invoices.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_invoices.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_invoices.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_invoices.InvoicesApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    filter_by = 'Status.All' # str | Invoices of particular status can be filtered by passing a param <code>filter_by</code>. Allowed values are Status.(<code>All</code>, <code>Sent</code>, <code>Draft</code>, <code>OverDue</code>, <code>Paid</code>, <code>PartiallyPaid</code>, <code>Void</code>, <code>Unpaid</code>). (optional)

    try:
        # List all invoices
        api_response = api_instance.invoices_get(x_com_zoho_subscriptions_organizationid, filter_by=filter_by)
        print("The response of InvoicesApi->invoices_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **filter_by** | **str**| Invoices of particular status can be filtered by passing a param &lt;code&gt;filter_by&lt;/code&gt;. Allowed values are Status.(&lt;code&gt;All&lt;/code&gt;, &lt;code&gt;Sent&lt;/code&gt;, &lt;code&gt;Draft&lt;/code&gt;, &lt;code&gt;OverDue&lt;/code&gt;, &lt;code&gt;Paid&lt;/code&gt;, &lt;code&gt;PartiallyPaid&lt;/code&gt;, &lt;code&gt;Void&lt;/code&gt;, &lt;code&gt;Unpaid&lt;/code&gt;). | [optional] 

### Return type

[**ListAllInvoicesResponse**](ListAllInvoicesResponse.md)

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

# **invoices_invoice_id_address_put**
> UpdateAddressResponse invoices_invoice_id_address_put(invoice_id, x_com_zoho_subscriptions_organizationid, update_address_request=update_address_request)

Update address

Update shipping and billing address of an invoice.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_invoices
from ls_zoho_billing_invoices.models.update_address_request import UpdateAddressRequest
from ls_zoho_billing_invoices.models.update_address_response import UpdateAddressResponse
from ls_zoho_billing_invoices.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_invoices.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_invoices.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_invoices.InvoicesApi(api_client)
    invoice_id = '903000000079426' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    update_address_request = ls_zoho_billing_invoices.UpdateAddressRequest() # UpdateAddressRequest |  (optional)

    try:
        # Update address
        api_response = api_instance.invoices_invoice_id_address_put(invoice_id, x_com_zoho_subscriptions_organizationid, update_address_request=update_address_request)
        print("The response of InvoicesApi->invoices_invoice_id_address_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_invoice_id_address_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **update_address_request** | [**UpdateAddressRequest**](UpdateAddressRequest.md)|  | [optional] 

### Return type

[**UpdateAddressResponse**](UpdateAddressResponse.md)

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

# **invoices_invoice_id_attachment_post**
> AddAttachmentToAnInvoiceResponse invoices_invoice_id_attachment_post(invoice_id, x_com_zoho_subscriptions_organizationid, add_attachment_to_an_invoice_request=add_attachment_to_an_invoice_request)

Add attachment to an invoice

Attach a file to an invoice.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_invoices
from ls_zoho_billing_invoices.models.add_attachment_to_an_invoice_request import AddAttachmentToAnInvoiceRequest
from ls_zoho_billing_invoices.models.add_attachment_to_an_invoice_response import AddAttachmentToAnInvoiceResponse
from ls_zoho_billing_invoices.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_invoices.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_invoices.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_invoices.InvoicesApi(api_client)
    invoice_id = '903000000079426' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    add_attachment_to_an_invoice_request = ls_zoho_billing_invoices.AddAttachmentToAnInvoiceRequest() # AddAttachmentToAnInvoiceRequest |  (optional)

    try:
        # Add attachment to an invoice
        api_response = api_instance.invoices_invoice_id_attachment_post(invoice_id, x_com_zoho_subscriptions_organizationid, add_attachment_to_an_invoice_request=add_attachment_to_an_invoice_request)
        print("The response of InvoicesApi->invoices_invoice_id_attachment_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_invoice_id_attachment_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **add_attachment_to_an_invoice_request** | [**AddAttachmentToAnInvoiceRequest**](AddAttachmentToAnInvoiceRequest.md)|  | [optional] 

### Return type

[**AddAttachmentToAnInvoiceResponse**](AddAttachmentToAnInvoiceResponse.md)

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

# **invoices_invoice_id_cancelwriteoff_post**
> CancelWriteOffResponse invoices_invoice_id_cancelwriteoff_post(invoice_id, x_com_zoho_subscriptions_organizationid)

Cancel write off

Cancel the write off amount of an invoice.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_invoices
from ls_zoho_billing_invoices.models.cancel_write_off_response import CancelWriteOffResponse
from ls_zoho_billing_invoices.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_invoices.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_invoices.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_invoices.InvoicesApi(api_client)
    invoice_id = '982000000567114' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Cancel write off
        api_response = api_instance.invoices_invoice_id_cancelwriteoff_post(invoice_id, x_com_zoho_subscriptions_organizationid)
        print("The response of InvoicesApi->invoices_invoice_id_cancelwriteoff_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_invoice_id_cancelwriteoff_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**CancelWriteOffResponse**](CancelWriteOffResponse.md)

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

# **invoices_invoice_id_collect_post**
> CollectChargeViaBankAccountCreditCardResponse invoices_invoice_id_collect_post(invoice_id, x_com_zoho_subscriptions_organizationid, collect_charge_via_bank_account_credit_card_request=collect_charge_via_bank_account_credit_card_request)

Collect charge via bank account / credit card

Charge a customer for an invoice using existing bank account.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_invoices
from ls_zoho_billing_invoices.models.collect_charge_via_bank_account_credit_card_request import CollectChargeViaBankAccountCreditCardRequest
from ls_zoho_billing_invoices.models.collect_charge_via_bank_account_credit_card_response import CollectChargeViaBankAccountCreditCardResponse
from ls_zoho_billing_invoices.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_invoices.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_invoices.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_invoices.InvoicesApi(api_client)
    invoice_id = '903000000079426' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    collect_charge_via_bank_account_credit_card_request = ls_zoho_billing_invoices.CollectChargeViaBankAccountCreditCardRequest() # CollectChargeViaBankAccountCreditCardRequest |  (optional)

    try:
        # Collect charge via bank account / credit card
        api_response = api_instance.invoices_invoice_id_collect_post(invoice_id, x_com_zoho_subscriptions_organizationid, collect_charge_via_bank_account_credit_card_request=collect_charge_via_bank_account_credit_card_request)
        print("The response of InvoicesApi->invoices_invoice_id_collect_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_invoice_id_collect_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **collect_charge_via_bank_account_credit_card_request** | [**CollectChargeViaBankAccountCreditCardRequest**](CollectChargeViaBankAccountCreditCardRequest.md)|  | [optional] 

### Return type

[**CollectChargeViaBankAccountCreditCardResponse**](CollectChargeViaBankAccountCreditCardResponse.md)

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

# **invoices_invoice_id_converttoopen_post**
> ConvertToOpenResponse invoices_invoice_id_converttoopen_post(invoice_id, x_com_zoho_subscriptions_organizationid)

Convert to open

Change the status of the invoice to open.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_invoices
from ls_zoho_billing_invoices.models.convert_to_open_response import ConvertToOpenResponse
from ls_zoho_billing_invoices.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_invoices.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_invoices.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_invoices.InvoicesApi(api_client)
    invoice_id = '903000000079426' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Convert to open
        api_response = api_instance.invoices_invoice_id_converttoopen_post(invoice_id, x_com_zoho_subscriptions_organizationid)
        print("The response of InvoicesApi->invoices_invoice_id_converttoopen_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_invoice_id_converttoopen_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**ConvertToOpenResponse**](ConvertToOpenResponse.md)

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

# **invoices_invoice_id_credits_post**
> ApplyMultipleCreditsToInvoiceResponse invoices_invoice_id_credits_post(invoice_id, x_com_zoho_subscriptions_organizationid, apply_multiple_credits_to_invoice_request=apply_multiple_credits_to_invoice_request)

Apply Multiple Credits to Invoice

To associate multiple creditnotes to a particular invoice.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_invoices
from ls_zoho_billing_invoices.models.apply_multiple_credits_to_invoice_request import ApplyMultipleCreditsToInvoiceRequest
from ls_zoho_billing_invoices.models.apply_multiple_credits_to_invoice_response import ApplyMultipleCreditsToInvoiceResponse
from ls_zoho_billing_invoices.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_invoices.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_invoices.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_invoices.InvoicesApi(api_client)
    invoice_id = '903000000079426' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    apply_multiple_credits_to_invoice_request = ls_zoho_billing_invoices.ApplyMultipleCreditsToInvoiceRequest() # ApplyMultipleCreditsToInvoiceRequest |  (optional)

    try:
        # Apply Multiple Credits to Invoice
        api_response = api_instance.invoices_invoice_id_credits_post(invoice_id, x_com_zoho_subscriptions_organizationid, apply_multiple_credits_to_invoice_request=apply_multiple_credits_to_invoice_request)
        print("The response of InvoicesApi->invoices_invoice_id_credits_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_invoice_id_credits_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **apply_multiple_credits_to_invoice_request** | [**ApplyMultipleCreditsToInvoiceRequest**](ApplyMultipleCreditsToInvoiceRequest.md)|  | [optional] 

### Return type

[**ApplyMultipleCreditsToInvoiceResponse**](ApplyMultipleCreditsToInvoiceResponse.md)

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

# **invoices_invoice_id_customfields_post**
> UpdateCustomFieldsResponse invoices_invoice_id_customfields_post(invoice_id, x_com_zoho_subscriptions_organizationid, update_custom_fields_request=update_custom_fields_request)

Update Custom Fields

Update the custom fields of an invoice.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_invoices
from ls_zoho_billing_invoices.models.update_custom_fields_request import UpdateCustomFieldsRequest
from ls_zoho_billing_invoices.models.update_custom_fields_response import UpdateCustomFieldsResponse
from ls_zoho_billing_invoices.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_invoices.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_invoices.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_invoices.InvoicesApi(api_client)
    invoice_id = '903000000079426' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    update_custom_fields_request = ls_zoho_billing_invoices.UpdateCustomFieldsRequest() # UpdateCustomFieldsRequest |  (optional)

    try:
        # Update Custom Fields
        api_response = api_instance.invoices_invoice_id_customfields_post(invoice_id, x_com_zoho_subscriptions_organizationid, update_custom_fields_request=update_custom_fields_request)
        print("The response of InvoicesApi->invoices_invoice_id_customfields_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_invoice_id_customfields_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **update_custom_fields_request** | [**UpdateCustomFieldsRequest**](UpdateCustomFieldsRequest.md)|  | [optional] 

### Return type

[**UpdateCustomFieldsResponse**](UpdateCustomFieldsResponse.md)

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

# **invoices_invoice_id_delete**
> DeleteAnInvoiceResponse invoices_invoice_id_delete(invoice_id, x_com_zoho_subscriptions_organizationid)

Delete an invoice

Delete an existing invoice. Invoices which have payment or credits note applied cannot be deleted.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_invoices
from ls_zoho_billing_invoices.models.delete_an_invoice_response import DeleteAnInvoiceResponse
from ls_zoho_billing_invoices.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_invoices.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_invoices.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_invoices.InvoicesApi(api_client)
    invoice_id = '903000000079426' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Delete an invoice
        api_response = api_instance.invoices_invoice_id_delete(invoice_id, x_com_zoho_subscriptions_organizationid)
        print("The response of InvoicesApi->invoices_invoice_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_invoice_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**DeleteAnInvoiceResponse**](DeleteAnInvoiceResponse.md)

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

# **invoices_invoice_id_email_post**
> EmailAnInvoiceResponse invoices_invoice_id_email_post(invoice_id, x_com_zoho_subscriptions_organizationid, email_an_invoice_request=email_an_invoice_request)

Email an invoice

Email an invoice.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_invoices
from ls_zoho_billing_invoices.models.email_an_invoice_request import EmailAnInvoiceRequest
from ls_zoho_billing_invoices.models.email_an_invoice_response import EmailAnInvoiceResponse
from ls_zoho_billing_invoices.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_invoices.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_invoices.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_invoices.InvoicesApi(api_client)
    invoice_id = '903000000079426' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    email_an_invoice_request = ls_zoho_billing_invoices.EmailAnInvoiceRequest() # EmailAnInvoiceRequest |  (optional)

    try:
        # Email an invoice
        api_response = api_instance.invoices_invoice_id_email_post(invoice_id, x_com_zoho_subscriptions_organizationid, email_an_invoice_request=email_an_invoice_request)
        print("The response of InvoicesApi->invoices_invoice_id_email_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_invoice_id_email_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **email_an_invoice_request** | [**EmailAnInvoiceRequest**](EmailAnInvoiceRequest.md)|  | [optional] 

### Return type

[**EmailAnInvoiceResponse**](EmailAnInvoiceResponse.md)

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

# **invoices_invoice_id_get**
> RetrieveAnInvoiceResponse invoices_invoice_id_get(invoice_id, x_com_zoho_subscriptions_organizationid)

Retrieve an invoice

Details of an existing invoice.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_invoices
from ls_zoho_billing_invoices.models.retrieve_an_invoice_response import RetrieveAnInvoiceResponse
from ls_zoho_billing_invoices.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_invoices.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_invoices.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_invoices.InvoicesApi(api_client)
    invoice_id = '903000000079426' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Retrieve an invoice
        api_response = api_instance.invoices_invoice_id_get(invoice_id, x_com_zoho_subscriptions_organizationid)
        print("The response of InvoicesApi->invoices_invoice_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_invoice_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**RetrieveAnInvoiceResponse**](RetrieveAnInvoiceResponse.md)

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

# **invoices_invoice_id_lineitems_item_id_delete**
> DeleteItemsFromAPendingInvoiceResponse invoices_invoice_id_lineitems_item_id_delete(invoice_id, x_com_zoho_subscriptions_organizationid, item_id)

Delete items from a pending invoice

Deleting an item from pending invoice.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_invoices
from ls_zoho_billing_invoices.models.delete_items_from_a_pending_invoice_response import DeleteItemsFromAPendingInvoiceResponse
from ls_zoho_billing_invoices.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_invoices.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_invoices.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_invoices.InvoicesApi(api_client)
    invoice_id = '903000000079426' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    item_id = '7000000079434' # str | 

    try:
        # Delete items from a pending invoice
        api_response = api_instance.invoices_invoice_id_lineitems_item_id_delete(invoice_id, x_com_zoho_subscriptions_organizationid, item_id)
        print("The response of InvoicesApi->invoices_invoice_id_lineitems_item_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_invoice_id_lineitems_item_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **item_id** | **str**|  | 

### Return type

[**DeleteItemsFromAPendingInvoiceResponse**](DeleteItemsFromAPendingInvoiceResponse.md)

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

# **invoices_invoice_id_lineitems_post**
> AddItemsToAPendingInvoiceResponse invoices_invoice_id_lineitems_post(invoice_id, x_com_zoho_subscriptions_organizationid, add_items_to_a_pending_invoice_request=add_items_to_a_pending_invoice_request)

Add items to a pending invoice

Editing a pending invoice to add usage charges.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_invoices
from ls_zoho_billing_invoices.models.add_items_to_a_pending_invoice_request import AddItemsToAPendingInvoiceRequest
from ls_zoho_billing_invoices.models.add_items_to_a_pending_invoice_response import AddItemsToAPendingInvoiceResponse
from ls_zoho_billing_invoices.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_invoices.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_invoices.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_invoices.InvoicesApi(api_client)
    invoice_id = '903000000079426' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    add_items_to_a_pending_invoice_request = ls_zoho_billing_invoices.AddItemsToAPendingInvoiceRequest() # AddItemsToAPendingInvoiceRequest |  (optional)

    try:
        # Add items to a pending invoice
        api_response = api_instance.invoices_invoice_id_lineitems_post(invoice_id, x_com_zoho_subscriptions_organizationid, add_items_to_a_pending_invoice_request=add_items_to_a_pending_invoice_request)
        print("The response of InvoicesApi->invoices_invoice_id_lineitems_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_invoice_id_lineitems_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **add_items_to_a_pending_invoice_request** | [**AddItemsToAPendingInvoiceRequest**](AddItemsToAPendingInvoiceRequest.md)|  | [optional] 

### Return type

[**AddItemsToAPendingInvoiceResponse**](AddItemsToAPendingInvoiceResponse.md)

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

# **invoices_invoice_id_put**
> UpdateAnInvoiceResponse invoices_invoice_id_put(invoice_id, x_com_zoho_subscriptions_organizationid, ignore_auto_number_generation=ignore_auto_number_generation, update_an_invoice_request=update_an_invoice_request)

Update an invoice

Update an existing invoice. To delete a line item just remove it from the invoice_items list.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_invoices
from ls_zoho_billing_invoices.models.update_an_invoice_request import UpdateAnInvoiceRequest
from ls_zoho_billing_invoices.models.update_an_invoice_response import UpdateAnInvoiceResponse
from ls_zoho_billing_invoices.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_invoices.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_invoices.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_invoices.InvoicesApi(api_client)
    invoice_id = '903000000079426' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    ignore_auto_number_generation = True # bool | Ignore auto invoice number generation for this invoice. This mandates the invoice number. Allowed values <code>true</code> and <code>false</code> (optional)
    update_an_invoice_request = ls_zoho_billing_invoices.UpdateAnInvoiceRequest() # UpdateAnInvoiceRequest |  (optional)

    try:
        # Update an invoice
        api_response = api_instance.invoices_invoice_id_put(invoice_id, x_com_zoho_subscriptions_organizationid, ignore_auto_number_generation=ignore_auto_number_generation, update_an_invoice_request=update_an_invoice_request)
        print("The response of InvoicesApi->invoices_invoice_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_invoice_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **ignore_auto_number_generation** | **bool**| Ignore auto invoice number generation for this invoice. This mandates the invoice number. Allowed values &lt;code&gt;true&lt;/code&gt; and &lt;code&gt;false&lt;/code&gt; | [optional] 
 **update_an_invoice_request** | [**UpdateAnInvoiceRequest**](UpdateAnInvoiceRequest.md)|  | [optional] 

### Return type

[**UpdateAnInvoiceResponse**](UpdateAnInvoiceResponse.md)

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

# **invoices_invoice_id_void_post**
> VoidAnInvoiceResponse invoices_invoice_id_void_post(invoice_id, x_com_zoho_subscriptions_organizationid)

Void an invoice

Mark an invoice status as void. Upon voiding, the payments and credits associated with the invoices will be unassociated and will be under customer credits.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_invoices
from ls_zoho_billing_invoices.models.void_an_invoice_response import VoidAnInvoiceResponse
from ls_zoho_billing_invoices.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_invoices.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_invoices.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_invoices.InvoicesApi(api_client)
    invoice_id = '982000000567114' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Void an invoice
        api_response = api_instance.invoices_invoice_id_void_post(invoice_id, x_com_zoho_subscriptions_organizationid)
        print("The response of InvoicesApi->invoices_invoice_id_void_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_invoice_id_void_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**VoidAnInvoiceResponse**](VoidAnInvoiceResponse.md)

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

# **invoices_invoice_id_writeoff_post**
> WriteOffResponse invoices_invoice_id_writeoff_post(invoice_id, x_com_zoho_subscriptions_organizationid, write_off_request=write_off_request)

Write off

Write off a invoice.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_invoices
from ls_zoho_billing_invoices.models.write_off_request import WriteOffRequest
from ls_zoho_billing_invoices.models.write_off_response import WriteOffResponse
from ls_zoho_billing_invoices.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_invoices.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_invoices.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_invoices.InvoicesApi(api_client)
    invoice_id = '903000000079426' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    write_off_request = ls_zoho_billing_invoices.WriteOffRequest() # WriteOffRequest |  (optional)

    try:
        # Write off
        api_response = api_instance.invoices_invoice_id_writeoff_post(invoice_id, x_com_zoho_subscriptions_organizationid, write_off_request=write_off_request)
        print("The response of InvoicesApi->invoices_invoice_id_writeoff_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_invoice_id_writeoff_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **write_off_request** | [**WriteOffRequest**](WriteOffRequest.md)|  | [optional] 

### Return type

[**WriteOffResponse**](WriteOffResponse.md)

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

# **invoices_post**
> CreateAnInvoiceResponse invoices_post(x_com_zoho_subscriptions_organizationid, send=send, ignore_auto_number_generation=ignore_auto_number_generation, create_an_invoice_request=create_an_invoice_request)

Create an invoice

Create an invoice for your customer.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_invoices
from ls_zoho_billing_invoices.models.create_an_invoice_request import CreateAnInvoiceRequest
from ls_zoho_billing_invoices.models.create_an_invoice_response import CreateAnInvoiceResponse
from ls_zoho_billing_invoices.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_invoices.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_invoices.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_invoices.InvoicesApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    send = True # bool | Send the invoice to the contact person(s) associated with the invoice. Allowed values <code>true</code> and <code>false</code>. (optional)
    ignore_auto_number_generation = True # bool | Ignore auto invoice number generation for this invoice. This mandates the invoice number. Allowed values <code>true</code> and <code>false</code> (optional)
    create_an_invoice_request = ls_zoho_billing_invoices.CreateAnInvoiceRequest() # CreateAnInvoiceRequest |  (optional)

    try:
        # Create an invoice
        api_response = api_instance.invoices_post(x_com_zoho_subscriptions_organizationid, send=send, ignore_auto_number_generation=ignore_auto_number_generation, create_an_invoice_request=create_an_invoice_request)
        print("The response of InvoicesApi->invoices_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **send** | **bool**| Send the invoice to the contact person(s) associated with the invoice. Allowed values &lt;code&gt;true&lt;/code&gt; and &lt;code&gt;false&lt;/code&gt;. | [optional] 
 **ignore_auto_number_generation** | **bool**| Ignore auto invoice number generation for this invoice. This mandates the invoice number. Allowed values &lt;code&gt;true&lt;/code&gt; and &lt;code&gt;false&lt;/code&gt; | [optional] 
 **create_an_invoice_request** | [**CreateAnInvoiceRequest**](CreateAnInvoiceRequest.md)|  | [optional] 

### Return type

[**CreateAnInvoiceResponse**](CreateAnInvoiceResponse.md)

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

