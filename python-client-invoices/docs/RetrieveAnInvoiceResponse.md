# RetrieveAnInvoiceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**invoice** | [**RetrieveAnInvoiceResponseInvoice**](RetrieveAnInvoiceResponseInvoice.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.retrieve_an_invoice_response import RetrieveAnInvoiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveAnInvoiceResponse from a JSON string
retrieve_an_invoice_response_instance = RetrieveAnInvoiceResponse.from_json(json)
# print the JSON string representation of the object
print(RetrieveAnInvoiceResponse.to_json())

# convert the object into a dict
retrieve_an_invoice_response_dict = retrieve_an_invoice_response_instance.to_dict()
# create an instance of RetrieveAnInvoiceResponse from a dict
retrieve_an_invoice_response_from_dict = RetrieveAnInvoiceResponse.from_dict(retrieve_an_invoice_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


