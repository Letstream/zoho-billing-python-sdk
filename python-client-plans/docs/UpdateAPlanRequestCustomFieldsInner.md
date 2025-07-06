# UpdateAPlanRequestCustomFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Label of the Custom Field | [optional] 
**value** | **str** | Value of the Custom Field | [optional] 

## Example

```python
from ls_zoho_billing_plans.models.update_a_plan_request_custom_fields_inner import UpdateAPlanRequestCustomFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAPlanRequestCustomFieldsInner from a JSON string
update_a_plan_request_custom_fields_inner_instance = UpdateAPlanRequestCustomFieldsInner.from_json(json)
# print the JSON string representation of the object
print(UpdateAPlanRequestCustomFieldsInner.to_json())

# convert the object into a dict
update_a_plan_request_custom_fields_inner_dict = update_a_plan_request_custom_fields_inner_instance.to_dict()
# create an instance of UpdateAPlanRequestCustomFieldsInner from a dict
update_a_plan_request_custom_fields_inner_from_dict = UpdateAPlanRequestCustomFieldsInner.from_dict(update_a_plan_request_custom_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


