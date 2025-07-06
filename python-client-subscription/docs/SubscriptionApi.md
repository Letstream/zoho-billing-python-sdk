# ls_zoho_billing_subscription.SubscriptionApi

All URIs are relative to *https://www.zohoapis.com/billing/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscriptions_get**](SubscriptionApi.md#subscriptions_get) | **GET** /subscriptions | List all subscriptions
[**subscriptions_post**](SubscriptionApi.md#subscriptions_post) | **POST** /subscriptions | Create a subscription
[**subscriptions_subscription_id_autocollect_post**](SubscriptionApi.md#subscriptions_subscription_id_autocollect_post) | **POST** /subscriptions/{subscription_id}/autocollect | Change to Online/Offline mode
[**subscriptions_subscription_id_buyonetimeaddon_post**](SubscriptionApi.md#subscriptions_subscription_id_buyonetimeaddon_post) | **POST** /subscriptions/{subscription_id}/buyonetimeaddon | Buy one-time addon
[**subscriptions_subscription_id_cancel_post**](SubscriptionApi.md#subscriptions_subscription_id_cancel_post) | **POST** /subscriptions/{subscription_id}/cancel | Cancel a subscription
[**subscriptions_subscription_id_card_delete**](SubscriptionApi.md#subscriptions_subscription_id_card_delete) | **DELETE** /subscriptions/{subscription_id}/card | Remove Card
[**subscriptions_subscription_id_card_post**](SubscriptionApi.md#subscriptions_subscription_id_card_post) | **POST** /subscriptions/{subscription_id}/card | Update Card
[**subscriptions_subscription_id_charge_post**](SubscriptionApi.md#subscriptions_subscription_id_charge_post) | **POST** /subscriptions/{subscription_id}/charge | Add Charge
[**subscriptions_subscription_id_contactpersons_post**](SubscriptionApi.md#subscriptions_subscription_id_contactpersons_post) | **POST** /subscriptions/{subscription_id}/contactpersons | Add contact person
[**subscriptions_subscription_id_coupons_coupon_code_post**](SubscriptionApi.md#subscriptions_subscription_id_coupons_coupon_code_post) | **POST** /subscriptions/{subscription_id}/coupons/{coupon_code} | Associate a coupon
[**subscriptions_subscription_id_coupons_delete**](SubscriptionApi.md#subscriptions_subscription_id_coupons_delete) | **DELETE** /subscriptions/{subscription_id}/coupons | Remove a coupon
[**subscriptions_subscription_id_customfields_post**](SubscriptionApi.md#subscriptions_subscription_id_customfields_post) | **POST** /subscriptions/{subscription_id}/customfields | Update Custom Fields
[**subscriptions_subscription_id_delete**](SubscriptionApi.md#subscriptions_subscription_id_delete) | **DELETE** /subscriptions/{subscription_id} | Delete a subscription
[**subscriptions_subscription_id_get**](SubscriptionApi.md#subscriptions_subscription_id_get) | **GET** /subscriptions/{subscription_id} | Retrieve a subscription
[**subscriptions_subscription_id_lineitems_plan_or_addon_code_post**](SubscriptionApi.md#subscriptions_subscription_id_lineitems_plan_or_addon_code_post) | **POST** /subscriptions/{subscription_id}/lineitems/{plan_or_addon_code} | Add/Edit description for a item in line items list
[**subscriptions_subscription_id_notes_note_id_delete**](SubscriptionApi.md#subscriptions_subscription_id_notes_note_id_delete) | **DELETE** /subscriptions/{subscription_id}/notes/{note_id} | Delete a note
[**subscriptions_subscription_id_notes_post**](SubscriptionApi.md#subscriptions_subscription_id_notes_post) | **POST** /subscriptions/{subscription_id}/notes | Add a note
[**subscriptions_subscription_id_postpone_post**](SubscriptionApi.md#subscriptions_subscription_id_postpone_post) | **POST** /subscriptions/{subscription_id}/postpone | Postpone renewal
[**subscriptions_subscription_id_put**](SubscriptionApi.md#subscriptions_subscription_id_put) | **PUT** /subscriptions/{subscription_id} | Update a subscription
[**subscriptions_subscription_id_reactivate_post**](SubscriptionApi.md#subscriptions_subscription_id_reactivate_post) | **POST** /subscriptions/{subscription_id}/reactivate | Reactivate subscription
[**subscriptions_subscription_id_recentactivities_get**](SubscriptionApi.md#subscriptions_subscription_id_recentactivities_get) | **GET** /subscriptions/{subscription_id}/recentactivities | Subscription Activities
[**subscriptions_subscription_id_reference_post**](SubscriptionApi.md#subscriptions_subscription_id_reference_post) | **POST** /subscriptions/{subscription_id}/reference | Update Reference
[**subscriptions_subscription_id_salesperson_post**](SubscriptionApi.md#subscriptions_subscription_id_salesperson_post) | **POST** /subscriptions/{subscription_id}/salesperson | Update Sales Person
[**subscriptions_subscription_id_scheduledchanges_get**](SubscriptionApi.md#subscriptions_subscription_id_scheduledchanges_get) | **GET** /subscriptions/{subscription_id}/scheduledchanges | View Scheduled Changes


# **subscriptions_get**
> ListAllSubscriptionsResponse subscriptions_get(x_com_zoho_subscriptions_organizationid, filter_by=filter_by)

List all subscriptions

List of subscriptions that match the given subscription status. <br><br> To list the subscriptions of a particular customer append a param <code>customer_id={customer_id}</code>. <br><br>To list subscriptions based on Reference#, append the param <code>reference_contains={reference_value}</code>.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_subscription
from ls_zoho_billing_subscription.models.list_all_subscriptions_response import ListAllSubscriptionsResponse
from ls_zoho_billing_subscription.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_subscription.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_subscription.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_subscription.SubscriptionApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    filter_by = 'SubscriptionStatus.ACTIVE' # str | The possible values for SubscriptionStatus are <code>All</code>, <code>ACTIVE</code>, <code>LIVE</code>, <code>FUTURE</code>, <code>TRIAL</code>, <code>PAST_DUE</code>, <code>UNPAID</code>, <code>NON_RENEWING</code>, <code>CANCELLED_FROM_DUNNING</code>, <code>CANCELLED</code>, <code>EXPIRED</code>, <code>TRIAL_EXPIRED</code>, <code>CANCELLED_LAST_MONTH</code>, <code>CANCELLED_THIS_MONTH</code>. <br><br>To list subscriptions based on Online/Offline, pass the <code>filter_by</code> param value as <code>SubscriptionMode.ONLINE</code> or <code>SubscriptionMode.OFFLINE</code>.  (optional)

    try:
        # List all subscriptions
        api_response = api_instance.subscriptions_get(x_com_zoho_subscriptions_organizationid, filter_by=filter_by)
        print("The response of SubscriptionApi->subscriptions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscriptions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **filter_by** | **str**| The possible values for SubscriptionStatus are &lt;code&gt;All&lt;/code&gt;, &lt;code&gt;ACTIVE&lt;/code&gt;, &lt;code&gt;LIVE&lt;/code&gt;, &lt;code&gt;FUTURE&lt;/code&gt;, &lt;code&gt;TRIAL&lt;/code&gt;, &lt;code&gt;PAST_DUE&lt;/code&gt;, &lt;code&gt;UNPAID&lt;/code&gt;, &lt;code&gt;NON_RENEWING&lt;/code&gt;, &lt;code&gt;CANCELLED_FROM_DUNNING&lt;/code&gt;, &lt;code&gt;CANCELLED&lt;/code&gt;, &lt;code&gt;EXPIRED&lt;/code&gt;, &lt;code&gt;TRIAL_EXPIRED&lt;/code&gt;, &lt;code&gt;CANCELLED_LAST_MONTH&lt;/code&gt;, &lt;code&gt;CANCELLED_THIS_MONTH&lt;/code&gt;. &lt;br&gt;&lt;br&gt;To list subscriptions based on Online/Offline, pass the &lt;code&gt;filter_by&lt;/code&gt; param value as &lt;code&gt;SubscriptionMode.ONLINE&lt;/code&gt; or &lt;code&gt;SubscriptionMode.OFFLINE&lt;/code&gt;.  | [optional] 

### Return type

[**ListAllSubscriptionsResponse**](ListAllSubscriptionsResponse.md)

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

# **subscriptions_post**
> CreateASubscriptionResponse subscriptions_post(x_com_zoho_subscriptions_organizationid, create_a_subscription_request=create_a_subscription_request)

Create a subscription

Create a new subscription. To create a subscription for a new customer, you have to pass the customer object. To create a subscription for a existing customer pass the <code>customer_id</code> of that customer.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_subscription
from ls_zoho_billing_subscription.models.create_a_subscription_request import CreateASubscriptionRequest
from ls_zoho_billing_subscription.models.create_a_subscription_response import CreateASubscriptionResponse
from ls_zoho_billing_subscription.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_subscription.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_subscription.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_subscription.SubscriptionApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    create_a_subscription_request = ls_zoho_billing_subscription.CreateASubscriptionRequest() # CreateASubscriptionRequest |  (optional)

    try:
        # Create a subscription
        api_response = api_instance.subscriptions_post(x_com_zoho_subscriptions_organizationid, create_a_subscription_request=create_a_subscription_request)
        print("The response of SubscriptionApi->subscriptions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscriptions_post: %s\n" % e)
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

# **subscriptions_subscription_id_autocollect_post**
> ChangeToOnlineofflineModeResponse subscriptions_subscription_id_autocollect_post(subscription_id, x_com_zoho_subscriptions_organizationid, change_to_onlineoffline_mode_request=change_to_onlineoffline_mode_request)

Change to Online/Offline mode

Change the status of a particular subscription to Online/Offline mode. If <code>auto_collect</code> is false, the subscription is in <strong>Offline</strong> mode. If <code>auto_collect</code> is true, the subscription is in <strong>Online</strong> mode.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_subscription
from ls_zoho_billing_subscription.models.change_to_onlineoffline_mode_request import ChangeToOnlineofflineModeRequest
from ls_zoho_billing_subscription.models.change_to_onlineoffline_mode_response import ChangeToOnlineofflineModeResponse
from ls_zoho_billing_subscription.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_subscription.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_subscription.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_subscription.SubscriptionApi(api_client)
    subscription_id = '90300000079200' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    change_to_onlineoffline_mode_request = ls_zoho_billing_subscription.ChangeToOnlineofflineModeRequest() # ChangeToOnlineofflineModeRequest |  (optional)

    try:
        # Change to Online/Offline mode
        api_response = api_instance.subscriptions_subscription_id_autocollect_post(subscription_id, x_com_zoho_subscriptions_organizationid, change_to_onlineoffline_mode_request=change_to_onlineoffline_mode_request)
        print("The response of SubscriptionApi->subscriptions_subscription_id_autocollect_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscriptions_subscription_id_autocollect_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **change_to_onlineoffline_mode_request** | [**ChangeToOnlineofflineModeRequest**](ChangeToOnlineofflineModeRequest.md)|  | [optional] 

### Return type

[**ChangeToOnlineofflineModeResponse**](ChangeToOnlineofflineModeResponse.md)

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

# **subscriptions_subscription_id_buyonetimeaddon_post**
> BuyOneTimeAddonResponse subscriptions_subscription_id_buyonetimeaddon_post(subscription_id, x_com_zoho_subscriptions_organizationid, buy_one_time_addon_request=buy_one_time_addon_request)

Buy one-time addon

Include a one-time addon in the subscription.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_subscription
from ls_zoho_billing_subscription.models.buy_one_time_addon_request import BuyOneTimeAddonRequest
from ls_zoho_billing_subscription.models.buy_one_time_addon_response import BuyOneTimeAddonResponse
from ls_zoho_billing_subscription.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_subscription.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_subscription.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_subscription.SubscriptionApi(api_client)
    subscription_id = '90300000079200' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    buy_one_time_addon_request = ls_zoho_billing_subscription.BuyOneTimeAddonRequest() # BuyOneTimeAddonRequest |  (optional)

    try:
        # Buy one-time addon
        api_response = api_instance.subscriptions_subscription_id_buyonetimeaddon_post(subscription_id, x_com_zoho_subscriptions_organizationid, buy_one_time_addon_request=buy_one_time_addon_request)
        print("The response of SubscriptionApi->subscriptions_subscription_id_buyonetimeaddon_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscriptions_subscription_id_buyonetimeaddon_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **buy_one_time_addon_request** | [**BuyOneTimeAddonRequest**](BuyOneTimeAddonRequest.md)|  | [optional] 

### Return type

[**BuyOneTimeAddonResponse**](BuyOneTimeAddonResponse.md)

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

# **subscriptions_subscription_id_cancel_post**
> CancelASubscriptionResponse subscriptions_subscription_id_cancel_post(subscription_id, x_com_zoho_subscriptions_organizationid, cancel_at_end=cancel_at_end)

Cancel a subscription

Your subscription can be either cancelled immediately or at the end of the current term based on the value of `cancel_at_end`.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_subscription
from ls_zoho_billing_subscription.models.cancel_a_subscription_response import CancelASubscriptionResponse
from ls_zoho_billing_subscription.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_subscription.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_subscription.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_subscription.SubscriptionApi(api_client)
    subscription_id = '90300000079200' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    cancel_at_end = 'PlanStatus.ACTIVE' # str | If `cancel_at_end` is set to <strong>true</strong> then the `status` of the subscription is changed to <strong>non_renewing</strong> and if it is <strong>false</strong>, the `status` would be <strong>cancelled</strong>. (optional)

    try:
        # Cancel a subscription
        api_response = api_instance.subscriptions_subscription_id_cancel_post(subscription_id, x_com_zoho_subscriptions_organizationid, cancel_at_end=cancel_at_end)
        print("The response of SubscriptionApi->subscriptions_subscription_id_cancel_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscriptions_subscription_id_cancel_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **cancel_at_end** | **str**| If &#x60;cancel_at_end&#x60; is set to &lt;strong&gt;true&lt;/strong&gt; then the &#x60;status&#x60; of the subscription is changed to &lt;strong&gt;non_renewing&lt;/strong&gt; and if it is &lt;strong&gt;false&lt;/strong&gt;, the &#x60;status&#x60; would be &lt;strong&gt;cancelled&lt;/strong&gt;. | [optional] 

### Return type

[**CancelASubscriptionResponse**](CancelASubscriptionResponse.md)

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

# **subscriptions_subscription_id_card_delete**
> RemoveCardResponse subscriptions_subscription_id_card_delete(subscription_id, x_com_zoho_subscriptions_organizationid)

Remove Card

Delete a card associated with the subscription. The subscription will become an offline subscription.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_subscription
from ls_zoho_billing_subscription.models.remove_card_response import RemoveCardResponse
from ls_zoho_billing_subscription.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_subscription.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_subscription.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_subscription.SubscriptionApi(api_client)
    subscription_id = '90300000079200' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Remove Card
        api_response = api_instance.subscriptions_subscription_id_card_delete(subscription_id, x_com_zoho_subscriptions_organizationid)
        print("The response of SubscriptionApi->subscriptions_subscription_id_card_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscriptions_subscription_id_card_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**RemoveCardResponse**](RemoveCardResponse.md)

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

# **subscriptions_subscription_id_card_post**
> UpdateCardResponse subscriptions_subscription_id_card_post(subscription_id, x_com_zoho_subscriptions_organizationid, update_card_request=update_card_request)

Update Card

Update the card details of a customer. Once updated, the past card will no longer be charged.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_subscription
from ls_zoho_billing_subscription.models.update_card_request import UpdateCardRequest
from ls_zoho_billing_subscription.models.update_card_response import UpdateCardResponse
from ls_zoho_billing_subscription.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_subscription.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_subscription.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_subscription.SubscriptionApi(api_client)
    subscription_id = '90300000079200' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    update_card_request = ls_zoho_billing_subscription.UpdateCardRequest() # UpdateCardRequest |  (optional)

    try:
        # Update Card
        api_response = api_instance.subscriptions_subscription_id_card_post(subscription_id, x_com_zoho_subscriptions_organizationid, update_card_request=update_card_request)
        print("The response of SubscriptionApi->subscriptions_subscription_id_card_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscriptions_subscription_id_card_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **update_card_request** | [**UpdateCardRequest**](UpdateCardRequest.md)|  | [optional] 

### Return type

[**UpdateCardResponse**](UpdateCardResponse.md)

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

# **subscriptions_subscription_id_charge_post**
> AddChargeResponse subscriptions_subscription_id_charge_post(subscription_id, x_com_zoho_subscriptions_organizationid, add_charge_request=add_charge_request)

Add Charge

Charge a one-time amount for the subscription.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_subscription
from ls_zoho_billing_subscription.models.add_charge_request import AddChargeRequest
from ls_zoho_billing_subscription.models.add_charge_response import AddChargeResponse
from ls_zoho_billing_subscription.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_subscription.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_subscription.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_subscription.SubscriptionApi(api_client)
    subscription_id = '90300000079200' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    add_charge_request = ls_zoho_billing_subscription.AddChargeRequest() # AddChargeRequest |  (optional)

    try:
        # Add Charge
        api_response = api_instance.subscriptions_subscription_id_charge_post(subscription_id, x_com_zoho_subscriptions_organizationid, add_charge_request=add_charge_request)
        print("The response of SubscriptionApi->subscriptions_subscription_id_charge_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscriptions_subscription_id_charge_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **add_charge_request** | [**AddChargeRequest**](AddChargeRequest.md)|  | [optional] 

### Return type

[**AddChargeResponse**](AddChargeResponse.md)

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

# **subscriptions_subscription_id_contactpersons_post**
> AddContactPersonResponse subscriptions_subscription_id_contactpersons_post(subscription_id, x_com_zoho_subscriptions_organizationid, add_contact_person_request=add_contact_person_request)

Add contact person

Associate a contact person with the subscription. Only an existing contact person can be associated.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_subscription
from ls_zoho_billing_subscription.models.add_contact_person_request import AddContactPersonRequest
from ls_zoho_billing_subscription.models.add_contact_person_response import AddContactPersonResponse
from ls_zoho_billing_subscription.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_subscription.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_subscription.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_subscription.SubscriptionApi(api_client)
    subscription_id = '90300000079200' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    add_contact_person_request = ls_zoho_billing_subscription.AddContactPersonRequest() # AddContactPersonRequest |  (optional)

    try:
        # Add contact person
        api_response = api_instance.subscriptions_subscription_id_contactpersons_post(subscription_id, x_com_zoho_subscriptions_organizationid, add_contact_person_request=add_contact_person_request)
        print("The response of SubscriptionApi->subscriptions_subscription_id_contactpersons_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscriptions_subscription_id_contactpersons_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **add_contact_person_request** | [**AddContactPersonRequest**](AddContactPersonRequest.md)|  | [optional] 

### Return type

[**AddContactPersonResponse**](AddContactPersonResponse.md)

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

# **subscriptions_subscription_id_coupons_coupon_code_post**
> AssociateACouponResponse subscriptions_subscription_id_coupons_coupon_code_post(subscription_id, x_com_zoho_subscriptions_organizationid, coupon_code)

Associate a coupon

Apply a coupon to a subscription which has been already created.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_subscription
from ls_zoho_billing_subscription.models.associate_a_coupon_response import AssociateACouponResponse
from ls_zoho_billing_subscription.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_subscription.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_subscription.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_subscription.SubscriptionApi(api_client)
    subscription_id = '90300000079200' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    coupon_code = 'Flat10' # str | 

    try:
        # Associate a coupon
        api_response = api_instance.subscriptions_subscription_id_coupons_coupon_code_post(subscription_id, x_com_zoho_subscriptions_organizationid, coupon_code)
        print("The response of SubscriptionApi->subscriptions_subscription_id_coupons_coupon_code_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscriptions_subscription_id_coupons_coupon_code_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **coupon_code** | **str**|  | 

### Return type

[**AssociateACouponResponse**](AssociateACouponResponse.md)

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

# **subscriptions_subscription_id_coupons_delete**
> RemoveACouponResponse subscriptions_subscription_id_coupons_delete(subscription_id, x_com_zoho_subscriptions_organizationid)

Remove a coupon

To remove coupon associated with a subscription.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_subscription
from ls_zoho_billing_subscription.models.remove_a_coupon_response import RemoveACouponResponse
from ls_zoho_billing_subscription.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_subscription.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_subscription.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_subscription.SubscriptionApi(api_client)
    subscription_id = '90300000079200' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Remove a coupon
        api_response = api_instance.subscriptions_subscription_id_coupons_delete(subscription_id, x_com_zoho_subscriptions_organizationid)
        print("The response of SubscriptionApi->subscriptions_subscription_id_coupons_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscriptions_subscription_id_coupons_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**RemoveACouponResponse**](RemoveACouponResponse.md)

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

# **subscriptions_subscription_id_customfields_post**
> UpdateCustomFieldsResponse subscriptions_subscription_id_customfields_post(subscription_id, x_com_zoho_subscriptions_organizationid, update_custom_fields_request=update_custom_fields_request)

Update Custom Fields

Update the custom fields associated with a particular subscription.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_subscription
from ls_zoho_billing_subscription.models.update_custom_fields_request import UpdateCustomFieldsRequest
from ls_zoho_billing_subscription.models.update_custom_fields_response import UpdateCustomFieldsResponse
from ls_zoho_billing_subscription.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_subscription.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_subscription.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_subscription.SubscriptionApi(api_client)
    subscription_id = '90300000079200' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    update_custom_fields_request = ls_zoho_billing_subscription.UpdateCustomFieldsRequest() # UpdateCustomFieldsRequest |  (optional)

    try:
        # Update Custom Fields
        api_response = api_instance.subscriptions_subscription_id_customfields_post(subscription_id, x_com_zoho_subscriptions_organizationid, update_custom_fields_request=update_custom_fields_request)
        print("The response of SubscriptionApi->subscriptions_subscription_id_customfields_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscriptions_subscription_id_customfields_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
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

# **subscriptions_subscription_id_delete**
> DeleteASubscriptionResponse subscriptions_subscription_id_delete(subscription_id, x_com_zoho_subscriptions_organizationid)

Delete a subscription

Delete an existing subscription.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_subscription
from ls_zoho_billing_subscription.models.delete_a_subscription_response import DeleteASubscriptionResponse
from ls_zoho_billing_subscription.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_subscription.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_subscription.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_subscription.SubscriptionApi(api_client)
    subscription_id = '90300000079200' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Delete a subscription
        api_response = api_instance.subscriptions_subscription_id_delete(subscription_id, x_com_zoho_subscriptions_organizationid)
        print("The response of SubscriptionApi->subscriptions_subscription_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscriptions_subscription_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**DeleteASubscriptionResponse**](DeleteASubscriptionResponse.md)

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

# **subscriptions_subscription_id_get**
> RetrieveASubscriptionResponse subscriptions_subscription_id_get(subscription_id, x_com_zoho_subscriptions_organizationid)

Retrieve a subscription

Details of an existing subscription.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_subscription
from ls_zoho_billing_subscription.models.retrieve_a_subscription_response import RetrieveASubscriptionResponse
from ls_zoho_billing_subscription.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_subscription.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_subscription.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_subscription.SubscriptionApi(api_client)
    subscription_id = '90300000079200' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Retrieve a subscription
        api_response = api_instance.subscriptions_subscription_id_get(subscription_id, x_com_zoho_subscriptions_organizationid)
        print("The response of SubscriptionApi->subscriptions_subscription_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscriptions_subscription_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**RetrieveASubscriptionResponse**](RetrieveASubscriptionResponse.md)

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

# **subscriptions_subscription_id_lineitems_plan_or_addon_code_post**
> AddeditDescriptionForAItemInLineItemsListResponse subscriptions_subscription_id_lineitems_plan_or_addon_code_post(subscription_id, x_com_zoho_subscriptions_organizationid, plan_code, addedit_description_for_a_item_in_line_items_list_request=addedit_description_for_a_item_in_line_items_list_request)

Add/Edit description for a item in line items list

Add/Edit description to a particular plan or addon in the line items list.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_subscription
from ls_zoho_billing_subscription.models.addedit_description_for_a_item_in_line_items_list_request import AddeditDescriptionForAItemInLineItemsListRequest
from ls_zoho_billing_subscription.models.addedit_description_for_a_item_in_line_items_list_response import AddeditDescriptionForAItemInLineItemsListResponse
from ls_zoho_billing_subscription.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_subscription.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_subscription.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_subscription.SubscriptionApi(api_client)
    subscription_id = '90300000079200' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    plan_code = 'basic-monthly' # str | 
    addedit_description_for_a_item_in_line_items_list_request = ls_zoho_billing_subscription.AddeditDescriptionForAItemInLineItemsListRequest() # AddeditDescriptionForAItemInLineItemsListRequest |  (optional)

    try:
        # Add/Edit description for a item in line items list
        api_response = api_instance.subscriptions_subscription_id_lineitems_plan_or_addon_code_post(subscription_id, x_com_zoho_subscriptions_organizationid, plan_code, addedit_description_for_a_item_in_line_items_list_request=addedit_description_for_a_item_in_line_items_list_request)
        print("The response of SubscriptionApi->subscriptions_subscription_id_lineitems_plan_or_addon_code_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscriptions_subscription_id_lineitems_plan_or_addon_code_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **plan_code** | **str**|  | 
 **addedit_description_for_a_item_in_line_items_list_request** | [**AddeditDescriptionForAItemInLineItemsListRequest**](AddeditDescriptionForAItemInLineItemsListRequest.md)|  | [optional] 

### Return type

[**AddeditDescriptionForAItemInLineItemsListResponse**](AddeditDescriptionForAItemInLineItemsListResponse.md)

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

# **subscriptions_subscription_id_notes_note_id_delete**
> DeleteANoteResponse subscriptions_subscription_id_notes_note_id_delete(subscription_id, x_com_zoho_subscriptions_organizationid, note_id)

Delete a note

Delete a specific note.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_subscription
from ls_zoho_billing_subscription.models.delete_a_note_response import DeleteANoteResponse
from ls_zoho_billing_subscription.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_subscription.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_subscription.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_subscription.SubscriptionApi(api_client)
    subscription_id = '90300000079200' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    note_id = '903000076543' # str | 

    try:
        # Delete a note
        api_response = api_instance.subscriptions_subscription_id_notes_note_id_delete(subscription_id, x_com_zoho_subscriptions_organizationid, note_id)
        print("The response of SubscriptionApi->subscriptions_subscription_id_notes_note_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscriptions_subscription_id_notes_note_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **note_id** | **str**|  | 

### Return type

[**DeleteANoteResponse**](DeleteANoteResponse.md)

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

# **subscriptions_subscription_id_notes_post**
> AddANoteResponse subscriptions_subscription_id_notes_post(subscription_id, x_com_zoho_subscriptions_organizationid, add_a_note_request=add_a_note_request)

Add a note

Notes related to the subscription can be added by the user at anytime.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_subscription
from ls_zoho_billing_subscription.models.add_a_note_request import AddANoteRequest
from ls_zoho_billing_subscription.models.add_a_note_response import AddANoteResponse
from ls_zoho_billing_subscription.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_subscription.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_subscription.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_subscription.SubscriptionApi(api_client)
    subscription_id = '90300000079200' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    add_a_note_request = ls_zoho_billing_subscription.AddANoteRequest() # AddANoteRequest |  (optional)

    try:
        # Add a note
        api_response = api_instance.subscriptions_subscription_id_notes_post(subscription_id, x_com_zoho_subscriptions_organizationid, add_a_note_request=add_a_note_request)
        print("The response of SubscriptionApi->subscriptions_subscription_id_notes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscriptions_subscription_id_notes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **add_a_note_request** | [**AddANoteRequest**](AddANoteRequest.md)|  | [optional] 

### Return type

[**AddANoteResponse**](AddANoteResponse.md)

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

# **subscriptions_subscription_id_postpone_post**
> PostponeRenewalResponse subscriptions_subscription_id_postpone_post(subscription_id, x_com_zoho_subscriptions_organizationid, postpone_renewal_request=postpone_renewal_request)

Postpone renewal

A subscription renewal date (billing date) can be postponed thereby extending the subscription term. Also, subscription renewal can only be postponed and not preponed.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_subscription
from ls_zoho_billing_subscription.models.postpone_renewal_request import PostponeRenewalRequest
from ls_zoho_billing_subscription.models.postpone_renewal_response import PostponeRenewalResponse
from ls_zoho_billing_subscription.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_subscription.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_subscription.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_subscription.SubscriptionApi(api_client)
    subscription_id = '90300000079200' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    postpone_renewal_request = ls_zoho_billing_subscription.PostponeRenewalRequest() # PostponeRenewalRequest |  (optional)

    try:
        # Postpone renewal
        api_response = api_instance.subscriptions_subscription_id_postpone_post(subscription_id, x_com_zoho_subscriptions_organizationid, postpone_renewal_request=postpone_renewal_request)
        print("The response of SubscriptionApi->subscriptions_subscription_id_postpone_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscriptions_subscription_id_postpone_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **postpone_renewal_request** | [**PostponeRenewalRequest**](PostponeRenewalRequest.md)|  | [optional] 

### Return type

[**PostponeRenewalResponse**](PostponeRenewalResponse.md)

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

# **subscriptions_subscription_id_put**
> UpdateASubscriptionResponse subscriptions_subscription_id_put(subscription_id, x_com_zoho_subscriptions_organizationid, update_a_subscription_request=update_a_subscription_request)

Update a subscription

Update details of an existing subscription.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_subscription
from ls_zoho_billing_subscription.models.update_a_subscription_request import UpdateASubscriptionRequest
from ls_zoho_billing_subscription.models.update_a_subscription_response import UpdateASubscriptionResponse
from ls_zoho_billing_subscription.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_subscription.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_subscription.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_subscription.SubscriptionApi(api_client)
    subscription_id = '90300000079200' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    update_a_subscription_request = ls_zoho_billing_subscription.UpdateASubscriptionRequest() # UpdateASubscriptionRequest |  (optional)

    try:
        # Update a subscription
        api_response = api_instance.subscriptions_subscription_id_put(subscription_id, x_com_zoho_subscriptions_organizationid, update_a_subscription_request=update_a_subscription_request)
        print("The response of SubscriptionApi->subscriptions_subscription_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscriptions_subscription_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_subscription_id_reactivate_post**
> ReactivateSubscriptionResponse subscriptions_subscription_id_reactivate_post(subscription_id, x_com_zoho_subscriptions_organizationid)

Reactivate subscription

Reactivate a subscription. You can reactivate a subscription only if the `status` of the subscription is <strong>non-renewing</strong>.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_subscription
from ls_zoho_billing_subscription.models.reactivate_subscription_response import ReactivateSubscriptionResponse
from ls_zoho_billing_subscription.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_subscription.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_subscription.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_subscription.SubscriptionApi(api_client)
    subscription_id = '90300000079200' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Reactivate subscription
        api_response = api_instance.subscriptions_subscription_id_reactivate_post(subscription_id, x_com_zoho_subscriptions_organizationid)
        print("The response of SubscriptionApi->subscriptions_subscription_id_reactivate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscriptions_subscription_id_reactivate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**ReactivateSubscriptionResponse**](ReactivateSubscriptionResponse.md)

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

# **subscriptions_subscription_id_recentactivities_get**
> SubscriptionActivitiesResponse subscriptions_subscription_id_recentactivities_get(subscription_id, x_com_zoho_subscriptions_organizationid)

Subscription Activities

List of all the recent activities associated to a subscription.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_subscription
from ls_zoho_billing_subscription.models.subscription_activities_response import SubscriptionActivitiesResponse
from ls_zoho_billing_subscription.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_subscription.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_subscription.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_subscription.SubscriptionApi(api_client)
    subscription_id = '90300000079200' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Subscription Activities
        api_response = api_instance.subscriptions_subscription_id_recentactivities_get(subscription_id, x_com_zoho_subscriptions_organizationid)
        print("The response of SubscriptionApi->subscriptions_subscription_id_recentactivities_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscriptions_subscription_id_recentactivities_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**SubscriptionActivitiesResponse**](SubscriptionActivitiesResponse.md)

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

# **subscriptions_subscription_id_reference_post**
> UpdateReferenceResponse subscriptions_subscription_id_reference_post(subscription_id, x_com_zoho_subscriptions_organizationid, update_reference_request=update_reference_request)

Update Reference

Update reference id to easily identify and keep track of your subscription.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_subscription
from ls_zoho_billing_subscription.models.update_reference_request import UpdateReferenceRequest
from ls_zoho_billing_subscription.models.update_reference_response import UpdateReferenceResponse
from ls_zoho_billing_subscription.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_subscription.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_subscription.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_subscription.SubscriptionApi(api_client)
    subscription_id = '90300000079200' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    update_reference_request = ls_zoho_billing_subscription.UpdateReferenceRequest() # UpdateReferenceRequest |  (optional)

    try:
        # Update Reference
        api_response = api_instance.subscriptions_subscription_id_reference_post(subscription_id, x_com_zoho_subscriptions_organizationid, update_reference_request=update_reference_request)
        print("The response of SubscriptionApi->subscriptions_subscription_id_reference_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscriptions_subscription_id_reference_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **update_reference_request** | [**UpdateReferenceRequest**](UpdateReferenceRequest.md)|  | [optional] 

### Return type

[**UpdateReferenceResponse**](UpdateReferenceResponse.md)

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

# **subscriptions_subscription_id_salesperson_post**
> UpdateSalesPersonResponse subscriptions_subscription_id_salesperson_post(subscription_id, x_com_zoho_subscriptions_organizationid, update_sales_person_request=update_sales_person_request)

Update Sales Person

Update a sales person associated with a particular subscription.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_subscription
from ls_zoho_billing_subscription.models.update_sales_person_request import UpdateSalesPersonRequest
from ls_zoho_billing_subscription.models.update_sales_person_response import UpdateSalesPersonResponse
from ls_zoho_billing_subscription.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_subscription.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_subscription.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_subscription.SubscriptionApi(api_client)
    subscription_id = '90300000079200' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    update_sales_person_request = ls_zoho_billing_subscription.UpdateSalesPersonRequest() # UpdateSalesPersonRequest |  (optional)

    try:
        # Update Sales Person
        api_response = api_instance.subscriptions_subscription_id_salesperson_post(subscription_id, x_com_zoho_subscriptions_organizationid, update_sales_person_request=update_sales_person_request)
        print("The response of SubscriptionApi->subscriptions_subscription_id_salesperson_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscriptions_subscription_id_salesperson_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **update_sales_person_request** | [**UpdateSalesPersonRequest**](UpdateSalesPersonRequest.md)|  | [optional] 

### Return type

[**UpdateSalesPersonResponse**](UpdateSalesPersonResponse.md)

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

# **subscriptions_subscription_id_scheduledchanges_get**
> ViewScheduledChangesResponse subscriptions_subscription_id_scheduledchanges_get(subscription_id, x_com_zoho_subscriptions_organizationid)

View Scheduled Changes

To view  the End of Term changes.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_subscription
from ls_zoho_billing_subscription.models.view_scheduled_changes_response import ViewScheduledChangesResponse
from ls_zoho_billing_subscription.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_subscription.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_subscription.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_subscription.SubscriptionApi(api_client)
    subscription_id = '90300000079200' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # View Scheduled Changes
        api_response = api_instance.subscriptions_subscription_id_scheduledchanges_get(subscription_id, x_com_zoho_subscriptions_organizationid)
        print("The response of SubscriptionApi->subscriptions_subscription_id_scheduledchanges_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionApi->subscriptions_subscription_id_scheduledchanges_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**ViewScheduledChangesResponse**](ViewScheduledChangesResponse.md)

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

