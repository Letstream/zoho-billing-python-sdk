# CreateAnCouponResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**coupon** | [**CouponResponse**](CouponResponse.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_coupons.models.create_an_coupon_response import CreateAnCouponResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAnCouponResponse from a JSON string
create_an_coupon_response_instance = CreateAnCouponResponse.from_json(json)
# print the JSON string representation of the object
print(CreateAnCouponResponse.to_json())

# convert the object into a dict
create_an_coupon_response_dict = create_an_coupon_response_instance.to_dict()
# create an instance of CreateAnCouponResponse from a dict
create_an_coupon_response_from_dict = CreateAnCouponResponse.from_dict(create_an_coupon_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


