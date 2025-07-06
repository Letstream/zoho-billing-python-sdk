# DataSubscriptionCoupon

The object containing the details of the added coupon. <code>coupon_code</code> and <code>discount_amount</code> applied to the invoice total.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coupon_code** | **str** | The coupon code of the coupon which is to be applied to the subscription. | [optional] 
**discount_amount** | **float** | The discount amount included in an invoice on applying a coupon. | [optional] 

## Example

```python
from ls_zoho_billing_hosted_pages.models.data_subscription_coupon import DataSubscriptionCoupon

# TODO update the JSON string below
json = "{}"
# create an instance of DataSubscriptionCoupon from a JSON string
data_subscription_coupon_instance = DataSubscriptionCoupon.from_json(json)
# print the JSON string representation of the object
print(DataSubscriptionCoupon.to_json())

# convert the object into a dict
data_subscription_coupon_dict = data_subscription_coupon_instance.to_dict()
# create an instance of DataSubscriptionCoupon from a dict
data_subscription_coupon_from_dict = DataSubscriptionCoupon.from_dict(data_subscription_coupon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


