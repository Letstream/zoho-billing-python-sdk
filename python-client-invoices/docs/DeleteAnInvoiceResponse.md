# DeleteAnInvoiceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_invoices.models.delete_an_invoice_response import DeleteAnInvoiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAnInvoiceResponse from a JSON string
delete_an_invoice_response_instance = DeleteAnInvoiceResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteAnInvoiceResponse.to_json())

# convert the object into a dict
delete_an_invoice_response_dict = delete_an_invoice_response_instance.to_dict()
# create an instance of DeleteAnInvoiceResponse from a dict
delete_an_invoice_response_from_dict = DeleteAnInvoiceResponse.from_dict(delete_an_invoice_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


