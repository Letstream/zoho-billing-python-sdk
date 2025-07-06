# ls_zoho_billing_credit_notes.CreditNotesApi

All URIs are relative to *https://www.zohoapis.com/billing/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**creditnotes_creditnote_id_converttoopen_post**](CreditNotesApi.md#creditnotes_creditnote_id_converttoopen_post) | **POST** /creditnotes/{creditnote_id}/converttoopen | Open a voided credit note
[**creditnotes_creditnote_id_delete**](CreditNotesApi.md#creditnotes_creditnote_id_delete) | **DELETE** /creditnotes/{creditnote_id} | Delete a credit note
[**creditnotes_creditnote_id_email_post**](CreditNotesApi.md#creditnotes_creditnote_id_email_post) | **POST** /creditnotes/{creditnote_id}/email | Email a credit note
[**creditnotes_creditnote_id_get**](CreditNotesApi.md#creditnotes_creditnote_id_get) | **GET** /creditnotes/{creditnote_id} | Retreive a credit note
[**creditnotes_creditnote_id_invoices_post**](CreditNotesApi.md#creditnotes_creditnote_id_invoices_post) | **POST** /creditnotes/{creditnote_id}/invoices | Apply Credits to Multiple Invoices
[**creditnotes_creditnote_id_void_post**](CreditNotesApi.md#creditnotes_creditnote_id_void_post) | **POST** /creditnotes/{creditnote_id}/void | Void a credit note
[**creditnotes_post**](CreditNotesApi.md#creditnotes_post) | **POST** /creditnotes | Create a credit note


# **creditnotes_creditnote_id_converttoopen_post**
> OpenAVoidedCreditNoteResponse creditnotes_creditnote_id_converttoopen_post(creditnote_id, x_com_zoho_subscriptions_organizationid)

Open a voided credit note

Convert a voided credit note to open.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_credit_notes
from ls_zoho_billing_credit_notes.models.open_a_voided_credit_note_response import OpenAVoidedCreditNoteResponse
from ls_zoho_billing_credit_notes.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_credit_notes.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_credit_notes.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_credit_notes.CreditNotesApi(api_client)
    creditnote_id = '90300000072369' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Open a voided credit note
        api_response = api_instance.creditnotes_creditnote_id_converttoopen_post(creditnote_id, x_com_zoho_subscriptions_organizationid)
        print("The response of CreditNotesApi->creditnotes_creditnote_id_converttoopen_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditNotesApi->creditnotes_creditnote_id_converttoopen_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creditnote_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**OpenAVoidedCreditNoteResponse**](OpenAVoidedCreditNoteResponse.md)

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

# **creditnotes_creditnote_id_delete**
> DeleteACreditNoteResponse creditnotes_creditnote_id_delete(creditnote_id, x_com_zoho_subscriptions_organizationid)

Delete a credit note

Delete an existing credit note.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_credit_notes
from ls_zoho_billing_credit_notes.models.delete_a_credit_note_response import DeleteACreditNoteResponse
from ls_zoho_billing_credit_notes.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_credit_notes.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_credit_notes.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_credit_notes.CreditNotesApi(api_client)
    creditnote_id = '90300000072369' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Delete a credit note
        api_response = api_instance.creditnotes_creditnote_id_delete(creditnote_id, x_com_zoho_subscriptions_organizationid)
        print("The response of CreditNotesApi->creditnotes_creditnote_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditNotesApi->creditnotes_creditnote_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creditnote_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**DeleteACreditNoteResponse**](DeleteACreditNoteResponse.md)

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

# **creditnotes_creditnote_id_email_post**
> EmailACreditNoteResponse creditnotes_creditnote_id_email_post(creditnote_id, x_com_zoho_subscriptions_organizationid, email_a_credit_note_request=email_a_credit_note_request)

Email a credit note

Email a credit note.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_credit_notes
from ls_zoho_billing_credit_notes.models.email_a_credit_note_request import EmailACreditNoteRequest
from ls_zoho_billing_credit_notes.models.email_a_credit_note_response import EmailACreditNoteResponse
from ls_zoho_billing_credit_notes.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_credit_notes.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_credit_notes.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_credit_notes.CreditNotesApi(api_client)
    creditnote_id = '90300000072369' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    email_a_credit_note_request = ls_zoho_billing_credit_notes.EmailACreditNoteRequest() # EmailACreditNoteRequest |  (optional)

    try:
        # Email a credit note
        api_response = api_instance.creditnotes_creditnote_id_email_post(creditnote_id, x_com_zoho_subscriptions_organizationid, email_a_credit_note_request=email_a_credit_note_request)
        print("The response of CreditNotesApi->creditnotes_creditnote_id_email_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditNotesApi->creditnotes_creditnote_id_email_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creditnote_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **email_a_credit_note_request** | [**EmailACreditNoteRequest**](EmailACreditNoteRequest.md)|  | [optional] 

### Return type

[**EmailACreditNoteResponse**](EmailACreditNoteResponse.md)

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

# **creditnotes_creditnote_id_get**
> RetreiveACreditNoteResponse creditnotes_creditnote_id_get(creditnote_id, x_com_zoho_subscriptions_organizationid)

Retreive a credit note

Details of an existing creditnote.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_credit_notes
from ls_zoho_billing_credit_notes.models.retreive_a_credit_note_response import RetreiveACreditNoteResponse
from ls_zoho_billing_credit_notes.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_credit_notes.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_credit_notes.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_credit_notes.CreditNotesApi(api_client)
    creditnote_id = '90300000072369' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Retreive a credit note
        api_response = api_instance.creditnotes_creditnote_id_get(creditnote_id, x_com_zoho_subscriptions_organizationid)
        print("The response of CreditNotesApi->creditnotes_creditnote_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditNotesApi->creditnotes_creditnote_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creditnote_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**RetreiveACreditNoteResponse**](RetreiveACreditNoteResponse.md)

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

# **creditnotes_creditnote_id_invoices_post**
> ApplyCreditsToMultipleInvoicesResponse creditnotes_creditnote_id_invoices_post(x_com_zoho_subscriptions_organizationid, creditnote_id, apply_credits_to_multiple_invoices_request=apply_credits_to_multiple_invoices_request)

Apply Credits to Multiple Invoices

To associate a creditnote to multiple invoices.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_credit_notes
from ls_zoho_billing_credit_notes.models.apply_credits_to_multiple_invoices_request import ApplyCreditsToMultipleInvoicesRequest
from ls_zoho_billing_credit_notes.models.apply_credits_to_multiple_invoices_response import ApplyCreditsToMultipleInvoicesResponse
from ls_zoho_billing_credit_notes.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_credit_notes.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_credit_notes.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_credit_notes.CreditNotesApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    creditnote_id = '90300000072369' # str | 
    apply_credits_to_multiple_invoices_request = ls_zoho_billing_credit_notes.ApplyCreditsToMultipleInvoicesRequest() # ApplyCreditsToMultipleInvoicesRequest |  (optional)

    try:
        # Apply Credits to Multiple Invoices
        api_response = api_instance.creditnotes_creditnote_id_invoices_post(x_com_zoho_subscriptions_organizationid, creditnote_id, apply_credits_to_multiple_invoices_request=apply_credits_to_multiple_invoices_request)
        print("The response of CreditNotesApi->creditnotes_creditnote_id_invoices_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditNotesApi->creditnotes_creditnote_id_invoices_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **creditnote_id** | **str**|  | 
 **apply_credits_to_multiple_invoices_request** | [**ApplyCreditsToMultipleInvoicesRequest**](ApplyCreditsToMultipleInvoicesRequest.md)|  | [optional] 

### Return type

[**ApplyCreditsToMultipleInvoicesResponse**](ApplyCreditsToMultipleInvoicesResponse.md)

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

# **creditnotes_creditnote_id_void_post**
> VoidACreditNoteResponse creditnotes_creditnote_id_void_post(creditnote_id, x_com_zoho_subscriptions_organizationid)

Void a credit note

Details of an existing creditnote.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_credit_notes
from ls_zoho_billing_credit_notes.models.void_a_credit_note_response import VoidACreditNoteResponse
from ls_zoho_billing_credit_notes.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_credit_notes.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_credit_notes.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_credit_notes.CreditNotesApi(api_client)
    creditnote_id = '90300000072369' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Void a credit note
        api_response = api_instance.creditnotes_creditnote_id_void_post(creditnote_id, x_com_zoho_subscriptions_organizationid)
        print("The response of CreditNotesApi->creditnotes_creditnote_id_void_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditNotesApi->creditnotes_creditnote_id_void_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creditnote_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**VoidACreditNoteResponse**](VoidACreditNoteResponse.md)

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

# **creditnotes_post**
> CreateACreditNoteResponse creditnotes_post(x_com_zoho_subscriptions_organizationid, create_a_credit_note_request=create_a_credit_note_request)

Create a credit note

Details of an existing creditnote.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_credit_notes
from ls_zoho_billing_credit_notes.models.create_a_credit_note_request import CreateACreditNoteRequest
from ls_zoho_billing_credit_notes.models.create_a_credit_note_response import CreateACreditNoteResponse
from ls_zoho_billing_credit_notes.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_credit_notes.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_credit_notes.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_credit_notes.CreditNotesApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    create_a_credit_note_request = ls_zoho_billing_credit_notes.CreateACreditNoteRequest() # CreateACreditNoteRequest |  (optional)

    try:
        # Create a credit note
        api_response = api_instance.creditnotes_post(x_com_zoho_subscriptions_organizationid, create_a_credit_note_request=create_a_credit_note_request)
        print("The response of CreditNotesApi->creditnotes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditNotesApi->creditnotes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **create_a_credit_note_request** | [**CreateACreditNoteRequest**](CreateACreditNoteRequest.md)|  | [optional] 

### Return type

[**CreateACreditNoteResponse**](CreateACreditNoteResponse.md)

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

