# DeleteCommentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_projects.models.delete_comment_response import DeleteCommentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteCommentResponse from a JSON string
delete_comment_response_instance = DeleteCommentResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteCommentResponse.to_json())

# convert the object into a dict
delete_comment_response_dict = delete_comment_response_instance.to_dict()
# create an instance of DeleteCommentResponse from a dict
delete_comment_response_from_dict = DeleteCommentResponse.from_dict(delete_comment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


