# ApplyMultipleCreditsToInvoiceResponseApplyCreditnotesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creditnotes_invoice_id** | **str** | Unique identifier to denote the Associated Credits to the invoice | [optional] 
**creditnote_id** | **str** | Unique ID denoting the credit note. | [optional] 
**invoice_id** | **str** | Unique ID generated for an invoice. | [optional] 
**amount_applied** | **float** | Amount paid for the invoice. | [optional] 
**var_date** | **str** | Date on which the invoice is paid. | [optional] 
**date_formatted** | **object** | Formatted value for the date. | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.apply_multiple_credits_to_invoice_response_apply_creditnotes_inner import ApplyMultipleCreditsToInvoiceResponseApplyCreditnotesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyMultipleCreditsToInvoiceResponseApplyCreditnotesInner from a JSON string
apply_multiple_credits_to_invoice_response_apply_creditnotes_inner_instance = ApplyMultipleCreditsToInvoiceResponseApplyCreditnotesInner.from_json(json)
# print the JSON string representation of the object
print(ApplyMultipleCreditsToInvoiceResponseApplyCreditnotesInner.to_json())

# convert the object into a dict
apply_multiple_credits_to_invoice_response_apply_creditnotes_inner_dict = apply_multiple_credits_to_invoice_response_apply_creditnotes_inner_instance.to_dict()
# create an instance of ApplyMultipleCreditsToInvoiceResponseApplyCreditnotesInner from a dict
apply_multiple_credits_to_invoice_response_apply_creditnotes_inner_from_dict = ApplyMultipleCreditsToInvoiceResponseApplyCreditnotesInner.from_dict(apply_multiple_credits_to_invoice_response_apply_creditnotes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


