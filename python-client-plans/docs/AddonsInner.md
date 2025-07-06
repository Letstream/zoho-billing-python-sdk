# AddonsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_code** | **str** | The addon code of the addon which is associated with the plan . | [optional] 
**name** | **object** | The name of the addon. | [optional] 

## Example

```python
from ls_zoho_billing_plans.models.addons_inner import AddonsInner

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


