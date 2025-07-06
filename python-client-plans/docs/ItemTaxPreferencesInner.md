# ItemTaxPreferencesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_specification** | **str** | Tax specification for the plan. It can be either &lt;code&gt;inter&lt;/code&gt; or &lt;code&gt;intra&lt;/code&gt;. | [optional] 
**tax_name** | **str** | Name of the tax to which subscription is associated. | [optional] 
**tax_percentage** | **float** | Percentage of tax applied to the plan/addon | [optional] 
**tax_id** | **str** | Tax ID to which you would like to associate with this plan. | [optional] [default to 'no tax will be associated']

## Example

```python
from ls_zoho_billing_plans.models.item_tax_preferences_inner import ItemTaxPreferencesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ItemTaxPreferencesInner from a JSON string
item_tax_preferences_inner_instance = ItemTaxPreferencesInner.from_json(json)
# print the JSON string representation of the object
print(ItemTaxPreferencesInner.to_json())

# convert the object into a dict
item_tax_preferences_inner_dict = item_tax_preferences_inner_instance.to_dict()
# create an instance of ItemTaxPreferencesInner from a dict
item_tax_preferences_inner_from_dict = ItemTaxPreferencesInner.from_dict(item_tax_preferences_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


