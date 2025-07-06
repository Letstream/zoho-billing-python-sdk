# CloneAProjectResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**project** | [**UpdateAProjectResponseProject**](UpdateAProjectResponseProject.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_projects.models.clone_a_project_response import CloneAProjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CloneAProjectResponse from a JSON string
clone_a_project_response_instance = CloneAProjectResponse.from_json(json)
# print the JSON string representation of the object
print(CloneAProjectResponse.to_json())

# convert the object into a dict
clone_a_project_response_dict = clone_a_project_response_instance.to_dict()
# create an instance of CloneAProjectResponse from a dict
clone_a_project_response_from_dict = CloneAProjectResponse.from_dict(clone_a_project_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


