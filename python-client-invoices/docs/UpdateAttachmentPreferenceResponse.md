# UpdateAttachmentPreferenceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_invoices.models.update_attachment_preference_response import UpdateAttachmentPreferenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAttachmentPreferenceResponse from a JSON string
update_attachment_preference_response_instance = UpdateAttachmentPreferenceResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateAttachmentPreferenceResponse.to_json())

# convert the object into a dict
update_attachment_preference_response_dict = update_attachment_preference_response_instance.to_dict()
# create an instance of UpdateAttachmentPreferenceResponse from a dict
update_attachment_preference_response_from_dict = UpdateAttachmentPreferenceResponse.from_dict(update_attachment_preference_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


