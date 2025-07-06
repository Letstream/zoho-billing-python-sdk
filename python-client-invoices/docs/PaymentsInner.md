# PaymentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_id** | **str** | The payment ID of the payment made for the invoice. | [optional] 
**payment_mode** | **str** | The mode in which payment is made for the invoice. This can be &lt;code&gt;check&lt;/code&gt;, &lt;code&gt;cash&lt;/code&gt;, &lt;code&gt;creditcard&lt;/code&gt;, &lt;code&gt;banktransfer&lt;/code&gt;, &lt;code&gt;bankremittance&lt;/code&gt;, &lt;code&gt;autotransaction&lt;/code&gt; or &lt;code&gt;others&lt;/code&gt;. | [optional] 
**invoice_payment_id** | **str** | Unique ID generated for an instalment of payment made for a particular invoice. | [optional] 
**gateway_transaction_id** | **str** | Gateway transaction ID provided for the payment made to the invoice. This is applicable only if &lt;code&gt;payment_mode&lt;/code&gt; is autotransaction. | [optional] 
**description** | **str** | Small description of the payment made for the invoice. | [optional] 
**var_date** | **str** | Date on which the invoice is paid. | [optional] 
**reference_number** | **str** | Reference number of the invoice for which payment is made. | [optional] 
**amount** | **float** | Amount paid for the invoice. | [optional] 
**bank_charges** | **float** | Denotes any additional bank charges. | [optional] 
**exchange_rate** | **float** | Exchange-Rate for the currency. | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.payments_inner import PaymentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentsInner from a JSON string
payments_inner_instance = PaymentsInner.from_json(json)
# print the JSON string representation of the object
print(PaymentsInner.to_json())

# convert the object into a dict
payments_inner_dict = payments_inner_instance.to_dict()
# create an instance of PaymentsInner from a dict
payments_inner_from_dict = PaymentsInner.from_dict(payments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


