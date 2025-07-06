# EmailACreditNoteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to_mail_ids** | **List[str]** | The email IDs to which the credit note is to be mailed. | 
**cc_mail_ids** | **List[str]** | The email IDs that have to be copied when the credit note is to be mailed. | [optional] 
**subject** | **str** | The subject of the email. | 
**body** | **str** | The body of the email. | 

## Example

```python
from ls_zoho_billing_credit_notes.models.email_a_credit_note_request import EmailACreditNoteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmailACreditNoteRequest from a JSON string
email_a_credit_note_request_instance = EmailACreditNoteRequest.from_json(json)
# print the JSON string representation of the object
print(EmailACreditNoteRequest.to_json())

# convert the object into a dict
email_a_credit_note_request_dict = email_a_credit_note_request_instance.to_dict()
# create an instance of EmailACreditNoteRequest from a dict
email_a_credit_note_request_from_dict = EmailACreditNoteRequest.from_dict(email_a_credit_note_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


