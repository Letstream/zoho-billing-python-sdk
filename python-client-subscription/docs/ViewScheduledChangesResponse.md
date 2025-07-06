# ViewScheduledChangesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**subscription** | [**ViewScheduledChangesResponseSubscription**](ViewScheduledChangesResponseSubscription.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_subscription.models.view_scheduled_changes_response import ViewScheduledChangesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ViewScheduledChangesResponse from a JSON string
view_scheduled_changes_response_instance = ViewScheduledChangesResponse.from_json(json)
# print the JSON string representation of the object
print(ViewScheduledChangesResponse.to_json())

# convert the object into a dict
view_scheduled_changes_response_dict = view_scheduled_changes_response_instance.to_dict()
# create an instance of ViewScheduledChangesResponse from a dict
view_scheduled_changes_response_from_dict = ViewScheduledChangesResponse.from_dict(view_scheduled_changes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


