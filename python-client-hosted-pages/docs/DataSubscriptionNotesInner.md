# DataSubscriptionNotesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note_id** | **str** | Unique ID generated for a note. | [optional] 
**description** | **str** | Comments about the subscription made by the user. | [optional] 
**commented_by** | **str** | Name of the user who added the comment. | [optional] 
**commented_time** | **str** | Time at which the comment was added. | [optional] 

## Example

```python
from ls_zoho_billing_hosted_pages.models.data_subscription_notes_inner import DataSubscriptionNotesInner

# TODO update the JSON string below
json = "{}"
# create an instance of DataSubscriptionNotesInner from a JSON string
data_subscription_notes_inner_instance = DataSubscriptionNotesInner.from_json(json)
# print the JSON string representation of the object
print(DataSubscriptionNotesInner.to_json())

# convert the object into a dict
data_subscription_notes_inner_dict = data_subscription_notes_inner_instance.to_dict()
# create an instance of DataSubscriptionNotesInner from a dict
data_subscription_notes_inner_from_dict = DataSubscriptionNotesInner.from_dict(data_subscription_notes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


