# UpdateAnExpenseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**expense** | [**UpdateAnExpenseResponseExpense**](UpdateAnExpenseResponseExpense.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_expenses.models.update_an_expense_response import UpdateAnExpenseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAnExpenseResponse from a JSON string
update_an_expense_response_instance = UpdateAnExpenseResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateAnExpenseResponse.to_json())

# convert the object into a dict
update_an_expense_response_dict = update_an_expense_response_instance.to_dict()
# create an instance of UpdateAnExpenseResponse from a dict
update_an_expense_response_from_dict = UpdateAnExpenseResponse.from_dict(update_an_expense_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


