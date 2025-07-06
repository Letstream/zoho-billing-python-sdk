# RetrieveAHostedPageResponseDataInvoicePaymentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_id** | **str** | The payment ID of the payment made for the invoice. | [optional] 
**payment_mode** | **str** | The mode in which payment is made for the invoice. This can be &lt;code&gt;check&lt;/code&gt;, &lt;code&gt;cash&lt;/code&gt;, &lt;code&gt;creditcard&lt;/code&gt;, &lt;code&gt;banktransfer&lt;/code&gt;, &lt;code&gt;bankremittance&lt;/code&gt;, &lt;code&gt;autotransaction&lt;/code&gt; or &lt;code&gt;others&lt;/code&gt;. | [optional] 
**invoice_payment_id** | **str** | Unique ID generated for an instalment of payment made for a particular invoice. | [optional] 
**gateway_transaction_id** | **str** | Gateway transaction ID provided for the payment made to the invoice. This is applicable only if &lt;code&gt;payment_mode&lt;/code&gt; is autotransaction. | [optional] 
**description** | **str** | Description of the plan exclusive to this subscription. This will be displayed in place of the plan name in invoices generated for this subscription. | [optional] 
**var_date** | **str** | Date at which the comment was commented. | [optional] 
**reference_number** | **str** | Reference number of the invoice for which payment is made. | [optional] 
**amount** | **float** | The amount that needs to be charged for the subscription. | [optional] 
**exchange_rate** | **float** | This will be the exchange rate provided for the organization&#39;s currency and the customer&#39;s currency. The subscription fee would be the multiplicative product of the original price and the exchange rate. | [optional] 

## Example

```python
from ls_zoho_billing_hosted_pages.models.retrieve_a_hosted_page_response_data_invoice_payments_inner import RetrieveAHostedPageResponseDataInvoicePaymentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveAHostedPageResponseDataInvoicePaymentsInner from a JSON string
retrieve_a_hosted_page_response_data_invoice_payments_inner_instance = RetrieveAHostedPageResponseDataInvoicePaymentsInner.from_json(json)
# print the JSON string representation of the object
print(RetrieveAHostedPageResponseDataInvoicePaymentsInner.to_json())

# convert the object into a dict
retrieve_a_hosted_page_response_data_invoice_payments_inner_dict = retrieve_a_hosted_page_response_data_invoice_payments_inner_instance.to_dict()
# create an instance of RetrieveAHostedPageResponseDataInvoicePaymentsInner from a dict
retrieve_a_hosted_page_response_data_invoice_payments_inner_from_dict = RetrieveAHostedPageResponseDataInvoicePaymentsInner.from_dict(retrieve_a_hosted_page_response_data_invoice_payments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


