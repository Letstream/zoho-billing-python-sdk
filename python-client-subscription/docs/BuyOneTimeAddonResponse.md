# BuyOneTimeAddonResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**invoice** | [**BuyOneTimeAddonResponseInvoice**](BuyOneTimeAddonResponseInvoice.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_subscription.models.buy_one_time_addon_response import BuyOneTimeAddonResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BuyOneTimeAddonResponse from a JSON string
buy_one_time_addon_response_instance = BuyOneTimeAddonResponse.from_json(json)
# print the JSON string representation of the object
print(BuyOneTimeAddonResponse.to_json())

# convert the object into a dict
buy_one_time_addon_response_dict = buy_one_time_addon_response_instance.to_dict()
# create an instance of BuyOneTimeAddonResponse from a dict
buy_one_time_addon_response_from_dict = BuyOneTimeAddonResponse.from_dict(buy_one_time_addon_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


