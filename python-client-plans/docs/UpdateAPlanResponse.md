# UpdateAPlanResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**plan** | [**UpdateAPlanResponsePlan**](UpdateAPlanResponsePlan.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_plans.models.update_a_plan_response import UpdateAPlanResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAPlanResponse from a JSON string
update_a_plan_response_instance = UpdateAPlanResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateAPlanResponse.to_json())

# convert the object into a dict
update_a_plan_response_dict = update_a_plan_response_instance.to_dict()
# create an instance of UpdateAPlanResponse from a dict
update_a_plan_response_from_dict = UpdateAPlanResponse.from_dict(update_a_plan_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


