# NotesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note_id** | **str** | Unique ID generated for a note. | [optional] 
**description** | **object** | Comments about the subscription made by the user. | [optional] 
**commented_by** | **str** | Name of the user who added the comment. | [optional] 
**commented_time** | **str** | Time at which the comment was added. | [optional] 

## Example

```python
from ls_zoho_billing_hosted_pages.models.notes_inner import NotesInner

# TODO update the JSON string below
json = "{}"
# create an instance of NotesInner from a JSON string
notes_inner_instance = NotesInner.from_json(json)
# print the JSON string representation of the object
print(NotesInner.to_json())

# convert the object into a dict
notes_inner_dict = notes_inner_instance.to_dict()
# create an instance of NotesInner from a dict
notes_inner_from_dict = NotesInner.from_dict(notes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


