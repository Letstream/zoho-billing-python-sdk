# ApplyMultipleCreditsToInvoiceRequestApplyCreditnotesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creditnote_id** | **str** | Unique ID denoting the credit note. | 
**amount_applied** | **object** | Credit amount to be applied to the invoice. | 

## Example

```python
from ls_zoho_billing_invoices.models.apply_multiple_credits_to_invoice_request_apply_creditnotes_inner import ApplyMultipleCreditsToInvoiceRequestApplyCreditnotesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyMultipleCreditsToInvoiceRequestApplyCreditnotesInner from a JSON string
apply_multiple_credits_to_invoice_request_apply_creditnotes_inner_instance = ApplyMultipleCreditsToInvoiceRequestApplyCreditnotesInner.from_json(json)
# print the JSON string representation of the object
print(ApplyMultipleCreditsToInvoiceRequestApplyCreditnotesInner.to_json())

# convert the object into a dict
apply_multiple_credits_to_invoice_request_apply_creditnotes_inner_dict = apply_multiple_credits_to_invoice_request_apply_creditnotes_inner_instance.to_dict()
# create an instance of ApplyMultipleCreditsToInvoiceRequestApplyCreditnotesInner from a dict
apply_multiple_credits_to_invoice_request_apply_creditnotes_inner_from_dict = ApplyMultipleCreditsToInvoiceRequestApplyCreditnotesInner.from_dict(apply_multiple_credits_to_invoice_request_apply_creditnotes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


