# RetrieveAPlanResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**plan** | [**RetrieveAPlanResponsePlan**](RetrieveAPlanResponsePlan.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_plans.models.retrieve_a_plan_response import RetrieveAPlanResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveAPlanResponse from a JSON string
retrieve_a_plan_response_instance = RetrieveAPlanResponse.from_json(json)
# print the JSON string representation of the object
print(RetrieveAPlanResponse.to_json())

# convert the object into a dict
retrieve_a_plan_response_dict = retrieve_a_plan_response_instance.to_dict()
# create an instance of RetrieveAPlanResponse from a dict
retrieve_a_plan_response_from_dict = RetrieveAPlanResponse.from_dict(retrieve_a_plan_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


