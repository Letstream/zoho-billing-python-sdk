# BuyOneTimeAddonRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addons** | [**List[BuyOneTimeAddonRequestAddonsInner]**](BuyOneTimeAddonRequestAddonsInner.md) | List of addon objects which are to be included in the subscription. Each object contains &lt;code&gt;addon_code&lt;/code&gt;, &lt;code&gt;name&lt;/code&gt;, &lt;code&gt;price&lt;/code&gt; and &lt;code&gt;quantity&lt;/code&gt;. | 
**exchange_rate** | **float** | This will be the exchange rate provided for the organization&#39;s currency and the customer&#39;s currency. The subscription fee would be the multiplicative product of the original price and the exchange rate. | [optional] 
**coupon_code** | **object** | The coupon code of the coupon which is to be applied to the one-time addon. | [optional] 
**add_to_unbilled_charges** | **bool** | When the value is given as true, the charges for the add-on will be put as unbilled. If the subscription already has unbilled-charges, this will be added as another line item to it. The unbilled charge can be converted to invoice at any later point of time. | [optional] 

## Example

```python
from ls_zoho_billing_subscription.models.buy_one_time_addon_request import BuyOneTimeAddonRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BuyOneTimeAddonRequest from a JSON string
buy_one_time_addon_request_instance = BuyOneTimeAddonRequest.from_json(json)
# print the JSON string representation of the object
print(BuyOneTimeAddonRequest.to_json())

# convert the object into a dict
buy_one_time_addon_request_dict = buy_one_time_addon_request_instance.to_dict()
# create an instance of BuyOneTimeAddonRequest from a dict
buy_one_time_addon_request_from_dict = BuyOneTimeAddonRequest.from_dict(buy_one_time_addon_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


