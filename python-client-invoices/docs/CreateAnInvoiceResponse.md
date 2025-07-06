# CreateAnInvoiceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**invoice** | [**InvoiceResponse**](InvoiceResponse.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.create_an_invoice_response import CreateAnInvoiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAnInvoiceResponse from a JSON string
create_an_invoice_response_instance = CreateAnInvoiceResponse.from_json(json)
# print the JSON string representation of the object
print(CreateAnInvoiceResponse.to_json())

# convert the object into a dict
create_an_invoice_response_dict = create_an_invoice_response_instance.to_dict()
# create an instance of CreateAnInvoiceResponse from a dict
create_an_invoice_response_from_dict = CreateAnInvoiceResponse.from_dict(create_an_invoice_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


