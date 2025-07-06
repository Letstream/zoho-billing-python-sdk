# CollectChargeViaBankAccountCreditCardResponsePaymentCustomFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Index of the custom field. It can hold any value from 1 to 10. | [optional] 
**value** | **str** | Value of the Custom Field | [optional] 
**label** | **str** | Label of the Custom Field | [optional] 
**data_type** | **str** | Data type of the custom field. | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.collect_charge_via_bank_account_credit_card_response_payment_custom_fields_inner import CollectChargeViaBankAccountCreditCardResponsePaymentCustomFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CollectChargeViaBankAccountCreditCardResponsePaymentCustomFieldsInner from a JSON string
collect_charge_via_bank_account_credit_card_response_payment_custom_fields_inner_instance = CollectChargeViaBankAccountCreditCardResponsePaymentCustomFieldsInner.from_json(json)
# print the JSON string representation of the object
print(CollectChargeViaBankAccountCreditCardResponsePaymentCustomFieldsInner.to_json())

# convert the object into a dict
collect_charge_via_bank_account_credit_card_response_payment_custom_fields_inner_dict = collect_charge_via_bank_account_credit_card_response_payment_custom_fields_inner_instance.to_dict()
# create an instance of CollectChargeViaBankAccountCreditCardResponsePaymentCustomFieldsInner from a dict
collect_charge_via_bank_account_credit_card_response_payment_custom_fields_inner_from_dict = CollectChargeViaBankAccountCreditCardResponsePaymentCustomFieldsInner.from_dict(collect_charge_via_bank_account_credit_card_response_payment_custom_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


