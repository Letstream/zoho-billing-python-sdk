# AddANoteResponseNote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notes** | [**List[SubscriptionResponseNotesInner]**](SubscriptionResponseNotesInner.md) | List of objects containing &lt;code&gt;note_id&lt;/code&gt;, &lt;code&gt;description&lt;/code&gt;, &lt;code&gt;commented_by&lt;/code&gt; and &lt;code&gt;commented_time&lt;/code&gt; | [optional] 

## Example

```python
from ls_zoho_billing_subscription.models.add_a_note_response_note import AddANoteResponseNote

# TODO update the JSON string below
json = "{}"
# create an instance of AddANoteResponseNote from a JSON string
add_a_note_response_note_instance = AddANoteResponseNote.from_json(json)
# print the JSON string representation of the object
print(AddANoteResponseNote.to_json())

# convert the object into a dict
add_a_note_response_note_dict = add_a_note_response_note_instance.to_dict()
# create an instance of AddANoteResponseNote from a dict
add_a_note_response_note_from_dict = AddANoteResponseNote.from_dict(add_a_note_response_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


