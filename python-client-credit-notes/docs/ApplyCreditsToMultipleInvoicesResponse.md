# ApplyCreditsToMultipleInvoicesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**invoices** | [**List[ApplyCreditsToMultipleInvoicesResponseInvoicesInner]**](ApplyCreditsToMultipleInvoicesResponseInvoicesInner.md) | List of invoices for which the credit note has been raised. This contains &lt;code&gt;invoice_id&lt;/code&gt; and &lt;code&gt;amount&lt;/code&gt;. | [optional] 

## Example

```python
from ls_zoho_billing_credit_notes.models.apply_credits_to_multiple_invoices_response import ApplyCreditsToMultipleInvoicesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyCreditsToMultipleInvoicesResponse from a JSON string
apply_credits_to_multiple_invoices_response_instance = ApplyCreditsToMultipleInvoicesResponse.from_json(json)
# print the JSON string representation of the object
print(ApplyCreditsToMultipleInvoicesResponse.to_json())

# convert the object into a dict
apply_credits_to_multiple_invoices_response_dict = apply_credits_to_multiple_invoices_response_instance.to_dict()
# create an instance of ApplyCreditsToMultipleInvoicesResponse from a dict
apply_credits_to_multiple_invoices_response_from_dict = ApplyCreditsToMultipleInvoicesResponse.from_dict(apply_credits_to_multiple_invoices_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


