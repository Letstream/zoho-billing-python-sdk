# GetAnInvoiceAttachmentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_invoices.models.get_an_invoice_attachment_response import GetAnInvoiceAttachmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAnInvoiceAttachmentResponse from a JSON string
get_an_invoice_attachment_response_instance = GetAnInvoiceAttachmentResponse.from_json(json)
# print the JSON string representation of the object
print(GetAnInvoiceAttachmentResponse.to_json())

# convert the object into a dict
get_an_invoice_attachment_response_dict = get_an_invoice_attachment_response_instance.to_dict()
# create an instance of GetAnInvoiceAttachmentResponse from a dict
get_an_invoice_attachment_response_from_dict = GetAnInvoiceAttachmentResponse.from_dict(get_an_invoice_attachment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


