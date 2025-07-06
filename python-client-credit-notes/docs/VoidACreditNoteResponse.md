# VoidACreditNoteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_credit_notes.models.void_a_credit_note_response import VoidACreditNoteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VoidACreditNoteResponse from a JSON string
void_a_credit_note_response_instance = VoidACreditNoteResponse.from_json(json)
# print the JSON string representation of the object
print(VoidACreditNoteResponse.to_json())

# convert the object into a dict
void_a_credit_note_response_dict = void_a_credit_note_response_instance.to_dict()
# create an instance of VoidACreditNoteResponse from a dict
void_a_credit_note_response_from_dict = VoidACreditNoteResponse.from_dict(void_a_credit_note_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


