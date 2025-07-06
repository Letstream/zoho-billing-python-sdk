# BuyOneTimeAddonForASubscriptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_id** | **str** | Unique ID generated for a subscription. | 
**addons** | [**List[BuyOneTimeAddonForASubscriptionRequestAddonsInner]**](BuyOneTimeAddonForASubscriptionRequestAddonsInner.md) | List of addon objects which are to be included in the subscription. Each object contains &lt;code&gt;addon_code&lt;/code&gt;, &lt;code&gt;name&lt;/code&gt;, &lt;code&gt;price&lt;/code&gt; and &lt;code&gt;quantity&lt;/code&gt;. | 
**redirect_url** | **str** | It specifies the url to which the customer will be redirected after successful transaction. | [optional] 
**coupon_code** | **object** | The coupon code of the coupon which is to be applied to the one-time addon. | [optional] 
**cfdi_usage** | **str** | Choose CFDI Usage. Allowed values:&lt;/br&gt;&lt;code&gt;acquisition_of_merchandise&lt;/code&gt;, &lt;code&gt;return_discount_bonus&lt;/code&gt;, &lt;code&gt;general_expense&lt;/code&gt;, &lt;code&gt;buildings&lt;/code&gt;, &lt;code&gt;furniture_office_equipment&lt;/code&gt;, &lt;code&gt;transport_equipment&lt;/code&gt;, &lt;code&gt;computer_equipmentdye_molds_tools&lt;/code&gt;, &lt;code&gt;telephone_communication&lt;/code&gt;, &lt;code&gt;satellite_communication&lt;/code&gt;, &lt;code&gt;other_machinery_equipment&lt;/code&gt;, &lt;code&gt;hospital_expense&lt;/code&gt;, &lt;code&gt;medical_expense_disability&lt;/code&gt;, &lt;code&gt;funeral_expense&lt;/code&gt;, &lt;code&gt;donation&lt;/code&gt;, &lt;code&gt;interest_mortage_loans&lt;/code&gt;, &lt;code&gt;contribution_sar&lt;/code&gt;, &lt;code&gt;medical_expense_insurance_pormium&lt;/code&gt;, &lt;code&gt;school_transportation_expense&lt;/code&gt;, &lt;code&gt;deposit_saving_account&lt;/code&gt;, &lt;code&gt;payment_educational_service&lt;/code&gt;, &lt;code&gt;no_tax_effect&lt;/code&gt;, &lt;code&gt;payment&lt;/code&gt;, &lt;code&gt;payroll&lt;/code&gt;. | [optional] 
**exchange_rate** | **float** | This will be the exchange rate provided for the organization&#39;s currency and the customer&#39;s currency. The subscription fee would be the multiplicative product of the original price and the exchange rate. | [optional] 
**payment_gateways** | [**List[PaymentGatewaysInner]**](PaymentGatewaysInner.md) | List of payment gateways configured for the customer. | [optional] 

## Example

```python
from ls_zoho_billing_hosted_pages.models.buy_one_time_addon_for_a_subscription_request import BuyOneTimeAddonForASubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BuyOneTimeAddonForASubscriptionRequest from a JSON string
buy_one_time_addon_for_a_subscription_request_instance = BuyOneTimeAddonForASubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print(BuyOneTimeAddonForASubscriptionRequest.to_json())

# convert the object into a dict
buy_one_time_addon_for_a_subscription_request_dict = buy_one_time_addon_for_a_subscription_request_instance.to_dict()
# create an instance of BuyOneTimeAddonForASubscriptionRequest from a dict
buy_one_time_addon_for_a_subscription_request_from_dict = BuyOneTimeAddonForASubscriptionRequest.from_dict(buy_one_time_addon_for_a_subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


