# ListChildExpensesCreatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**expensehistory** | [**List[ListChildExpensesCreatedResponseExpensehistoryInner]**](ListChildExpensesCreatedResponseExpensehistoryInner.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_recurring_expenses.models.list_child_expenses_created_response import ListChildExpensesCreatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListChildExpensesCreatedResponse from a JSON string
list_child_expenses_created_response_instance = ListChildExpensesCreatedResponse.from_json(json)
# print the JSON string representation of the object
print(ListChildExpensesCreatedResponse.to_json())

# convert the object into a dict
list_child_expenses_created_response_dict = list_child_expenses_created_response_instance.to_dict()
# create an instance of ListChildExpensesCreatedResponse from a dict
list_child_expenses_created_response_from_dict = ListChildExpensesCreatedResponse.from_dict(list_child_expenses_created_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


