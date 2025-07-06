# DeleteACreditNoteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_credit_notes.models.delete_a_credit_note_response import DeleteACreditNoteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteACreditNoteResponse from a JSON string
delete_a_credit_note_response_instance = DeleteACreditNoteResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteACreditNoteResponse.to_json())

# convert the object into a dict
delete_a_credit_note_response_dict = delete_a_credit_note_response_instance.to_dict()
# create an instance of DeleteACreditNoteResponse from a dict
delete_a_credit_note_response_from_dict = DeleteACreditNoteResponse.from_dict(delete_a_credit_note_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


