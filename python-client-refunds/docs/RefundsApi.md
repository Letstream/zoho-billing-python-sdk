# ls_zoho_billing_refunds.RefundsApi

All URIs are relative to *https://www.zohoapis.com/billing/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**creditnotes_creditnote_id_refunds_post**](RefundsApi.md#creditnotes_creditnote_id_refunds_post) | **POST** /creditnotes/{creditnote_id}/refunds | Refund a credit note
[**creditnotes_refunds_refund_id_get**](RefundsApi.md#creditnotes_refunds_refund_id_get) | **GET** /creditnotes/refunds/{refund_id} | Retrieve refund details
[**payments_payment_id_refunds_post**](RefundsApi.md#payments_payment_id_refunds_post) | **POST** /payments/{payment_id}/refunds | Refund a payment


# **creditnotes_creditnote_id_refunds_post**
> RefundACreditNoteResponse creditnotes_creditnote_id_refunds_post(creditnote_id, x_com_zoho_subscriptions_organizationid, refund_a_credit_note_request=refund_a_credit_note_request)

Refund a credit note

Refund is made on the credit note.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_refunds
from ls_zoho_billing_refunds.models.refund_a_credit_note_request import RefundACreditNoteRequest
from ls_zoho_billing_refunds.models.refund_a_credit_note_response import RefundACreditNoteResponse
from ls_zoho_billing_refunds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_refunds.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_refunds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_refunds.RefundsApi(api_client)
    creditnote_id = '90300000081375' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    refund_a_credit_note_request = ls_zoho_billing_refunds.RefundACreditNoteRequest() # RefundACreditNoteRequest |  (optional)

    try:
        # Refund a credit note
        api_response = api_instance.creditnotes_creditnote_id_refunds_post(creditnote_id, x_com_zoho_subscriptions_organizationid, refund_a_credit_note_request=refund_a_credit_note_request)
        print("The response of RefundsApi->creditnotes_creditnote_id_refunds_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RefundsApi->creditnotes_creditnote_id_refunds_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creditnote_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **refund_a_credit_note_request** | [**RefundACreditNoteRequest**](RefundACreditNoteRequest.md)|  | [optional] 

### Return type

[**RefundACreditNoteResponse**](RefundACreditNoteResponse.md)

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

# **creditnotes_refunds_refund_id_get**
> RetrieveRefundDetailsResponse creditnotes_refunds_refund_id_get(refund_id, x_com_zoho_subscriptions_organizationid)

Retrieve refund details

Details of an existing refund.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_refunds
from ls_zoho_billing_refunds.models.retrieve_refund_details_response import RetrieveRefundDetailsResponse
from ls_zoho_billing_refunds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_refunds.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_refunds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_refunds.RefundsApi(api_client)
    refund_id = '90300000081385' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Retrieve refund details
        api_response = api_instance.creditnotes_refunds_refund_id_get(refund_id, x_com_zoho_subscriptions_organizationid)
        print("The response of RefundsApi->creditnotes_refunds_refund_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RefundsApi->creditnotes_refunds_refund_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refund_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**RetrieveRefundDetailsResponse**](RetrieveRefundDetailsResponse.md)

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

# **payments_payment_id_refunds_post**
> RefundAPaymentResponse payments_payment_id_refunds_post(payment_id, x_com_zoho_subscriptions_organizationid, refund_a_payment_request=refund_a_payment_request)

Refund a payment

A new credit note is created for the amount to be refund. Refund is then made for the credit note.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_refunds
from ls_zoho_billing_refunds.models.refund_a_payment_request import RefundAPaymentRequest
from ls_zoho_billing_refunds.models.refund_a_payment_response import RefundAPaymentResponse
from ls_zoho_billing_refunds.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_refunds.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_refunds.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_refunds.RefundsApi(api_client)
    payment_id = '90300000081385' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    refund_a_payment_request = ls_zoho_billing_refunds.RefundAPaymentRequest() # RefundAPaymentRequest |  (optional)

    try:
        # Refund a payment
        api_response = api_instance.payments_payment_id_refunds_post(payment_id, x_com_zoho_subscriptions_organizationid, refund_a_payment_request=refund_a_payment_request)
        print("The response of RefundsApi->payments_payment_id_refunds_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RefundsApi->payments_payment_id_refunds_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **refund_a_payment_request** | [**RefundAPaymentRequest**](RefundAPaymentRequest.md)|  | [optional] 

### Return type

[**RefundAPaymentResponse**](RefundAPaymentResponse.md)

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

