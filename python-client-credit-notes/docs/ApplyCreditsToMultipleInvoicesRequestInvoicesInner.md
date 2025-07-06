# ApplyCreditsToMultipleInvoicesRequestInvoicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **str** | Invoice ID of the required invoice. | 
**amount_applied** | **object** | Credit amount to be applied to the invoice. | 

## Example

```python
from ls_zoho_billing_credit_notes.models.apply_credits_to_multiple_invoices_request_invoices_inner import ApplyCreditsToMultipleInvoicesRequestInvoicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyCreditsToMultipleInvoicesRequestInvoicesInner from a JSON string
apply_credits_to_multiple_invoices_request_invoices_inner_instance = ApplyCreditsToMultipleInvoicesRequestInvoicesInner.from_json(json)
# print the JSON string representation of the object
print(ApplyCreditsToMultipleInvoicesRequestInvoicesInner.to_json())

# convert the object into a dict
apply_credits_to_multiple_invoices_request_invoices_inner_dict = apply_credits_to_multiple_invoices_request_invoices_inner_instance.to_dict()
# create an instance of ApplyCreditsToMultipleInvoicesRequestInvoicesInner from a dict
apply_credits_to_multiple_invoices_request_invoices_inner_from_dict = ApplyCreditsToMultipleInvoicesRequestInvoicesInner.from_dict(apply_credits_to_multiple_invoices_request_invoices_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


