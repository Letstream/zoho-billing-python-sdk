# Autotransaction

If the refund mode is <code>autotransaction</code>, autotransaction information will be displayed in the autotransaction object. It contains <code>autotransaction_id</code>, <code>payment_gateway</code>, <code>gateway_transaction_id</code>, <code>card_id</code>, <code>last_four_digits</code>, <code>expiry_month</code> and <code>expiry_year</code>.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autotransaction_id** | **str** | Auto-transaction ID generated for the payment made. | [optional] 
**payment_gateway** | **str** | Name of the payment gateway associated with payment. | [optional] 
**gateway_transaction_id** | **str** | Transaction ID of the gateway associated with payment. | [optional] 
**gateway_error_message** | **str** | Gateway error for a failed transaction. | [optional] 
**card_id** | **str** | Card ID of the card. | [optional] 
**last_four_digits** | **int** | Last four digits of the card. | [optional] 
**expiry_month** | **int** | Expiry month of the card. | [optional] 
**expiry_year** | **int** | Expiry year of the card. | [optional] 

## Example

```python
from ls_zoho_billing_refunds.models.autotransaction import Autotransaction

# TODO update the JSON string below
json = "{}"
# create an instance of Autotransaction from a JSON string
autotransaction_instance = Autotransaction.from_json(json)
# print the JSON string representation of the object
print(Autotransaction.to_json())

# convert the object into a dict
autotransaction_dict = autotransaction_instance.to_dict()
# create an instance of Autotransaction from a dict
autotransaction_from_dict = Autotransaction.from_dict(autotransaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


