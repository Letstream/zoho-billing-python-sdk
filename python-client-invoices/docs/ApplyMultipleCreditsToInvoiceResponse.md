# ApplyMultipleCreditsToInvoiceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**apply_creditnotes** | [**List[ApplyMultipleCreditsToInvoiceResponseApplyCreditnotesInner]**](ApplyMultipleCreditsToInvoiceResponseApplyCreditnotesInner.md) | List of creditnotes applied to the object. | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.apply_multiple_credits_to_invoice_response import ApplyMultipleCreditsToInvoiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyMultipleCreditsToInvoiceResponse from a JSON string
apply_multiple_credits_to_invoice_response_instance = ApplyMultipleCreditsToInvoiceResponse.from_json(json)
# print the JSON string representation of the object
print(ApplyMultipleCreditsToInvoiceResponse.to_json())

# convert the object into a dict
apply_multiple_credits_to_invoice_response_dict = apply_multiple_credits_to_invoice_response_instance.to_dict()
# create an instance of ApplyMultipleCreditsToInvoiceResponse from a dict
apply_multiple_credits_to_invoice_response_from_dict = ApplyMultipleCreditsToInvoiceResponse.from_dict(apply_multiple_credits_to_invoice_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


