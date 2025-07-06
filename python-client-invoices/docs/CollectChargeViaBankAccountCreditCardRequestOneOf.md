# CollectChargeViaBankAccountCreditCardRequestOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Unique ID of the bank account. If you are collecting charge via credit card, use &lt;code&gt;card_id&lt;/code&gt; (Card ID of the card associated with the transaction) | 

## Example

```python
from ls_zoho_billing_invoices.models.collect_charge_via_bank_account_credit_card_request_one_of import CollectChargeViaBankAccountCreditCardRequestOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of CollectChargeViaBankAccountCreditCardRequestOneOf from a JSON string
collect_charge_via_bank_account_credit_card_request_one_of_instance = CollectChargeViaBankAccountCreditCardRequestOneOf.from_json(json)
# print the JSON string representation of the object
print(CollectChargeViaBankAccountCreditCardRequestOneOf.to_json())

# convert the object into a dict
collect_charge_via_bank_account_credit_card_request_one_of_dict = collect_charge_via_bank_account_credit_card_request_one_of_instance.to_dict()
# create an instance of CollectChargeViaBankAccountCreditCardRequestOneOf from a dict
collect_charge_via_bank_account_credit_card_request_one_of_from_dict = CollectChargeViaBankAccountCreditCardRequestOneOf.from_dict(collect_charge_via_bank_account_credit_card_request_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


