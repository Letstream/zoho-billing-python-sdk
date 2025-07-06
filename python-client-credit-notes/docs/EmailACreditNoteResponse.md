# EmailACreditNoteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_credit_notes.models.email_a_credit_note_response import EmailACreditNoteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmailACreditNoteResponse from a JSON string
email_a_credit_note_response_instance = EmailACreditNoteResponse.from_json(json)
# print the JSON string representation of the object
print(EmailACreditNoteResponse.to_json())

# convert the object into a dict
email_a_credit_note_response_dict = email_a_credit_note_response_instance.to_dict()
# create an instance of EmailACreditNoteResponse from a dict
email_a_credit_note_response_from_dict = EmailACreditNoteResponse.from_dict(email_a_credit_note_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


