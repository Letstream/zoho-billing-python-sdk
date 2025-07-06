# CreateAnExpenseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**expense** | [**ExpenseResponse**](ExpenseResponse.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_expenses.models.create_an_expense_response import CreateAnExpenseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAnExpenseResponse from a JSON string
create_an_expense_response_instance = CreateAnExpenseResponse.from_json(json)
# print the JSON string representation of the object
print(CreateAnExpenseResponse.to_json())

# convert the object into a dict
create_an_expense_response_dict = create_an_expense_response_instance.to_dict()
# create an instance of CreateAnExpenseResponse from a dict
create_an_expense_response_from_dict = CreateAnExpenseResponse.from_dict(create_an_expense_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


