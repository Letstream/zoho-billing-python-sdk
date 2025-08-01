# AddonsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_code** | **str** | Addon code of the addon. | [optional] 
**name** | **object** | Name of the addon. | [optional] 
**addon_description** | **str** | Description of the addon exclusive to this subscription. This will be displayed in place of the addon name in invoices generated for this subscription. | [optional] 
**quantity** | **int** | Required quantity of the chosen addon. | [optional] [default to 1]
**price** | **float** | A value can be provided here if the per unit addon price has to be overridden for this subscription. | [optional] [default to 10]
**discount** | **str** | Discount applied for the addon. | [optional] 
**total** | **str** | Total amount for the addon. | [optional] 
**tax_id** | **str** | Unique ID of the tax applied for the addon. | [optional] 

## Example

```python
from ls_zoho_billing_subscription.models.addons_inner import AddonsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AddonsInner from a JSON string
addons_inner_instance = AddonsInner.from_json(json)
# print the JSON string representation of the object
print(AddonsInner.to_json())

# convert the object into a dict
addons_inner_dict = addons_inner_instance.to_dict()
# create an instance of AddonsInner from a dict
addons_inner_from_dict = AddonsInner.from_dict(addons_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


