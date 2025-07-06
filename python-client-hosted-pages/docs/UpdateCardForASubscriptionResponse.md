# UpdateCardForASubscriptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**hostedpage** | [**UpdateCardForASubscriptionResponseHostedpage**](UpdateCardForASubscriptionResponseHostedpage.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_hosted_pages.models.update_card_for_a_subscription_response import UpdateCardForASubscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCardForASubscriptionResponse from a JSON string
update_card_for_a_subscription_response_instance = UpdateCardForASubscriptionResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateCardForASubscriptionResponse.to_json())

# convert the object into a dict
update_card_for_a_subscription_response_dict = update_card_for_a_subscription_response_instance.to_dict()
# create an instance of UpdateCardForASubscriptionResponse from a dict
update_card_for_a_subscription_response_from_dict = UpdateCardForASubscriptionResponse.from_dict(update_card_for_a_subscription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


