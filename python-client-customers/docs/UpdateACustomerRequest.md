# UpdateACustomerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Name of the customer which will be displayed in the interface and invoices. | 
**salutation** | **str** | Salutation of the customer. | [optional] 
**first_name** | **str** | First name of the customer. | [optional] 
**last_name** | **str** | Last name of the customer. | [optional] 
**email** | **str** | Email address of the customer. | 
**tags** | [**List[TagsInner]**](TagsInner.md) |  | [optional] 
**company_name** | **str** | Registered name of the company the customer represents. | [optional] 
**phone** | **str** | Customer&#39;s landline or fixed-line number. | [optional] 
**mobile** | **str** | Customer&#39;s mobile phone number. | [optional] 
**billing_address** | [**BillingAddress**](BillingAddress.md) |  | [optional] 
**shipping_address** | [**ShippingAddress**](ShippingAddress.md) |  | [optional] 
**fax** | **str** | Fax number for the customer&#39;s billing address. | [optional] 
**currency_code** | **str** | Currency code of the currency in which the customer wants to pay. If currency_code is not specified here, the currency chosen in your Zoho Billing organization will be used for billing. | [optional] [default to 'currency_code chosen in organization profile settings']
**twitter** | **str** | Twitter profile of the customer. | [optional] 
**facebook** | **str** | Facebook profile of the customer. | [optional] 
**skype** | **str** | Skype ID of the customer | [optional] 
**is_portal_enabled** | **bool** | Is Client portal enabled for the customer. | [optional] 
**gst_no** | **str** | GSTIN Number for the customer. | [optional] 
**gst_treatment** | **str** | GST Treatment for the customer.&lt;br&gt;Allowed values for &lt;strong&gt;&lt;code&gt;gst_treatment&lt;/code&gt;&lt;/strong&gt; : &lt;br&gt;&lt;code&gt;business_gst&lt;/code&gt;, &lt;code&gt;business_none&lt;/code&gt;, &lt;code&gt;consumer&lt;/code&gt;, &lt;code&gt;overseas&lt;/code&gt;&lt;br&gt; &lt;code&gt;business_gst&lt;/code&gt; - For a GST Registered business owner. &lt;br&gt;&lt;code&gt;business_none&lt;/code&gt; - For a GST unregistered business owner. &lt;br&gt;&lt;code&gt;consumer&lt;/code&gt; - For a consumer. &lt;br&gt;&lt;code&gt;overseas&lt;/code&gt; - Customer for whom you export your goods/services. | [optional] 
**place_of_contact** | **str** | Customer&#39;s place of contact. | [optional] 
**vat_treatment** | **str** | VAT treatment of the contact.Allowed Values: &lt;br/&gt;&lt;code&gt;uk&lt;/code&gt; (A business that is located in the UK.),&lt;br/&gt;&lt;code&gt;eu_vat_registered&lt;/code&gt; (A business that is reg for VAT and trade goods between Northern Ireland and EU. This node is available only for organizations enabled for NI protocal in VAT Settings.) and&lt;br/&gt;&lt;code&gt;overseas&lt;/code&gt; (A business that is located outside UK. Pre Brexit, this was split as &lt;code&gt;eu_vat_registered&lt;/code&gt;, &lt;code&gt;eu_vat_not_registered&lt;/code&gt; and &lt;code&gt;non_eu&lt;/code&gt; ). | [optional] 
**vat_reg_no** | **str** | VAT Registration number of a contact with length should be between 2 and 12 characters. | [optional] 
**is_taxable** | **str** | Set to true if customer&#39;s transactions must be tax inclusive. | [optional] 
**tax_id** | **str** | Unique ID of the tax or tax group that can be collected from the contact. Tax can be given only if &lt;code&gt;is_taxable&lt;/code&gt; is &lt;code&gt;true&lt;/code&gt;. | [optional] 
**tax_authority_id** | **str** | Unique ID of the tax authority. Tax authority depends on the location of the customer. For example, if the customer is located in NY, then the tax authority is NY tax authority. | 
**tax_authority_name** | **str** | Unique name of the tax authority. Either tax_authority_id or tax_authority_name can be given. | 
**tax_exemption_id** | **str** | Unique ID of the tax exemption. | [optional] 
**tax_exemption_code** | **str** | Unique code of the tax exemption. | [optional] 
**default_templates** | [**CustomerResponseDefaultTemplates**](CustomerResponseDefaultTemplates.md) |  | [optional] 
**tax_reg_no** | **str** | 12 digit Tax Registration number of a contact with Tax treatment as &lt;/br&gt; &lt;code&gt;home_country_mexico&lt;/code&gt;, &lt;code&gt;border_region_mexico&lt;/code&gt;, &lt;code&gt;non_mexico&lt;/code&gt;.&lt;/br&gt; Consumers generic RFC: &lt;code&gt;XAXX010101000&lt;/code&gt;, Overseas generic RFC: &lt;code&gt;XEXX010101000&lt;/code&gt; | [optional] 
**tds_tax_id** | **str** | ID of the TDS tax. | [optional] 
**tax_treatment** | **str** | VAT treatment of the contact.Allowed Values:&lt;/br&gt; &lt;code&gt;home_country_mexico&lt;/code&gt; (A business that is located within MX)&lt;/br&gt;&lt;code&gt;border_region_mexico&lt;/code&gt; (A business that is located in the northern and southern border regions in MX)&lt;/br&gt;&lt;code&gt;non_mexico&lt;/code&gt; (A business that is located outside MX). | [optional] 
**tax_regime** | **str** | Tax Regime of the contact.Allowed Values: &lt;code&gt;general_legal_person&lt;/code&gt;, &lt;code&gt;legal_entities_non_profit&lt;/code&gt;, &lt;code&gt;resident_abroad&lt;/code&gt;, &lt;code&gt;production_cooperative_societies&lt;/code&gt;, &lt;code&gt;agricultural_livestock&lt;/code&gt;, &lt;code&gt;optional_group_of_companies&lt;/code&gt;, &lt;code&gt;coordinated&lt;/code&gt;, &lt;code&gt;simplified_trust&lt;/code&gt;, &lt;code&gt;wages_salaries_income&lt;/code&gt;, &lt;code&gt;lease&lt;/code&gt;, &lt;code&gt;property_disposal_acquisition&lt;/code&gt;, &lt;code&gt;other_income&lt;/code&gt;, &lt;code&gt;resident_abroad&lt;/code&gt;, &lt;code&gt;divident_income&lt;/code&gt;, &lt;code&gt;individual_business_professional&lt;/code&gt;, &lt;code&gt;interest_income&lt;/code&gt;, &lt;code&gt;income_obtaining_price&lt;/code&gt;, &lt;code&gt;no_tax_obligation&lt;/code&gt;, &lt;code&gt;tax_incorporation&lt;/code&gt;, &lt;code&gt;income_through_technology_platform&lt;/code&gt;, &lt;code&gt;simplified_trust&lt;/code&gt;. | [optional] 
**is_tds_registered** | **bool** | Boolean to check if tax is registered. | [optional] 
**custom_fields** | [**List[UpdateACustomerRequestCustomFieldsInner]**](UpdateACustomerRequestCustomFieldsInner.md) | Additional fields for customers. | [optional] 

## Example

```python
from ls_zoho_billing_customers.models.update_a_customer_request import UpdateACustomerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateACustomerRequest from a JSON string
update_a_customer_request_instance = UpdateACustomerRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateACustomerRequest.to_json())

# convert the object into a dict
update_a_customer_request_dict = update_a_customer_request_instance.to_dict()
# create an instance of UpdateACustomerRequest from a dict
update_a_customer_request_from_dict = UpdateACustomerRequest.from_dict(update_a_customer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


