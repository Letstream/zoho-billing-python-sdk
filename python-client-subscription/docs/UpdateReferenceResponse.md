# UpdateReferenceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**subscription** | [**ChangeToOnlineofflineModeResponseSubscription**](ChangeToOnlineofflineModeResponseSubscription.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_subscription.models.update_reference_response import UpdateReferenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateReferenceResponse from a JSON string
update_reference_response_instance = UpdateReferenceResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateReferenceResponse.to_json())

# convert the object into a dict
update_reference_response_dict = update_reference_response_instance.to_dict()
# create an instance of UpdateReferenceResponse from a dict
update_reference_response_from_dict = UpdateReferenceResponse.from_dict(update_reference_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


