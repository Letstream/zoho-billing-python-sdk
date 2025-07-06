# UpdateAnAddonRequestPriceBracketsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_quantity** | **int** | Lower limit of the addon range. | 
**end_quantity** | **int** | Upper limit of the addon range. | 
**price** | **float** | Per unit cost of the addon for the selected range. For the “package” pricing scheme, this would be the price of the specified quantity of addons. | 

## Example

```python
from openapi_client.models.update_an_addon_request_price_brackets_inner import UpdateAnAddonRequestPriceBracketsInner

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAnAddonRequestPriceBracketsInner from a JSON string
update_an_addon_request_price_brackets_inner_instance = UpdateAnAddonRequestPriceBracketsInner.from_json(json)
# print the JSON string representation of the object
print(UpdateAnAddonRequestPriceBracketsInner.to_json())

# convert the object into a dict
update_an_addon_request_price_brackets_inner_dict = update_an_addon_request_price_brackets_inner_instance.to_dict()
# create an instance of UpdateAnAddonRequestPriceBracketsInner from a dict
update_an_addon_request_price_brackets_inner_from_dict = UpdateAnAddonRequestPriceBracketsInner.from_dict(update_an_addon_request_price_brackets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


