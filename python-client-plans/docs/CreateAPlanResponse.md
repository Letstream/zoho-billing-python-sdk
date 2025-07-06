# CreateAPlanResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**plan** | [**PlanResponse**](PlanResponse.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_plans.models.create_a_plan_response import CreateAPlanResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAPlanResponse from a JSON string
create_a_plan_response_instance = CreateAPlanResponse.from_json(json)
# print the JSON string representation of the object
print(CreateAPlanResponse.to_json())

# convert the object into a dict
create_a_plan_response_dict = create_a_plan_response_instance.to_dict()
# create an instance of CreateAPlanResponse from a dict
create_a_plan_response_from_dict = CreateAPlanResponse.from_dict(create_a_plan_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


