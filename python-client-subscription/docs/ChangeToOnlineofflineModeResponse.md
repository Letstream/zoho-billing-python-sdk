# ChangeToOnlineofflineModeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**subscription** | [**ChangeToOnlineofflineModeResponseSubscription**](ChangeToOnlineofflineModeResponseSubscription.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_subscription.models.change_to_onlineoffline_mode_response import ChangeToOnlineofflineModeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeToOnlineofflineModeResponse from a JSON string
change_to_onlineoffline_mode_response_instance = ChangeToOnlineofflineModeResponse.from_json(json)
# print the JSON string representation of the object
print(ChangeToOnlineofflineModeResponse.to_json())

# convert the object into a dict
change_to_onlineoffline_mode_response_dict = change_to_onlineoffline_mode_response_instance.to_dict()
# create an instance of ChangeToOnlineofflineModeResponse from a dict
change_to_onlineoffline_mode_response_from_dict = ChangeToOnlineofflineModeResponse.from_dict(change_to_onlineoffline_mode_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


