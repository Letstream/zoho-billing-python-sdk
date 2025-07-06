# DeleteASubscriptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_subscription.models.delete_a_subscription_response import DeleteASubscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteASubscriptionResponse from a JSON string
delete_a_subscription_response_instance = DeleteASubscriptionResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteASubscriptionResponse.to_json())

# convert the object into a dict
delete_a_subscription_response_dict = delete_a_subscription_response_instance.to_dict()
# create an instance of DeleteASubscriptionResponse from a dict
delete_a_subscription_response_from_dict = DeleteASubscriptionResponse.from_dict(delete_a_subscription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


