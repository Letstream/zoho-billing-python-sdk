# ListInvoicePaymentsResponsePaymentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_id** | **str** | The payment ID of the payment made for the invoice. | [optional] 
**payment_number** | **int** | The payment Serial Number | [optional] 
**invoice_id** | **str** | Unique ID generated for an invoice. | [optional] 
**invoice_payment_id** | **str** | Unique ID generated for an instalment of payment made for a particular invoice. | [optional] 
**payment_mode** | **str** | The mode in which payment is made for the invoice. This can be &lt;code&gt;check&lt;/code&gt;, &lt;code&gt;cash&lt;/code&gt;, &lt;code&gt;creditcard&lt;/code&gt;, &lt;code&gt;banktransfer&lt;/code&gt;, &lt;code&gt;bankremittance&lt;/code&gt;, &lt;code&gt;autotransaction&lt;/code&gt; or &lt;code&gt;others&lt;/code&gt;. | [optional] 
**description** | **str** | Small description of the payment made for the invoice. | [optional] 
**var_date** | **str** | Date on which the invoice is paid. | [optional] 
**reference_number** | **str** | Reference number of the invoice for which payment is made. | [optional] 
**exchange_rate** | **float** | Exchange-Rate for the currency. | [optional] 
**amount** | **float** | Amount paid for the invoice. | [optional] 
**tax_amount_withheld** | **float** | The tax amount which has been withheld | [optional] 
**online_transaction_id** | **str** | Unique ID of an online transaction | [optional] 
**is_single_invoice_payment** | **bool** | To check if invoice is paid in a single payment or multiple payments | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.list_invoice_payments_response_payments_inner import ListInvoicePaymentsResponsePaymentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListInvoicePaymentsResponsePaymentsInner from a JSON string
list_invoice_payments_response_payments_inner_instance = ListInvoicePaymentsResponsePaymentsInner.from_json(json)
# print the JSON string representation of the object
print(ListInvoicePaymentsResponsePaymentsInner.to_json())

# convert the object into a dict
list_invoice_payments_response_payments_inner_dict = list_invoice_payments_response_payments_inner_instance.to_dict()
# create an instance of ListInvoicePaymentsResponsePaymentsInner from a dict
list_invoice_payments_response_payments_inner_from_dict = ListInvoicePaymentsResponsePaymentsInner.from_dict(list_invoice_payments_response_payments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


