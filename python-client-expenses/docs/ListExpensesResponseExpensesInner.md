# ListExpensesResponseExpensesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expense_id** | **str** | Unique ID of the expense | [optional] 
**var_date** | **str** | Date of the expense | [optional] 
**account_name** | **str** | Name of the expense account in which that expense is recorded | [optional] 
**description** | **str** | Description of the expense. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
**currency_id** | **str** | Unique ID of the currency | [optional] 
**currency_code** | **str** | Code of the currency | [optional] 
**bcy_total** | **float** | Total value of expense in Base currency | [optional] 
**bcy_total_without_tax** | **float** | Total expense in Base currency excluding tax | [optional] 
**total** | **float** | Total value of expense | [optional] 
**total_without_tax** | **float** | Total expense excluding tax | [optional] 
**is_billable** | **bool** | Check if an expense is billable | [optional] 
**reference_number** | **str** | Reference number of the expense. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
**customer_id** | **str** | ID of the expense account. | [optional] 
**customer_name** | **str** | Name of the Customer for whom expense is raised. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
**status** | **str** | Expense status | [optional] 
**custom_fields** | [**List[CustomFieldsInner]**](CustomFieldsInner.md) | Custom fields for an expense. | [optional] 
**created_time** | **str** | Time of expense creation | [optional] 
**last_modified_time** | **str** | Date of last modification to the expense | [optional] 
**expense_receipt_name** | **str** | Name of the expense receipt | [optional] 
**mileage_rate** | **float** | Mileage rate for a particular mileage expense. | [optional] 
**mileage_unit** | **str** | Unit of the distance travelled. Allowed Values: &lt;code&gt;km&lt;/code&gt; and &lt;code&gt;mile&lt;/code&gt; | [optional] 
**expense_type** | **str** | Type of the expense | [optional] 
**start_reading** | **float** | Start reading of odometer when creating a mileage expense where &lt;code&gt;mileage_type&lt;/code&gt; is &lt;code&gt;odometer&lt;/code&gt;. | [optional] 
**end_reading** | **float** | End reading of odometer when creating a mileage expense where &lt;code&gt;mileage_type&lt;/code&gt; is &lt;code&gt;odometer&lt;/code&gt;. | [optional] 

## Example

```python
from ls_zoho_billing_expenses.models.list_expenses_response_expenses_inner import ListExpensesResponseExpensesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListExpensesResponseExpensesInner from a JSON string
list_expenses_response_expenses_inner_instance = ListExpensesResponseExpensesInner.from_json(json)
# print the JSON string representation of the object
print(ListExpensesResponseExpensesInner.to_json())

# convert the object into a dict
list_expenses_response_expenses_inner_dict = list_expenses_response_expenses_inner_instance.to_dict()
# create an instance of ListExpensesResponseExpensesInner from a dict
list_expenses_response_expenses_inner_from_dict = ListExpensesResponseExpensesInner.from_dict(list_expenses_response_expenses_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


