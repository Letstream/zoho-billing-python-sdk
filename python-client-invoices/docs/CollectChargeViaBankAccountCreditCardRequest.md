# CollectChargeViaBankAccountCreditCardRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Unique ID of the bank account. If you are collecting charge via credit card, use &lt;code&gt;card_id&lt;/code&gt; (Card ID of the card associated with the transaction) | 
**card_id** | **str** | Card ID of the card associated with the transaction. If you are collecting charge via bank account, use &lt;code&gt;account_id&lt;/code&gt; (Unique ID of the bank account) | 

## Example

```python
from ls_zoho_billing_invoices.models.collect_charge_via_bank_account_credit_card_request import CollectChargeViaBankAccountCreditCardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CollectChargeViaBankAccountCreditCardRequest from a JSON string
collect_charge_via_bank_account_credit_card_request_instance = CollectChargeViaBankAccountCreditCardRequest.from_json(json)
# print the JSON string representation of the object
print(CollectChargeViaBankAccountCreditCardRequest.to_json())

# convert the object into a dict
collect_charge_via_bank_account_credit_card_request_dict = collect_charge_via_bank_account_credit_card_request_instance.to_dict()
# create an instance of CollectChargeViaBankAccountCreditCardRequest from a dict
collect_charge_via_bank_account_credit_card_request_from_dict = CollectChargeViaBankAccountCreditCardRequest.from_dict(collect_charge_via_bank_account_credit_card_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


