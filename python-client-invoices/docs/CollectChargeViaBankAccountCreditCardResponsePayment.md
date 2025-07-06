# CollectChargeViaBankAccountCreditCardResponsePayment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_id** | **str** | The payment ID of the payment made for the invoice. | [optional] 
**payment_mode** | **str** | The mode in which payment is made for the invoice. This can be &lt;code&gt;check&lt;/code&gt;, &lt;code&gt;cash&lt;/code&gt;, &lt;code&gt;creditcard&lt;/code&gt;, &lt;code&gt;banktransfer&lt;/code&gt;, &lt;code&gt;bankremittance&lt;/code&gt;, &lt;code&gt;autotransaction&lt;/code&gt; or &lt;code&gt;others&lt;/code&gt;. | [optional] 
**amount** | **float** | Amount paid for the invoice. | [optional] 
**amount_refunded** | **float** | Amount that is refund. Refunds are applicable only for payments whose payment_mode is &lt;code&gt;autotransaction&lt;/code&gt;. Refunds would be made to the respective card provided by the customer. | [optional] 
**bank_charges** | **float** | Denotes any additional bank charges. | [optional] 
**var_date** | **str** | Date on which the invoice is paid. | [optional] 
**status** | **str** | Status of the invoice. It can be &lt;code&gt;paid&lt;/code&gt;, &lt;code&gt;sent&lt;/code&gt;, &lt;code&gt;overdue&lt;/code&gt;, &lt;code&gt;partially_paid&lt;/code&gt; or &lt;code&gt;void&lt;/code&gt;. | [optional] 
**reference_number** | **str** | Reference number of the invoice for which payment is made. | [optional] 
**due_date** | **str** | Date on which the invoice is due. If the invoice is not fully paid on or before this date, the status of the invoice will be changed to &lt;code&gt;overdue&lt;/code&gt;. If the invoice is only partially paid, its status will be &lt;code&gt;partially_paid&lt;/code&gt;. | [optional] 
**amount_due** | **float** | Balance amount that is due for the invoice. | [optional] 
**description** | **str** | Small description of the payment made for the invoice. | [optional] 
**customer_id** | **str** | Customer ID of the customer to whom the invoice is raised. | [optional] 
**customer_name** | **str** | Name of the customer to whom the invoice is raised. | [optional] 
**email** | **str** | Email address of the customer. | [optional] 
**autotransaction** | [**CollectChargeViaBankAccountCreditCardResponsePaymentAutotransaction**](CollectChargeViaBankAccountCreditCardResponsePaymentAutotransaction.md) |  | [optional] 
**invoices** | [**List[CollectChargeViaBankAccountCreditCardResponsePaymentInvoicesInner]**](CollectChargeViaBankAccountCreditCardResponsePaymentInvoicesInner.md) | List of invoices associated with the payment. Each invoice object contains &lt;code&gt;invoice_id&lt;/code&gt;, &lt;code&gt;invoice_number&lt;/code&gt;, &lt;code&gt;date&lt;/code&gt;, &lt;code&gt;invoice_amount&lt;/code&gt;, &lt;code&gt;amount_applied&lt;/code&gt; and &lt;code&gt;balance_amount&lt;/code&gt;. | [optional] 
**currency_code** | **str** | The customer&#39;s currency code. | [optional] 
**currency_symbol** | **str** | The customer&#39;s currency symbol. | [optional] 
**custom_fields** | [**List[CollectChargeViaBankAccountCreditCardResponsePaymentCustomFieldsInner]**](CollectChargeViaBankAccountCreditCardResponsePaymentCustomFieldsInner.md) | Additional fields for the invoices. | [optional] 
**created_time** | **str** | Time when the invoice was created. | [optional] 
**updated_time** | **str** | Time when the invoice details were last updated. | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.collect_charge_via_bank_account_credit_card_response_payment import CollectChargeViaBankAccountCreditCardResponsePayment

# TODO update the JSON string below
json = "{}"
# create an instance of CollectChargeViaBankAccountCreditCardResponsePayment from a JSON string
collect_charge_via_bank_account_credit_card_response_payment_instance = CollectChargeViaBankAccountCreditCardResponsePayment.from_json(json)
# print the JSON string representation of the object
print(CollectChargeViaBankAccountCreditCardResponsePayment.to_json())

# convert the object into a dict
collect_charge_via_bank_account_credit_card_response_payment_dict = collect_charge_via_bank_account_credit_card_response_payment_instance.to_dict()
# create an instance of CollectChargeViaBankAccountCreditCardResponsePayment from a dict
collect_charge_via_bank_account_credit_card_response_payment_from_dict = CollectChargeViaBankAccountCreditCardResponsePayment.from_dict(collect_charge_via_bank_account_credit_card_response_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


