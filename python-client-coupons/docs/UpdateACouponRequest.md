# UpdateACouponRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the coupon to be displayed in the interface and invoices. | 
**description** | **str** | A small description about the coupon. | [optional] 
**max_redemption** | **int** | Maximum number of subscriptions the coupon can be used for. The status of the coupon will be changed to &lt;code&gt;maxed_out&lt;/code&gt; once this limit is reached. | [optional] 
**expiry_at** | **str** | Date on which the coupon expires. The coupon cannot be applied to new subscriptions after this date. However, coupons with &lt;code&gt;type&lt;/code&gt;&#x3D;&lt;code&gt;forever&lt;/code&gt; already applied to subscriptions can still be redeemed. | [optional] 

## Example

```python
from ls_zoho_billing_coupons.models.update_a_coupon_request import UpdateACouponRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateACouponRequest from a JSON string
update_a_coupon_request_instance = UpdateACouponRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateACouponRequest.to_json())

# convert the object into a dict
update_a_coupon_request_dict = update_a_coupon_request_instance.to_dict()
# create an instance of UpdateACouponRequest from a dict
update_a_coupon_request_from_dict = UpdateACouponRequest.from_dict(update_a_coupon_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


