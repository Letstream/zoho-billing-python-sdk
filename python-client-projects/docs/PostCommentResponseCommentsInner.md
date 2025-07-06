# PostCommentResponseCommentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | Unoque ID of the project | [optional] 
**comment_id** | **str** | Unique ID of the project | [optional] 
**description** | **str** | Project Description - A short note on the project details | [optional] 
**commented_by_id** | **str** | Sort comment by ID of individual | [optional] 
**commented_by** | **str** | Name of the individual who added comment | [optional] 
**var_date** | **str** | Date of the comment | [optional] 
**date_description** | **str** | Number of days since the comment was made | [optional] 
**time** | **str** | Time of the comment | [optional] 

## Example

```python
from ls_zoho_billing_projects.models.post_comment_response_comments_inner import PostCommentResponseCommentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostCommentResponseCommentsInner from a JSON string
post_comment_response_comments_inner_instance = PostCommentResponseCommentsInner.from_json(json)
# print the JSON string representation of the object
print(PostCommentResponseCommentsInner.to_json())

# convert the object into a dict
post_comment_response_comments_inner_dict = post_comment_response_comments_inner_instance.to_dict()
# create an instance of PostCommentResponseCommentsInner from a dict
post_comment_response_comments_inner_from_dict = PostCommentResponseCommentsInner.from_dict(post_comment_response_comments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


