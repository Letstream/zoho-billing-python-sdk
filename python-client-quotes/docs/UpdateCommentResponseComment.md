# UpdateCommentResponseComment

Comment on the quote

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment_id** | **str** | The ID of the comment | [optional] 
**estimate_id** | **str** | The  unique id of a particular quote | [optional] 
**description** | **str** | The description of the line items | [optional] 
**commented_by_id** | **str** | Comment by comment ID | [optional] 
**commented_by** | **str** | Name of the person who has commented | [optional] 
**var_date** | **str** | Date on the quote. | [optional] 
**date_description** | **str** | Number of days since the comment has been made | [optional] 
**time** | **str** | time when quote was created | [optional] 
**comment_type** | **str** | Type of comment made | [optional] 

## Example

```python
from ls_zoho_billing_quotes.models.update_comment_response_comment import UpdateCommentResponseComment

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCommentResponseComment from a JSON string
update_comment_response_comment_instance = UpdateCommentResponseComment.from_json(json)
# print the JSON string representation of the object
print(UpdateCommentResponseComment.to_json())

# convert the object into a dict
update_comment_response_comment_dict = update_comment_response_comment_instance.to_dict()
# create an instance of UpdateCommentResponseComment from a dict
update_comment_response_comment_from_dict = UpdateCommentResponseComment.from_dict(update_comment_response_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


