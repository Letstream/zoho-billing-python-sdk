# WriteOffInvoiceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_invoices.models.write_off_invoice_response import WriteOffInvoiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WriteOffInvoiceResponse from a JSON string
write_off_invoice_response_instance = WriteOffInvoiceResponse.from_json(json)
# print the JSON string representation of the object
print(WriteOffInvoiceResponse.to_json())

# convert the object into a dict
write_off_invoice_response_dict = write_off_invoice_response_instance.to_dict()
# create an instance of WriteOffInvoiceResponse from a dict
write_off_invoice_response_from_dict = WriteOffInvoiceResponse.from_dict(write_off_invoice_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


