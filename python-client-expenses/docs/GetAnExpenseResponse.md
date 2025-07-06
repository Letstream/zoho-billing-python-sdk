# GetAnExpenseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**expense** | [**GetAnExpenseResponseExpense**](GetAnExpenseResponseExpense.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_expenses.models.get_an_expense_response import GetAnExpenseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAnExpenseResponse from a JSON string
get_an_expense_response_instance = GetAnExpenseResponse.from_json(json)
# print the JSON string representation of the object
print(GetAnExpenseResponse.to_json())

# convert the object into a dict
get_an_expense_response_dict = get_an_expense_response_instance.to_dict()
# create an instance of GetAnExpenseResponse from a dict
get_an_expense_response_from_dict = GetAnExpenseResponse.from_dict(get_an_expense_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


