# PlanResponseTagsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_option_id** | **int** | Id of the Tag Option | [optional] 
**is_tag_mandatory** | **str** |  | [optional] 
**tag_name** | **str** |  | [optional] 
**tag_id** | **int** | ID of the Tag | [optional] 
**tag_option_name** | **str** |  | [optional] 

## Example

```python
from ls_zoho_billing_plans.models.plan_response_tags_inner import PlanResponseTagsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PlanResponseTagsInner from a JSON string
plan_response_tags_inner_instance = PlanResponseTagsInner.from_json(json)
# print the JSON string representation of the object
print(PlanResponseTagsInner.to_json())

# convert the object into a dict
plan_response_tags_inner_dict = plan_response_tags_inner_instance.to_dict()
# create an instance of PlanResponseTagsInner from a dict
plan_response_tags_inner_from_dict = PlanResponseTagsInner.from_dict(plan_response_tags_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


