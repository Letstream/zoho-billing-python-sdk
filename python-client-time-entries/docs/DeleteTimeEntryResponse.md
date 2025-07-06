# DeleteTimeEntryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_time_entries.models.delete_time_entry_response import DeleteTimeEntryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteTimeEntryResponse from a JSON string
delete_time_entry_response_instance = DeleteTimeEntryResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteTimeEntryResponse.to_json())

# convert the object into a dict
delete_time_entry_response_dict = delete_time_entry_response_instance.to_dict()
# create an instance of DeleteTimeEntryResponse from a dict
delete_time_entry_response_from_dict = DeleteTimeEntryResponse.from_dict(delete_time_entry_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


