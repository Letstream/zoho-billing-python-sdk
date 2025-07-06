# RetrieveASubscriptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**subscription** | [**RetrieveASubscriptionResponseSubscription**](RetrieveASubscriptionResponseSubscription.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_subscription.models.retrieve_a_subscription_response import RetrieveASubscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveASubscriptionResponse from a JSON string
retrieve_a_subscription_response_instance = RetrieveASubscriptionResponse.from_json(json)
# print the JSON string representation of the object
print(RetrieveASubscriptionResponse.to_json())

# convert the object into a dict
retrieve_a_subscription_response_dict = retrieve_a_subscription_response_instance.to_dict()
# create an instance of RetrieveASubscriptionResponse from a dict
retrieve_a_subscription_response_from_dict = RetrieveASubscriptionResponse.from_dict(retrieve_a_subscription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


