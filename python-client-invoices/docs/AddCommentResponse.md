# AddCommentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_invoices.models.add_comment_response import AddCommentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddCommentResponse from a JSON string
add_comment_response_instance = AddCommentResponse.from_json(json)
# print the JSON string representation of the object
print(AddCommentResponse.to_json())

# convert the object into a dict
add_comment_response_dict = add_comment_response_instance.to_dict()
# create an instance of AddCommentResponse from a dict
add_comment_response_from_dict = AddCommentResponse.from_dict(add_comment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


