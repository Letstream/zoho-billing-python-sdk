# AddonResponseCustomFieldsInner


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
from openapi_client.models.addon_response_custom_fields_inner import AddonResponseCustomFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AddonResponseCustomFieldsInner from a JSON string
addon_response_custom_fields_inner_instance = AddonResponseCustomFieldsInner.from_json(json)
# print the JSON string representation of the object
print(AddonResponseCustomFieldsInner.to_json())

# convert the object into a dict
addon_response_custom_fields_inner_dict = addon_response_custom_fields_inner_instance.to_dict()
# create an instance of AddonResponseCustomFieldsInner from a dict
addon_response_custom_fields_inner_from_dict = AddonResponseCustomFieldsInner.from_dict(addon_response_custom_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


