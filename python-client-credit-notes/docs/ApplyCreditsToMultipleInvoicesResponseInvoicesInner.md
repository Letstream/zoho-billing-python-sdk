# ApplyCreditsToMultipleInvoicesResponseInvoicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **str** | Invoice ID of the required invoice. | [optional] 
**amount_applied** | **float** | Amount paid for the invoice. | [optional] 

## Example

```python
from ls_zoho_billing_credit_notes.models.apply_credits_to_multiple_invoices_response_invoices_inner import ApplyCreditsToMultipleInvoicesResponseInvoicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyCreditsToMultipleInvoicesResponseInvoicesInner from a JSON string
apply_credits_to_multiple_invoices_response_invoices_inner_instance = ApplyCreditsToMultipleInvoicesResponseInvoicesInner.from_json(json)
# print the JSON string representation of the object
print(ApplyCreditsToMultipleInvoicesResponseInvoicesInner.to_json())

# convert the object into a dict
apply_credits_to_multiple_invoices_response_invoices_inner_dict = apply_credits_to_multiple_invoices_response_invoices_inner_instance.to_dict()
# create an instance of ApplyCreditsToMultipleInvoicesResponseInvoicesInner from a dict
apply_credits_to_multiple_invoices_response_invoices_inner_from_dict = ApplyCreditsToMultipleInvoicesResponseInvoicesInner.from_dict(apply_credits_to_multiple_invoices_response_invoices_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


