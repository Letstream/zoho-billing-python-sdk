# CreateAnAddonRequestOneOf2PriceBracketsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **float** | Per unit cost of the addon for the selected range. For the “package” pricing scheme, this would be the price of the specified quantity of addons. | [optional] 

## Example

```python
from ls_zoho_billing_addons.models.create_an_addon_request_one_of2_price_brackets_inner import CreateAnAddonRequestOneOf2PriceBracketsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAnAddonRequestOneOf2PriceBracketsInner from a JSON string
create_an_addon_request_one_of2_price_brackets_inner_instance = CreateAnAddonRequestOneOf2PriceBracketsInner.from_json(json)
# print the JSON string representation of the object
print(CreateAnAddonRequestOneOf2PriceBracketsInner.to_json())

# convert the object into a dict
create_an_addon_request_one_of2_price_brackets_inner_dict = create_an_addon_request_one_of2_price_brackets_inner_instance.to_dict()
# create an instance of CreateAnAddonRequestOneOf2PriceBracketsInner from a dict
create_an_addon_request_one_of2_price_brackets_inner_from_dict = CreateAnAddonRequestOneOf2PriceBracketsInner.from_dict(create_an_addon_request_one_of2_price_brackets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


