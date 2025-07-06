# CancelASubscriptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**subscription** | [**CancelASubscriptionResponseSubscription**](CancelASubscriptionResponseSubscription.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_subscription.models.cancel_a_subscription_response import CancelASubscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CancelASubscriptionResponse from a JSON string
cancel_a_subscription_response_instance = CancelASubscriptionResponse.from_json(json)
# print the JSON string representation of the object
print(CancelASubscriptionResponse.to_json())

# convert the object into a dict
cancel_a_subscription_response_dict = cancel_a_subscription_response_instance.to_dict()
# create an instance of CancelASubscriptionResponse from a dict
cancel_a_subscription_response_from_dict = CancelASubscriptionResponse.from_dict(cancel_a_subscription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


