# CreateAnAddonRequestOneOfPlansInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_code** | **str** | The plan code of the plan to which the addon is to be applied. | [optional] 

## Example

```python
from ls_zoho_billing_addons.models.create_an_addon_request_one_of_plans_inner import CreateAnAddonRequestOneOfPlansInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAnAddonRequestOneOfPlansInner from a JSON string
create_an_addon_request_one_of_plans_inner_instance = CreateAnAddonRequestOneOfPlansInner.from_json(json)
# print the JSON string representation of the object
print(CreateAnAddonRequestOneOfPlansInner.to_json())

# convert the object into a dict
create_an_addon_request_one_of_plans_inner_dict = create_an_addon_request_one_of_plans_inner_instance.to_dict()
# create an instance of CreateAnAddonRequestOneOfPlansInner from a dict
create_an_addon_request_one_of_plans_inner_from_dict = CreateAnAddonRequestOneOfPlansInner.from_dict(create_an_addon_request_one_of_plans_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


