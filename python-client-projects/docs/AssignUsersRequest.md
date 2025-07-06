# AssignUsersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | ID of the user to be added to the project. | 
**rate** | **float** | Total project cost | [optional] 
**budget_hours** | **str** | Planned hours for completion of project | [optional] 

## Example

```python
from ls_zoho_billing_projects.models.assign_users_request import AssignUsersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssignUsersRequest from a JSON string
assign_users_request_instance = AssignUsersRequest.from_json(json)
# print the JSON string representation of the object
print(AssignUsersRequest.to_json())

# convert the object into a dict
assign_users_request_dict = assign_users_request_instance.to_dict()
# create an instance of AssignUsersRequest from a dict
assign_users_request_from_dict = AssignUsersRequest.from_dict(assign_users_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


