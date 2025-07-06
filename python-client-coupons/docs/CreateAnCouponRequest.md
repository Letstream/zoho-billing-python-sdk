# CreateAnCouponRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coupon_code** | **str** | Unique string of your choice which lets you identify this coupon. | 
**name** | **str** | Name of the coupon to be displayed in the interface and invoices. | 
**description** | **str** | A small description about the coupon. | [optional] 
**type** | **str** | This indicates whether the coupon is to be applied only once, particular number of times or every time an invoice is raised for the subscription. It can either be &lt;code&gt;one_time&lt;/code&gt;, &lt;code&gt;duration&lt;/code&gt;, &lt;code&gt;forever&lt;/code&gt;. | 
**duration** | **int** | This indicates the number of times the coupon has to applied to the invoices generated for a particular subscription. | 
**discount_by** | **str** | Percentage off or Flat rate discounts can be offered. The value can either be &lt;code&gt;flat&lt;/code&gt; or &lt;code&gt;percentage&lt;/code&gt;. | 
**discount_value** | **float** | Value of the discount associated with a coupon. Depending on the value of &lt;code&gt;discount_by&lt;/code&gt;, it can be flat discount or a percentage value. Discount will be deducted from the plans/addons the coupon is associated with. | [optional] 
**product_id** | **str** | The Product ID of the product for which the coupon has to be created. | 
**max_redemption** | **int** | Maximum number of subscriptions the coupon can be used for. The status of the coupon will be changed to &lt;code&gt;maxed_out&lt;/code&gt; once this limit is reached. | [optional] 
**expiry_at** | **str** | Date on which the coupon expires. The coupon cannot be applied to new subscriptions after this date. However, coupons with &lt;code&gt;type&lt;/code&gt;&#x3D;&lt;code&gt;forever&lt;/code&gt; already applied to subscriptions can still be redeemed. | [optional] 
**apply_to_plans** | **str** | The coupon can be applied to all existing plans, selected plans or none of the existing plans. The values can be &lt;code&gt;all&lt;/code&gt;, &lt;code&gt;none&lt;/code&gt; or &lt;code&gt;select&lt;/code&gt;. | [optional] 
**plans** | [**List[CreateAnCouponRequestPlansInner]**](CreateAnCouponRequestPlansInner.md) | List of plans that the coupon needs to be associated with. If a coupon is to be associated with only two plans - \&quot;basic\&quot; and \&quot;professional\&quot;, then &lt;code&gt;apply_to_plans&lt;/code&gt; is set to be selected. Only the plan codes of the plans that need to be associated with the coupon are required. | 
**apply_to_addons** | **str** | The coupon can be applied to all one-time addons,all recurring addons,all addons, selected addons or none of the existing addons. The values can be &lt;code&gt;all_addons&lt;/code&gt;, &lt;code&gt;all_recurring&lt;/code&gt;,&lt;code&gt;all_onetime&lt;/code&gt;, &lt;code&gt;none&lt;/code&gt; or &lt;code&gt;select&lt;/code&gt;. | [optional] 
**addons** | [**List[CreateAnCouponRequestAddonsInner]**](CreateAnCouponRequestAddonsInner.md) | List of addons that the coupon needs to be associated with. If a coupon is to be associated with only two addons - \&quot;Email Basic\&quot; and \&quot;Email Professional\&quot;, then &lt;code&gt;apply_to_addons&lt;/code&gt; is set to be selected. Only the addon codes of the addons that need to be associated with the coupon are required. | 

## Example

```python
from ls_zoho_billing_coupons.models.create_an_coupon_request import CreateAnCouponRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAnCouponRequest from a JSON string
create_an_coupon_request_instance = CreateAnCouponRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAnCouponRequest.to_json())

# convert the object into a dict
create_an_coupon_request_dict = create_an_coupon_request_instance.to_dict()
# create an instance of CreateAnCouponRequest from a dict
create_an_coupon_request_from_dict = CreateAnCouponRequest.from_dict(create_an_coupon_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


