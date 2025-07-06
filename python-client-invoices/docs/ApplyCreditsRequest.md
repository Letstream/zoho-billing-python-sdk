# ApplyCreditsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_payments** | [**List[ApplyCreditsRequestInvoicePaymentsInner]**](ApplyCreditsRequestInvoicePaymentsInner.md) | Payments applied to an invoice. | [optional] 
**apply_creditnotes** | [**List[ApplyCreditsRequestApplyCreditnotesInner]**](ApplyCreditsRequestApplyCreditnotesInner.md) | Credits applied to invoice. | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.apply_credits_request import ApplyCreditsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyCreditsRequest from a JSON string
apply_credits_request_instance = ApplyCreditsRequest.from_json(json)
# print the JSON string representation of the object
print(ApplyCreditsRequest.to_json())

# convert the object into a dict
apply_credits_request_dict = apply_credits_request_instance.to_dict()
# create an instance of ApplyCreditsRequest from a dict
apply_credits_request_from_dict = ApplyCreditsRequest.from_dict(apply_credits_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


