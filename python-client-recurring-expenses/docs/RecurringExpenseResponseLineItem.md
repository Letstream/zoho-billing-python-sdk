# RecurringExpenseResponseLineItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_item_id** | **str** | Unique ID of Item listed | [optional] 
**account_id** | **str** | Unique ID of an account | [optional] 
**account_name** | **str** | For which Account the Expense is raised. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
**description** | **str** | Search recurring expenses by description. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
**tax_amount** | **float** | Total value of tax applied | [optional] 
**tax_id** | **str** | Unique ID for the tax | [optional] 
**tax_name** | **str** | Name of the tax | [optional] 
**tax_type** | **str** | Type of tax applied | [optional] 
**tax_percentage** | **float** | Percentage of tax levied | [optional] 
**item_total** | **str** | Total value of items | [optional] 
**item_order** | **str** | Order of items | [optional] 
**hsn_or_sac** | **str** | Add HSN/SAC code for your goods/services | [optional] 
**reverse_charge_tax_id** | **str** | Enter reverse charge tax ID | [optional] 
**reverse_charge_tax_name** | **str** | Enter reverse charge tax name | [optional] 
**reverse_charge_tax_percentage** | **float** | Tax percentage of the reverse charge | [optional] 
**reverse_charge_tax_amount** | **float** | Tax amount of the reverse charge | [optional] 

## Example

```python
from ls_zoho_billing_recurring_expenses.models.recurring_expense_response_line_item import RecurringExpenseResponseLineItem

# TODO update the JSON string below
json = "{}"
# create an instance of RecurringExpenseResponseLineItem from a JSON string
recurring_expense_response_line_item_instance = RecurringExpenseResponseLineItem.from_json(json)
# print the JSON string representation of the object
print(RecurringExpenseResponseLineItem.to_json())

# convert the object into a dict
recurring_expense_response_line_item_dict = recurring_expense_response_line_item_instance.to_dict()
# create an instance of RecurringExpenseResponseLineItem from a dict
recurring_expense_response_line_item_from_dict = RecurringExpenseResponseLineItem.from_dict(recurring_expense_response_line_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


