# AddANoteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**note** | [**AddANoteResponseNote**](AddANoteResponseNote.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_subscription.models.add_a_note_response import AddANoteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddANoteResponse from a JSON string
add_a_note_response_instance = AddANoteResponse.from_json(json)
# print the JSON string representation of the object
print(AddANoteResponse.to_json())

# convert the object into a dict
add_a_note_response_dict = add_a_note_response_instance.to_dict()
# create an instance of AddANoteResponse from a dict
add_a_note_response_from_dict = AddANoteResponse.from_dict(add_a_note_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


