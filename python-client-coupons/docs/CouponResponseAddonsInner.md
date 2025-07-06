# CouponResponseAddonsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_code** | **str** | The addon code of the addon to which the coupon is to be applied. | [optional] 
**name** | **object** | Name of the coupon. | [optional] 

## Example

```python
from ls_zoho_billing_coupons.models.coupon_response_addons_inner import CouponResponseAddonsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CouponResponseAddonsInner from a JSON string
coupon_response_addons_inner_instance = CouponResponseAddonsInner.from_json(json)
# print the JSON string representation of the object
print(CouponResponseAddonsInner.to_json())

# convert the object into a dict
coupon_response_addons_inner_dict = coupon_response_addons_inner_instance.to_dict()
# create an instance of CouponResponseAddonsInner from a dict
coupon_response_addons_inner_from_dict = CouponResponseAddonsInner.from_dict(coupon_response_addons_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


