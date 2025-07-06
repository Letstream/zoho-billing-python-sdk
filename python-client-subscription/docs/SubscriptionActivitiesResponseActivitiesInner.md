# SubscriptionActivitiesResponseActivitiesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_id** | **str** | Unique ID to represent the activity. | [optional] 
**description** | **str** | Make a note of why the customer was charged so that if can be used for any future reference. | [optional] 
**activity_time** | **str** | Time in which the activity was recorded. | [optional] 
**commented_by** | **object** | Name of the user who added the comment. | [optional] 

## Example

```python
from ls_zoho_billing_subscription.models.subscription_activities_response_activities_inner import SubscriptionActivitiesResponseActivitiesInner

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionActivitiesResponseActivitiesInner from a JSON string
subscription_activities_response_activities_inner_instance = SubscriptionActivitiesResponseActivitiesInner.from_json(json)
# print the JSON string representation of the object
print(SubscriptionActivitiesResponseActivitiesInner.to_json())

# convert the object into a dict
subscription_activities_response_activities_inner_dict = subscription_activities_response_activities_inner_instance.to_dict()
# create an instance of SubscriptionActivitiesResponseActivitiesInner from a dict
subscription_activities_response_activities_inner_from_dict = SubscriptionActivitiesResponseActivitiesInner.from_dict(subscription_activities_response_activities_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


