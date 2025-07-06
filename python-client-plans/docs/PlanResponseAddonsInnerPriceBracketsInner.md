# PlanResponseAddonsInnerPriceBracketsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_quantity** | **int** | Lower limit of the addon range. | [optional] 
**end_quantity** | **int** | Upper limit of the addon range. | [optional] 
**price** | **float** | Per unit cost of the addon for the selected range. For the “package” pricing scheme, this would be the price of the specified quantity of addons. | [optional] 

## Example

```python
from ls_zoho_billing_plans.models.plan_response_addons_inner_price_brackets_inner import PlanResponseAddonsInnerPriceBracketsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PlanResponseAddonsInnerPriceBracketsInner from a JSON string
plan_response_addons_inner_price_brackets_inner_instance = PlanResponseAddonsInnerPriceBracketsInner.from_json(json)
# print the JSON string representation of the object
print(PlanResponseAddonsInnerPriceBracketsInner.to_json())

# convert the object into a dict
plan_response_addons_inner_price_brackets_inner_dict = plan_response_addons_inner_price_brackets_inner_instance.to_dict()
# create an instance of PlanResponseAddonsInnerPriceBracketsInner from a dict
plan_response_addons_inner_price_brackets_inner_from_dict = PlanResponseAddonsInnerPriceBracketsInner.from_dict(plan_response_addons_inner_price_brackets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


