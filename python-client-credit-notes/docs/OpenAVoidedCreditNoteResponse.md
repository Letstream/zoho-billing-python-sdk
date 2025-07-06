# OpenAVoidedCreditNoteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_credit_notes.models.open_a_voided_credit_note_response import OpenAVoidedCreditNoteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OpenAVoidedCreditNoteResponse from a JSON string
open_a_voided_credit_note_response_instance = OpenAVoidedCreditNoteResponse.from_json(json)
# print the JSON string representation of the object
print(OpenAVoidedCreditNoteResponse.to_json())

# convert the object into a dict
open_a_voided_credit_note_response_dict = open_a_voided_credit_note_response_instance.to_dict()
# create an instance of OpenAVoidedCreditNoteResponse from a dict
open_a_voided_credit_note_response_from_dict = OpenAVoidedCreditNoteResponse.from_dict(open_a_voided_credit_note_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


