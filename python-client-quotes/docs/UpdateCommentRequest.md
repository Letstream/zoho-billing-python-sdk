# UpdateCommentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A short note on the quote | [optional] 
**show_comment_to_clients** | **bool** | Boolean to show the comments to contacts in portal. | [optional] 

## Example

```python
from ls_zoho_billing_quotes.models.update_comment_request import UpdateCommentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCommentRequest from a JSON string
update_comment_request_instance = UpdateCommentRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateCommentRequest.to_json())

# convert the object into a dict
update_comment_request_dict = update_comment_request_instance.to_dict()
# create an instance of UpdateCommentRequest from a dict
update_comment_request_from_dict = UpdateCommentRequest.from_dict(update_comment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


