# StopARecurringExpenseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_recurring_expenses.models.stop_a_recurring_expense_response import StopARecurringExpenseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StopARecurringExpenseResponse from a JSON string
stop_a_recurring_expense_response_instance = StopARecurringExpenseResponse.from_json(json)
# print the JSON string representation of the object
print(StopARecurringExpenseResponse.to_json())

# convert the object into a dict
stop_a_recurring_expense_response_dict = stop_a_recurring_expense_response_instance.to_dict()
# create an instance of StopARecurringExpenseResponse from a dict
stop_a_recurring_expense_response_from_dict = StopARecurringExpenseResponse.from_dict(stop_a_recurring_expense_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


