# ls_zoho_billing_contact_persons.ContactPersonsApi

All URIs are relative to *https://www.zohoapis.com/billing/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customers_customer_id_contactpersons_contactperson_id_delete**](ContactPersonsApi.md#customers_customer_id_contactpersons_contactperson_id_delete) | **DELETE** /customers/{customer_id}/contactpersons/{contactperson_id} | Delete a contact person
[**customers_customer_id_contactpersons_contactperson_id_get**](ContactPersonsApi.md#customers_customer_id_contactpersons_contactperson_id_get) | **GET** /customers/{customer_id}/contactpersons/{contactperson_id} | Retrieve a contact person
[**customers_customer_id_contactpersons_contactperson_id_put**](ContactPersonsApi.md#customers_customer_id_contactpersons_contactperson_id_put) | **PUT** /customers/{customer_id}/contactpersons/{contactperson_id} | Update a contact person
[**customers_customer_id_contactpersons_get**](ContactPersonsApi.md#customers_customer_id_contactpersons_get) | **GET** /customers/{customer_id}/contactpersons | List of all contact persons
[**customers_customer_id_contactpersons_post**](ContactPersonsApi.md#customers_customer_id_contactpersons_post) | **POST** /customers/{customer_id}/contactpersons | Create a contact person


# **customers_customer_id_contactpersons_contactperson_id_delete**
> DeleteAContactPersonResponse customers_customer_id_contactpersons_contactperson_id_delete(customer_id, x_com_zoho_subscriptions_organizationid, contactperson_id)

Delete a contact person

Delete an existing contact person.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_contact_persons
from ls_zoho_billing_contact_persons.models.delete_a_contact_person_response import DeleteAContactPersonResponse
from ls_zoho_billing_contact_persons.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_contact_persons.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_contact_persons.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_contact_persons.ContactPersonsApi(api_client)
    customer_id = '903000000000099' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    contactperson_id = '903000000053362' # str | 

    try:
        # Delete a contact person
        api_response = api_instance.customers_customer_id_contactpersons_contactperson_id_delete(customer_id, x_com_zoho_subscriptions_organizationid, contactperson_id)
        print("The response of ContactPersonsApi->customers_customer_id_contactpersons_contactperson_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactPersonsApi->customers_customer_id_contactpersons_contactperson_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **contactperson_id** | **str**|  | 

### Return type

[**DeleteAContactPersonResponse**](DeleteAContactPersonResponse.md)

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

# **customers_customer_id_contactpersons_contactperson_id_get**
> RetrieveAContactPersonResponse customers_customer_id_contactpersons_contactperson_id_get(customer_id, x_com_zoho_subscriptions_organizationid, contactperson_id)

Retrieve a contact person

Details of an existing contact person.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_contact_persons
from ls_zoho_billing_contact_persons.models.retrieve_a_contact_person_response import RetrieveAContactPersonResponse
from ls_zoho_billing_contact_persons.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_contact_persons.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_contact_persons.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_contact_persons.ContactPersonsApi(api_client)
    customer_id = '903000000000099' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    contactperson_id = '903000000053362' # str | 

    try:
        # Retrieve a contact person
        api_response = api_instance.customers_customer_id_contactpersons_contactperson_id_get(customer_id, x_com_zoho_subscriptions_organizationid, contactperson_id)
        print("The response of ContactPersonsApi->customers_customer_id_contactpersons_contactperson_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactPersonsApi->customers_customer_id_contactpersons_contactperson_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **contactperson_id** | **str**|  | 

### Return type

[**RetrieveAContactPersonResponse**](RetrieveAContactPersonResponse.md)

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

# **customers_customer_id_contactpersons_contactperson_id_put**
> UpdateAContactPersonResponse customers_customer_id_contactpersons_contactperson_id_put(customer_id, x_com_zoho_subscriptions_organizationid, contactperson_id, update_a_contact_person_request=update_a_contact_person_request)

Update a contact person

Update the details of an existing contact person.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_contact_persons
from ls_zoho_billing_contact_persons.models.update_a_contact_person_request import UpdateAContactPersonRequest
from ls_zoho_billing_contact_persons.models.update_a_contact_person_response import UpdateAContactPersonResponse
from ls_zoho_billing_contact_persons.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_contact_persons.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_contact_persons.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_contact_persons.ContactPersonsApi(api_client)
    customer_id = '903000000000099' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    contactperson_id = '903000000053362' # str | 
    update_a_contact_person_request = ls_zoho_billing_contact_persons.UpdateAContactPersonRequest() # UpdateAContactPersonRequest |  (optional)

    try:
        # Update a contact person
        api_response = api_instance.customers_customer_id_contactpersons_contactperson_id_put(customer_id, x_com_zoho_subscriptions_organizationid, contactperson_id, update_a_contact_person_request=update_a_contact_person_request)
        print("The response of ContactPersonsApi->customers_customer_id_contactpersons_contactperson_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactPersonsApi->customers_customer_id_contactpersons_contactperson_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **contactperson_id** | **str**|  | 
 **update_a_contact_person_request** | [**UpdateAContactPersonRequest**](UpdateAContactPersonRequest.md)|  | [optional] 

### Return type

[**UpdateAContactPersonResponse**](UpdateAContactPersonResponse.md)

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

# **customers_customer_id_contactpersons_get**
> ListOfAllContactPersonsResponse customers_customer_id_contactpersons_get(customer_id, x_com_zoho_subscriptions_organizationid)

List of all contact persons

List of all contact persons of a customer.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_contact_persons
from ls_zoho_billing_contact_persons.models.list_of_all_contact_persons_response import ListOfAllContactPersonsResponse
from ls_zoho_billing_contact_persons.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_contact_persons.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_contact_persons.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_contact_persons.ContactPersonsApi(api_client)
    customer_id = '903000000000099' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # List of all contact persons
        api_response = api_instance.customers_customer_id_contactpersons_get(customer_id, x_com_zoho_subscriptions_organizationid)
        print("The response of ContactPersonsApi->customers_customer_id_contactpersons_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactPersonsApi->customers_customer_id_contactpersons_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**ListOfAllContactPersonsResponse**](ListOfAllContactPersonsResponse.md)

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

# **customers_customer_id_contactpersons_post**
> CreateAContactPersonResponse customers_customer_id_contactpersons_post(customer_id, x_com_zoho_subscriptions_organizationid, create_a_contact_person_request=create_a_contact_person_request)

Create a contact person

Create a new contact person.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_contact_persons
from ls_zoho_billing_contact_persons.models.create_a_contact_person_request import CreateAContactPersonRequest
from ls_zoho_billing_contact_persons.models.create_a_contact_person_response import CreateAContactPersonResponse
from ls_zoho_billing_contact_persons.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_contact_persons.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_contact_persons.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_contact_persons.ContactPersonsApi(api_client)
    customer_id = '903000000000099' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    create_a_contact_person_request = ls_zoho_billing_contact_persons.CreateAContactPersonRequest() # CreateAContactPersonRequest |  (optional)

    try:
        # Create a contact person
        api_response = api_instance.customers_customer_id_contactpersons_post(customer_id, x_com_zoho_subscriptions_organizationid, create_a_contact_person_request=create_a_contact_person_request)
        print("The response of ContactPersonsApi->customers_customer_id_contactpersons_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactPersonsApi->customers_customer_id_contactpersons_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **create_a_contact_person_request** | [**CreateAContactPersonRequest**](CreateAContactPersonRequest.md)|  | [optional] 

### Return type

[**CreateAContactPersonResponse**](CreateAContactPersonResponse.md)

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

