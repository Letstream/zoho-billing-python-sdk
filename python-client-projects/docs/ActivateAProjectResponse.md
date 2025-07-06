# ActivateAProjectResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_projects.models.activate_a_project_response import ActivateAProjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ActivateAProjectResponse from a JSON string
activate_a_project_response_instance = ActivateAProjectResponse.from_json(json)
# print the JSON string representation of the object
print(ActivateAProjectResponse.to_json())

# convert the object into a dict
activate_a_project_response_dict = activate_a_project_response_instance.to_dict()
# create an instance of ActivateAProjectResponse from a dict
activate_a_project_response_from_dict = ActivateAProjectResponse.from_dict(activate_a_project_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


