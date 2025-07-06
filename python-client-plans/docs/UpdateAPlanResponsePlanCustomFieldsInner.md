# UpdateAPlanResponsePlanCustomFieldsInner


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
from ls_zoho_billing_plans.models.update_a_plan_response_plan_custom_fields_inner import UpdateAPlanResponsePlanCustomFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAPlanResponsePlanCustomFieldsInner from a JSON string
update_a_plan_response_plan_custom_fields_inner_instance = UpdateAPlanResponsePlanCustomFieldsInner.from_json(json)
# print the JSON string representation of the object
print(UpdateAPlanResponsePlanCustomFieldsInner.to_json())

# convert the object into a dict
update_a_plan_response_plan_custom_fields_inner_dict = update_a_plan_response_plan_custom_fields_inner_instance.to_dict()
# create an instance of UpdateAPlanResponsePlanCustomFieldsInner from a dict
update_a_plan_response_plan_custom_fields_inner_from_dict = UpdateAPlanResponsePlanCustomFieldsInner.from_dict(update_a_plan_response_plan_custom_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


