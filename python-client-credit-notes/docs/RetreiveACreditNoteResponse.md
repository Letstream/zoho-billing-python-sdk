# RetreiveACreditNoteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**credit_note** | [**RetreiveACreditNoteResponseCreditNote**](RetreiveACreditNoteResponseCreditNote.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_credit_notes.models.retreive_a_credit_note_response import RetreiveACreditNoteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RetreiveACreditNoteResponse from a JSON string
retreive_a_credit_note_response_instance = RetreiveACreditNoteResponse.from_json(json)
# print the JSON string representation of the object
print(RetreiveACreditNoteResponse.to_json())

# convert the object into a dict
retreive_a_credit_note_response_dict = retreive_a_credit_note_response_instance.to_dict()
# create an instance of RetreiveACreditNoteResponse from a dict
retreive_a_credit_note_response_from_dict = RetreiveACreditNoteResponse.from_dict(retreive_a_credit_note_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


