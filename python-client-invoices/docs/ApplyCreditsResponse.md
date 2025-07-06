# ApplyCreditsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_invoices.models.apply_credits_response import ApplyCreditsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyCreditsResponse from a JSON string
apply_credits_response_instance = ApplyCreditsResponse.from_json(json)
# print the JSON string representation of the object
print(ApplyCreditsResponse.to_json())

# convert the object into a dict
apply_credits_response_dict = apply_credits_response_instance.to_dict()
# create an instance of ApplyCreditsResponse from a dict
apply_credits_response_from_dict = ApplyCreditsResponse.from_dict(apply_credits_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


