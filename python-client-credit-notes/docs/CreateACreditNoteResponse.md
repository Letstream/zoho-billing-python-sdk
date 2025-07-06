# CreateACreditNoteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**credit_note** | [**CreditNoteResponse**](CreditNoteResponse.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_credit_notes.models.create_a_credit_note_response import CreateACreditNoteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateACreditNoteResponse from a JSON string
create_a_credit_note_response_instance = CreateACreditNoteResponse.from_json(json)
# print the JSON string representation of the object
print(CreateACreditNoteResponse.to_json())

# convert the object into a dict
create_a_credit_note_response_dict = create_a_credit_note_response_instance.to_dict()
# create an instance of CreateACreditNoteResponse from a dict
create_a_credit_note_response_from_dict = CreateACreditNoteResponse.from_dict(create_a_credit_note_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


