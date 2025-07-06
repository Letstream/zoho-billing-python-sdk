# CreateAnCouponRequestAddonsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_code** | **str** | The addon code of the addon to which the coupon is to be applied. | 

## Example

```python
from ls_zoho_billing_coupons.models.create_an_coupon_request_addons_inner import CreateAnCouponRequestAddonsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAnCouponRequestAddonsInner from a JSON string
create_an_coupon_request_addons_inner_instance = CreateAnCouponRequestAddonsInner.from_json(json)
# print the JSON string representation of the object
print(CreateAnCouponRequestAddonsInner.to_json())

# convert the object into a dict
create_an_coupon_request_addons_inner_dict = create_an_coupon_request_addons_inner_instance.to_dict()
# create an instance of CreateAnCouponRequestAddonsInner from a dict
create_an_coupon_request_addons_inner_from_dict = CreateAnCouponRequestAddonsInner.from_dict(create_an_coupon_request_addons_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


