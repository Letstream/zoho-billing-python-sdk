# AddCommentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_quotes.models.add_comments_response import AddCommentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddCommentsResponse from a JSON string
add_comments_response_instance = AddCommentsResponse.from_json(json)
# print the JSON string representation of the object
print(AddCommentsResponse.to_json())

# convert the object into a dict
add_comments_response_dict = add_comments_response_instance.to_dict()
# create an instance of AddCommentsResponse from a dict
add_comments_response_from_dict = AddCommentsResponse.from_dict(add_comments_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


