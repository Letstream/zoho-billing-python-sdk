# GetAnInvoiceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**invoice** | [**GetAnInvoiceResponseInvoice**](GetAnInvoiceResponseInvoice.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.get_an_invoice_response import GetAnInvoiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAnInvoiceResponse from a JSON string
get_an_invoice_response_instance = GetAnInvoiceResponse.from_json(json)
# print the JSON string representation of the object
print(GetAnInvoiceResponse.to_json())

# convert the object into a dict
get_an_invoice_response_dict = get_an_invoice_response_instance.to_dict()
# create an instance of GetAnInvoiceResponse from a dict
get_an_invoice_response_from_dict = GetAnInvoiceResponse.from_dict(get_an_invoice_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


