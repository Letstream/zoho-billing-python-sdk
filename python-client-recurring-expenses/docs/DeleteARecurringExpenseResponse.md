# DeleteARecurringExpenseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_recurring_expenses.models.delete_a_recurring_expense_response import DeleteARecurringExpenseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteARecurringExpenseResponse from a JSON string
delete_a_recurring_expense_response_instance = DeleteARecurringExpenseResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteARecurringExpenseResponse.to_json())

# convert the object into a dict
delete_a_recurring_expense_response_dict = delete_a_recurring_expense_response_instance.to_dict()
# create an instance of DeleteARecurringExpenseResponse from a dict
delete_a_recurring_expense_response_from_dict = DeleteARecurringExpenseResponse.from_dict(delete_a_recurring_expense_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


