# AssignUsersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**users** | [**List[AssignUsersResponseUsersInner]**](AssignUsersResponseUsersInner.md) | Users of a project | [optional] 

## Example

```python
from ls_zoho_billing_projects.models.assign_users_response import AssignUsersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssignUsersResponse from a JSON string
assign_users_response_instance = AssignUsersResponse.from_json(json)
# print the JSON string representation of the object
print(AssignUsersResponse.to_json())

# convert the object into a dict
assign_users_response_dict = assign_users_response_instance.to_dict()
# create an instance of AssignUsersResponse from a dict
assign_users_response_from_dict = AssignUsersResponse.from_dict(assign_users_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


