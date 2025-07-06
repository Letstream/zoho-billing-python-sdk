# InvoiceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **str** | Unique ID generated for an invoice. | [optional] 
**ach_payment_initiated** | **bool** | Set to true if ACH payment is initiated. | [optional] 
**invoice_number** | **str** | Unique ID (starts with INV) of an invoice. | [optional] 
**is_pre_gst** | **bool** | Applicable for transactions that fall before july 1, 2017 | [optional] 
**place_of_supply** | **str** | Place where the goods/services are supplied to. (If not given, &lt;code&gt;place of contact&lt;/code&gt; given for the contact will be taken) | [optional] 
**gst_no** | **str** | 15 digit GST identification number of the customer. | [optional] 
**gst_treatment** | **str** | Choose whether the contact is GST registered/unregistered/consumer/overseas. Allowed values are &lt;code&gt; business_gst &lt;/code&gt; , &lt;code&gt; business_none &lt;/code&gt; , &lt;code&gt; overseas &lt;/code&gt; , &lt;code&gt; consumer &lt;/code&gt;. | [optional] 
**tax_treatment** | **str** | VAT treatment for the Estimate.Allowed Values:&lt;/br&gt;&lt;code&gt;home_country_mexico&lt;/code&gt;,&lt;code&gt;border_region_mexico&lt;/code&gt;,&lt;code&gt;non_mexico&lt;/code&gt; supported only for &lt;b&gt;MX&lt;/b&gt;. | [optional] 
**cfdi_usage** | **str** | Choose CFDI Usage. Allowed values:&lt;/br&gt;&lt;code&gt;acquisition_of_merchandise&lt;/code&gt;, &lt;code&gt;return_discount_bonus&lt;/code&gt;, &lt;code&gt;general_expense&lt;/code&gt;, &lt;code&gt;buildings&lt;/code&gt;, &lt;code&gt;furniture_office_equipment&lt;/code&gt;, &lt;code&gt;transport_equipment&lt;/code&gt;, &lt;code&gt;computer_equipmentdye_molds_tools&lt;/code&gt;, &lt;code&gt;telephone_communication&lt;/code&gt;, &lt;code&gt;satellite_communication&lt;/code&gt;, &lt;code&gt;other_machinery_equipment&lt;/code&gt;, &lt;code&gt;hospital_expense&lt;/code&gt;, &lt;code&gt;medical_expense_disability&lt;/code&gt;, &lt;code&gt;funeral_expense&lt;/code&gt;, &lt;code&gt;donation&lt;/code&gt;, &lt;code&gt;interest_mortage_loans&lt;/code&gt;, &lt;code&gt;contribution_sar&lt;/code&gt;, &lt;code&gt;medical_expense_insurance_pormium&lt;/code&gt;, &lt;code&gt;school_transportation_expense&lt;/code&gt;, &lt;code&gt;deposit_saving_account&lt;/code&gt;, &lt;code&gt;payment_educational_service&lt;/code&gt;, &lt;code&gt;no_tax_effect&lt;/code&gt;, &lt;code&gt;payment&lt;/code&gt;, &lt;code&gt;payroll&lt;/code&gt;. | [optional] 
**vat_treatment** | **str** | (Optional) VAT treatment for the invoices. VAT treatment denotes the location of the customer, if the customer resides in UK then the VAT treatment is &lt;code&gt;uk&lt;/code&gt;. If the customer is in an EU country &amp; VAT registered, you are resides in Northen Ireland and selling Goods then his VAT treatment is &lt;code&gt;eu_vat_registered&lt;/code&gt;, if he resides outside of the UK then his VAT treatment is &lt;code&gt;overseas&lt;/code&gt; (For Pre Brexit, this can be split as &lt;code&gt;eu_vat_registered&lt;/code&gt;, &lt;code&gt;eu_vat_not_registered&lt;/code&gt; and &lt;code&gt;non_eu&lt;/code&gt;). | [optional] 
**vat_reg_no** | **str** | Enter VAT registration number. | [optional] 
**var_date** | **str** | Date on which the invoice is paid. | [optional] 
**status** | **str** | Status of the invoice. It can be &lt;code&gt;paid&lt;/code&gt;, &lt;code&gt;sent&lt;/code&gt;, &lt;code&gt;overdue&lt;/code&gt;, &lt;code&gt;partially_paid&lt;/code&gt; or &lt;code&gt;void&lt;/code&gt;. | [optional] 
**payment_terms** | **int** | Payment terms in days e.g. 15, 30, 60. Invoice due date will be calculated based on this. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
**payment_terms_label** | **str** | Used to override the default payment terms label. Default value for 15 days is \&quot;Net 15 Days\&quot;. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
**due_date** | **str** | Date on which the invoice is due. If the invoice is not fully paid on or before this date, the status of the invoice will be changed to &lt;code&gt;overdue&lt;/code&gt;. If the invoice is only partially paid, its status will be &lt;code&gt;partially_paid&lt;/code&gt;. | [optional] 
**payment_expected_date** | **str** | A date to specify the expected payment date. | [optional] 
**last_payment_date** | **str** | The last payment date of the invoice | [optional] 
**reference_number** | **str** | Reference number of the invoice for which payment is made. | [optional] 
**customer_id** | **str** | Customer ID of the customer to whom the invoice is raised. | [optional] 
**customer_name** | **str** | Name of the customer to whom the invoice is raised. | [optional] 
**contact_persons** | [**List[ContactPersonsInner]**](ContactPersonsInner.md) | The IDs of the contact person associated with the contact. | [optional] 
**currency_id** | **str** | The currenct id of the currency | [optional] 
**currency_code** | **str** | The customer&#39;s currency code. | [optional] 
**exchange_rate** | **float** | Exchange-Rate for the currency. | [optional] 
**discount** | **float** | Discount applied to the invoice. It can be either in % or in amount. e.g. 12.5% or 190. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
**is_discount_before_tax** | **bool** | Check if discount is exclusive of tax | [optional] 
**discount_type** | **str** | Type of discount. Allowed values: &lt;code&gt;entity_level&lt;/code&gt; and &lt;code&gt;item_level&lt;/code&gt;. | [optional] 
**is_inclusive_tax** | **bool** | To check if discount is inclusive of tax | [optional] 
**is_viewed_by_client** | **bool** | Check if invoice is viewed by client | [optional] 
**has_attachment** | **object** | Denotes whether a customer has any attachments associated with it. | [optional] 
**client_viewed_time** | **str** | Time when client viewed the statement | [optional] 
**invoice_items** | [**List[InvoiceResponseInvoiceItemsInner]**](InvoiceResponseInvoiceItemsInner.md) | Items listed in invoice | [optional] 
**shipping_charge** | **str** | Shipping charges applied to the invoice. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
**adjustment** | **float** | Adjustments made to the invoice. | [optional] 
**adjustment_description** | **str** | Customize the adjustment description. E.g. Rounding off. | [optional] 
**sub_total** | **float** | The sub total of the all items | [optional] 
**tax_total** | **float** | The total amount of the tax levied | [optional] 
**total** | **float** | Total amount to be paid for the invoice. This would be the sum of individual costs of all items involved in the invoice. Total is determined only after customer credits (if any) are applied. | [optional] 
**taxes** | [**List[TaxesInner]**](TaxesInner.md) | List of the taxes levied | [optional] 
**payment_reminder_enabled** | **bool** | Boolean to check if reminders have been enabled | [optional] 
**payment_made** | **float** | Payments can be made in multiple instalments. payment_made refers to the amount paid for the invoice in the respective instalment. | [optional] 
**credits_applied** | **float** | Credits applied for the invoice. | [optional] 
**tax_amount_withheld** | **float** | The tax amount which has been withheld | [optional] 
**balance** | **float** | The unpaid amount of an invoice. | [optional] 
**write_off_amount** | **float** | The unpaid amount of an invoice that is written off. | [optional] 
**allow_partial_payments** | **bool** | Boolean to check if partial payments are allowed for the contact | [optional] 
**price_precision** | **int** | The precision value on the price | [optional] 
**payment_options** | [**PaymentOptions**](PaymentOptions.md) |  | [optional] 
**is_emailed** | **bool** | Boolean check to see if the mail has been sent | [optional] 
**reminders_sent** | **int** | The number of reminders sent | [optional] 
**last_reminder_sent_date** | **str** | The date the last email was sent | [optional] 
**billing_address** | [**BillingAddress**](BillingAddress.md) |  | [optional] 
**shipping_address** | [**ShippingAddress**](ShippingAddress.md) |  | [optional] 
**notes** | **str** | The notes added below expressing gratitude or for conveying some information. | [optional] 
**terms** | **str** | The terms added below expressing gratitude or for conveying some information. | [optional] 
**custom_fields** | **List[str]** | Additional fields for the invoices. | [optional] 
**template_id** | **str** | ID of the pdf template associated with the invoice. | [optional] 
**template_name** | **str** | Name of the invoice template used | [optional] 
**created_time** | **str** | Time when the invoice was created. | [optional] 
**last_modified_time** | **str** | Date of last modification of the invoice | [optional] 
**attachment_name** | **str** | Name of the file attached | [optional] 
**can_send_in_mail** | **object** | Set to true if all the attachments of this invoice can be attached in Invoice Emails. | [optional] 
**salesperson_id** | **str** | Unique Id to denote the sales person. | [optional] 
**salesperson_name** | **str** | Name of the sales person associated with the invoice for offline payments. | [optional] 
**invoice_url** | **str** | Url which corresponds to the invoice. | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.invoice_response import InvoiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceResponse from a JSON string
invoice_response_instance = InvoiceResponse.from_json(json)
# print the JSON string representation of the object
print(InvoiceResponse.to_json())

# convert the object into a dict
invoice_response_dict = invoice_response_instance.to_dict()
# create an instance of InvoiceResponse from a dict
invoice_response_from_dict = InvoiceResponse.from_dict(invoice_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


