# ls_zoho_billing_recurring_expenses.RecurringExpensesApi

All URIs are relative to *https://www.zohoapis.com/billing/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recurringexpenses_get**](RecurringExpensesApi.md#recurringexpenses_get) | **GET** /recurringexpenses | List recurring expenses
[**recurringexpenses_post**](RecurringExpensesApi.md#recurringexpenses_post) | **POST** /recurringexpenses | Create a recurring expense
[**recurringexpenses_recurring_expense_id_comments_get**](RecurringExpensesApi.md#recurringexpenses_recurring_expense_id_comments_get) | **GET** /recurringexpenses/{recurring_expense_id}/comments | List recurring expense history
[**recurringexpenses_recurring_expense_id_delete**](RecurringExpensesApi.md#recurringexpenses_recurring_expense_id_delete) | **DELETE** /recurringexpenses/{recurring_expense_id} | Delete a recurring expense
[**recurringexpenses_recurring_expense_id_expenses_get**](RecurringExpensesApi.md#recurringexpenses_recurring_expense_id_expenses_get) | **GET** /recurringexpenses/{recurring_expense_id}/expenses | List child expenses created
[**recurringexpenses_recurring_expense_id_get**](RecurringExpensesApi.md#recurringexpenses_recurring_expense_id_get) | **GET** /recurringexpenses/{recurring_expense_id} | Retrieve a recurring expense
[**recurringexpenses_recurring_expense_id_post**](RecurringExpensesApi.md#recurringexpenses_recurring_expense_id_post) | **POST** /recurringexpenses/{recurring_expense_id} | Update a recurring expense
[**recurringexpenses_recurring_expense_id_status_resume_post**](RecurringExpensesApi.md#recurringexpenses_recurring_expense_id_status_resume_post) | **POST** /recurringexpenses/{recurring_expense_id}/status/resume | Resume a recurring Expense
[**recurringexpenses_recurring_expense_id_status_stop_post**](RecurringExpensesApi.md#recurringexpenses_recurring_expense_id_status_stop_post) | **POST** /recurringexpenses/{recurring_expense_id}/status/stop | Stop a recurring expense


# **recurringexpenses_get**
> ListRecurringExpensesResponse recurringexpenses_get(x_com_zoho_subscriptions_organizationid, recurrence_name=recurrence_name, last_created_date=last_created_date, next_expense_date=next_expense_date, status=status, account_id=account_id, account_name=account_name, amount=amount, customer_name=customer_name, customer_id=customer_id, paid_through_account_id=paid_through_account_id, filter_by=filter_by, search_text=search_text, sort_column=sort_column)

List recurring expenses

List all the Expenses with pagination.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_recurring_expenses
from ls_zoho_billing_recurring_expenses.models.list_recurring_expenses_response import ListRecurringExpensesResponse
from ls_zoho_billing_recurring_expenses.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_recurring_expenses.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_recurring_expenses.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_recurring_expenses.RecurringExpensesApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    recurrence_name = 'Monthly Rental' # str | Search recurring expenses by recurring expense name. Variants: <code>recurrence_name_startswith</code> and <code>recurrence_name_contains</code>. <code>Maximum length [100]</code> (optional)
    last_created_date = '2013-11-18T00:00:00.000Z' # str | Search recurring expenses by date on when last expense was generated. Variants: <code>last_created_date_start</code>, <code>last_created_date_end</code>, <code>last_created_date_before</code> and <code>last_created_date_after</code> . <code>Format [yyyy-mm-dd]</code> (optional)
    next_expense_date = '2013-12-18T00:00:00.000Z' # str | Search recurring expenses by date on which next expense will be generated. Variants: <code>next_expense_date_start</code>, <code>next_expense_date_end</code>, <code>next_expense_date_before</code> and <code>next_expense_date_after</code> . <code>Format [yyyy-mm-dd]</code> (optional)
    status = 'active' # str | Search expenses by expense status. Allowed Values <code>active</code>, <code>stopped</code> and <code>expired</code> (optional)
    account_id = '982000000561057' # str | Unique ID of an account (optional)
    account_name = 'Rent' # str | Search expenses by expense account name. Variants <code>account_name_startswith</code> and <code>account_name_contains</code> . <code>Maximum length [100]</code> (optional)
    amount = 112.5 # float | Search expenses by amount. Variants: <code>amount_less_than</code>, <code>amount_less_equals</code>, <code>amount_greater_than</code> and <code>amount_greater_than</code> (optional)
    customer_name = 'Bowman & Co' # str | Search expenses by customer name. Variants: <code>customer_name_startswith</code> and <code>customer_name_contains</code> . <code>Maximum length [100]</code> (optional)
    customer_id = '982000000567001' # str | Search expenses by customer id. (optional)
    paid_through_account_id = '982000000567250' # str | Search expenses by paid through account id. (optional)
    filter_by = 'Status.Billable' # str | Filter expenses by expense status. Allowed Values <code>Status.All</code>, <code>Status.Active</code>, <code>Status.Expired</code> and <code>Status.Stopped</code> (optional)
    search_text = 'Rent' # str | Search expenses by account name or description or <code>customer name</code>  or <code>vendor name</code>. <code>Maximum length [100]</code> . (optional)
    sort_column = 'account_name' # str | Sort expenses.Allowed Values <code>next_expense_date</code>, <code>account_name</code>, <code>total</code>, <code>last_created_date</code>, <code>recurrence_name</code>, <code>customer_name</code> and <code>created_time</code> (optional)

    try:
        # List recurring expenses
        api_response = api_instance.recurringexpenses_get(x_com_zoho_subscriptions_organizationid, recurrence_name=recurrence_name, last_created_date=last_created_date, next_expense_date=next_expense_date, status=status, account_id=account_id, account_name=account_name, amount=amount, customer_name=customer_name, customer_id=customer_id, paid_through_account_id=paid_through_account_id, filter_by=filter_by, search_text=search_text, sort_column=sort_column)
        print("The response of RecurringExpensesApi->recurringexpenses_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecurringExpensesApi->recurringexpenses_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **recurrence_name** | **str**| Search recurring expenses by recurring expense name. Variants: &lt;code&gt;recurrence_name_startswith&lt;/code&gt; and &lt;code&gt;recurrence_name_contains&lt;/code&gt;. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
 **last_created_date** | **str**| Search recurring expenses by date on when last expense was generated. Variants: &lt;code&gt;last_created_date_start&lt;/code&gt;, &lt;code&gt;last_created_date_end&lt;/code&gt;, &lt;code&gt;last_created_date_before&lt;/code&gt; and &lt;code&gt;last_created_date_after&lt;/code&gt; . &lt;code&gt;Format [yyyy-mm-dd]&lt;/code&gt; | [optional] 
 **next_expense_date** | **str**| Search recurring expenses by date on which next expense will be generated. Variants: &lt;code&gt;next_expense_date_start&lt;/code&gt;, &lt;code&gt;next_expense_date_end&lt;/code&gt;, &lt;code&gt;next_expense_date_before&lt;/code&gt; and &lt;code&gt;next_expense_date_after&lt;/code&gt; . &lt;code&gt;Format [yyyy-mm-dd]&lt;/code&gt; | [optional] 
 **status** | **str**| Search expenses by expense status. Allowed Values &lt;code&gt;active&lt;/code&gt;, &lt;code&gt;stopped&lt;/code&gt; and &lt;code&gt;expired&lt;/code&gt; | [optional] 
 **account_id** | **str**| Unique ID of an account | [optional] 
 **account_name** | **str**| Search expenses by expense account name. Variants &lt;code&gt;account_name_startswith&lt;/code&gt; and &lt;code&gt;account_name_contains&lt;/code&gt; . &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
 **amount** | **float**| Search expenses by amount. Variants: &lt;code&gt;amount_less_than&lt;/code&gt;, &lt;code&gt;amount_less_equals&lt;/code&gt;, &lt;code&gt;amount_greater_than&lt;/code&gt; and &lt;code&gt;amount_greater_than&lt;/code&gt; | [optional] 
 **customer_name** | **str**| Search expenses by customer name. Variants: &lt;code&gt;customer_name_startswith&lt;/code&gt; and &lt;code&gt;customer_name_contains&lt;/code&gt; . &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
 **customer_id** | **str**| Search expenses by customer id. | [optional] 
 **paid_through_account_id** | **str**| Search expenses by paid through account id. | [optional] 
 **filter_by** | **str**| Filter expenses by expense status. Allowed Values &lt;code&gt;Status.All&lt;/code&gt;, &lt;code&gt;Status.Active&lt;/code&gt;, &lt;code&gt;Status.Expired&lt;/code&gt; and &lt;code&gt;Status.Stopped&lt;/code&gt; | [optional] 
 **search_text** | **str**| Search expenses by account name or description or &lt;code&gt;customer name&lt;/code&gt;  or &lt;code&gt;vendor name&lt;/code&gt;. &lt;code&gt;Maximum length [100]&lt;/code&gt; . | [optional] 
 **sort_column** | **str**| Sort expenses.Allowed Values &lt;code&gt;next_expense_date&lt;/code&gt;, &lt;code&gt;account_name&lt;/code&gt;, &lt;code&gt;total&lt;/code&gt;, &lt;code&gt;last_created_date&lt;/code&gt;, &lt;code&gt;recurrence_name&lt;/code&gt;, &lt;code&gt;customer_name&lt;/code&gt; and &lt;code&gt;created_time&lt;/code&gt; | [optional] 

### Return type

[**ListRecurringExpensesResponse**](ListRecurringExpensesResponse.md)

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

# **recurringexpenses_post**
> CreateARecurringExpenseResponse recurringexpenses_post(x_com_zoho_subscriptions_organizationid, create_a_recurring_expense_request=create_a_recurring_expense_request)

Create a recurring expense

Create a new recurring expense.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_recurring_expenses
from ls_zoho_billing_recurring_expenses.models.create_a_recurring_expense_request import CreateARecurringExpenseRequest
from ls_zoho_billing_recurring_expenses.models.create_a_recurring_expense_response import CreateARecurringExpenseResponse
from ls_zoho_billing_recurring_expenses.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_recurring_expenses.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_recurring_expenses.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_recurring_expenses.RecurringExpensesApi(api_client)
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    create_a_recurring_expense_request = ls_zoho_billing_recurring_expenses.CreateARecurringExpenseRequest() # CreateARecurringExpenseRequest |  (optional)

    try:
        # Create a recurring expense
        api_response = api_instance.recurringexpenses_post(x_com_zoho_subscriptions_organizationid, create_a_recurring_expense_request=create_a_recurring_expense_request)
        print("The response of RecurringExpensesApi->recurringexpenses_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecurringExpensesApi->recurringexpenses_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **create_a_recurring_expense_request** | [**CreateARecurringExpenseRequest**](CreateARecurringExpenseRequest.md)|  | [optional] 

### Return type

[**CreateARecurringExpenseResponse**](CreateARecurringExpenseResponse.md)

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

# **recurringexpenses_recurring_expense_id_comments_get**
> ListRecurringExpenseHistoryResponse recurringexpenses_recurring_expense_id_comments_get(recurring_expense_id, x_com_zoho_subscriptions_organizationid)

List recurring expense history

Get history and comments of a recurring expense.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_recurring_expenses
from ls_zoho_billing_recurring_expenses.models.list_recurring_expense_history_response import ListRecurringExpenseHistoryResponse
from ls_zoho_billing_recurring_expenses.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_recurring_expenses.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_recurring_expenses.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_recurring_expenses.RecurringExpensesApi(api_client)
    recurring_expense_id = '982000000567240' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # List recurring expense history
        api_response = api_instance.recurringexpenses_recurring_expense_id_comments_get(recurring_expense_id, x_com_zoho_subscriptions_organizationid)
        print("The response of RecurringExpensesApi->recurringexpenses_recurring_expense_id_comments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecurringExpensesApi->recurringexpenses_recurring_expense_id_comments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recurring_expense_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**ListRecurringExpenseHistoryResponse**](ListRecurringExpenseHistoryResponse.md)

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

# **recurringexpenses_recurring_expense_id_delete**
> DeleteARecurringExpenseResponse recurringexpenses_recurring_expense_id_delete(recurring_expense_id, x_com_zoho_subscriptions_organizationid)

Delete a recurring expense

Deleting an existing recurring expense.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_recurring_expenses
from ls_zoho_billing_recurring_expenses.models.delete_a_recurring_expense_response import DeleteARecurringExpenseResponse
from ls_zoho_billing_recurring_expenses.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_recurring_expenses.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_recurring_expenses.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_recurring_expenses.RecurringExpensesApi(api_client)
    recurring_expense_id = '982000000567240' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Delete a recurring expense
        api_response = api_instance.recurringexpenses_recurring_expense_id_delete(recurring_expense_id, x_com_zoho_subscriptions_organizationid)
        print("The response of RecurringExpensesApi->recurringexpenses_recurring_expense_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecurringExpensesApi->recurringexpenses_recurring_expense_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recurring_expense_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**DeleteARecurringExpenseResponse**](DeleteARecurringExpenseResponse.md)

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

# **recurringexpenses_recurring_expense_id_expenses_get**
> ListChildExpensesCreatedResponse recurringexpenses_recurring_expense_id_expenses_get(recurring_expense_id, x_com_zoho_subscriptions_organizationid, sort_column=sort_column)

List child expenses created

List child expenses created from recurring expense.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_recurring_expenses
from ls_zoho_billing_recurring_expenses.models.list_child_expenses_created_response import ListChildExpensesCreatedResponse
from ls_zoho_billing_recurring_expenses.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_recurring_expenses.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_recurring_expenses.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_recurring_expenses.RecurringExpensesApi(api_client)
    recurring_expense_id = '982000000567240' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    sort_column = 'account_name' # str | Sort expenses.Allowed Values <code>next_expense_date</code>, <code>account_name</code>, <code>total</code>, <code>last_created_date</code>, <code>recurrence_name</code>, <code>customer_name</code> and <code>created_time</code> (optional)

    try:
        # List child expenses created
        api_response = api_instance.recurringexpenses_recurring_expense_id_expenses_get(recurring_expense_id, x_com_zoho_subscriptions_organizationid, sort_column=sort_column)
        print("The response of RecurringExpensesApi->recurringexpenses_recurring_expense_id_expenses_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecurringExpensesApi->recurringexpenses_recurring_expense_id_expenses_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recurring_expense_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **sort_column** | **str**| Sort expenses.Allowed Values &lt;code&gt;next_expense_date&lt;/code&gt;, &lt;code&gt;account_name&lt;/code&gt;, &lt;code&gt;total&lt;/code&gt;, &lt;code&gt;last_created_date&lt;/code&gt;, &lt;code&gt;recurrence_name&lt;/code&gt;, &lt;code&gt;customer_name&lt;/code&gt; and &lt;code&gt;created_time&lt;/code&gt; | [optional] 

### Return type

[**ListChildExpensesCreatedResponse**](ListChildExpensesCreatedResponse.md)

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

# **recurringexpenses_recurring_expense_id_get**
> GetARecurringExpenseResponse recurringexpenses_recurring_expense_id_get(recurring_expense_id, x_com_zoho_subscriptions_organizationid)

Retrieve a recurring expense

Fetch the details of the recurring expense.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_recurring_expenses
from ls_zoho_billing_recurring_expenses.models.get_a_recurring_expense_response import GetARecurringExpenseResponse
from ls_zoho_billing_recurring_expenses.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_recurring_expenses.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_recurring_expenses.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_recurring_expenses.RecurringExpensesApi(api_client)
    recurring_expense_id = '982000000567240' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Retrieve a recurring expense
        api_response = api_instance.recurringexpenses_recurring_expense_id_get(recurring_expense_id, x_com_zoho_subscriptions_organizationid)
        print("The response of RecurringExpensesApi->recurringexpenses_recurring_expense_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecurringExpensesApi->recurringexpenses_recurring_expense_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recurring_expense_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**GetARecurringExpenseResponse**](GetARecurringExpenseResponse.md)

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

# **recurringexpenses_recurring_expense_id_post**
> UpdateARecurringExpenseResponse recurringexpenses_recurring_expense_id_post(recurring_expense_id, x_com_zoho_subscriptions_organizationid, update_a_recurring_expense_request=update_a_recurring_expense_request)

Update a recurring expense

Update an existing recurring expense.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_recurring_expenses
from ls_zoho_billing_recurring_expenses.models.update_a_recurring_expense_request import UpdateARecurringExpenseRequest
from ls_zoho_billing_recurring_expenses.models.update_a_recurring_expense_response import UpdateARecurringExpenseResponse
from ls_zoho_billing_recurring_expenses.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_recurring_expenses.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_recurring_expenses.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_recurring_expenses.RecurringExpensesApi(api_client)
    recurring_expense_id = '982000000567240' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization
    update_a_recurring_expense_request = ls_zoho_billing_recurring_expenses.UpdateARecurringExpenseRequest() # UpdateARecurringExpenseRequest |  (optional)

    try:
        # Update a recurring expense
        api_response = api_instance.recurringexpenses_recurring_expense_id_post(recurring_expense_id, x_com_zoho_subscriptions_organizationid, update_a_recurring_expense_request=update_a_recurring_expense_request)
        print("The response of RecurringExpensesApi->recurringexpenses_recurring_expense_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecurringExpensesApi->recurringexpenses_recurring_expense_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recurring_expense_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 
 **update_a_recurring_expense_request** | [**UpdateARecurringExpenseRequest**](UpdateARecurringExpenseRequest.md)|  | [optional] 

### Return type

[**UpdateARecurringExpenseResponse**](UpdateARecurringExpenseResponse.md)

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

# **recurringexpenses_recurring_expense_id_status_resume_post**
> ResumeARecurringExpenseResponse recurringexpenses_recurring_expense_id_status_resume_post(recurring_expense_id, x_com_zoho_subscriptions_organizationid)

Resume a recurring Expense

Resume a stopped recurring expense.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_recurring_expenses
from ls_zoho_billing_recurring_expenses.models.resume_a_recurring_expense_response import ResumeARecurringExpenseResponse
from ls_zoho_billing_recurring_expenses.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_recurring_expenses.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_recurring_expenses.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_recurring_expenses.RecurringExpensesApi(api_client)
    recurring_expense_id = '982000000567240' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Resume a recurring Expense
        api_response = api_instance.recurringexpenses_recurring_expense_id_status_resume_post(recurring_expense_id, x_com_zoho_subscriptions_organizationid)
        print("The response of RecurringExpensesApi->recurringexpenses_recurring_expense_id_status_resume_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecurringExpensesApi->recurringexpenses_recurring_expense_id_status_resume_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recurring_expense_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**ResumeARecurringExpenseResponse**](ResumeARecurringExpenseResponse.md)

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

# **recurringexpenses_recurring_expense_id_status_stop_post**
> StopARecurringExpenseResponse recurringexpenses_recurring_expense_id_status_stop_post(recurring_expense_id, x_com_zoho_subscriptions_organizationid)

Stop a recurring expense

Stop an active recurring expense.

### Example

* OAuth Authentication (Zoho_Auth):

```python
import ls_zoho_billing_recurring_expenses
from ls_zoho_billing_recurring_expenses.models.stop_a_recurring_expense_response import StopARecurringExpenseResponse
from ls_zoho_billing_recurring_expenses.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ls_zoho_billing_recurring_expenses.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with ls_zoho_billing_recurring_expenses.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ls_zoho_billing_recurring_expenses.RecurringExpensesApi(api_client)
    recurring_expense_id = '982000000567240' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Stop a recurring expense
        api_response = api_instance.recurringexpenses_recurring_expense_id_status_stop_post(recurring_expense_id, x_com_zoho_subscriptions_organizationid)
        print("The response of RecurringExpensesApi->recurringexpenses_recurring_expense_id_status_stop_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecurringExpensesApi->recurringexpenses_recurring_expense_id_status_stop_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recurring_expense_id** | **str**|  | 
 **x_com_zoho_subscriptions_organizationid** | **str**| ID of the organization | 

### Return type

[**StopARecurringExpenseResponse**](StopARecurringExpenseResponse.md)

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

