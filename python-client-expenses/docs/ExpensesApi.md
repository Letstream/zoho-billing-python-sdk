# ls_zoho_billing_expenses.ExpensesApi

All URIs are relative to *https://www.zohoapis.com/billing/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**expenses_expense_id_delete**](ExpensesApi.md#expenses_expense_id_delete) | **DELETE** /expenses/{expense_id} | Delete an Expense
[**expenses_expense_id_get**](ExpensesApi.md#expenses_expense_id_get) | **GET** /expenses/{expense_id} | Retrieve an Expense
[**expenses_expense_id_put**](ExpensesApi.md#expenses_expense_id_put) | **PUT** /expenses/{expense_id} | Update an Expense
[**expenses_get**](ExpensesApi.md#expenses_get) | **GET** /expenses | List Expenses
[**expenses_post**](ExpensesApi.md#expenses_post) | **POST** /expenses | Create an Expense


# **expenses_expense_id_delete**
> DeleteAnExpenseResponse expenses_expense_id_delete(expense_id, x_com_zoho_subscriptions_organizationid)

Delete an Expense

Delete an existing expense.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_expenses
from ls_zoho_billing_expenses.models.delete_an_expense_response import DeleteAnExpenseResponse
from ls_zoho_billing_expenses.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_expenses.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_expenses.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_expenses.ExpensesApi(api_client)
    expense_id = '982000000030049' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Delete an Expense
        api_response = api_instance.expenses_expense_id_delete(expense_id, x_com_zoho_subscriptions_organizationid)
        print("The response of ExpensesApi->expenses_expense_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpensesApi->expenses_expense_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expense_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**DeleteAnExpenseResponse**](DeleteAnExpenseResponse.md)

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

# **expenses_expense_id_get**
> GetAnExpenseResponse expenses_expense_id_get(expense_id, x_com_zoho_subscriptions_organizationid)

Retrieve an Expense

Fetch the details of the Expense.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_expenses
from ls_zoho_billing_expenses.models.get_an_expense_response import GetAnExpenseResponse
from ls_zoho_billing_expenses.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_expenses.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_expenses.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_expenses.ExpensesApi(api_client)
    expense_id = '982000000030049' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Retrieve an Expense
        api_response = api_instance.expenses_expense_id_get(expense_id, x_com_zoho_subscriptions_organizationid)
        print("The response of ExpensesApi->expenses_expense_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpensesApi->expenses_expense_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expense_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**GetAnExpenseResponse**](GetAnExpenseResponse.md)

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

# **expenses_expense_id_put**
> UpdateAnExpenseResponse expenses_expense_id_put(expense_id, x_com_zoho_subscriptions_organizationid, receipt=receipt, delete_receipt=delete_receipt, update_an_expense_request=update_an_expense_request)

Update an Expense

Update an existing Expense.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_expenses
from ls_zoho_billing_expenses.models.update_an_expense_request import UpdateAnExpenseRequest
from ls_zoho_billing_expenses.models.update_an_expense_response import UpdateAnExpenseResponse
from ls_zoho_billing_expenses.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_expenses.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_expenses.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_expenses.ExpensesApi(api_client)
    expense_id = '982000000030049' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    receipt = png # bytearray | Expense receipt file to attach. Allowed Extensions: <code>gif</code>, <code>png</code>, <code>jpeg</code>, <code>jpg</code>, <code>bmp</code> and <code>pdf</code>. It should be sent in multipart/formdata. (optional)
    delete_receipt = false # bool | A historic receipt (optional)
    update_an_expense_request = ls_zoho_billing_expenses.UpdateAnExpenseRequest() # UpdateAnExpenseRequest |  (optional)

    try:
        # Update an Expense
        api_response = api_instance.expenses_expense_id_put(expense_id, x_com_zoho_subscriptions_organizationid, receipt=receipt, delete_receipt=delete_receipt, update_an_expense_request=update_an_expense_request)
        print("The response of ExpensesApi->expenses_expense_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpensesApi->expenses_expense_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expense_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **receipt** | **bytearray**| Expense receipt file to attach. Allowed Extensions: &lt;code&gt;gif&lt;/code&gt;, &lt;code&gt;png&lt;/code&gt;, &lt;code&gt;jpeg&lt;/code&gt;, &lt;code&gt;jpg&lt;/code&gt;, &lt;code&gt;bmp&lt;/code&gt; and &lt;code&gt;pdf&lt;/code&gt;. It should be sent in multipart/formdata. | [optional] 
 **delete_receipt** | **bool**| A historic receipt | [optional] 
 **update_an_expense_request** | [**UpdateAnExpenseRequest**](UpdateAnExpenseRequest.md)|  | [optional] 

### Return type

[**UpdateAnExpenseResponse**](UpdateAnExpenseResponse.md)

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

# **expenses_get**
> ListExpensesResponse expenses_get(x_com_zoho_subscriptions_organizationid, description=description, reference_number=reference_number, var_date=var_date, status=status, amount=amount, account_name=account_name, customer_name=customer_name, search_text=search_text, sort_column=sort_column, filter_by=filter_by)

List Expenses

List all the Expenses with pagination.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_expenses
from ls_zoho_billing_expenses.models.list_expenses_response import ListExpensesResponse
from ls_zoho_billing_expenses.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_expenses.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_expenses.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_expenses.ExpensesApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    description = 'Marketing' # str | Search expenses by description.Variants <code>description_startswith</code> and <code>description_contains</code>. <code>Maximum length [100]</code> (optional)
    reference_number = '#562SD23R4' # str | Search expenses by reference number. Variants <code>reference_number_startswith</code> and <code>reference_number_contains</code>. <code>Maximum length [100]</code> (optional)
    var_date = '2013-11-18T00:00:00.000Z' # str | Search expenses by expense date. Variants <code>date_start</code>, <code>date_end</code>, <code>date_before</code> and <code>date_after</code>. <code>Date Format [yyyy-mm-dd]</code> (optional)
    status = 'unbilled' # str | Search expenses by expense status. Allowed Values <code>unbilled</code>, <code>invoiced</code>, <code>reimbursed</code>, <code>non-billable</code> and <code>billable</code> (optional)
    amount = 112.5 # float | Search expenses by amount. Variants: <code>amount_less_than</code>, <code>amount_less_equals</code>, <code>amount_greater_than</code> and <code>amount_greater_than</code> (optional)
    account_name = 'Rent' # str | Search expenses by expense account name. Variants <code>account_name_startswith</code> and <code>account_name_contains</code>. <code>Maximum length [100]</code> (optional)
    customer_name = 'Bowman & Co' # str | Search expenses by customer name. Variants: <code>customer_name_startswith</code> and <code>customer_name_contains</code>. <code>Maximum length [100]</code> (optional)
    search_text = 'Rent' # str | Search expenses by account name or description or <code>customer name</code>  or <code>vendor name</code>. <code>Maximum length [100]</code> (optional)
    sort_column = 'total' # str | Sort expenses.Allowed Values <code>date</code>, <code>account_name</code>, <code>total</code>, <code>bcy_total</code>, <code>reference_number</code>, <code>customer_name</code> and <code>created_time</code> (optional)
    filter_by = 'Status.Billable' # str | Filter expenses by expense status. Allowed Values <code>Status.All</code>, <code>Status.Billable</code>, <code>Status.Nonbillable</code>, <code>Status.Reimbursed</code>, <code>Status.Invoiced</code> and <code>Status.Unbilled</code> (optional)

    try:
        # List Expenses
        api_response = api_instance.expenses_get(x_com_zoho_subscriptions_organizationid, description=description, reference_number=reference_number, var_date=var_date, status=status, amount=amount, account_name=account_name, customer_name=customer_name, search_text=search_text, sort_column=sort_column, filter_by=filter_by)
        print("The response of ExpensesApi->expenses_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpensesApi->expenses_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **description** | **str**| Search expenses by description.Variants &lt;code&gt;description_startswith&lt;/code&gt; and &lt;code&gt;description_contains&lt;/code&gt;. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
 **reference_number** | **str**| Search expenses by reference number. Variants &lt;code&gt;reference_number_startswith&lt;/code&gt; and &lt;code&gt;reference_number_contains&lt;/code&gt;. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
 **var_date** | **str**| Search expenses by expense date. Variants &lt;code&gt;date_start&lt;/code&gt;, &lt;code&gt;date_end&lt;/code&gt;, &lt;code&gt;date_before&lt;/code&gt; and &lt;code&gt;date_after&lt;/code&gt;. &lt;code&gt;Date Format [yyyy-mm-dd]&lt;/code&gt; | [optional] 
 **status** | **str**| Search expenses by expense status. Allowed Values &lt;code&gt;unbilled&lt;/code&gt;, &lt;code&gt;invoiced&lt;/code&gt;, &lt;code&gt;reimbursed&lt;/code&gt;, &lt;code&gt;non-billable&lt;/code&gt; and &lt;code&gt;billable&lt;/code&gt; | [optional] 
 **amount** | **float**| Search expenses by amount. Variants: &lt;code&gt;amount_less_than&lt;/code&gt;, &lt;code&gt;amount_less_equals&lt;/code&gt;, &lt;code&gt;amount_greater_than&lt;/code&gt; and &lt;code&gt;amount_greater_than&lt;/code&gt; | [optional] 
 **account_name** | **str**| Search expenses by expense account name. Variants &lt;code&gt;account_name_startswith&lt;/code&gt; and &lt;code&gt;account_name_contains&lt;/code&gt;. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
 **customer_name** | **str**| Search expenses by customer name. Variants: &lt;code&gt;customer_name_startswith&lt;/code&gt; and &lt;code&gt;customer_name_contains&lt;/code&gt;. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
 **search_text** | **str**| Search expenses by account name or description or &lt;code&gt;customer name&lt;/code&gt;  or &lt;code&gt;vendor name&lt;/code&gt;. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
 **sort_column** | **str**| Sort expenses.Allowed Values &lt;code&gt;date&lt;/code&gt;, &lt;code&gt;account_name&lt;/code&gt;, &lt;code&gt;total&lt;/code&gt;, &lt;code&gt;bcy_total&lt;/code&gt;, &lt;code&gt;reference_number&lt;/code&gt;, &lt;code&gt;customer_name&lt;/code&gt; and &lt;code&gt;created_time&lt;/code&gt; | [optional] 
 **filter_by** | **str**| Filter expenses by expense status. Allowed Values &lt;code&gt;Status.All&lt;/code&gt;, &lt;code&gt;Status.Billable&lt;/code&gt;, &lt;code&gt;Status.Nonbillable&lt;/code&gt;, &lt;code&gt;Status.Reimbursed&lt;/code&gt;, &lt;code&gt;Status.Invoiced&lt;/code&gt; and &lt;code&gt;Status.Unbilled&lt;/code&gt; | [optional] 

### Return type

[**ListExpensesResponse**](ListExpensesResponse.md)

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

# **expenses_post**
> CreateAnExpenseResponse expenses_post(x_com_zoho_subscriptions_organizationid, receipt=receipt, create_an_expense_request=create_an_expense_request)

Create an Expense

Create billable or non-billable expense.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_expenses
from ls_zoho_billing_expenses.models.create_an_expense_request import CreateAnExpenseRequest
from ls_zoho_billing_expenses.models.create_an_expense_response import CreateAnExpenseResponse
from ls_zoho_billing_expenses.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_expenses.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_expenses.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_expenses.ExpensesApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    receipt = png # bytearray | Expense receipt file to attach. Allowed Extensions: <code>gif</code>, <code>png</code>, <code>jpeg</code>, <code>jpg</code>, <code>bmp</code> and <code>pdf</code>. It should be sent in multipart/formdata. (optional)
    create_an_expense_request = ls_zoho_billing_expenses.CreateAnExpenseRequest() # CreateAnExpenseRequest |  (optional)

    try:
        # Create an Expense
        api_response = api_instance.expenses_post(x_com_zoho_subscriptions_organizationid, receipt=receipt, create_an_expense_request=create_an_expense_request)
        print("The response of ExpensesApi->expenses_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpensesApi->expenses_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **receipt** | **bytearray**| Expense receipt file to attach. Allowed Extensions: &lt;code&gt;gif&lt;/code&gt;, &lt;code&gt;png&lt;/code&gt;, &lt;code&gt;jpeg&lt;/code&gt;, &lt;code&gt;jpg&lt;/code&gt;, &lt;code&gt;bmp&lt;/code&gt; and &lt;code&gt;pdf&lt;/code&gt;. It should be sent in multipart/formdata. | [optional] 
 **create_an_expense_request** | [**CreateAnExpenseRequest**](CreateAnExpenseRequest.md)|  | [optional] 

### Return type

[**CreateAnExpenseResponse**](CreateAnExpenseResponse.md)

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

