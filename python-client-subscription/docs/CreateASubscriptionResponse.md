# CreateASubscriptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**subscription** | [**SubscriptionResponse**](SubscriptionResponse.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_subscription.models.create_a_subscription_response import CreateASubscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateASubscriptionResponse from a JSON string
create_a_subscription_response_instance = CreateASubscriptionResponse.from_json(json)
# print the JSON string representation of the object
print(CreateASubscriptionResponse.to_json())

# convert the object into a dict
create_a_subscription_response_dict = create_a_subscription_response_instance.to_dict()
# create an instance of CreateASubscriptionResponse from a dict
create_a_subscription_response_from_dict = CreateASubscriptionResponse.from_dict(create_a_subscription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


