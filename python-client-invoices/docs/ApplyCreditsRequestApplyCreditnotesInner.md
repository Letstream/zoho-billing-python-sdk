# ApplyCreditsRequestApplyCreditnotesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creditnote_id** | **str** | ID of the credit note from which credit has to be applied. | [optional] 
**amount_applied** | **float** | Amount applied to the invoice. | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.apply_credits_request_apply_creditnotes_inner import ApplyCreditsRequestApplyCreditnotesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyCreditsRequestApplyCreditnotesInner from a JSON string
apply_credits_request_apply_creditnotes_inner_instance = ApplyCreditsRequestApplyCreditnotesInner.from_json(json)
# print the JSON string representation of the object
print(ApplyCreditsRequestApplyCreditnotesInner.to_json())

# convert the object into a dict
apply_credits_request_apply_creditnotes_inner_dict = apply_credits_request_apply_creditnotes_inner_instance.to_dict()
# create an instance of ApplyCreditsRequestApplyCreditnotesInner from a dict
apply_credits_request_apply_creditnotes_inner_from_dict = ApplyCreditsRequestApplyCreditnotesInner.from_dict(apply_credits_request_apply_creditnotes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


