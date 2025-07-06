# DeleteAnExpenseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_expenses.models.delete_an_expense_response import DeleteAnExpenseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAnExpenseResponse from a JSON string
delete_an_expense_response_instance = DeleteAnExpenseResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteAnExpenseResponse.to_json())

# convert the object into a dict
delete_an_expense_response_dict = delete_an_expense_response_instance.to_dict()
# create an instance of DeleteAnExpenseResponse from a dict
delete_an_expense_response_from_dict = DeleteAnExpenseResponse.from_dict(delete_an_expense_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


