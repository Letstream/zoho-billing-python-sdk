# UpdateAnInvoiceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**invoice** | [**UpdateAnInvoiceResponseInvoice**](UpdateAnInvoiceResponseInvoice.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.update_an_invoice_response import UpdateAnInvoiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAnInvoiceResponse from a JSON string
update_an_invoice_response_instance = UpdateAnInvoiceResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateAnInvoiceResponse.to_json())

# convert the object into a dict
update_an_invoice_response_dict = update_an_invoice_response_instance.to_dict()
# create an instance of UpdateAnInvoiceResponse from a dict
update_an_invoice_response_from_dict = UpdateAnInvoiceResponse.from_dict(update_an_invoice_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


