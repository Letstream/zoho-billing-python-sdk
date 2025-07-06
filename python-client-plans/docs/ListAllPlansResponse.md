# ListAllPlansResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**plans** | [**List[ListAllPlansResponsePlansInner]**](ListAllPlansResponsePlansInner.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_plans.models.list_all_plans_response import ListAllPlansResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListAllPlansResponse from a JSON string
list_all_plans_response_instance = ListAllPlansResponse.from_json(json)
# print the JSON string representation of the object
print(ListAllPlansResponse.to_json())

# convert the object into a dict
list_all_plans_response_dict = list_all_plans_response_instance.to_dict()
# create an instance of ListAllPlansResponse from a dict
list_all_plans_response_from_dict = ListAllPlansResponse.from_dict(list_all_plans_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


