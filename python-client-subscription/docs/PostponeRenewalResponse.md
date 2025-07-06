# PostponeRenewalResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**subscription** | [**PostponeRenewalResponseSubscription**](PostponeRenewalResponseSubscription.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_subscription.models.postpone_renewal_response import PostponeRenewalResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostponeRenewalResponse from a JSON string
postpone_renewal_response_instance = PostponeRenewalResponse.from_json(json)
# print the JSON string representation of the object
print(PostponeRenewalResponse.to_json())

# convert the object into a dict
postpone_renewal_response_dict = postpone_renewal_response_instance.to_dict()
# create an instance of PostponeRenewalResponse from a dict
postpone_renewal_response_from_dict = PostponeRenewalResponse.from_dict(postpone_renewal_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


