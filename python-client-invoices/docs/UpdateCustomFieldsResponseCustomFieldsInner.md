# UpdateCustomFieldsResponseCustomFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customfield_id** | **int** |  | [optional] 
**show_in_store** | **bool** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**index** | **int** |  | [optional] 
**show_in_hp** | **bool** |  | [optional] 
**is_mandatory** | **bool** |  | [optional] 
**label** | **str** |  | [optional] 
**is_custom_field** | **bool** |  | [optional] 
**is_mandatory_in_sales_item** | **bool** |  | [optional] 
**is_mandatory_in_hp** | **bool** |  | [optional] 
**edit_on_store** | **bool** |  | [optional] 
**show_in_all_pdf** | **bool** |  | [optional] 
**search_entity** | **str** |  | [optional] 
**data_type** | **str** |  | [optional] 
**pii_type** | **str** |  | [optional] 
**placeholder** | **str** |  | [optional] 
**is_inherited_value** | **bool** |  | [optional] 
**value** | **str** |  | [optional] 
**is_dependent_field** | **bool** |  | [optional] 
**max_length** | **int** |  | [optional] 
**help_text** | **str** |  | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.update_custom_fields_response_custom_fields_inner import UpdateCustomFieldsResponseCustomFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCustomFieldsResponseCustomFieldsInner from a JSON string
update_custom_fields_response_custom_fields_inner_instance = UpdateCustomFieldsResponseCustomFieldsInner.from_json(json)
# print the JSON string representation of the object
print(UpdateCustomFieldsResponseCustomFieldsInner.to_json())

# convert the object into a dict
update_custom_fields_response_custom_fields_inner_dict = update_custom_fields_response_custom_fields_inner_instance.to_dict()
# create an instance of UpdateCustomFieldsResponseCustomFieldsInner from a dict
update_custom_fields_response_custom_fields_inner_from_dict = UpdateCustomFieldsResponseCustomFieldsInner.from_dict(update_custom_fields_response_custom_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


