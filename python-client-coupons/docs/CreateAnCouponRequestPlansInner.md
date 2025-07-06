# CreateAnCouponRequestPlansInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_code** | **str** | The plan code of the plan to which the coupon is to be applied. | 

## Example

```python
from ls_zoho_billing_coupons.models.create_an_coupon_request_plans_inner import CreateAnCouponRequestPlansInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAnCouponRequestPlansInner from a JSON string
create_an_coupon_request_plans_inner_instance = CreateAnCouponRequestPlansInner.from_json(json)
# print the JSON string representation of the object
print(CreateAnCouponRequestPlansInner.to_json())

# convert the object into a dict
create_an_coupon_request_plans_inner_dict = create_an_coupon_request_plans_inner_instance.to_dict()
# create an instance of CreateAnCouponRequestPlansInner from a dict
create_an_coupon_request_plans_inner_from_dict = CreateAnCouponRequestPlansInner.from_dict(create_an_coupon_request_plans_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


