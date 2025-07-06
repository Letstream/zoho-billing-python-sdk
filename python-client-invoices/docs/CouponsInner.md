# CouponsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coupon_code** | **str** | The coupon code of the coupon applied to the invoice. | [optional] 
**coupon_name** | **str** | Name of the coupon applied to the subscription. | [optional] 
**discount_amount** | **float** | The discount amount included in an invoice on applying a coupon. | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.coupons_inner import CouponsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CouponsInner from a JSON string
coupons_inner_instance = CouponsInner.from_json(json)
# print the JSON string representation of the object
print(CouponsInner.to_json())

# convert the object into a dict
coupons_inner_dict = coupons_inner_instance.to_dict()
# create an instance of CouponsInner from a dict
coupons_inner_from_dict = CouponsInner.from_dict(coupons_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


