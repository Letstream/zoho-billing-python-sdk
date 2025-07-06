# CreateAnInvoiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | Customer ID of the customer to whom the invoice is raised. | 
**contact_persons** | [**List[ContactPersonsInner]**](ContactPersonsInner.md) | The IDs of the contact person associated with the contact. | [optional] 
**invoice_number** | **str** | Unique ID (starts with INV) of an invoice. | [optional] 
**reference_number** | **str** | Reference number of the invoice for which payment is made. | [optional] 
**place_of_supply** | **str** | Place where the goods/services are supplied to. (If not given, &lt;code&gt;place of contact&lt;/code&gt; given for the contact will be taken) | [optional] 
**vat_treatment** | **str** | (Optional) VAT treatment for the invoices. VAT treatment denotes the location of the customer, if the customer resides in UK then the VAT treatment is &lt;code&gt;uk&lt;/code&gt;. If the customer is in an EU country &amp; VAT registered, you are resides in Northen Ireland and selling Goods then his VAT treatment is &lt;code&gt;eu_vat_registered&lt;/code&gt;, if he resides outside of the UK then his VAT treatment is &lt;code&gt;overseas&lt;/code&gt; (For Pre Brexit, this can be split as &lt;code&gt;eu_vat_registered&lt;/code&gt;, &lt;code&gt;eu_vat_not_registered&lt;/code&gt; and &lt;code&gt;non_eu&lt;/code&gt;). | [optional] 
**gst_treatment** | **str** | Choose whether the contact is GST registered/unregistered/consumer/overseas. Allowed values are &lt;code&gt; business_gst &lt;/code&gt; , &lt;code&gt; business_none &lt;/code&gt; , &lt;code&gt; overseas &lt;/code&gt; , &lt;code&gt; consumer &lt;/code&gt;. | [optional] 
**tax_treatment** | **str** | VAT treatment for the Estimate.Allowed Values:&lt;/br&gt;&lt;code&gt;home_country_mexico&lt;/code&gt;,&lt;code&gt;border_region_mexico&lt;/code&gt;,&lt;code&gt;non_mexico&lt;/code&gt; supported only for &lt;b&gt;MX&lt;/b&gt;. | [optional] 
**cfdi_usage** | **str** | Choose CFDI Usage. Allowed values:&lt;/br&gt;&lt;code&gt;acquisition_of_merchandise&lt;/code&gt;, &lt;code&gt;return_discount_bonus&lt;/code&gt;, &lt;code&gt;general_expense&lt;/code&gt;, &lt;code&gt;buildings&lt;/code&gt;, &lt;code&gt;furniture_office_equipment&lt;/code&gt;, &lt;code&gt;transport_equipment&lt;/code&gt;, &lt;code&gt;computer_equipmentdye_molds_tools&lt;/code&gt;, &lt;code&gt;telephone_communication&lt;/code&gt;, &lt;code&gt;satellite_communication&lt;/code&gt;, &lt;code&gt;other_machinery_equipment&lt;/code&gt;, &lt;code&gt;hospital_expense&lt;/code&gt;, &lt;code&gt;medical_expense_disability&lt;/code&gt;, &lt;code&gt;funeral_expense&lt;/code&gt;, &lt;code&gt;donation&lt;/code&gt;, &lt;code&gt;interest_mortage_loans&lt;/code&gt;, &lt;code&gt;contribution_sar&lt;/code&gt;, &lt;code&gt;medical_expense_insurance_pormium&lt;/code&gt;, &lt;code&gt;school_transportation_expense&lt;/code&gt;, &lt;code&gt;deposit_saving_account&lt;/code&gt;, &lt;code&gt;payment_educational_service&lt;/code&gt;, &lt;code&gt;no_tax_effect&lt;/code&gt;, &lt;code&gt;payment&lt;/code&gt;, &lt;code&gt;payroll&lt;/code&gt;. | [optional] 
**gst_no** | **str** | 15 digit GST identification number of the customer. | [optional] 
**template_id** | **str** | ID of the pdf template associated with the invoice. | [optional] 
**var_date** | **str** | Date on which the invoice is paid. | 
**payment_terms** | **int** | Payment terms in days e.g. 15, 30, 60. Invoice due date will be calculated based on this. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
**payment_terms_label** | **str** | Used to override the default payment terms label. Default value for 15 days is \&quot;Net 15 Days\&quot;. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
**due_date** | **str** | Date on which the invoice is due. If the invoice is not fully paid on or before this date, the status of the invoice will be changed to &lt;code&gt;overdue&lt;/code&gt;. If the invoice is only partially paid, its status will be &lt;code&gt;partially_paid&lt;/code&gt;. | [optional] 
**discount** | **float** | Discount applied to the invoice. It can be either in % or in amount. e.g. 12.5% or 190. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
**is_discount_before_tax** | **bool** | Check if discount is exclusive of tax | [optional] 
**discount_type** | **str** | Type of discount. Allowed values: &lt;code&gt;entity_level&lt;/code&gt; and &lt;code&gt;item_level&lt;/code&gt;. | [optional] 
**is_inclusive_tax** | **bool** | To check if discount is inclusive of tax | [optional] 
**exchange_rate** | **float** | Exchange-Rate for the currency. | [optional] 
**invoiced_estimate_id** | **str** | ID of the invoice from which the invoice is created. | [optional] 
**salesperson_name** | **str** | Name of the sales person associated with the invoice for offline payments. | [optional] 
**custom_fields** | [**List[ItemCustomFieldsInner]**](ItemCustomFieldsInner.md) | Custom fields for an invoice. | [optional] 
**project_id** | **str** | Unique ID of the projet associated to an invoice | [optional] 
**invoice_items** | [**List[CreateAnInvoiceRequestInvoiceItemsInner]**](CreateAnInvoiceRequestInvoiceItemsInner.md) | Line items of an invoice. | 
**payment_options** | [**PaymentOptions**](PaymentOptions.md) |  | [optional] 
**allow_partial_payments** | **bool** | Boolean to check if partial payments are allowed for the contact | [optional] 
**custom_body** | **str** | Customized email content | [optional] 
**custom_subject** | **str** | Customized Subject line | [optional] 
**notes** | **str** | The notes added below expressing gratitude or for conveying some information. | [optional] 
**terms** | **str** | The terms added below expressing gratitude or for conveying some information. | [optional] 
**shipping_charge** | **str** | Shipping charges applied to the invoice. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
**adjustment** | **float** | Adjustments made to the invoice. | [optional] 
**adjustment_description** | **str** | Customize the adjustment description. E.g. Rounding off. | [optional] 
**reason** | **str** | Description of the attachment | [optional] 
**tax_authority_id** | **str** | ID of the tax authority. Tax authority depends on the location of the customer. For example, if the customer is located in NY, then the tax authority is NY tax authority. | [optional] 
**tax_exemption_id** | **str** | Unique Tax Exemption ID if you dont want to associate a tax to the plan. | [optional] 
**avatax_use_code** | **str** | Used to group like customers for exemption purposes. It is a custom value that links customers to a tax rule. Select from Avalara [standard codes][1] or enter a custom code. &lt;code&gt;Maximum length [25]&lt;/code&gt; | [optional] 
**avatax_tax_code** | **str** | A tax code is a unique label used to group Items (products, services, or charges) together. &lt;code&gt;Maximum length [25]&lt;/code&gt; | [optional] 
**avatax_exempt_no** | **str** | Exemption certificate number of the customer. &lt;code&gt;Maximum length [25]&lt;/code&gt; | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.create_an_invoice_request import CreateAnInvoiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAnInvoiceRequest from a JSON string
create_an_invoice_request_instance = CreateAnInvoiceRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAnInvoiceRequest.to_json())

# convert the object into a dict
create_an_invoice_request_dict = create_an_invoice_request_instance.to_dict()
# create an instance of CreateAnInvoiceRequest from a dict
create_an_invoice_request_from_dict = CreateAnInvoiceRequest.from_dict(create_an_invoice_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


