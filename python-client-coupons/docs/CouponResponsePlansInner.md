# CouponResponsePlansInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_code** | **str** | The plan code of the plan to which the coupon is to be applied. | [optional] 
**name** | **object** | Plan to which the coupon is to be applied. | [optional] 

## Example

```python
from ls_zoho_billing_coupons.models.coupon_response_plans_inner import CouponResponsePlansInner

# TODO update the JSON string below
json = "{}"
# create an instance of CouponResponsePlansInner from a JSON string
coupon_response_plans_inner_instance = CouponResponsePlansInner.from_json(json)
# print the JSON string representation of the object
print(CouponResponsePlansInner.to_json())

# convert the object into a dict
coupon_response_plans_inner_dict = coupon_response_plans_inner_instance.to_dict()
# create an instance of CouponResponsePlansInner from a dict
coupon_response_plans_inner_from_dict = CouponResponsePlansInner.from_dict(coupon_response_plans_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


