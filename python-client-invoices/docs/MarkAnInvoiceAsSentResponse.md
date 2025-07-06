# MarkAnInvoiceAsSentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_invoices.models.mark_an_invoice_as_sent_response import MarkAnInvoiceAsSentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MarkAnInvoiceAsSentResponse from a JSON string
mark_an_invoice_as_sent_response_instance = MarkAnInvoiceAsSentResponse.from_json(json)
# print the JSON string representation of the object
print(MarkAnInvoiceAsSentResponse.to_json())

# convert the object into a dict
mark_an_invoice_as_sent_response_dict = mark_an_invoice_as_sent_response_instance.to_dict()
# create an instance of MarkAnInvoiceAsSentResponse from a dict
mark_an_invoice_as_sent_response_from_dict = MarkAnInvoiceAsSentResponse.from_dict(mark_an_invoice_as_sent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


