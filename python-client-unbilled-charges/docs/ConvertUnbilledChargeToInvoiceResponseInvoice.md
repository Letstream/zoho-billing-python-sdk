# ConvertUnbilledChargeToInvoiceResponseInvoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **str** | Unique ID generated for an invoice. | [optional] 
**number** | **str** | Unique number (starts with INV) generated for display in interface. | [optional] 
**status** | **str** | Status of the unbilled charge. It can be &lt;code&gt;invoiced&lt;/code&gt;, &lt;code&gt;open&lt;/code&gt; | [optional] 
**invoice_date** | **str** | The date on which the invoice is raised. | [optional] 
**due_date** | **str** | Date on which the invoice is due. If the invoice is not fully paid on or before this date, the status of the invoice will be changed to &lt;code&gt;overdue&lt;/code&gt;. If the invoice is only partially paid, its status will be &lt;code&gt;partially_paid&lt;/code&gt;. | [optional] 
**payment_expected_date** | **str** | A date to specify the expected payment date. | [optional] 
**ach_payment_initiated** | **bool** | Set to true if ACH payment is initiated. | [optional] 
**transaction_type** | **str** | Type of the transaction made. | [optional] 
**customer_id** | **List[str]** | Customer ID of the customer to whom the unbilled charge was raised. | [optional] 
**customer_name** | **str** | Name of the customer to whom the unbilled charge was raised. | [optional] 
**email** | **str** | Email address of the customer. | [optional] 
**invoice_items** | [**List[InvoiceItemsInner]**](InvoiceItemsInner.md) |  | [optional] 
**coupons** | [**List[CouponsInner]**](CouponsInner.md) | The array of objects which contains the details of the added coupon. &lt;code&gt;coupon_code&lt;/code&gt; and &lt;code&gt;discount_amount&lt;/code&gt; are applied to the total. | [optional] 
**credits** | [**List[CreditsInner]**](CreditsInner.md) |  | [optional] 
**total** | **float** | Total amount to be paid. This would be the sum of individual costs of all items. | [optional] 
**payment_made** | **float** | Payments can be made in multiple instalments. payment_made refers to the amount paid for the invoice in the respective instalment. | [optional] 
**balance** | **float** | The unpaid amount of an invoice. | [optional] 
**credits_applied** | **float** | Credits applied for the invoice. | [optional] 
**write_off_amount** | **float** | The unpaid amount of an invoice that is written off. | [optional] 
**payments** | [**List[PaymentsInner]**](PaymentsInner.md) |  | [optional] 
**currency_code** | **str** | Currency code in which the payment is made. | [optional] 
**currency_symbol** | **str** | Customer&#39;s currency symbol. | [optional] 
**created_time** | **str** | Time when the unbilled charge was created. | [optional] 
**updated_time** | **str** | Time when the unbilled charge details were last updated. | [optional] 
**salesperson_id** | **str** | Unique Id to denote the sales person. | [optional] 
**salesperson_name** | **str** | Name of the sales person associated with the invoice for offline payments. | [optional] 
**invoice_url** | **str** | Url which corresponds to the invoice. | [optional] 
**billing_address** | [**BillingAddress**](BillingAddress.md) |  | [optional] 
**shipping_address** | [**ShippingAddress**](ShippingAddress.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_unbilled_charges.models.convert_unbilled_charge_to_invoice_response_invoice import ConvertUnbilledChargeToInvoiceResponseInvoice

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertUnbilledChargeToInvoiceResponseInvoice from a JSON string
convert_unbilled_charge_to_invoice_response_invoice_instance = ConvertUnbilledChargeToInvoiceResponseInvoice.from_json(json)
# print the JSON string representation of the object
print(ConvertUnbilledChargeToInvoiceResponseInvoice.to_json())

# convert the object into a dict
convert_unbilled_charge_to_invoice_response_invoice_dict = convert_unbilled_charge_to_invoice_response_invoice_instance.to_dict()
# create an instance of ConvertUnbilledChargeToInvoiceResponseInvoice from a dict
convert_unbilled_charge_to_invoice_response_invoice_from_dict = ConvertUnbilledChargeToInvoiceResponseInvoice.from_dict(convert_unbilled_charge_to_invoice_response_invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


