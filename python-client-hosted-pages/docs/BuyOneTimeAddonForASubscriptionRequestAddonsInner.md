# BuyOneTimeAddonForASubscriptionRequestAddonsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_code** | **str** | Addon code of the addon. | 
**quantity** | **int** | Required quantity of the chosen plan. | [optional] 
**tags** | [**List[TagsInner]**](TagsInner.md) |  | [optional] 
**item_custom_fields** | [**List[ItemCustomFieldsInner]**](ItemCustomFieldsInner.md) | Custom fields for a item. | [optional] 
**price** | **float** | Price of a plan for a particular subscription. If a value is provided here, the plan’s price for this subscription will be changed to the given value. If no value is provided, the plan’s price would be the same as what it was when it was created. | [optional] 
**tax_id** | **object** | Unique ID of Tax or Tax Group that must be associated with the addon. &lt;code&gt;tax_id&lt;/code&gt; must be empty for applying tax Exemption. | 
**tax_exemption_id** | **str** | Unique ID of the tax exemption. | [optional] 
**tax_exemption_code** | **str** | Unique code of the tax exemption. | [optional] 
**product_type** | **str** | Product type for UK Edition. | [optional] 

## Example

```python
from ls_zoho_billing_hosted_pages.models.buy_one_time_addon_for_a_subscription_request_addons_inner import BuyOneTimeAddonForASubscriptionRequestAddonsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BuyOneTimeAddonForASubscriptionRequestAddonsInner from a JSON string
buy_one_time_addon_for_a_subscription_request_addons_inner_instance = BuyOneTimeAddonForASubscriptionRequestAddonsInner.from_json(json)
# print the JSON string representation of the object
print(BuyOneTimeAddonForASubscriptionRequestAddonsInner.to_json())

# convert the object into a dict
buy_one_time_addon_for_a_subscription_request_addons_inner_dict = buy_one_time_addon_for_a_subscription_request_addons_inner_instance.to_dict()
# create an instance of BuyOneTimeAddonForASubscriptionRequestAddonsInner from a dict
buy_one_time_addon_for_a_subscription_request_addons_inner_from_dict = BuyOneTimeAddonForASubscriptionRequestAddonsInner.from_dict(buy_one_time_addon_for_a_subscription_request_addons_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


