# AddChargeResponseInvoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **str** | Unique ID generated for an invoice. | [optional] 
**number** | **str** | Unique number generated for the invoice. | [optional] 
**status** | **str** | The status of the subscription. It can be &lt;code&gt;live&lt;/code&gt;, &lt;code&gt;trial&lt;/code&gt;, &lt;code&gt;dunning&lt;/code&gt;, &lt;code&gt;unpaid&lt;/code&gt;, &lt;code&gt;non_renewing&lt;/code&gt;, &lt;code&gt;cancelled&lt;/code&gt;, &lt;code&gt;creation_failed&lt;/code&gt;, &lt;code&gt;cancelled_from_dunning&lt;/code&gt;, &lt;code&gt;expired&lt;/code&gt;, &lt;code&gt;trial_expired&lt;/code&gt; or &lt;code&gt;future&lt;/code&gt;. | [optional] 
**invoice_items** | [**List[AddChargeResponseInvoiceInvoiceItemsInner]**](AddChargeResponseInvoiceInvoiceItemsInner.md) | The list of items which are all included in the invoice. Each item object will have &lt;code&gt;item_id&lt;/code&gt;, &lt;code&gt;name&lt;/code&gt;, &lt;code&gt;code&lt;/code&gt;, &lt;code&gt;price&lt;/code&gt;, &lt;code&gt;quantity&lt;/code&gt; and &lt;code&gt;item_total&lt;/code&gt;. | [optional] 
**invoice_date** | **str** | Date in which the invoice was generated. | [optional] 
**due_date** | **str** | Date on which the payment is due for the invoice. | [optional] 
**payment_expected_date** | **str** | A date to specify the expected payment date. | [optional] 
**ach_payment_initiated** | **bool** | Set to true if ACH payment is initiated. | [optional] 
**transaction_type** | **str** | Small description about the type of transaction. | [optional] 
**customer_id** | **str** | Customer ID of the customer for whom a subscription needs to be created. | [optional] 
**customer_name** | **str** | Name of the customer. | [optional] 
**email** | **str** | Email address of the customer. | [optional] 
**total** | **float** | Total amount for the plan. | [optional] 
**payment_made** | **object** | Payments can be made in multiple instalments. payment_made refers to the amount paid for the invoice in the respective instalment. | [optional] 
**balance** | **float** | The unpaid amount of an invoice. | [optional] 
**credits_applied** | **float** | Credits applied for the invoice. | [optional] 
**write_off_amount** | **float** | The unpaid amount of an invoice that is written off. | [optional] 
**payments** | [**List[BuyOneTimeAddonResponseInvoicePaymentsInner]**](BuyOneTimeAddonResponseInvoicePaymentsInner.md) | List of payment objects. Each object will contain &lt;code&gt;payment_id&lt;/code&gt;, &lt;code&gt;payment_mode&lt;/code&gt;, &lt;code&gt;invoice_payment_id&lt;/code&gt;, &lt;code&gt;gateway_transaction_id&lt;/code&gt;, &lt;code&gt;description&lt;/code&gt;, &lt;code&gt;date&lt;/code&gt;, &lt;code&gt;reference_number&lt;/code&gt; and &lt;code&gt;amount&lt;/code&gt;. | [optional] 
**currency_code** | **str** | Currency code of the currency in which the customer wants to pay. If &lt;code&gt;currency_code&lt;/code&gt; is not specified here, the currency chosen in your Zoho Billing organization will be used for billing. &lt;code&gt;currency_id&lt;/code&gt; and &lt;code&gt;currency_symbol&lt;/code&gt; are set automatically in accordance to the currency_code. | [optional] 
**currency_symbol** | **str** | Symbol of the customer&#39;s currency. | [optional] 
**created_time** | **str** | Time at which the subscription was created. | [optional] 
**updated_time** | **str** | Time at which the subscription details were last updated. | [optional] 
**billing_address** | [**BillingAddress**](BillingAddress.md) |  | [optional] 
**comments** | [**List[AddChargeResponseInvoiceCommentsInner]**](AddChargeResponseInvoiceCommentsInner.md) | Lists the comments added by the system or by user. | [optional] 

## Example

```python
from ls_zoho_billing_subscription.models.add_charge_response_invoice import AddChargeResponseInvoice

# TODO update the JSON string below
json = "{}"
# create an instance of AddChargeResponseInvoice from a JSON string
add_charge_response_invoice_instance = AddChargeResponseInvoice.from_json(json)
# print the JSON string representation of the object
print(AddChargeResponseInvoice.to_json())

# convert the object into a dict
add_charge_response_invoice_dict = add_charge_response_invoice_instance.to_dict()
# create an instance of AddChargeResponseInvoice from a dict
add_charge_response_invoice_from_dict = AddChargeResponseInvoice.from_dict(add_charge_response_invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


