# DeleteTheExpenseReceiptResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_invoices.models.delete_the_expense_receipt_response import DeleteTheExpenseReceiptResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteTheExpenseReceiptResponse from a JSON string
delete_the_expense_receipt_response_instance = DeleteTheExpenseReceiptResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteTheExpenseReceiptResponse.to_json())

# convert the object into a dict
delete_the_expense_receipt_response_dict = delete_the_expense_receipt_response_instance.to_dict()
# create an instance of DeleteTheExpenseReceiptResponse from a dict
delete_the_expense_receipt_response_from_dict = DeleteTheExpenseReceiptResponse.from_dict(delete_the_expense_receipt_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


