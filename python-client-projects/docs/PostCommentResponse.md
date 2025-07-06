# PostCommentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**comments** | [**List[PostCommentResponseCommentsInner]**](PostCommentResponseCommentsInner.md) | A short noteon the project | [optional] 

## Example

```python
from ls_zoho_billing_projects.models.post_comment_response import PostCommentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostCommentResponse from a JSON string
post_comment_response_instance = PostCommentResponse.from_json(json)
# print the JSON string representation of the object
print(PostCommentResponse.to_json())

# convert the object into a dict
post_comment_response_dict = post_comment_response_instance.to_dict()
# create an instance of PostCommentResponse from a dict
post_comment_response_from_dict = PostCommentResponse.from_dict(post_comment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


