# PaymentResponseAutotransaction

If the payment mode is <code>autotransaction</code>, autotransaction information will be displayed in the autotransaction object. It contains <code>autotransaction_id</code>, <code>payment_gateway</code>, <code>gateway_transaction_id</code>, <code>card_id</code>, <code>last_four_digits</code>, <code>expiry_month</code> and <code>expiry_year</code>.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autotransaction_id** | **str** | Auto-transaction ID generated for the payment made. | [optional] 
**payment_gateway** | **str** | Name of the payment gateway associated with payment. | [optional] 
**gateway_transaction_id** | **str** | Transaction ID provided by the gateway for the transaction. | [optional] 
**gateway_error_message** | **str** | Gateway error message for a failed transaction. | [optional] 
**card_id** | **str** | Card ID of the card associated with the transaction. | [optional] 
**last_four_digits** | **int** | Last four digits of the card. | [optional] 
**expiry_month** | **int** | Expiry month of the card. | [optional] 
**expiry_year** | **int** | Expiry year of the card. | [optional] 

## Example

```python
from ls_zoho_billing_payments.models.payment_response_autotransaction import PaymentResponseAutotransaction

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentResponseAutotransaction from a JSON string
payment_response_autotransaction_instance = PaymentResponseAutotransaction.from_json(json)
# print the JSON string representation of the object
print(PaymentResponseAutotransaction.to_json())

# convert the object into a dict
payment_response_autotransaction_dict = payment_response_autotransaction_instance.to_dict()
# create an instance of PaymentResponseAutotransaction from a dict
payment_response_autotransaction_from_dict = PaymentResponseAutotransaction.from_dict(payment_response_autotransaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


