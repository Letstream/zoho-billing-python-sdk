# ListAllPlansResponsePlansInnerAddonsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_code** | **str** | The addon code of the addon which is associated with the plan . | [optional] 
**name** | **str** | Name of your choice to be displayed in the interface and invoices. | [optional] 

## Example

```python
from ls_zoho_billing_plans.models.list_all_plans_response_plans_inner_addons_inner import ListAllPlansResponsePlansInnerAddonsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListAllPlansResponsePlansInnerAddonsInner from a JSON string
list_all_plans_response_plans_inner_addons_inner_instance = ListAllPlansResponsePlansInnerAddonsInner.from_json(json)
# print the JSON string representation of the object
print(ListAllPlansResponsePlansInnerAddonsInner.to_json())

# convert the object into a dict
list_all_plans_response_plans_inner_addons_inner_dict = list_all_plans_response_plans_inner_addons_inner_instance.to_dict()
# create an instance of ListAllPlansResponsePlansInnerAddonsInner from a dict
list_all_plans_response_plans_inner_addons_inner_from_dict = ListAllPlansResponsePlansInnerAddonsInner.from_dict(list_all_plans_response_plans_inner_addons_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


