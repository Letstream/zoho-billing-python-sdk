# PlanResponseAddonsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_code** | **str** | The addon code of the addon which is associated with the plan . | [optional] 
**name** | **object** | The name of the addon. | [optional] 
**status** | **str** | Status of the plan. It can be either &lt;code&gt; active &lt;/code&gt;  or &lt;code&gt; inactive &lt;/code&gt;. | [optional] 
**pricing_scheme** | **str** | Pricing type of the addon | [optional] 
**unit_name** | **str** | A name of your choice to refer to one unit of the addon. | [optional] 
**price_brackets** | [**List[PlanResponseAddonsInnerPriceBracketsInner]**](PlanResponseAddonsInnerPriceBracketsInner.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_plans.models.plan_response_addons_inner import PlanResponseAddonsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PlanResponseAddonsInner from a JSON string
plan_response_addons_inner_instance = PlanResponseAddonsInner.from_json(json)
# print the JSON string representation of the object
print(PlanResponseAddonsInner.to_json())

# convert the object into a dict
plan_response_addons_inner_dict = plan_response_addons_inner_instance.to_dict()
# create an instance of PlanResponseAddonsInner from a dict
plan_response_addons_inner_from_dict = PlanResponseAddonsInner.from_dict(plan_response_addons_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


