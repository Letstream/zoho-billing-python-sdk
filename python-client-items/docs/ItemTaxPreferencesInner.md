# ItemTaxPreferencesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_id** | **str** | ID of the tax to be associated to the item. | [optional] 
**tax_specification** | **str** | Set whether the tax type is intra/interstate | [optional] 

## Example

```python
from ls_zoho_billing_items.models.item_tax_preferences_inner import ItemTaxPreferencesInner

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


