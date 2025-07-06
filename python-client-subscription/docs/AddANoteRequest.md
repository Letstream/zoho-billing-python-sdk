# AddANoteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **object** | Small description about the note. | [optional] 

## Example

```python
from ls_zoho_billing_subscription.models.add_a_note_request import AddANoteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddANoteRequest from a JSON string
add_a_note_request_instance = AddANoteRequest.from_json(json)
# print the JSON string representation of the object
print(AddANoteRequest.to_json())

# convert the object into a dict
add_a_note_request_dict = add_a_note_request_instance.to_dict()
# create an instance of AddANoteRequest from a dict
add_a_note_request_from_dict = AddANoteRequest.from_dict(add_a_note_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


