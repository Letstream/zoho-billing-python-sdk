# UpdateAPaymentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | Customer ID of the customer involved in the payment. | 
**payment_mode** | **str** | Mode through which payment is made. This can be &lt;code&gt;check&lt;/code&gt;, &lt;code&gt;cash&lt;/code&gt;, &lt;code&gt;creditcard&lt;/code&gt;, &lt;code&gt;banktransfer&lt;/code&gt;, &lt;code&gt;bankremittance&lt;/code&gt;, &lt;code&gt;autotransaction&lt;/code&gt; or &lt;code&gt;others&lt;/code&gt;. | 
**amount** | **float** | Amount paid in the respective payment. | 
**var_date** | **str** | Date on which payment is made. | [optional] 
**reference_number** | **str** | Reference number generated for the payment. A string of your choice can also be used as the reference number. | [optional] 
**description** | **str** | Description about the payment. | [optional] 
**invoices** | [**List[CreateAPaymentRequestInvoicesInner]**](CreateAPaymentRequestInvoicesInner.md) | List of invoices associated with the payment. Each invoice object contains &lt;code&gt;invoice_id&lt;/code&gt;, &lt;code&gt;invoice_number&lt;/code&gt;, &lt;code&gt;date&lt;/code&gt;, &lt;code&gt;invoice_amount&lt;/code&gt;, &lt;code&gt;amount_applied&lt;/code&gt; and &lt;code&gt;balance_amount&lt;/code&gt;. | 
**exchange_rate** | **float** | Exchange rate for the currency used in the invoices and customer&#39;s currency. The payment amount would be the multiplicative product of the original amount and the exchange rate. | [optional] [default to 1]
**bank_charges** | **float** | Denotes any additional bank charges. | [optional] 
**tax_account_id** | **str** | Unique ID of the account which was used for transaction. | [optional] 
**account_id** | **str** | Unique ID of the account. | [optional] 
**custom_fields** | [**List[CreateAPaymentRequestCustomFieldsInner]**](CreateAPaymentRequestCustomFieldsInner.md) | Additional fields for the payments. | [optional] 

## Example

```python
from ls_zoho_billing_payments.models.update_a_payment_request import UpdateAPaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAPaymentRequest from a JSON string
update_a_payment_request_instance = UpdateAPaymentRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAPaymentRequest.to_json())

# convert the object into a dict
update_a_payment_request_dict = update_a_payment_request_instance.to_dict()
# create an instance of UpdateAPaymentRequest from a dict
update_a_payment_request_from_dict = UpdateAPaymentRequest.from_dict(update_a_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


