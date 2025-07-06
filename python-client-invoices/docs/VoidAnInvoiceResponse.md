# VoidAnInvoiceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_invoices.models.void_an_invoice_response import VoidAnInvoiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VoidAnInvoiceResponse from a JSON string
void_an_invoice_response_instance = VoidAnInvoiceResponse.from_json(json)
# print the JSON string representation of the object
print(VoidAnInvoiceResponse.to_json())

# convert the object into a dict
void_an_invoice_response_dict = void_an_invoice_response_instance.to_dict()
# create an instance of VoidAnInvoiceResponse from a dict
void_an_invoice_response_from_dict = VoidAnInvoiceResponse.from_dict(void_an_invoice_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


