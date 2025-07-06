# CollectChargeViaBankAccountCreditCardResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**payment** | [**CollectChargeViaBankAccountCreditCardResponsePayment**](CollectChargeViaBankAccountCreditCardResponsePayment.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.collect_charge_via_bank_account_credit_card_response import CollectChargeViaBankAccountCreditCardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CollectChargeViaBankAccountCreditCardResponse from a JSON string
collect_charge_via_bank_account_credit_card_response_instance = CollectChargeViaBankAccountCreditCardResponse.from_json(json)
# print the JSON string representation of the object
print(CollectChargeViaBankAccountCreditCardResponse.to_json())

# convert the object into a dict
collect_charge_via_bank_account_credit_card_response_dict = collect_charge_via_bank_account_credit_card_response_instance.to_dict()
# create an instance of CollectChargeViaBankAccountCreditCardResponse from a dict
collect_charge_via_bank_account_credit_card_response_from_dict = CollectChargeViaBankAccountCreditCardResponse.from_dict(collect_charge_via_bank_account_credit_card_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


