# DeleteAPlanResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_plans.models.delete_a_plan_response import DeleteAPlanResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAPlanResponse from a JSON string
delete_a_plan_response_instance = DeleteAPlanResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteAPlanResponse.to_json())

# convert the object into a dict
delete_a_plan_response_dict = delete_a_plan_response_instance.to_dict()
# create an instance of DeleteAPlanResponse from a dict
delete_a_plan_response_from_dict = DeleteAPlanResponse.from_dict(delete_a_plan_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


