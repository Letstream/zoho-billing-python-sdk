# BuyOneTimeAddonResponseInvoiceCouponsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coupon_code** | **str** | The coupon code of the coupon which is to be applied to the subscription. | [optional] 
**coupon_name** | **str** | Name of the coupon applied to the subscription. | [optional] 
**discount_amount** | **float** | The discount amount included in an invoice on applying a coupon. | [optional] 

## Example

```python
from ls_zoho_billing_subscription.models.buy_one_time_addon_response_invoice_coupons_inner import BuyOneTimeAddonResponseInvoiceCouponsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BuyOneTimeAddonResponseInvoiceCouponsInner from a JSON string
buy_one_time_addon_response_invoice_coupons_inner_instance = BuyOneTimeAddonResponseInvoiceCouponsInner.from_json(json)
# print the JSON string representation of the object
print(BuyOneTimeAddonResponseInvoiceCouponsInner.to_json())

# convert the object into a dict
buy_one_time_addon_response_invoice_coupons_inner_dict = buy_one_time_addon_response_invoice_coupons_inner_instance.to_dict()
# create an instance of BuyOneTimeAddonResponseInvoiceCouponsInner from a dict
buy_one_time_addon_response_invoice_coupons_inner_from_dict = BuyOneTimeAddonResponseInvoiceCouponsInner.from_dict(buy_one_time_addon_response_invoice_coupons_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


