# AddCommentsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A short note on the quote | [optional] 
**show_comment_to_clients** | **bool** | Boolean to show the comments to contacts in portal. | [optional] 

## Example

```python
from ls_zoho_billing_quotes.models.add_comments_request import AddCommentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddCommentsRequest from a JSON string
add_comments_request_instance = AddCommentsRequest.from_json(json)
# print the JSON string representation of the object
print(AddCommentsRequest.to_json())

# convert the object into a dict
add_comments_request_dict = add_comments_request_instance.to_dict()
# create an instance of AddCommentsRequest from a dict
add_comments_request_from_dict = AddCommentsRequest.from_dict(add_comments_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


