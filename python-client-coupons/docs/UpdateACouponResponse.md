# UpdateACouponResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**coupon** | [**RetrieveACouponResponseCoupon**](RetrieveACouponResponseCoupon.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_coupons.models.update_a_coupon_response import UpdateACouponResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateACouponResponse from a JSON string
update_a_coupon_response_instance = UpdateACouponResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateACouponResponse.to_json())

# convert the object into a dict
update_a_coupon_response_dict = update_a_coupon_response_instance.to_dict()
# create an instance of UpdateACouponResponse from a dict
update_a_coupon_response_from_dict = UpdateACouponResponse.from_dict(update_a_coupon_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


