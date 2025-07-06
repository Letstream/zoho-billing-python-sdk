# PostCommentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Project description. &lt;code&gt;Maximum length [500]&lt;/code&gt; | 

## Example

```python
from ls_zoho_billing_projects.models.post_comment_request import PostCommentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostCommentRequest from a JSON string
post_comment_request_instance = PostCommentRequest.from_json(json)
# print the JSON string representation of the object
print(PostCommentRequest.to_json())

# convert the object into a dict
post_comment_request_dict = post_comment_request_instance.to_dict()
# create an instance of PostCommentRequest from a dict
post_comment_request_from_dict = PostCommentRequest.from_dict(post_comment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


