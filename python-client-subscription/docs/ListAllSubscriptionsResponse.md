# ListAllSubscriptionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**subscriptions** | [**List[ListAllSubscriptionsResponseSubscriptionsInner]**](ListAllSubscriptionsResponseSubscriptionsInner.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_subscription.models.list_all_subscriptions_response import ListAllSubscriptionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListAllSubscriptionsResponse from a JSON string
list_all_subscriptions_response_instance = ListAllSubscriptionsResponse.from_json(json)
# print the JSON string representation of the object
print(ListAllSubscriptionsResponse.to_json())

# convert the object into a dict
list_all_subscriptions_response_dict = list_all_subscriptions_response_instance.to_dict()
# create an instance of ListAllSubscriptionsResponse from a dict
list_all_subscriptions_response_from_dict = ListAllSubscriptionsResponse.from_dict(list_all_subscriptions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


