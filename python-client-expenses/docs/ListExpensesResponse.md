# ListExpensesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**expenses** | [**List[ListExpensesResponseExpensesInner]**](ListExpensesResponseExpensesInner.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_expenses.models.list_expenses_response import ListExpensesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListExpensesResponse from a JSON string
list_expenses_response_instance = ListExpensesResponse.from_json(json)
# print the JSON string representation of the object
print(ListExpensesResponse.to_json())

# convert the object into a dict
list_expenses_response_dict = list_expenses_response_instance.to_dict()
# create an instance of ListExpensesResponse from a dict
list_expenses_response_from_dict = ListExpensesResponse.from_dict(list_expenses_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


