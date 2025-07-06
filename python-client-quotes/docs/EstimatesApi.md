# ls_zoho_billing_quotes.EstimatesApi

All URIs are relative to *https://www.zohoapis.com/billing/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**estimates_email_post**](EstimatesApi.md#estimates_email_post) | **POST** /estimates/email | Email multiple quotes
[**estimates_estimate_id_comments_comment_id_delete**](EstimatesApi.md#estimates_estimate_id_comments_comment_id_delete) | **DELETE** /estimates/{estimate_id}/comments/{comment_id} | Delete a comment
[**estimates_estimate_id_comments_comment_id_put**](EstimatesApi.md#estimates_estimate_id_comments_comment_id_put) | **PUT** /estimates/{estimate_id}/comments/{comment_id} | Update comment
[**estimates_estimate_id_comments_get**](EstimatesApi.md#estimates_estimate_id_comments_get) | **GET** /estimates/{estimate_id}/comments | List quote comments &amp; history
[**estimates_estimate_id_comments_post**](EstimatesApi.md#estimates_estimate_id_comments_post) | **POST** /estimates/{estimate_id}/comments | Add Comments
[**estimates_estimate_id_delete**](EstimatesApi.md#estimates_estimate_id_delete) | **DELETE** /estimates/{estimate_id} | Delete a Quote
[**estimates_estimate_id_email_get**](EstimatesApi.md#estimates_estimate_id_email_get) | **GET** /estimates/{estimate_id}/email | Get quote email content
[**estimates_estimate_id_email_post**](EstimatesApi.md#estimates_estimate_id_email_post) | **POST** /estimates/{estimate_id}/email | Email a quote
[**estimates_estimate_id_get**](EstimatesApi.md#estimates_estimate_id_get) | **GET** /estimates/{estimate_id} | Retrieve a Quote
[**estimates_estimate_id_put**](EstimatesApi.md#estimates_estimate_id_put) | **PUT** /estimates/{estimate_id} | Update a Quote
[**estimates_estimate_id_status_accepted_post**](EstimatesApi.md#estimates_estimate_id_status_accepted_post) | **POST** /estimates/{estimate_id}/status/accepted | Mark a Quote as accepted
[**estimates_estimate_id_status_declined_post**](EstimatesApi.md#estimates_estimate_id_status_declined_post) | **POST** /estimates/{estimate_id}/status/declined | Mark a Quote as declined
[**estimates_estimate_id_status_sent_post**](EstimatesApi.md#estimates_estimate_id_status_sent_post) | **POST** /estimates/{estimate_id}/status/sent | Mark a Quote as sent
[**estimates_estimate_id_templates_template_id_put**](EstimatesApi.md#estimates_estimate_id_templates_template_id_put) | **PUT** /estimates/{estimate_id}/templates/{template_id} | Update quote template
[**estimates_get**](EstimatesApi.md#estimates_get) | **GET** /estimates | List Quotes
[**estimates_pdf_get**](EstimatesApi.md#estimates_pdf_get) | **GET** /estimates/pdf | Bulk export quotes
[**estimates_post**](EstimatesApi.md#estimates_post) | **POST** /estimates | Create a Quote
[**estimates_print_get**](EstimatesApi.md#estimates_print_get) | **GET** /estimates/print | Bulk print Quotes
[**estimates_templates_get**](EstimatesApi.md#estimates_templates_get) | **GET** /estimates/templates | List quote templates


# **estimates_email_post**
> EmailMultipleEstimatesResponse estimates_email_post(x_com_zoho_subscriptions_organizationid, estimate_ids)

Email multiple quotes

Send quotes to your customers by email. Maximum of 10 quotes can be sent at once.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_quotes
from ls_zoho_billing_quotes.models.email_multiple_estimates_response import EmailMultipleEstimatesResponse
from ls_zoho_billing_quotes.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_quotes.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_quotes.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_quotes.EstimatesApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    estimate_ids = '' # str | Comma separated quote ids which are to be emailed.

    try:
        # Email multiple quotes
        api_response = api_instance.estimates_email_post(x_com_zoho_subscriptions_organizationid, estimate_ids)
        print("The response of EstimatesApi->estimates_email_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EstimatesApi->estimates_email_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **estimate_ids** | **str**| Comma separated quote ids which are to be emailed. | 

### Return type

[**EmailMultipleEstimatesResponse**](EmailMultipleEstimatesResponse.md)

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

# **estimates_estimate_id_comments_comment_id_delete**
> DeleteACommentResponse estimates_estimate_id_comments_comment_id_delete(estimate_id, x_com_zoho_subscriptions_organizationid, comment_id)

Delete a comment

Delete a quote comment.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_quotes
from ls_zoho_billing_quotes.models.delete_a_comment_response import DeleteACommentResponse
from ls_zoho_billing_quotes.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_quotes.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_quotes.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_quotes.EstimatesApi(api_client)
    estimate_id = '982000000567011' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    comment_id = '982000000567019' # str | 

    try:
        # Delete a comment
        api_response = api_instance.estimates_estimate_id_comments_comment_id_delete(estimate_id, x_com_zoho_subscriptions_organizationid, comment_id)
        print("The response of EstimatesApi->estimates_estimate_id_comments_comment_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EstimatesApi->estimates_estimate_id_comments_comment_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **estimate_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **comment_id** | **str**|  | 

### Return type

[**DeleteACommentResponse**](DeleteACommentResponse.md)

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

# **estimates_estimate_id_comments_comment_id_put**
> UpdateCommentResponse estimates_estimate_id_comments_comment_id_put(estimate_id, x_com_zoho_subscriptions_organizationid, comment_id, update_comment_request=update_comment_request)

Update comment

Update an existing comment of a quote.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_quotes
from ls_zoho_billing_quotes.models.update_comment_request import UpdateCommentRequest
from ls_zoho_billing_quotes.models.update_comment_response import UpdateCommentResponse
from ls_zoho_billing_quotes.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_quotes.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_quotes.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_quotes.EstimatesApi(api_client)
    estimate_id = '982000000567011' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    comment_id = '982000000567019' # str | 
    update_comment_request = ls_zoho_billing_quotes.UpdateCommentRequest() # UpdateCommentRequest |  (optional)

    try:
        # Update comment
        api_response = api_instance.estimates_estimate_id_comments_comment_id_put(estimate_id, x_com_zoho_subscriptions_organizationid, comment_id, update_comment_request=update_comment_request)
        print("The response of EstimatesApi->estimates_estimate_id_comments_comment_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EstimatesApi->estimates_estimate_id_comments_comment_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **estimate_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **comment_id** | **str**|  | 
 **update_comment_request** | [**UpdateCommentRequest**](UpdateCommentRequest.md)|  | [optional] 

### Return type

[**UpdateCommentResponse**](UpdateCommentResponse.md)

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

# **estimates_estimate_id_comments_get**
> ListEstimateCommentsAndHistoryResponse estimates_estimate_id_comments_get(estimate_id, x_com_zoho_subscriptions_organizationid)

List quote comments & history

Get the complete history and comments of a quote.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_quotes
from ls_zoho_billing_quotes.models.list_estimate_comments_and_history_response import ListEstimateCommentsAndHistoryResponse
from ls_zoho_billing_quotes.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_quotes.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_quotes.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_quotes.EstimatesApi(api_client)
    estimate_id = '982000000567011' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # List quote comments & history
        api_response = api_instance.estimates_estimate_id_comments_get(estimate_id, x_com_zoho_subscriptions_organizationid)
        print("The response of EstimatesApi->estimates_estimate_id_comments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EstimatesApi->estimates_estimate_id_comments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **estimate_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**ListEstimateCommentsAndHistoryResponse**](ListEstimateCommentsAndHistoryResponse.md)

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

# **estimates_estimate_id_comments_post**
> AddCommentsResponse estimates_estimate_id_comments_post(estimate_id, x_com_zoho_subscriptions_organizationid, add_comments_request=add_comments_request)

Add Comments

Add a comment for a quote.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_quotes
from ls_zoho_billing_quotes.models.add_comments_request import AddCommentsRequest
from ls_zoho_billing_quotes.models.add_comments_response import AddCommentsResponse
from ls_zoho_billing_quotes.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_quotes.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_quotes.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_quotes.EstimatesApi(api_client)
    estimate_id = '982000000567011' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    add_comments_request = ls_zoho_billing_quotes.AddCommentsRequest() # AddCommentsRequest |  (optional)

    try:
        # Add Comments
        api_response = api_instance.estimates_estimate_id_comments_post(estimate_id, x_com_zoho_subscriptions_organizationid, add_comments_request=add_comments_request)
        print("The response of EstimatesApi->estimates_estimate_id_comments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EstimatesApi->estimates_estimate_id_comments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **estimate_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **add_comments_request** | [**AddCommentsRequest**](AddCommentsRequest.md)|  | [optional] 

### Return type

[**AddCommentsResponse**](AddCommentsResponse.md)

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

# **estimates_estimate_id_delete**
> DeleteAnEstimateResponse estimates_estimate_id_delete(estimate_id, x_com_zoho_subscriptions_organizationid)

Delete a Quote

Delete an existing quote.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_quotes
from ls_zoho_billing_quotes.models.delete_an_estimate_response import DeleteAnEstimateResponse
from ls_zoho_billing_quotes.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_quotes.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_quotes.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_quotes.EstimatesApi(api_client)
    estimate_id = '982000000567011' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Delete a Quote
        api_response = api_instance.estimates_estimate_id_delete(estimate_id, x_com_zoho_subscriptions_organizationid)
        print("The response of EstimatesApi->estimates_estimate_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EstimatesApi->estimates_estimate_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **estimate_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**DeleteAnEstimateResponse**](DeleteAnEstimateResponse.md)

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

# **estimates_estimate_id_email_get**
> GetEstimateEmailContentResponse estimates_estimate_id_email_get(estimate_id, x_com_zoho_subscriptions_organizationid, email_template_id)

Get quote email content

Get the email content of a Quote.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_quotes
from ls_zoho_billing_quotes.models.get_estimate_email_content_response import GetEstimateEmailContentResponse
from ls_zoho_billing_quotes.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_quotes.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_quotes.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_quotes.EstimatesApi(api_client)
    estimate_id = '982000000567011' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    email_template_id = '982000000000079' # str | Get the email content based on a specific email template. If this param is not inputted, then the content will be based on the email template associated with the customer. If no template is associated with the customer, then default template will be used.

    try:
        # Get quote email content
        api_response = api_instance.estimates_estimate_id_email_get(estimate_id, x_com_zoho_subscriptions_organizationid, email_template_id)
        print("The response of EstimatesApi->estimates_estimate_id_email_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EstimatesApi->estimates_estimate_id_email_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **estimate_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **email_template_id** | **str**| Get the email content based on a specific email template. If this param is not inputted, then the content will be based on the email template associated with the customer. If no template is associated with the customer, then default template will be used. | 

### Return type

[**GetEstimateEmailContentResponse**](GetEstimateEmailContentResponse.md)

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

# **estimates_estimate_id_email_post**
> EmailAnEstimateResponse estimates_estimate_id_email_post(estimate_id, x_com_zoho_subscriptions_organizationid, attachments=attachments, email_an_estimate_request=email_an_estimate_request)

Email a quote

Email a quote to the customer. Input json string is not mandatory. If input json string is empty, mail will be send with default mail content.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_quotes
from ls_zoho_billing_quotes.models.email_an_estimate_request import EmailAnEstimateRequest
from ls_zoho_billing_quotes.models.email_an_estimate_response import EmailAnEstimateResponse
from ls_zoho_billing_quotes.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_quotes.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_quotes.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_quotes.EstimatesApi(api_client)
    estimate_id = '982000000567011' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    attachments =  # bytearray | Files to be attached to the email (optional)
    email_an_estimate_request = ls_zoho_billing_quotes.EmailAnEstimateRequest() # EmailAnEstimateRequest |  (optional)

    try:
        # Email a quote
        api_response = api_instance.estimates_estimate_id_email_post(estimate_id, x_com_zoho_subscriptions_organizationid, attachments=attachments, email_an_estimate_request=email_an_estimate_request)
        print("The response of EstimatesApi->estimates_estimate_id_email_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EstimatesApi->estimates_estimate_id_email_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **estimate_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **attachments** | **bytearray**| Files to be attached to the email | [optional] 
 **email_an_estimate_request** | [**EmailAnEstimateRequest**](EmailAnEstimateRequest.md)|  | [optional] 

### Return type

[**EmailAnEstimateResponse**](EmailAnEstimateResponse.md)

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

# **estimates_estimate_id_get**
> GetAnEstimateResponse estimates_estimate_id_get(estimate_id, x_com_zoho_subscriptions_organizationid, var_print=var_print, accept=accept)

Retrieve a Quote

Fetch the details of a quote.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_quotes
from ls_zoho_billing_quotes.models.get_an_estimate_response import GetAnEstimateResponse
from ls_zoho_billing_quotes.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_quotes.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_quotes.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_quotes.EstimatesApi(api_client)
    estimate_id = '982000000567011' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    var_print =   # bool | Print the exported pdf. Allowed Values: <code>true</code> and <code>false</code> (optional)
    accept = '' # str | Get the details of a particular quote in formats such as json/ pdf/ html. Default format is json.Allowed Values: <code>json</code>, <code>pdf</code> and <code>html</code> (optional)

    try:
        # Retrieve a Quote
        api_response = api_instance.estimates_estimate_id_get(estimate_id, x_com_zoho_subscriptions_organizationid, var_print=var_print, accept=accept)
        print("The response of EstimatesApi->estimates_estimate_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EstimatesApi->estimates_estimate_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **estimate_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **var_print** | **bool**| Print the exported pdf. Allowed Values: &lt;code&gt;true&lt;/code&gt; and &lt;code&gt;false&lt;/code&gt; | [optional] 
 **accept** | **str**| Get the details of a particular quote in formats such as json/ pdf/ html. Default format is json.Allowed Values: &lt;code&gt;json&lt;/code&gt;, &lt;code&gt;pdf&lt;/code&gt; and &lt;code&gt;html&lt;/code&gt; | [optional] 

### Return type

[**GetAnEstimateResponse**](GetAnEstimateResponse.md)

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

# **estimates_estimate_id_put**
> UpdateAnEstimateResponse estimates_estimate_id_put(estimate_id, x_com_zoho_subscriptions_organizationid, ignore_auto_number_generation=ignore_auto_number_generation, update_an_estimate_request=update_an_estimate_request)

Update a Quote

Update an existing quote. To delete a line item just remove it from the line_items list.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_quotes
from ls_zoho_billing_quotes.models.update_an_estimate_request import UpdateAnEstimateRequest
from ls_zoho_billing_quotes.models.update_an_estimate_response import UpdateAnEstimateResponse
from ls_zoho_billing_quotes.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_quotes.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_quotes.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_quotes.EstimatesApi(api_client)
    estimate_id = '982000000567011' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    ignore_auto_number_generation = false # bool | Ignore auto quote number generation for this quote. This mandates the quote number to be entered manually. (optional)
    update_an_estimate_request = ls_zoho_billing_quotes.UpdateAnEstimateRequest() # UpdateAnEstimateRequest |  (optional)

    try:
        # Update a Quote
        api_response = api_instance.estimates_estimate_id_put(estimate_id, x_com_zoho_subscriptions_organizationid, ignore_auto_number_generation=ignore_auto_number_generation, update_an_estimate_request=update_an_estimate_request)
        print("The response of EstimatesApi->estimates_estimate_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EstimatesApi->estimates_estimate_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **estimate_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **ignore_auto_number_generation** | **bool**| Ignore auto quote number generation for this quote. This mandates the quote number to be entered manually. | [optional] 
 **update_an_estimate_request** | [**UpdateAnEstimateRequest**](UpdateAnEstimateRequest.md)|  | [optional] 

### Return type

[**UpdateAnEstimateResponse**](UpdateAnEstimateResponse.md)

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

# **estimates_estimate_id_status_accepted_post**
> MarkAnEstimateAsAcceptedResponse estimates_estimate_id_status_accepted_post(estimate_id, x_com_zoho_subscriptions_organizationid)

Mark a Quote as accepted

Mark a sent quote as accepted if the customer has accepted it.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_quotes
from ls_zoho_billing_quotes.models.mark_an_estimate_as_accepted_response import MarkAnEstimateAsAcceptedResponse
from ls_zoho_billing_quotes.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_quotes.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_quotes.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_quotes.EstimatesApi(api_client)
    estimate_id = '982000000567011' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Mark a Quote as accepted
        api_response = api_instance.estimates_estimate_id_status_accepted_post(estimate_id, x_com_zoho_subscriptions_organizationid)
        print("The response of EstimatesApi->estimates_estimate_id_status_accepted_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EstimatesApi->estimates_estimate_id_status_accepted_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **estimate_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**MarkAnEstimateAsAcceptedResponse**](MarkAnEstimateAsAcceptedResponse.md)

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

# **estimates_estimate_id_status_declined_post**
> MarkAnEstimateAsDeclinedResponse estimates_estimate_id_status_declined_post(estimate_id, x_com_zoho_subscriptions_organizationid)

Mark a Quote as declined

Mark a sent quote as declined if the customer has rejected it.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_quotes
from ls_zoho_billing_quotes.models.mark_an_estimate_as_declined_response import MarkAnEstimateAsDeclinedResponse
from ls_zoho_billing_quotes.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_quotes.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_quotes.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_quotes.EstimatesApi(api_client)
    estimate_id = '982000000567011' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Mark a Quote as declined
        api_response = api_instance.estimates_estimate_id_status_declined_post(estimate_id, x_com_zoho_subscriptions_organizationid)
        print("The response of EstimatesApi->estimates_estimate_id_status_declined_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EstimatesApi->estimates_estimate_id_status_declined_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **estimate_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**MarkAnEstimateAsDeclinedResponse**](MarkAnEstimateAsDeclinedResponse.md)

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

# **estimates_estimate_id_status_sent_post**
> MarkAnEstimateAsSentResponse estimates_estimate_id_status_sent_post(estimate_id, x_com_zoho_subscriptions_organizationid)

Mark a Quote as sent

Mark a draft quote as sent.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_quotes
from ls_zoho_billing_quotes.models.mark_an_estimate_as_sent_response import MarkAnEstimateAsSentResponse
from ls_zoho_billing_quotes.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_quotes.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_quotes.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_quotes.EstimatesApi(api_client)
    estimate_id = '982000000567011' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Mark a Quote as sent
        api_response = api_instance.estimates_estimate_id_status_sent_post(estimate_id, x_com_zoho_subscriptions_organizationid)
        print("The response of EstimatesApi->estimates_estimate_id_status_sent_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EstimatesApi->estimates_estimate_id_status_sent_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **estimate_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**MarkAnEstimateAsSentResponse**](MarkAnEstimateAsSentResponse.md)

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

# **estimates_estimate_id_templates_template_id_put**
> UpdateEstimateTemplateResponse estimates_estimate_id_templates_template_id_put(estimate_id, x_com_zoho_subscriptions_organizationid, template_id)

Update quote template

Update the pdf template associated with the quote.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_quotes
from ls_zoho_billing_quotes.models.update_estimate_template_response import UpdateEstimateTemplateResponse
from ls_zoho_billing_quotes.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_quotes.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_quotes.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_quotes.EstimatesApi(api_client)
    estimate_id = '982000000567011' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    template_id = '982000000000143' # str | 

    try:
        # Update quote template
        api_response = api_instance.estimates_estimate_id_templates_template_id_put(estimate_id, x_com_zoho_subscriptions_organizationid, template_id)
        print("The response of EstimatesApi->estimates_estimate_id_templates_template_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EstimatesApi->estimates_estimate_id_templates_template_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **estimate_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **template_id** | **str**|  | 

### Return type

[**UpdateEstimateTemplateResponse**](UpdateEstimateTemplateResponse.md)

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

# **estimates_get**
> ListEstimatesResponse estimates_get(x_com_zoho_subscriptions_organizationid, zcrm_potential_id=zcrm_potential_id)

List Quotes

List all quotes with pagination.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_quotes
from ls_zoho_billing_quotes.models.list_estimates_response import ListEstimatesResponse
from ls_zoho_billing_quotes.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_quotes.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_quotes.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_quotes.EstimatesApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    zcrm_potential_id = 460000000026049 # int | Potential ID of a Deal in CRM. (optional)

    try:
        # List Quotes
        api_response = api_instance.estimates_get(x_com_zoho_subscriptions_organizationid, zcrm_potential_id=zcrm_potential_id)
        print("The response of EstimatesApi->estimates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EstimatesApi->estimates_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **zcrm_potential_id** | **int**| Potential ID of a Deal in CRM. | [optional] 

### Return type

[**ListEstimatesResponse**](ListEstimatesResponse.md)

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

# **estimates_pdf_get**
> BulkExportEstimatesResponse estimates_pdf_get(x_com_zoho_subscriptions_organizationid, estimate_ids)

Bulk export quotes

Maximum of 25 quotes can be exported in a single pdf.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_quotes
from ls_zoho_billing_quotes.models.bulk_export_estimates_response import BulkExportEstimatesResponse
from ls_zoho_billing_quotes.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_quotes.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_quotes.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_quotes.EstimatesApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    estimate_ids = '' # str | Comma separated quote ids which are to be emailed.

    try:
        # Bulk export quotes
        api_response = api_instance.estimates_pdf_get(x_com_zoho_subscriptions_organizationid, estimate_ids)
        print("The response of EstimatesApi->estimates_pdf_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EstimatesApi->estimates_pdf_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **estimate_ids** | **str**| Comma separated quote ids which are to be emailed. | 

### Return type

[**BulkExportEstimatesResponse**](BulkExportEstimatesResponse.md)

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

# **estimates_post**
> CreateAnEstimateResponse estimates_post(x_com_zoho_subscriptions_organizationid, send=send, ignore_auto_number_generation=ignore_auto_number_generation, create_an_estimate_request=create_an_estimate_request)

Create a Quote

Create a quote for your customer.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_quotes
from ls_zoho_billing_quotes.models.create_an_estimate_request import CreateAnEstimateRequest
from ls_zoho_billing_quotes.models.create_an_estimate_response import CreateAnEstimateResponse
from ls_zoho_billing_quotes.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_quotes.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_quotes.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_quotes.EstimatesApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    send = True # bool | Send the quote to the contact person(s) associated with the quote.Allowed Values: <code>true</code> and <code>false</code> (optional)
    ignore_auto_number_generation = false # bool | Ignore auto quote number generation for this quote. This mandates the quote number to be entered manually. (optional)
    create_an_estimate_request = ls_zoho_billing_quotes.CreateAnEstimateRequest() # CreateAnEstimateRequest |  (optional)

    try:
        # Create a Quote
        api_response = api_instance.estimates_post(x_com_zoho_subscriptions_organizationid, send=send, ignore_auto_number_generation=ignore_auto_number_generation, create_an_estimate_request=create_an_estimate_request)
        print("The response of EstimatesApi->estimates_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EstimatesApi->estimates_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **send** | **bool**| Send the quote to the contact person(s) associated with the quote.Allowed Values: &lt;code&gt;true&lt;/code&gt; and &lt;code&gt;false&lt;/code&gt; | [optional] 
 **ignore_auto_number_generation** | **bool**| Ignore auto quote number generation for this quote. This mandates the quote number to be entered manually. | [optional] 
 **create_an_estimate_request** | [**CreateAnEstimateRequest**](CreateAnEstimateRequest.md)|  | [optional] 

### Return type

[**CreateAnEstimateResponse**](CreateAnEstimateResponse.md)

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

# **estimates_print_get**
> BulkPrintEstimatesResponse estimates_print_get(x_com_zoho_subscriptions_organizationid, estimate_ids)

Bulk print Quotes

Export Quotes as pdf and print them. Maximum of 25 quotes can be printed.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_quotes
from ls_zoho_billing_quotes.models.bulk_print_estimates_response import BulkPrintEstimatesResponse
from ls_zoho_billing_quotes.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_quotes.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_quotes.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_quotes.EstimatesApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    estimate_ids = '' # str | Comma separated quote ids which are to be emailed.

    try:
        # Bulk print Quotes
        api_response = api_instance.estimates_print_get(x_com_zoho_subscriptions_organizationid, estimate_ids)
        print("The response of EstimatesApi->estimates_print_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EstimatesApi->estimates_print_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **estimate_ids** | **str**| Comma separated quote ids which are to be emailed. | 

### Return type

[**BulkPrintEstimatesResponse**](BulkPrintEstimatesResponse.md)

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

# **estimates_templates_get**
> ListEstimateTemplatesResponse estimates_templates_get(x_com_zoho_subscriptions_organizationid)

List quote templates

Get all quote pdf templates.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_quotes
from ls_zoho_billing_quotes.models.list_estimate_templates_response import ListEstimateTemplatesResponse
from ls_zoho_billing_quotes.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_quotes.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_quotes.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_quotes.EstimatesApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # List quote templates
        api_response = api_instance.estimates_templates_get(x_com_zoho_subscriptions_organizationid)
        print("The response of EstimatesApi->estimates_templates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EstimatesApi->estimates_templates_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**ListEstimateTemplatesResponse**](ListEstimateTemplatesResponse.md)

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

