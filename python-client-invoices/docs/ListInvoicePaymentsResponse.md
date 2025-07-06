# ListInvoicePaymentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**payments** | [**List[ListInvoicePaymentsResponsePaymentsInner]**](ListInvoicePaymentsResponsePaymentsInner.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.list_invoice_payments_response import ListInvoicePaymentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListInvoicePaymentsResponse from a JSON string
list_invoice_payments_response_instance = ListInvoicePaymentsResponse.from_json(json)
# print the JSON string representation of the object
print(ListInvoicePaymentsResponse.to_json())

# convert the object into a dict
list_invoice_payments_response_dict = list_invoice_payments_response_instance.to_dict()
# create an instance of ListInvoicePaymentsResponse from a dict
list_invoice_payments_response_from_dict = ListInvoicePaymentsResponse.from_dict(list_invoice_payments_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


