# ListAllCouponsResponseCouponsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coupon_code** | **str** | Unique string of your choice which lets you identify this coupon. | [optional] 
**name** | **str** | Name of the coupon to be displayed in the interface and invoices. | [optional] 
**description** | **str** | A small description about the coupon. | [optional] 
**type** | **str** | This indicates whether the coupon is to be applied only once, particular number of times or every time an invoice is raised for the subscription. It can either be &lt;code&gt;one_time&lt;/code&gt;, &lt;code&gt;duration&lt;/code&gt;, &lt;code&gt;forever&lt;/code&gt;. | [optional] 
**status** | **str** | Status of the coupon. It can either be &lt;code&gt;active&lt;/code&gt;, &lt;code&gt;inactive&lt;/code&gt;, &lt;code&gt;expired&lt;/code&gt; or &lt;code&gt;maxed_out&lt;/code&gt; | [optional] 
**discount_by** | **str** | Percentage off or Flat rate discounts can be offered. The value can either be &lt;code&gt;flat&lt;/code&gt; or &lt;code&gt;percentage&lt;/code&gt;. | [optional] 
**discount_value** | **float** | Value of the discount associated with a coupon. Depending on the value of &lt;code&gt;discount_by&lt;/code&gt;, it can be flat discount or a percentage value. Discount will be deducted from the plans/addons the coupon is associated with. | [optional] 
**product_id** | **str** | The Product ID of the product for which the coupon has to be created. | [optional] 
**max_redemption** | **int** | Maximum number of subscriptions the coupon can be used for. The status of the coupon will be changed to &lt;code&gt;maxed_out&lt;/code&gt; once this limit is reached. | [optional] 
**redemption_count** | **int** | Number of subscriptions the coupon has been used for at present. | [optional] 
**expiry_at** | **str** | Date on which the coupon expires. The coupon cannot be applied to new subscriptions after this date. However, coupons with &lt;code&gt;type&lt;/code&gt;&#x3D;&lt;code&gt;forever&lt;/code&gt; already applied to subscriptions can still be redeemed. | [optional] 
**created_time** | **str** | Time at which the coupon was created. | [optional] 
**updated_time** | **str** | Time at which the coupon details were last updated. | [optional] 

## Example

```python
from ls_zoho_billing_coupons.models.list_all_coupons_response_coupons_inner import ListAllCouponsResponseCouponsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListAllCouponsResponseCouponsInner from a JSON string
list_all_coupons_response_coupons_inner_instance = ListAllCouponsResponseCouponsInner.from_json(json)
# print the JSON string representation of the object
print(ListAllCouponsResponseCouponsInner.to_json())

# convert the object into a dict
list_all_coupons_response_coupons_inner_dict = list_all_coupons_response_coupons_inner_instance.to_dict()
# create an instance of ListAllCouponsResponseCouponsInner from a dict
list_all_coupons_response_coupons_inner_from_dict = ListAllCouponsResponseCouponsInner.from_dict(list_all_coupons_response_coupons_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


