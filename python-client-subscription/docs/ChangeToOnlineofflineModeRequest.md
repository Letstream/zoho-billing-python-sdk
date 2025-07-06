# ChangeToOnlineofflineModeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_collect** | **object** | auto_collect is set to true for creating an online subscription which will charge the customer’s card automatically on every renewal. To create an offline subscriptions, set auto_collect to false. | 

## Example

```python
from ls_zoho_billing_subscription.models.change_to_onlineoffline_mode_request import ChangeToOnlineofflineModeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeToOnlineofflineModeRequest from a JSON string
change_to_onlineoffline_mode_request_instance = ChangeToOnlineofflineModeRequest.from_json(json)
# print the JSON string representation of the object
print(ChangeToOnlineofflineModeRequest.to_json())

# convert the object into a dict
change_to_onlineoffline_mode_request_dict = change_to_onlineoffline_mode_request_instance.to_dict()
# create an instance of ChangeToOnlineofflineModeRequest from a dict
change_to_onlineoffline_mode_request_from_dict = ChangeToOnlineofflineModeRequest.from_dict(change_to_onlineoffline_mode_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


