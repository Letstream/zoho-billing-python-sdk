# CollectChargeViaBankAccountCreditCardResponsePaymentAutotransaction

If the payment mode is <code>autotransaction</code>, autotransaction information will be displayed in the autotransaction object. It contains <code>autotransaction_id</code>, <code>payment_gateway</code>, <code>gateway_transaction_id</code>, <code>card_id</code>, <code>last_four_digits</code>, <code>expiry_month</code> and <code>expiry_year</code>.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autotransaction_id** | **str** | Auto-transaction ID generated for the payment made. | [optional] 
**payment_gateway** | **str** | Name of the payment gateway associated with payment. | [optional] 
**gateway_transaction_id** | **str** | Gateway transaction ID provided for the payment made to the invoice. This is applicable only if &lt;code&gt;payment_mode&lt;/code&gt; is autotransaction. | [optional] 
**gateway_error_message** | **str** | Gateway error message for a failed transaction. | [optional] 
**account_id** | **str** | Unique ID of the bank account. If you are collecting charge via credit card, use &lt;code&gt;card_id&lt;/code&gt; (Card ID of the card associated with the transaction) | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.collect_charge_via_bank_account_credit_card_response_payment_autotransaction import CollectChargeViaBankAccountCreditCardResponsePaymentAutotransaction

# TODO update the JSON string below
json = "{}"
# create an instance of CollectChargeViaBankAccountCreditCardResponsePaymentAutotransaction from a JSON string
collect_charge_via_bank_account_credit_card_response_payment_autotransaction_instance = CollectChargeViaBankAccountCreditCardResponsePaymentAutotransaction.from_json(json)
# print the JSON string representation of the object
print(CollectChargeViaBankAccountCreditCardResponsePaymentAutotransaction.to_json())

# convert the object into a dict
collect_charge_via_bank_account_credit_card_response_payment_autotransaction_dict = collect_charge_via_bank_account_credit_card_response_payment_autotransaction_instance.to_dict()
# create an instance of CollectChargeViaBankAccountCreditCardResponsePaymentAutotransaction from a dict
collect_charge_via_bank_account_credit_card_response_payment_autotransaction_from_dict = CollectChargeViaBankAccountCreditCardResponsePaymentAutotransaction.from_dict(collect_charge_via_bank_account_credit_card_response_payment_autotransaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


