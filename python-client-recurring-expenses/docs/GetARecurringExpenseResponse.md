# GetARecurringExpenseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**recurring_expense** | [**GetARecurringExpenseResponseRecurringExpense**](GetARecurringExpenseResponseRecurringExpense.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_recurring_expenses.models.get_a_recurring_expense_response import GetARecurringExpenseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetARecurringExpenseResponse from a JSON string
get_a_recurring_expense_response_instance = GetARecurringExpenseResponse.from_json(json)
# print the JSON string representation of the object
print(GetARecurringExpenseResponse.to_json())

# convert the object into a dict
get_a_recurring_expense_response_dict = get_a_recurring_expense_response_instance.to_dict()
# create an instance of GetARecurringExpenseResponse from a dict
get_a_recurring_expense_response_from_dict = GetARecurringExpenseResponse.from_dict(get_a_recurring_expense_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


