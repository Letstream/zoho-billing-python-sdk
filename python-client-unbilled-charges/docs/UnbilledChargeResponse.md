# UnbilledChargeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unbilled_charge_id** | **str** | Unique ID generated for an unbilled charge. | [optional] 
**number** | **str** | Unique number (starts with UNBILL) generated for display in interface. | [optional] 
**status** | **str** | Status of the unbilled charge. It can be &lt;code&gt;invoiced&lt;/code&gt;, &lt;code&gt;open&lt;/code&gt; | [optional] 
**unbilled_charge_date** | **str** | The date on which the unbilled charge was raised. | [optional] 
**customer_id** | **List[str]** | Customer ID of the customer to whom the unbilled charge was raised. | [optional] 
**customer_name** | **str** | Name of the customer to whom the unbilled charge was raised. | [optional] 
**email** | **str** | Email address of the customer. | [optional] 
**unbilled_charge_items** | [**List[UnbilledChargeItemsInner]**](UnbilledChargeItemsInner.md) | Multiple items can be added as unbilled charges for a subscription : buy one time addon, add charge. | [optional] 
**coupons** | [**List[CouponsInner]**](CouponsInner.md) | The array of objects which contains the details of the added coupon. &lt;code&gt;coupon_code&lt;/code&gt; and &lt;code&gt;discount_amount&lt;/code&gt; are applied to the total. | [optional] 
**total** | **float** | Total amount to be paid. This would be the sum of individual costs of all items. | [optional] 
**currency_code** | **str** | Currency code in which the payment is made. | [optional] 
**currency_symbol** | **str** | Customer&#39;s currency symbol. | [optional] 
**created_time** | **str** | Time when the unbilled charge was created. | [optional] 
**updated_time** | **str** | Time when the unbilled charge details were last updated. | [optional] 
**billing_address** | [**BillingAddress**](BillingAddress.md) |  | [optional] 
**shipping_address** | [**ShippingAddress**](ShippingAddress.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_unbilled_charges.models.unbilled_charge_response import UnbilledChargeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnbilledChargeResponse from a JSON string
unbilled_charge_response_instance = UnbilledChargeResponse.from_json(json)
# print the JSON string representation of the object
print(UnbilledChargeResponse.to_json())

# convert the object into a dict
unbilled_charge_response_dict = unbilled_charge_response_instance.to_dict()
# create an instance of UnbilledChargeResponse from a dict
unbilled_charge_response_from_dict = UnbilledChargeResponse.from_dict(unbilled_charge_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


