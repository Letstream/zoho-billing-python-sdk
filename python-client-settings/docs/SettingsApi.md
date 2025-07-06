# ls_zoho_billing_settings.SettingsApi

All URIs are relative to *https://www.zohoapis.com/billing/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**settings_preferences_churnmessages_get**](SettingsApi.md#settings_preferences_churnmessages_get) | **GET** /settings/preferences/churnmessages | Retrieve Churn Message preferences
[**settings_taxauthorities_get**](SettingsApi.md#settings_taxauthorities_get) | **GET** /settings/taxauthorities | Retrieve list of tax Authorities
[**settings_taxes_get**](SettingsApi.md#settings_taxes_get) | **GET** /settings/taxes | Retrieve list of taxes
[**settings_taxexemptions_get**](SettingsApi.md#settings_taxexemptions_get) | **GET** /settings/taxexemptions | Retrieve list of tax Exemptions


# **settings_preferences_churnmessages_get**
> RetrieveChurnMessagePreferencesResponse settings_preferences_churnmessages_get(x_com_zoho_subscriptions_organizationid)

Retrieve Churn Message preferences

Retrieves list of Advanced Churn Message preferences.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_settings
from ls_zoho_billing_settings.models.retrieve_churn_message_preferences_response import RetrieveChurnMessagePreferencesResponse
from ls_zoho_billing_settings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_settings.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_settings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_settings.SettingsApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Retrieve Churn Message preferences
        api_response = api_instance.settings_preferences_churnmessages_get(x_com_zoho_subscriptions_organizationid)
        print("The response of SettingsApi->settings_preferences_churnmessages_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_preferences_churnmessages_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**RetrieveChurnMessagePreferencesResponse**](RetrieveChurnMessagePreferencesResponse.md)

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

# **settings_taxauthorities_get**
> RetrieveListOfTaxAuthoritiesResponse settings_taxauthorities_get(x_com_zoho_subscriptions_organizationid)

Retrieve list of tax Authorities

Retrieves the list of tax Authorities.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_settings
from ls_zoho_billing_settings.models.retrieve_list_of_tax_authorities_response import RetrieveListOfTaxAuthoritiesResponse
from ls_zoho_billing_settings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_settings.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_settings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_settings.SettingsApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Retrieve list of tax Authorities
        api_response = api_instance.settings_taxauthorities_get(x_com_zoho_subscriptions_organizationid)
        print("The response of SettingsApi->settings_taxauthorities_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_taxauthorities_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**RetrieveListOfTaxAuthoritiesResponse**](RetrieveListOfTaxAuthoritiesResponse.md)

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

# **settings_taxes_get**
> RetrieveListOfTaxesResponse settings_taxes_get(x_com_zoho_subscriptions_organizationid)

Retrieve list of taxes

Retrieves the list of taxes along with their details.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_settings
from ls_zoho_billing_settings.models.retrieve_list_of_taxes_response import RetrieveListOfTaxesResponse
from ls_zoho_billing_settings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_settings.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_settings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_settings.SettingsApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Retrieve list of taxes
        api_response = api_instance.settings_taxes_get(x_com_zoho_subscriptions_organizationid)
        print("The response of SettingsApi->settings_taxes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_taxes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**RetrieveListOfTaxesResponse**](RetrieveListOfTaxesResponse.md)

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

# **settings_taxexemptions_get**
> RetrieveListOfTaxExemptionsResponse settings_taxexemptions_get(x_com_zoho_subscriptions_organizationid)

Retrieve list of tax Exemptions

Retrieves the list of tax Exemptions.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_settings
from ls_zoho_billing_settings.models.retrieve_list_of_tax_exemptions_response import RetrieveListOfTaxExemptionsResponse
from ls_zoho_billing_settings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_settings.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_settings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_settings.SettingsApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Retrieve list of tax Exemptions
        api_response = api_instance.settings_taxexemptions_get(x_com_zoho_subscriptions_organizationid)
        print("The response of SettingsApi->settings_taxexemptions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->settings_taxexemptions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**RetrieveListOfTaxExemptionsResponse**](RetrieveListOfTaxExemptionsResponse.md)

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

