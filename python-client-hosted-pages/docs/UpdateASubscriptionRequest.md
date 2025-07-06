# UpdateASubscriptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_id** | **str** | Unique ID generated for a subscription. | 
**plan** | [**UpdateASubscriptionRequestPlan**](UpdateASubscriptionRequestPlan.md) |  | 
**addons** | [**List[CreateASubscriptionRequestAddonsInner]**](CreateASubscriptionRequestAddonsInner.md) | List of addon objects which are to be included in the subscription. Each object contains &lt;code&gt;addon_code&lt;/code&gt;, &lt;code&gt;name&lt;/code&gt;, &lt;code&gt;price&lt;/code&gt; and &lt;code&gt;quantity&lt;/code&gt;. | [optional] 
**reference_id** | **str** | A string of your choice is required to easily identify and keep track of your subscriptions. | [optional] 
**starts_at** | **str** | Generally the subscription will start on the day it is created. But, the date can also be a future  or past date depending upon your usecase. For future dates, the subscription status would be Future till the starts_at date. And for past dates, the subscription status can be Trial, Live or Expired depending on the subscription interval that you have selected. | [optional] 
**custom_fields** | [**List[ItemCustomFieldsInner]**](ItemCustomFieldsInner.md) | Additional fields for the Hosted pages. | [optional] 
**coupon_code** | **str** | The coupon code of the coupon which is to be applied to the subscription. | [optional] 
**salesperson_name** | **str** | Name of tha sales person assigned for the subscription. | [optional] 
**can_charge_setup_fee_immediately** | **bool** | If set to \&quot;true\&quot;, a separate invoice will be raised for the setup fee as soon as the subscription&#39;s trial period starts. Set the value as \&quot;false\&quot;, or remove this optional argument if you want the setup fee to be billed at the end of the trial period, along with the other subscription related charges. | [optional] 
**gst_treatment** | **str** | GST Treatment for the customer.&lt;br&gt;Allowed values for &lt;strong&gt;&lt;code&gt;gst_treatment&lt;/code&gt;&lt;/strong&gt; : &lt;br&gt;&lt;code&gt;business_gst&lt;/code&gt;, &lt;code&gt;business_none&lt;/code&gt;, &lt;code&gt;consumer&lt;/code&gt;, &lt;code&gt;overseas&lt;/code&gt;&lt;br&gt; &lt;code&gt;business_gst&lt;/code&gt; - For a GST Registered business owner. &lt;br&gt;&lt;code&gt;business_none&lt;/code&gt; - For a GST unregistered business owner. &lt;br&gt;&lt;code&gt;consumer&lt;/code&gt; - For a consumer. &lt;br&gt;&lt;code&gt;overseas&lt;/code&gt; - Customer for whom you export your goods/services. | [optional] 
**gst_no** | **str** | GSTIN Number for the customer. | [optional] 
**cfdi_usage** | **str** | Choose CFDI Usage. Allowed values:&lt;/br&gt;&lt;code&gt;acquisition_of_merchandise&lt;/code&gt;, &lt;code&gt;return_discount_bonus&lt;/code&gt;, &lt;code&gt;general_expense&lt;/code&gt;, &lt;code&gt;buildings&lt;/code&gt;, &lt;code&gt;furniture_office_equipment&lt;/code&gt;, &lt;code&gt;transport_equipment&lt;/code&gt;, &lt;code&gt;computer_equipmentdye_molds_tools&lt;/code&gt;, &lt;code&gt;telephone_communication&lt;/code&gt;, &lt;code&gt;satellite_communication&lt;/code&gt;, &lt;code&gt;other_machinery_equipment&lt;/code&gt;, &lt;code&gt;hospital_expense&lt;/code&gt;, &lt;code&gt;medical_expense_disability&lt;/code&gt;, &lt;code&gt;funeral_expense&lt;/code&gt;, &lt;code&gt;donation&lt;/code&gt;, &lt;code&gt;interest_mortage_loans&lt;/code&gt;, &lt;code&gt;contribution_sar&lt;/code&gt;, &lt;code&gt;medical_expense_insurance_pormium&lt;/code&gt;, &lt;code&gt;school_transportation_expense&lt;/code&gt;, &lt;code&gt;deposit_saving_account&lt;/code&gt;, &lt;code&gt;payment_educational_service&lt;/code&gt;, &lt;code&gt;no_tax_effect&lt;/code&gt;, &lt;code&gt;payment&lt;/code&gt;, &lt;code&gt;payroll&lt;/code&gt;. | [optional] 
**payment_gateways** | [**List[PaymentGatewaysInner]**](PaymentGatewaysInner.md) | List of payment gateways configured for the customer. | [optional] 
**exchange_rate** | **float** | This will be the exchange rate provided for the organization&#39;s currency and the customer&#39;s currency. The subscription fee would be the multiplicative product of the original price and the exchange rate. | [optional] 
**place_of_supply** | **str** | Place of Supply for the customer&#39;s subscription. | [optional] 
**billing_address_id** | **str** |  ID of the respective billing address | [optional] 
**shipping_address_id** | **str** |  ID of the respective Shipping address | [optional] 
**branch_id** | **str** |  branch under which this transaction will fall under | [optional] 
**template_id** | **int** | Unique Id used to denote the invoice template. | [optional] 
**redirect_url** | **str** | It specifies the url to which the customer will be redirected after successful transaction. | [optional] 

## Example

```python
from ls_zoho_billing_hosted_pages.models.update_a_subscription_request import UpdateASubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateASubscriptionRequest from a JSON string
update_a_subscription_request_instance = UpdateASubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateASubscriptionRequest.to_json())

# convert the object into a dict
update_a_subscription_request_dict = update_a_subscription_request_instance.to_dict()
# create an instance of UpdateASubscriptionRequest from a dict
update_a_subscription_request_from_dict = UpdateASubscriptionRequest.from_dict(update_a_subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


