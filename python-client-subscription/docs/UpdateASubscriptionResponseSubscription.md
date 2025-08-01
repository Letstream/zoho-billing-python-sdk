# UpdateASubscriptionResponseSubscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_id** | **str** | Unique ID generated for a subscription. | [optional] 
**name** | **str** | Name generated by concatenation of the product name and the selected plan. | [optional] 
**status** | **str** | The status of the subscription. It can be &lt;code&gt;live&lt;/code&gt;, &lt;code&gt;trial&lt;/code&gt;, &lt;code&gt;dunning&lt;/code&gt;, &lt;code&gt;unpaid&lt;/code&gt;, &lt;code&gt;non_renewing&lt;/code&gt;, &lt;code&gt;cancelled&lt;/code&gt;, &lt;code&gt;creation_failed&lt;/code&gt;, &lt;code&gt;cancelled_from_dunning&lt;/code&gt;, &lt;code&gt;expired&lt;/code&gt;, &lt;code&gt;trial_expired&lt;/code&gt; or &lt;code&gt;future&lt;/code&gt;. | [optional] 
**amount** | **float** | The amount that needs to be charged for the subscription. | [optional] 
**created_at** | **str** | Date at which the subscription was created. | [optional] 
**activated_at** | **str** | Date at which the subscription was activated. | [optional] 
**current_term_starts_at** | **str** | Date on which the current term of the subscription started. | [optional] 
**current_term_ends_at** | **str** | Date on which the current term of the subscription ends. | [optional] 
**last_billing_at** | **str** | The date on which the customer was billed last. | [optional] 
**next_billing_at** | **str** | The date on which the customer will be billed next. This will also be the date on which the next term of the subscription starts. | [optional] 
**expires_at** | **str** | This is applicable only when &lt;code&gt;billing_cycle&lt;/code&gt; is set for a plan. A subscription expires on the last day of the last billing cycle. | [optional] 
**interval** | **str** | Indicates the number of intervals between each billing. If interval&#x3D;2, the customer would be billed every two months or years depending on the value for interval_unit. | [optional] 
**interval_unit** | **str** | It can be either &lt;code&gt;months&lt;/code&gt; or &lt;code&gt;years&lt;/code&gt;. For interval&#x3D;2 and interval_unit&#x3D;months, the customer is billed every two months. | [optional] 
**auto_collect** | **bool** | auto_collect is set to true for creating an online subscription which will charge the customer’s card automatically on every renewal. To create an offline subscriptions, set auto_collect to false. | [optional] 
**created_time** | **str** | Time at which the subscription was created. | [optional] 
**updated_time** | **str** | Time at which the subscription details were last updated. | [optional] 
**reference_id** | **str** | A string of your choice is required to easily identify and keep track of your subscriptions. | [optional] 
**salesperson_id** | **str** | Unique Id of the sales person assigned for the subscription. | [optional] 
**salesperson_name** | **str** | Name of the sales person assigned for the subscription. | [optional] 
**child_invoice_id** | **str** | Invoice ID of the most recent invoice to which the subscription is associated with. | [optional] 
**currency_code** | **str** | Currency code of the currency in which the customer wants to pay. If &lt;code&gt;currency_code&lt;/code&gt; is not specified here, the currency chosen in your Zoho Billing organization will be used for billing. &lt;code&gt;currency_id&lt;/code&gt; and &lt;code&gt;currency_symbol&lt;/code&gt; are set automatically in accordance to the currency_code. | [optional] 
**currency_symbol** | **str** | Symbol of the customer&#39;s currency. | [optional] 
**end_of_term** | **bool** | If there are any changes in the plan&#39;s subscriptions, those subscription changes can be made immediately if &lt;code&gt;end_of_term&lt;/code&gt; is set to false. If &lt;code&gt;end_of_term&lt;/code&gt; is set to true, the subscription changes take effect only after the current term of the subscription ends. | [optional] 
**product_id** | **str** | Product ID of the product to which the plan is associated with. | [optional] 
**product_name** | **str** | Name of the product which the plan belongs to. | [optional] 
**plan** | [**SubscriptionResponsePlan**](SubscriptionResponsePlan.md) |  | [optional] 
**addons** | [**List[RetrieveASubscriptionResponseSubscriptionAddonsInner]**](RetrieveASubscriptionResponseSubscriptionAddonsInner.md) | List of addon objects which are to be included in the subscription. Each object contains &lt;code&gt;addon_code&lt;/code&gt;, &lt;code&gt;name&lt;/code&gt;, &lt;code&gt;price&lt;/code&gt; and &lt;code&gt;quantity&lt;/code&gt;. | [optional] 
**coupon** | [**SubscriptionResponseCoupon**](SubscriptionResponseCoupon.md) |  | [optional] 
**card** | [**UpdateASubscriptionResponseSubscriptionCard**](UpdateASubscriptionResponseSubscriptionCard.md) |  | [optional] 
**payment_terms** | **int** | Payment Due details for the invoices. | [optional] 
**payment_terms_label** | **str** | Label for the paymet due details. | [optional] 
**can_add_bank_account** | **bool** | Set to true if Bank account can be added for the customer to perform ACH transactions. | [optional] 
**customer** | [**UpdateASubscriptionResponseSubscriptionCustomer**](UpdateASubscriptionResponseSubscriptionCustomer.md) |  | [optional] 
**custom_fields** | [**List[SubscriptionResponseCustomFieldsInner]**](SubscriptionResponseCustomFieldsInner.md) | Additional fields for the invoices. | [optional] 
**taxes** | [**List[SubscriptionResponseTaxesInner]**](SubscriptionResponseTaxesInner.md) | Taxes associated wit the subscription. | [optional] 
**contactpersons** | [**List[SubscriptionResponseContactpersonsInner]**](SubscriptionResponseContactpersonsInner.md) | List of contact person objects. Each object contains &lt;code&gt;contactperson_id&lt;/code&gt;. | [optional] 
**notes** | [**List[SubscriptionResponseNotesInner]**](SubscriptionResponseNotesInner.md) | List of objects containing &lt;code&gt;note_id&lt;/code&gt;, &lt;code&gt;description&lt;/code&gt;, &lt;code&gt;commented_by&lt;/code&gt; and &lt;code&gt;commented_time&lt;/code&gt; | [optional] 
**payment_gateways** | [**List[SubscriptionResponsePaymentGatewaysInner]**](SubscriptionResponsePaymentGatewaysInner.md) | List of payment gateways configured for the customer. | [optional] 
**can_charge_setup_fee_immediately** | **bool** | If set to \&quot;true\&quot;, a separate invoice will be raised for the setup fee as soon as the subscription&#39;s trial period starts. Set the value as \&quot;false\&quot;, or remove this optional argument if you want the setup fee to be billed at the end of the trial period, along with the other subscription related charges. | [optional] 

## Example

```python
from ls_zoho_billing_subscription.models.update_a_subscription_response_subscription import UpdateASubscriptionResponseSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateASubscriptionResponseSubscription from a JSON string
update_a_subscription_response_subscription_instance = UpdateASubscriptionResponseSubscription.from_json(json)
# print the JSON string representation of the object
print(UpdateASubscriptionResponseSubscription.to_json())

# convert the object into a dict
update_a_subscription_response_subscription_dict = update_a_subscription_response_subscription_instance.to_dict()
# create an instance of UpdateASubscriptionResponseSubscription from a dict
update_a_subscription_response_subscription_from_dict = UpdateASubscriptionResponseSubscription.from_dict(update_a_subscription_response_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


