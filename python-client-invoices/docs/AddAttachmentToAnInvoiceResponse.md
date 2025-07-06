# AddAttachmentToAnInvoiceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_invoices.models.add_attachment_to_an_invoice_response import AddAttachmentToAnInvoiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddAttachmentToAnInvoiceResponse from a JSON string
add_attachment_to_an_invoice_response_instance = AddAttachmentToAnInvoiceResponse.from_json(json)
# print the JSON string representation of the object
print(AddAttachmentToAnInvoiceResponse.to_json())

# convert the object into a dict
add_attachment_to_an_invoice_response_dict = add_attachment_to_an_invoice_response_instance.to_dict()
# create an instance of AddAttachmentToAnInvoiceResponse from a dict
add_attachment_to_an_invoice_response_from_dict = AddAttachmentToAnInvoiceResponse.from_dict(add_attachment_to_an_invoice_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


