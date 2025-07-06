# GetAnExpenseResponseExpenseLineItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_item_id** | **str** | ID of the items in the expense | [optional] 
**account_id** | **str** | ID of the expense account. | [optional] 
**account_name** | **str** | Name of the expense account in which that expense is recorded | [optional] 
**description** | **str** | Description of the expense. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
**tax_amount** | **float** | total expense amount | [optional] 
**tax_id** | **str** | Tax ID applied | [optional] 
**tax_name** | **str** | Name of the tax levied | [optional] 
**tax_type** | **str** | Type of tax applied | [optional] 
**tax_percentage** | **float** | Percentage of tax charged | [optional] 
**item_total** | **str** | Total value of the ites billed | [optional] 
**item_order** | **str** | Order of the items | [optional] 
**amount** | **float** | Total expense value | [optional] 
**hsn_or_sac** | **str** | Add HSN/SAC code for your goods/services | [optional] 
**reverse_charge_tax_id** | **str** | ID of the reverse charge tax | [optional] 
**reverse_charge_tax_name** | **str** | Enter name of the reverse charge tax | [optional] 
**reverse_charge_tax_percentage** | **float** | Enter percentage of the reverse charge tax | [optional] 
**reverse_charge_tax_amount** | **int** | Enter amount of the reverse charge tax | [optional] 

## Example

```python
from ls_zoho_billing_expenses.models.get_an_expense_response_expense_line_item import GetAnExpenseResponseExpenseLineItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetAnExpenseResponseExpenseLineItem from a JSON string
get_an_expense_response_expense_line_item_instance = GetAnExpenseResponseExpenseLineItem.from_json(json)
# print the JSON string representation of the object
print(GetAnExpenseResponseExpenseLineItem.to_json())

# convert the object into a dict
get_an_expense_response_expense_line_item_dict = get_an_expense_response_expense_line_item_instance.to_dict()
# create an instance of GetAnExpenseResponseExpenseLineItem from a dict
get_an_expense_response_expense_line_item_from_dict = GetAnExpenseResponseExpenseLineItem.from_dict(get_an_expense_response_expense_line_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


