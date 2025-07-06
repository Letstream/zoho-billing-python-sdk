# ListRecurringExpensesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**recurring_expenses** | [**List[ListRecurringExpensesResponseRecurringExpensesInner]**](ListRecurringExpensesResponseRecurringExpensesInner.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_recurring_expenses.models.list_recurring_expenses_response import ListRecurringExpensesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListRecurringExpensesResponse from a JSON string
list_recurring_expenses_response_instance = ListRecurringExpensesResponse.from_json(json)
# print the JSON string representation of the object
print(ListRecurringExpensesResponse.to_json())

# convert the object into a dict
list_recurring_expenses_response_dict = list_recurring_expenses_response_instance.to_dict()
# create an instance of ListRecurringExpensesResponse from a dict
list_recurring_expenses_response_from_dict = ListRecurringExpensesResponse.from_dict(list_recurring_expenses_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


