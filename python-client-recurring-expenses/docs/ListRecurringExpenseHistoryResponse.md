# ListRecurringExpenseHistoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**comments** | [**List[ListRecurringExpenseHistoryResponseCommentsInner]**](ListRecurringExpenseHistoryResponseCommentsInner.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_recurring_expenses.models.list_recurring_expense_history_response import ListRecurringExpenseHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListRecurringExpenseHistoryResponse from a JSON string
list_recurring_expense_history_response_instance = ListRecurringExpenseHistoryResponse.from_json(json)
# print the JSON string representation of the object
print(ListRecurringExpenseHistoryResponse.to_json())

# convert the object into a dict
list_recurring_expense_history_response_dict = list_recurring_expense_history_response_instance.to_dict()
# create an instance of ListRecurringExpenseHistoryResponse from a dict
list_recurring_expense_history_response_from_dict = ListRecurringExpenseHistoryResponse.from_dict(list_recurring_expense_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


