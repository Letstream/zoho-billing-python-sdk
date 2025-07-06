# SubscriptionActivitiesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**activities** | [**List[SubscriptionActivitiesResponseActivitiesInner]**](SubscriptionActivitiesResponseActivitiesInner.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_subscription.models.subscription_activities_response import SubscriptionActivitiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionActivitiesResponse from a JSON string
subscription_activities_response_instance = SubscriptionActivitiesResponse.from_json(json)
# print the JSON string representation of the object
print(SubscriptionActivitiesResponse.to_json())

# convert the object into a dict
subscription_activities_response_dict = subscription_activities_response_instance.to_dict()
# create an instance of SubscriptionActivitiesResponse from a dict
subscription_activities_response_from_dict = SubscriptionActivitiesResponse.from_dict(subscription_activities_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


