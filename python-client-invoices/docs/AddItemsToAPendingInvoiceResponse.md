# AddItemsToAPendingInvoiceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**invoice** | [**AddItemsToAPendingInvoiceResponseInvoice**](AddItemsToAPendingInvoiceResponseInvoice.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.add_items_to_a_pending_invoice_response import AddItemsToAPendingInvoiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddItemsToAPendingInvoiceResponse from a JSON string
add_items_to_a_pending_invoice_response_instance = AddItemsToAPendingInvoiceResponse.from_json(json)
# print the JSON string representation of the object
print(AddItemsToAPendingInvoiceResponse.to_json())

# convert the object into a dict
add_items_to_a_pending_invoice_response_dict = add_items_to_a_pending_invoice_response_instance.to_dict()
# create an instance of AddItemsToAPendingInvoiceResponse from a dict
add_items_to_a_pending_invoice_response_from_dict = AddItemsToAPendingInvoiceResponse.from_dict(add_items_to_a_pending_invoice_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


