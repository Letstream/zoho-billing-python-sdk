# DeleteAnAttachmentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_invoices.models.delete_an_attachment_response import DeleteAnAttachmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAnAttachmentResponse from a JSON string
delete_an_attachment_response_instance = DeleteAnAttachmentResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteAnAttachmentResponse.to_json())

# convert the object into a dict
delete_an_attachment_response_dict = delete_an_attachment_response_instance.to_dict()
# create an instance of DeleteAnAttachmentResponse from a dict
delete_an_attachment_response_from_dict = DeleteAnAttachmentResponse.from_dict(delete_an_attachment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


