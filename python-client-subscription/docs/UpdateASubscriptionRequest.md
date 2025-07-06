# UpdateASubscriptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_id** | **object** | Enter the card_id of the card which has to be updated. | 
**exchange_rate** | **float** | This will be the exchange rate provided for the organization&#39;s currency and the customer&#39;s currency. The subscription fee would be the multiplicative product of the original price and the exchange rate. | [optional] 
**plan** | [**UpdateASubscriptionRequestPlan**](UpdateASubscriptionRequestPlan.md) |  | 
**addons** | [**List[CreateASubscriptionRequestAddonsInner]**](CreateASubscriptionRequestAddonsInner.md) | List of addon objects which are to be included in the subscription. Each object contains &lt;code&gt;addon_code&lt;/code&gt;, &lt;code&gt;name&lt;/code&gt;, &lt;code&gt;price&lt;/code&gt; and &lt;code&gt;quantity&lt;/code&gt;. | [optional] 
**auto_collect** | **bool** | auto_collect is set to true for creating an online subscription which will charge the customer’s card automatically on every renewal. To create an offline subscriptions, set auto_collect to false. | [optional] 
**coupon_code** | **str** | The coupon code of the coupon which is to be applied to the subscription. | [optional] 
**reference_id** | **str** | A string of your choice is required to easily identify and keep track of your subscriptions. | [optional] 
**salesperson_id** | **str** | Unique Id of the sales person assigned for the subscription. | [optional] 
**salesperson_name** | **str** | Name of the sales person assigned for the subscription. | [optional] 
**end_of_term** | **bool** | If there are any changes in the plan&#39;s subscriptions, those subscription changes can be made immediately if &lt;code&gt;end_of_term&lt;/code&gt; is set to false. If &lt;code&gt;end_of_term&lt;/code&gt; is set to true, the subscription changes take effect only after the current term of the subscription ends. | [optional] 
**contactpersons** | [**List[CreateASubscriptionRequestContactpersonsInner]**](CreateASubscriptionRequestContactpersonsInner.md) | List of contact person objects. Each object contains &lt;code&gt;contactperson_id&lt;/code&gt;. | [optional] 
**payment_terms** | **int** | Payment Due details for the invoices. | [optional] 
**payment_terms_label** | **str** | Label for the paymet due details. | [optional] 
**payment_gateways** | [**List[SubscriptionResponsePaymentGatewaysInner]**](SubscriptionResponsePaymentGatewaysInner.md) | List of payment gateways configured for the customer. | [optional] 
**custom_fields** | [**List[SubscriptionResponseCustomFieldsInner]**](SubscriptionResponseCustomFieldsInner.md) | Additional fields for the invoices. | [optional] 
**template_id** | **str** | Defaulte Invoice Template ID for all the invoices created from the subscription. | [optional] 
**can_charge_setup_fee_immediately** | **bool** | If set to \&quot;true\&quot;, a separate invoice will be raised for the setup fee as soon as the subscription&#39;s trial period starts. Set the value as \&quot;false\&quot;, or remove this optional argument if you want the setup fee to be billed at the end of the trial period, along with the other subscription related charges. | [optional] 
**cfdi_usage** | **str** | Choose CFDI Usage. Allowed values:&lt;/br&gt;&lt;code&gt;acquisition_of_merchandise&lt;/code&gt;, &lt;code&gt;return_discount_bonus&lt;/code&gt;, &lt;code&gt;general_expense&lt;/code&gt;, &lt;code&gt;buildings&lt;/code&gt;, &lt;code&gt;furniture_office_equipment&lt;/code&gt;, &lt;code&gt;transport_equipment&lt;/code&gt;, &lt;code&gt;computer_equipmentdye_molds_tools&lt;/code&gt;, &lt;code&gt;telephone_communication&lt;/code&gt;, &lt;code&gt;satellite_communication&lt;/code&gt;, &lt;code&gt;other_machinery_equipment&lt;/code&gt;, &lt;code&gt;hospital_expense&lt;/code&gt;, &lt;code&gt;medical_expense_disability&lt;/code&gt;, &lt;code&gt;funeral_expense&lt;/code&gt;, &lt;code&gt;donation&lt;/code&gt;, &lt;code&gt;interest_mortage_loans&lt;/code&gt;, &lt;code&gt;contribution_sar&lt;/code&gt;, &lt;code&gt;medical_expense_insurance_pormium&lt;/code&gt;, &lt;code&gt;school_transportation_expense&lt;/code&gt;, &lt;code&gt;deposit_saving_account&lt;/code&gt;, &lt;code&gt;payment_educational_service&lt;/code&gt;, &lt;code&gt;no_tax_effect&lt;/code&gt;, &lt;code&gt;payment&lt;/code&gt;, &lt;code&gt;payroll&lt;/code&gt;. | [optional] 
**allow_partial_payments** | **bool** | Boolean to check if partial payments are allowed for the contact | [optional] 
**customer_id** | **str** | Customer ID of the customer for whom a subscription needs to be created. | 
**account_id** | **str** | Account ID of the bank account from which payment is made by the customer. | 

## Example

```python
from ls_zoho_billing_subscription.models.update_a_subscription_request import UpdateASubscriptionRequest

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


