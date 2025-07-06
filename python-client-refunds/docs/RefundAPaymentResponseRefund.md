# RefundAPaymentResponseRefund


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refund_id** | **str** | Unique ID generated for a refund made. | [optional] 
**var_date** | **str** | The date on which refund is made. | [optional] 
**amount** | **float** | The amount to be refund. | [optional] 
**description** | **str** | A small description about the refund. | [optional] 
**reference_number** | **str** | Reference number for the refund made. A custom string can also be set as the reference number. | [optional] 
**refund_mode** | **str** | Mode through which refund is made. This can be &lt;code&gt;check&lt;/code&gt;, &lt;code&gt;cash&lt;/code&gt;, &lt;code&gt;creditcard&lt;/code&gt;, &lt;code&gt;banktransfer&lt;/code&gt;, &lt;code&gt;bankremittance&lt;/code&gt;, &lt;code&gt;autotransaction&lt;/code&gt; or &lt;code&gt;others&lt;/code&gt;. | [optional] 
**status** | **str** | Status of the refund made. This can be either &lt;code&gt;success&lt;/code&gt; or &lt;code&gt;failure&lt;/code&gt;. | [optional] 
**customer_id** | **str** | Customer ID of the customer to whom the refund is to be made. | [optional] 
**email** | **str** | Email address of the customer. | [optional] 
**creditnote** | [**RefundResponseCreditnote**](RefundResponseCreditnote.md) |  | [optional] 
**autotransaction** | [**RefundResponseAutotransaction**](RefundResponseAutotransaction.md) |  | [optional] 
**currency_code** | **str** | Customer&#39;s currency code. Refunds will be made in the customer&#39;s currency. | [optional] 
**currency_symbol** | **str** | The currency symbol of the currency chosen for the customer. | [optional] 

## Example

```python
from ls_zoho_billing_refunds.models.refund_a_payment_response_refund import RefundAPaymentResponseRefund

# TODO update the JSON string below
json = "{}"
# create an instance of RefundAPaymentResponseRefund from a JSON string
refund_a_payment_response_refund_instance = RefundAPaymentResponseRefund.from_json(json)
# print the JSON string representation of the object
print(RefundAPaymentResponseRefund.to_json())

# convert the object into a dict
refund_a_payment_response_refund_dict = refund_a_payment_response_refund_instance.to_dict()
# create an instance of RefundAPaymentResponseRefund from a dict
refund_a_payment_response_refund_from_dict = RefundAPaymentResponseRefund.from_dict(refund_a_payment_response_refund_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


