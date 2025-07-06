# PlanResponseCustomFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customfield_id** | **str** |  | [optional] 
**is_active** | **str** |  | [optional] 
**show_in_all_pdf** | **str** |  | [optional] 
**value_formatted** | **str** |  | [optional] 
**data_type** | **str** |  | [optional] 
**index** | **int** |  | [optional] 
**label** | **str** | Label of the Custom Field | [optional] 
**show_on_pdf** | **str** |  | [optional] 
**placeholder** | **str** |  | [optional] 
**value** | **str** | Value of the Custom Field | [optional] 

## Example

```python
from ls_zoho_billing_plans.models.plan_response_custom_fields_inner import PlanResponseCustomFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PlanResponseCustomFieldsInner from a JSON string
plan_response_custom_fields_inner_instance = PlanResponseCustomFieldsInner.from_json(json)
# print the JSON string representation of the object
print(PlanResponseCustomFieldsInner.to_json())

# convert the object into a dict
plan_response_custom_fields_inner_dict = plan_response_custom_fields_inner_instance.to_dict()
# create an instance of PlanResponseCustomFieldsInner from a dict
plan_response_custom_fields_inner_from_dict = PlanResponseCustomFieldsInner.from_dict(plan_response_custom_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


