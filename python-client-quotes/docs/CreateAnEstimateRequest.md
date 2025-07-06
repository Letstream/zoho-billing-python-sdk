# CreateAnEstimateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | Customer ID on the quote. | 
**contact_persons** | **List[str]** | Array of contact person(s) for whom quote has to be sent. | [optional] 
**template_id** | **str** | ID of the template used for the quote | [optional] 
**place_of_supply** | **str** | Place where the goods/services are supplied to. (If not given, &lt;code&gt;place of contact&lt;/code&gt; given for the contact will be taken) | [optional] 
**gst_treatment** | **str** | Choose whether the contact is GST registered/unregistered/consumer/overseas. Allowed values are &lt;code&gt; business_gst &lt;/code&gt; , &lt;code&gt; business_none &lt;/code&gt; , &lt;code&gt; overseas &lt;/code&gt; , &lt;code&gt; consumer &lt;/code&gt;. | [optional] 
**tax_treatment** | **str** | VAT treatment for the quote.Allowed Values:&lt;/br&gt;&lt;code&gt;home_country_mexico&lt;/code&gt;,&lt;code&gt;border_region_mexico&lt;/code&gt;,&lt;code&gt;non_mexico&lt;/code&gt; supported only for &lt;b&gt;MX&lt;/b&gt;. | [optional] 
**gst_no** | **str** | 15 digit GST identification number of the customer. | [optional] 
**estimate_number** | **str** | quote Serial number. | [optional] 
**reference_number** | **str** | Transaction reference number. | [optional] 
**var_date** | **str** | Date on the quote. | [optional] 
**expiry_date** | **str** | The date of expiration of the quotes | [optional] 
**exchange_rate** | **float** | Foreign Exchange rate of the currency. | [optional] 
**discount** | **float** | Discount applied to the invoice. It can be either in % or in amount. e.g. 12.5% or 190. | [optional] 
**is_discount_before_tax** | **bool** | Used to specify how the discount has to applied. Either before or after the calculation of tax. | [optional] 
**discount_type** | **str** | How the discount is specified. Allowed values are entity_level or item_level.Allowed Values: &lt;code&gt;entity_level&lt;/code&gt; and &lt;code&gt;item_level&lt;/code&gt; | [optional] 
**is_inclusive_tax** | **bool** | Used to specify whether the line item rates are inclusive or exclusive of tax. | [optional] 
**custom_body** | **str** | Custom content of the email | [optional] 
**custom_subject** | **str** | Subjet for the email to be sent | [optional] 
**salesperson_name** | **str** | Name of the sales person. | [optional] 
**custom_fields** | [**List[CreateAnEstimateRequestCustomFieldsInner]**](CreateAnEstimateRequestCustomFieldsInner.md) | Custom fields for an quote. | [optional] 
**line_items** | [**List[CreateAnEstimateRequestLineItemsInner]**](CreateAnEstimateRequestLineItemsInner.md) | Line items of an quote. | 
**notes** | **str** | The notes added below expressing gratitude or for conveying some information. | [optional] 
**terms** | **str** | Enlist the terms &amp; conditions for quote | [optional] 
**shipping_charge** | **str** | Shipping charges applied to the invoice. | [optional] 
**adjustment** | **float** | Adjustments made to the invoice. | [optional] 
**adjustment_description** | **str** | Customize the adjustment description. E.g. Rounding off value. | [optional] 
**tax_id** | **str** | ID of the tax or tax group applied to the quote | [optional] 
**tax_exemption_id** | **str** | ID of the tax exemption. | [optional] 
**tax_authority_id** | **str** | ID of the tax authority. Tax authority depends on the location of the customer. For example, if the customer is located in NY, then the tax authority is NY tax authority. | [optional] 
**avatax_use_code** | **str** | Used to group like customers for exemption purposes. It is a custom value that links customers to a tax rule. Select from Avalara [standard codes][1] or enter a custom code. | [optional] 
**avatax_tax_code** | **str** | A tax code is a unique label used to group Items (products, services, or charges) together. &lt;code&gt;Maximum length [25]&lt;/code&gt; | [optional] 
**avatax_exempt_no** | **str** | Exemption certificate number of the customer. | [optional] 
**vat_treatment** | **str** | (Optional) VAT treatment for the quotes. VAT treatment denotes the location of the customer, if the customer resides in UK then the VAT treatment is &lt;code&gt;uk&lt;/code&gt;. If the customer is in an EU country &amp; VAT registered, you are resides in Northen Ireland and selling Goods then his VAT treatment is &lt;code&gt;eu_vat_registered&lt;/code&gt;, if he resides outside of the UK then his VAT treatment is &lt;code&gt;overseas&lt;/code&gt; (For Pre Brexit, this can be split as &lt;code&gt;eu_vat_registered&lt;/code&gt;, &lt;code&gt;eu_vat_not_registered&lt;/code&gt; and &lt;code&gt;non_eu&lt;/code&gt;). | [optional] 
**project_id** | **str** | ID of the project | [optional] 

## Example

```python
from ls_zoho_billing_quotes.models.create_an_estimate_request import CreateAnEstimateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAnEstimateRequest from a JSON string
create_an_estimate_request_instance = CreateAnEstimateRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAnEstimateRequest.to_json())

# convert the object into a dict
create_an_estimate_request_dict = create_an_estimate_request_instance.to_dict()
# create an instance of CreateAnEstimateRequest from a dict
create_an_estimate_request_from_dict = CreateAnEstimateRequest.from_dict(create_an_estimate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


