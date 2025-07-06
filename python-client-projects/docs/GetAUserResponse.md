# GetAUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**users** | [**GetAUserResponseUsers**](GetAUserResponseUsers.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_projects.models.get_a_user_response import GetAUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAUserResponse from a JSON string
get_a_user_response_instance = GetAUserResponse.from_json(json)
# print the JSON string representation of the object
print(GetAUserResponse.to_json())

# convert the object into a dict
get_a_user_response_dict = get_a_user_response_instance.to_dict()
# create an instance of GetAUserResponse from a dict
get_a_user_response_from_dict = GetAUserResponse.from_dict(get_a_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


