# ApplyCreditsToMultipleInvoicesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoices** | [**List[ApplyCreditsToMultipleInvoicesRequestInvoicesInner]**](ApplyCreditsToMultipleInvoicesRequestInvoicesInner.md) | List of invoices for which the credit note has been raised. This contains &lt;code&gt;invoice_id&lt;/code&gt; and &lt;code&gt;amount&lt;/code&gt;. | 

## Example

```python
from ls_zoho_billing_credit_notes.models.apply_credits_to_multiple_invoices_request import ApplyCreditsToMultipleInvoicesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyCreditsToMultipleInvoicesRequest from a JSON string
apply_credits_to_multiple_invoices_request_instance = ApplyCreditsToMultipleInvoicesRequest.from_json(json)
# print the JSON string representation of the object
print(ApplyCreditsToMultipleInvoicesRequest.to_json())

# convert the object into a dict
apply_credits_to_multiple_invoices_request_dict = apply_credits_to_multiple_invoices_request_instance.to_dict()
# create an instance of ApplyCreditsToMultipleInvoicesRequest from a dict
apply_credits_to_multiple_invoices_request_from_dict = ApplyCreditsToMultipleInvoicesRequest.from_dict(apply_credits_to_multiple_invoices_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


