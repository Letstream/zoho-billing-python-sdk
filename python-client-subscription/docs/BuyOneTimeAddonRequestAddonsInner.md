# BuyOneTimeAddonRequestAddonsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_code** | **str** | Addon code of the addon. | 
**quantity** | **int** | Required quantity of the chosen addon. | [optional] 
**tags** | [**List[TagsInner]**](TagsInner.md) |  | [optional] 
**item_custom_fields** | [**List[ItemCustomFieldsInner]**](ItemCustomFieldsInner.md) | Custom fields for a item. | [optional] 
**price** | **float** | A value can be provided here if the per unit addon price has to be overridden for this subscription. | [optional] 
**tax_id** | **object** | Unique ID of Tax or Tax Group that must be associated with the addon. &lt;code&gt;tax_id&lt;/code&gt; must be empty for applying tax Exemption. | 
**tax_exemption_id** | **object** | Unique ID of the tax exemption applied for the addon. To apply tax exemption also include tax_id as empty string. | [optional] 
**tax_exemption_code** | **object** | Unique Code of the tax exemption applied for the addon. To apply tax exemption also include tax_id as empty string. | [optional] 
**product_type** | **str** | Product type for UK Edition. | [optional] 

## Example

```python
from ls_zoho_billing_subscription.models.buy_one_time_addon_request_addons_inner import BuyOneTimeAddonRequestAddonsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BuyOneTimeAddonRequestAddonsInner from a JSON string
buy_one_time_addon_request_addons_inner_instance = BuyOneTimeAddonRequestAddonsInner.from_json(json)
# print the JSON string representation of the object
print(BuyOneTimeAddonRequestAddonsInner.to_json())

# convert the object into a dict
buy_one_time_addon_request_addons_inner_dict = buy_one_time_addon_request_addons_inner_instance.to_dict()
# create an instance of BuyOneTimeAddonRequestAddonsInner from a dict
buy_one_time_addon_request_addons_inner_from_dict = BuyOneTimeAddonRequestAddonsInner.from_dict(buy_one_time_addon_request_addons_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


