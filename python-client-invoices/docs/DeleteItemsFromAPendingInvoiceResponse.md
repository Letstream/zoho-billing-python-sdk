# DeleteItemsFromAPendingInvoiceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_invoices.models.delete_items_from_a_pending_invoice_response import DeleteItemsFromAPendingInvoiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteItemsFromAPendingInvoiceResponse from a JSON string
delete_items_from_a_pending_invoice_response_instance = DeleteItemsFromAPendingInvoiceResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteItemsFromAPendingInvoiceResponse.to_json())

# convert the object into a dict
delete_items_from_a_pending_invoice_response_dict = delete_items_from_a_pending_invoice_response_instance.to_dict()
# create an instance of DeleteItemsFromAPendingInvoiceResponse from a dict
delete_items_from_a_pending_invoice_response_from_dict = DeleteItemsFromAPendingInvoiceResponse.from_dict(delete_items_from_a_pending_invoice_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


