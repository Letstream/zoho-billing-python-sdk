# DeleteANoteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_subscription.models.delete_a_note_response import DeleteANoteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteANoteResponse from a JSON string
delete_a_note_response_instance = DeleteANoteResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteANoteResponse.to_json())

# convert the object into a dict
delete_a_note_response_dict = delete_a_note_response_instance.to_dict()
# create an instance of DeleteANoteResponse from a dict
delete_a_note_response_from_dict = DeleteANoteResponse.from_dict(delete_a_note_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


