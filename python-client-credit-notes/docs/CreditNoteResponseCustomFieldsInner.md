# CreditNoteResponseCustomFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Index of the custom field. It can hold any value from 1 to 10. | [optional] 
**value** | **str** | Value of the Custom Field | [optional] 
**label** | **str** | Label of the Custom Field | [optional] 
**data_type** | **str** | Data type of the custom field. | [optional] 

## Example

```python
from ls_zoho_billing_credit_notes.models.credit_note_response_custom_fields_inner import CreditNoteResponseCustomFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreditNoteResponseCustomFieldsInner from a JSON string
credit_note_response_custom_fields_inner_instance = CreditNoteResponseCustomFieldsInner.from_json(json)
# print the JSON string representation of the object
print(CreditNoteResponseCustomFieldsInner.to_json())

# convert the object into a dict
credit_note_response_custom_fields_inner_dict = credit_note_response_custom_fields_inner_instance.to_dict()
# create an instance of CreditNoteResponseCustomFieldsInner from a dict
credit_note_response_custom_fields_inner_from_dict = CreditNoteResponseCustomFieldsInner.from_dict(credit_note_response_custom_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


