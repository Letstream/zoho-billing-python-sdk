# AddonResponsePlansInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_code** | **str** | The plan code of the plan to which the addon is to be applied. | [optional] 
**name** | **object** | The name of the plan. | [optional] 

## Example

```python
from openapi_client.models.addon_response_plans_inner import AddonResponsePlansInner

# TODO update the JSON string below
json = "{}"
# create an instance of AddonResponsePlansInner from a JSON string
addon_response_plans_inner_instance = AddonResponsePlansInner.from_json(json)
# print the JSON string representation of the object
print(AddonResponsePlansInner.to_json())

# convert the object into a dict
addon_response_plans_inner_dict = addon_response_plans_inner_instance.to_dict()
# create an instance of AddonResponsePlansInner from a dict
addon_response_plans_inner_from_dict = AddonResponsePlansInner.from_dict(addon_response_plans_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


