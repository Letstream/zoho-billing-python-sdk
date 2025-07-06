# AddonResponsePriceBracketsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_quantity** | **int** | Lower limit of the addon range. | [optional] 
**end_quantity** | **int** | Upper limit of the addon range. | [optional] 
**price** | **float** | Per unit cost of the addon for the selected range. For the “package” pricing scheme, this would be the price of the specified quantity of addons. | [optional] 

## Example

```python
from ls_zoho_billing_addons.models.addon_response_price_brackets_inner import AddonResponsePriceBracketsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AddonResponsePriceBracketsInner from a JSON string
addon_response_price_brackets_inner_instance = AddonResponsePriceBracketsInner.from_json(json)
# print the JSON string representation of the object
print(AddonResponsePriceBracketsInner.to_json())

# convert the object into a dict
addon_response_price_brackets_inner_dict = addon_response_price_brackets_inner_instance.to_dict()
# create an instance of AddonResponsePriceBracketsInner from a dict
addon_response_price_brackets_inner_from_dict = AddonResponsePriceBracketsInner.from_dict(addon_response_price_brackets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


