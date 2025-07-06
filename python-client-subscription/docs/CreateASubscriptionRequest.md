# CreateASubscriptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_to_unbilled_charges** | **bool** | When the value is given as true, the subscription would be created and charges for the current billing cycle will be put as unbilled. This can be converted to invoice at any later point of time. | [optional] 
**customer** | [**CreateASubscriptionRequestCustomer**](CreateASubscriptionRequestCustomer.md) |  | 
**customer_id** | **object** | Customer ID of the customer for whom a subscription needs to be created. | 
**payment_terms** | **int** | Payment Due details for the invoices. | [optional] 
**payment_terms_label** | **str** | Label for the paymet due details. | [optional] 
**custom_fields** | [**List[ItemCustomFieldsInner]**](ItemCustomFieldsInner.md) | Additional fields for the invoices. | [optional] 
**contactpersons** | [**List[CreateASubscriptionRequestContactpersonsInner]**](CreateASubscriptionRequestContactpersonsInner.md) | List of contact person objects. Each object contains &lt;code&gt;contactperson_id&lt;/code&gt;. | [optional] 
**card_id** | **object** | Enter the card_id of the card which has to be updated. | 
**starts_at** | **str** | Generally the subscription will start on the day it is created. But, the date can also be a future  or past date depending upon your usecase. For future dates, the subscription status would be Future till the starts_at date. And for past dates, the subscription status can be Trial, Live or Expired depending on the subscription interval that you have selected. | [optional] 
**exchange_rate** | **float** | This will be the exchange rate provided for the organization&#39;s currency and the customer&#39;s currency. The subscription fee would be the multiplicative product of the original price and the exchange rate. | [optional] 
**place_of_supply** | **str** | Place of Supply for the customer&#39;s subscription. | [optional] 
**plan** | [**CreateASubscriptionRequestPlan**](CreateASubscriptionRequestPlan.md) |  | 
**addons** | [**List[CreateASubscriptionRequestAddonsInner]**](CreateASubscriptionRequestAddonsInner.md) | List of addon objects which are to be included in the subscription. Each object contains &lt;code&gt;addon_code&lt;/code&gt;, &lt;code&gt;name&lt;/code&gt;, &lt;code&gt;price&lt;/code&gt; and &lt;code&gt;quantity&lt;/code&gt;. | [optional] 
**coupon_code** | **str** | The coupon code of the coupon which is to be applied to the subscription. | [optional] 
**auto_collect** | **bool** | auto_collect is set to true for creating an online subscription which will charge the customer’s card automatically on every renewal. To create an offline subscriptions, set auto_collect to false. | [optional] 
**reference_id** | **str** | A string of your choice is required to easily identify and keep track of your subscriptions. | [optional] 
**salesperson_name** | **str** | Name of the sales person assigned for the subscription. | [optional] 
**payment_gateways** | [**List[SubscriptionResponsePaymentGatewaysInner]**](SubscriptionResponsePaymentGatewaysInner.md) | List of payment gateways configured for the customer. | [optional] 
**create_backdated_invoice** | **bool** | To allow creation of invoice for current billing cycle for back dated subscriptions. | [optional] 
**can_charge_setup_fee_immediately** | **bool** | If set to \&quot;true\&quot;, a separate invoice will be raised for the setup fee as soon as the subscription&#39;s trial period starts. Set the value as \&quot;false\&quot;, or remove this optional argument if you want the setup fee to be billed at the end of the trial period, along with the other subscription related charges. | [optional] 
**template_id** | **str** | Defaulte Invoice Template ID for all the invoices created from the subscription. | [optional] 
**cfdi_usage** | **str** | Choose CFDI Usage. Allowed values:&lt;/br&gt;&lt;code&gt;acquisition_of_merchandise&lt;/code&gt;, &lt;code&gt;return_discount_bonus&lt;/code&gt;, &lt;code&gt;general_expense&lt;/code&gt;, &lt;code&gt;buildings&lt;/code&gt;, &lt;code&gt;furniture_office_equipment&lt;/code&gt;, &lt;code&gt;transport_equipment&lt;/code&gt;, &lt;code&gt;computer_equipmentdye_molds_tools&lt;/code&gt;, &lt;code&gt;telephone_communication&lt;/code&gt;, &lt;code&gt;satellite_communication&lt;/code&gt;, &lt;code&gt;other_machinery_equipment&lt;/code&gt;, &lt;code&gt;hospital_expense&lt;/code&gt;, &lt;code&gt;medical_expense_disability&lt;/code&gt;, &lt;code&gt;funeral_expense&lt;/code&gt;, &lt;code&gt;donation&lt;/code&gt;, &lt;code&gt;interest_mortage_loans&lt;/code&gt;, &lt;code&gt;contribution_sar&lt;/code&gt;, &lt;code&gt;medical_expense_insurance_pormium&lt;/code&gt;, &lt;code&gt;school_transportation_expense&lt;/code&gt;, &lt;code&gt;deposit_saving_account&lt;/code&gt;, &lt;code&gt;payment_educational_service&lt;/code&gt;, &lt;code&gt;no_tax_effect&lt;/code&gt;, &lt;code&gt;payment&lt;/code&gt;, &lt;code&gt;payroll&lt;/code&gt;. | [optional] 
**allow_partial_payments** | **bool** | Boolean to check if partial payments are allowed for the contact | [optional] 
**account_id** | **str** | Account ID of the bank account from which payment is made by the customer. | 

## Example

```python
from ls_zoho_billing_subscription.models.create_a_subscription_request import CreateASubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateASubscriptionRequest from a JSON string
create_a_subscription_request_instance = CreateASubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateASubscriptionRequest.to_json())

# convert the object into a dict
create_a_subscription_request_dict = create_a_subscription_request_instance.to_dict()
# create an instance of CreateASubscriptionRequest from a dict
create_a_subscription_request_from_dict = CreateASubscriptionRequest.from_dict(create_a_subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


