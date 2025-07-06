# BuyOneTimeAddonForASubscriptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**hostedpage** | [**BuyOneTimeAddonForASubscriptionResponseHostedpage**](BuyOneTimeAddonForASubscriptionResponseHostedpage.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_hosted_pages.models.buy_one_time_addon_for_a_subscription_response import BuyOneTimeAddonForASubscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BuyOneTimeAddonForASubscriptionResponse from a JSON string
buy_one_time_addon_for_a_subscription_response_instance = BuyOneTimeAddonForASubscriptionResponse.from_json(json)
# print the JSON string representation of the object
print(BuyOneTimeAddonForASubscriptionResponse.to_json())

# convert the object into a dict
buy_one_time_addon_for_a_subscription_response_dict = buy_one_time_addon_for_a_subscription_response_instance.to_dict()
# create an instance of BuyOneTimeAddonForASubscriptionResponse from a dict
buy_one_time_addon_for_a_subscription_response_from_dict = BuyOneTimeAddonForASubscriptionResponse.from_dict(buy_one_time_addon_for_a_subscription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


