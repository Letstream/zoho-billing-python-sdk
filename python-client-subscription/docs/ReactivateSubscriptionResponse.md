# ReactivateSubscriptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**subscription** | [**ReactivateSubscriptionResponseSubscription**](ReactivateSubscriptionResponseSubscription.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_subscription.models.reactivate_subscription_response import ReactivateSubscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReactivateSubscriptionResponse from a JSON string
reactivate_subscription_response_instance = ReactivateSubscriptionResponse.from_json(json)
# print the JSON string representation of the object
print(ReactivateSubscriptionResponse.to_json())

# convert the object into a dict
reactivate_subscription_response_dict = reactivate_subscription_response_instance.to_dict()
# create an instance of ReactivateSubscriptionResponse from a dict
reactivate_subscription_response_from_dict = ReactivateSubscriptionResponse.from_dict(reactivate_subscription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


