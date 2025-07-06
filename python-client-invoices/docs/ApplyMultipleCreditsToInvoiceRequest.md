# ApplyMultipleCreditsToInvoiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apply_creditnotes** | [**List[ApplyMultipleCreditsToInvoiceRequestApplyCreditnotesInner]**](ApplyMultipleCreditsToInvoiceRequestApplyCreditnotesInner.md) | List of creditnotes applied to the object. | 

## Example

```python
from ls_zoho_billing_invoices.models.apply_multiple_credits_to_invoice_request import ApplyMultipleCreditsToInvoiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyMultipleCreditsToInvoiceRequest from a JSON string
apply_multiple_credits_to_invoice_request_instance = ApplyMultipleCreditsToInvoiceRequest.from_json(json)
# print the JSON string representation of the object
print(ApplyMultipleCreditsToInvoiceRequest.to_json())

# convert the object into a dict
apply_multiple_credits_to_invoice_request_dict = apply_multiple_credits_to_invoice_request_instance.to_dict()
# create an instance of ApplyMultipleCreditsToInvoiceRequest from a dict
apply_multiple_credits_to_invoice_request_from_dict = ApplyMultipleCreditsToInvoiceRequest.from_dict(apply_multiple_credits_to_invoice_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


