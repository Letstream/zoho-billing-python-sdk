# RetrieveAnInvoiceResponseInvoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **str** | Unique ID generated for an invoice. | [optional] 
**number** | **str** | Unique invoice number (starts with INV) generated for an invoice which will be used to display in interface and invoices. | [optional] 
**status** | **str** | Status of the invoice. It can be &lt;code&gt;paid&lt;/code&gt;, &lt;code&gt;sent&lt;/code&gt;, &lt;code&gt;overdue&lt;/code&gt;, &lt;code&gt;partially_paid&lt;/code&gt; or &lt;code&gt;void&lt;/code&gt;. | [optional] 
**invoice_date** | **str** | The date on which the invoice is raised. | [optional] 
**due_date** | **str** | Date on which the invoice is due. If the invoice is not fully paid on or before this date, the status of the invoice will be changed to &lt;code&gt;overdue&lt;/code&gt;. If the invoice is only partially paid, its status will be &lt;code&gt;partially_paid&lt;/code&gt;. | [optional] 
**payment_expected_date** | **str** | A date to specify the expected payment date. | [optional] 
**ach_payment_initiated** | **bool** | Set to true if ACH payment is initiated. | [optional] 
**transaction_type** | **str** | Type of the transaction made. | [optional] 
**customer_id** | **str** | Customer ID of the customer to whom the invoice is raised. | [optional] 
**customer_name** | **str** | Name of the customer to whom the invoice is raised. | [optional] 
**email** | **str** | Email address of the customer. | [optional] 
**invoice_items** | [**List[RetrieveAnInvoiceResponseInvoiceInvoiceItemsInner]**](RetrieveAnInvoiceResponseInvoiceInvoiceItemsInner.md) | The list of items which are all included in the invoice. Each item object will have &lt;code&gt;item_id&lt;/code&gt;, &lt;code&gt;name&lt;/code&gt;, &lt;code&gt;code&lt;/code&gt;, &lt;code&gt;price&lt;/code&gt;, &lt;code&gt;quantity&lt;/code&gt; and &lt;code&gt;item_total&lt;/code&gt;. description: Small description about the Invoice item. example: \&quot;Charges for this duration (from 16-April-2016 to 8-June-2016)\&quot; | [optional] 
**coupons** | [**List[CouponsInner]**](CouponsInner.md) | The array of objects which contains the details of the added coupon. &lt;code&gt;coupon_code&lt;/code&gt; and &lt;code&gt;discount_amount&lt;/code&gt; are applied to the invoice total. | [optional] 
**credits** | [**List[RetrieveAnInvoiceResponseInvoiceCreditsInner]**](RetrieveAnInvoiceResponseInvoiceCreditsInner.md) |  | [optional] 
**total** | **float** | Total amount to be paid for the invoice. This would be the sum of individual costs of all items involved in the invoice. Total is determined only after customer credits (if any) are applied. | [optional] 
**payment_made** | **float** | Payments can be made in multiple instalments. payment_made refers to the amount paid for the invoice in the respective instalment. | [optional] 
**balance** | **float** | The unpaid amount of an invoice. | [optional] 
**credits_applied** | **float** | Credits applied for the invoice. | [optional] 
**write_off_amount** | **float** | The unpaid amount of an invoice that is written off. | [optional] 
**payments** | [**List[RetrieveAnInvoiceResponseInvoicePaymentsInner]**](RetrieveAnInvoiceResponseInvoicePaymentsInner.md) | List of payment objects. Each object will contain &lt;code&gt;payment_id&lt;/code&gt;, &lt;code&gt;payment_mode&lt;/code&gt;, &lt;code&gt;invoice_payment_id&lt;/code&gt;, &lt;code&gt;gateway_transaction_id&lt;/code&gt;, &lt;code&gt;description&lt;/code&gt;, &lt;code&gt;date&lt;/code&gt;, &lt;code&gt;reference_number&lt;/code&gt;, &lt;code&gt;amount&lt;/code&gt; and &lt;code&gt;bank_charges&lt;/code&gt;. | [optional] 
**currency_code** | **str** | The customer&#39;s currency code. | [optional] 
**currency_symbol** | **str** | The customer&#39;s currency symbol. | [optional] 
**created_time** | **str** | Time when the invoice was created. | [optional] 
**updated_time** | **str** | Time when the invoice details were last updated. | [optional] 
**salesperson_id** | **str** | Unique Id to denote the sales person. | [optional] 
**salesperson_name** | **str** | Name of the sales person associated with the invoice for offline payments. | [optional] 
**invoice_url** | **str** | Url which corresponds to the invoice. | [optional] 
**billing_address** | [**RetrieveAnInvoiceResponseInvoiceBillingAddress**](RetrieveAnInvoiceResponseInvoiceBillingAddress.md) |  | [optional] 
**shipping_address** | [**ShippingAddress**](ShippingAddress.md) |  | [optional] 
**comments** | [**List[RetrieveAnInvoiceResponseInvoiceCommentsInner]**](RetrieveAnInvoiceResponseInvoiceCommentsInner.md) | Lists the comments added by the system or by user. | [optional] 
**custom_fields** | [**List[RetrieveAnInvoiceResponseInvoiceCustomFieldsInner]**](RetrieveAnInvoiceResponseInvoiceCustomFieldsInner.md) | Additional fields for the invoices. | [optional] 
**can_send_in_mail** | **object** | Set to true if all the attachments of this invoice can be attached in Invoice Emails. | [optional] 
**documents** | [**List[DocumentsInner]**](DocumentsInner.md) | List of files attached to a particular customer. | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.retrieve_an_invoice_response_invoice import RetrieveAnInvoiceResponseInvoice

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveAnInvoiceResponseInvoice from a JSON string
retrieve_an_invoice_response_invoice_instance = RetrieveAnInvoiceResponseInvoice.from_json(json)
# print the JSON string representation of the object
print(RetrieveAnInvoiceResponseInvoice.to_json())

# convert the object into a dict
retrieve_an_invoice_response_invoice_dict = retrieve_an_invoice_response_invoice_instance.to_dict()
# create an instance of RetrieveAnInvoiceResponseInvoice from a dict
retrieve_an_invoice_response_invoice_from_dict = RetrieveAnInvoiceResponseInvoice.from_dict(retrieve_an_invoice_response_invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


