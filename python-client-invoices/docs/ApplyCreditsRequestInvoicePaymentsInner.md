# ApplyCreditsRequestInvoicePaymentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_id** | **str** | ID of the payment from which credit has to be applied. | [optional] 
**amount_applied** | **float** | Amount applied to the invoice. | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.apply_credits_request_invoice_payments_inner import ApplyCreditsRequestInvoicePaymentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyCreditsRequestInvoicePaymentsInner from a JSON string
apply_credits_request_invoice_payments_inner_instance = ApplyCreditsRequestInvoicePaymentsInner.from_json(json)
# print the JSON string representation of the object
print(ApplyCreditsRequestInvoicePaymentsInner.to_json())

# convert the object into a dict
apply_credits_request_invoice_payments_inner_dict = apply_credits_request_invoice_payments_inner_instance.to_dict()
# create an instance of ApplyCreditsRequestInvoicePaymentsInner from a dict
apply_credits_request_invoice_payments_inner_from_dict = ApplyCreditsRequestInvoicePaymentsInner.from_dict(apply_credits_request_invoice_payments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


