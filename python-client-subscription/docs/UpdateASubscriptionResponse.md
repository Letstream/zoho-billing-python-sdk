# UpdateASubscriptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**subscription** | [**UpdateASubscriptionResponseSubscription**](UpdateASubscriptionResponseSubscription.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_subscription.models.update_a_subscription_response import UpdateASubscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateASubscriptionResponse from a JSON string
update_a_subscription_response_instance = UpdateASubscriptionResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateASubscriptionResponse.to_json())

# convert the object into a dict
update_a_subscription_response_dict = update_a_subscription_response_instance.to_dict()
# create an instance of UpdateASubscriptionResponse from a dict
update_a_subscription_response_from_dict = UpdateASubscriptionResponse.from_dict(update_a_subscription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


