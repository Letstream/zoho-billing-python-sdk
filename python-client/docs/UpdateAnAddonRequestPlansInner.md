# UpdateAnAddonRequestPlansInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_code** | **str** | The plan code of the plan to which the addon is to be applied. | 
**name** | **object** | The name of the plan. | [optional] 

## Example

```python
from openapi_client.models.update_an_addon_request_plans_inner import UpdateAnAddonRequestPlansInner

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAnAddonRequestPlansInner from a JSON string
update_an_addon_request_plans_inner_instance = UpdateAnAddonRequestPlansInner.from_json(json)
# print the JSON string representation of the object
print(UpdateAnAddonRequestPlansInner.to_json())

# convert the object into a dict
update_an_addon_request_plans_inner_dict = update_an_addon_request_plans_inner_instance.to_dict()
# create an instance of UpdateAnAddonRequestPlansInner from a dict
update_an_addon_request_plans_inner_from_dict = UpdateAnAddonRequestPlansInner.from_dict(update_an_addon_request_plans_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


