# DeactivateAProjectResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_projects.models.deactivate_a_project_response import DeactivateAProjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeactivateAProjectResponse from a JSON string
deactivate_a_project_response_instance = DeactivateAProjectResponse.from_json(json)
# print the JSON string representation of the object
print(DeactivateAProjectResponse.to_json())

# convert the object into a dict
deactivate_a_project_response_dict = deactivate_a_project_response_instance.to_dict()
# create an instance of DeactivateAProjectResponse from a dict
deactivate_a_project_response_from_dict = DeactivateAProjectResponse.from_dict(deactivate_a_project_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


