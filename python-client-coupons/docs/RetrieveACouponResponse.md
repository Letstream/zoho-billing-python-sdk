# RetrieveACouponResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**coupon** | [**RetrieveACouponResponseCoupon**](RetrieveACouponResponseCoupon.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_coupons.models.retrieve_a_coupon_response import RetrieveACouponResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveACouponResponse from a JSON string
retrieve_a_coupon_response_instance = RetrieveACouponResponse.from_json(json)
# print the JSON string representation of the object
print(RetrieveACouponResponse.to_json())

# convert the object into a dict
retrieve_a_coupon_response_dict = retrieve_a_coupon_response_instance.to_dict()
# create an instance of RetrieveACouponResponse from a dict
retrieve_a_coupon_response_from_dict = RetrieveACouponResponse.from_dict(retrieve_a_coupon_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


