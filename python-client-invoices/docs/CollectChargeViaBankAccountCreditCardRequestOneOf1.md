# CollectChargeViaBankAccountCreditCardRequestOneOf1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_id** | **str** | Card ID of the card associated with the transaction. If you are collecting charge via bank account, use &lt;code&gt;account_id&lt;/code&gt; (Unique ID of the bank account) | 

## Example

```python
from ls_zoho_billing_invoices.models.collect_charge_via_bank_account_credit_card_request_one_of1 import CollectChargeViaBankAccountCreditCardRequestOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of CollectChargeViaBankAccountCreditCardRequestOneOf1 from a JSON string
collect_charge_via_bank_account_credit_card_request_one_of1_instance = CollectChargeViaBankAccountCreditCardRequestOneOf1.from_json(json)
# print the JSON string representation of the object
print(CollectChargeViaBankAccountCreditCardRequestOneOf1.to_json())

# convert the object into a dict
collect_charge_via_bank_account_credit_card_request_one_of1_dict = collect_charge_via_bank_account_credit_card_request_one_of1_instance.to_dict()
# create an instance of CollectChargeViaBankAccountCreditCardRequestOneOf1 from a dict
collect_charge_via_bank_account_credit_card_request_one_of1_from_dict = CollectChargeViaBankAccountCreditCardRequestOneOf1.from_dict(collect_charge_via_bank_account_credit_card_request_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


