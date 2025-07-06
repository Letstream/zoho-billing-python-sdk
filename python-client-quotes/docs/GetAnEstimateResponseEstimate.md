# GetAnEstimateResponseEstimate

Quote to be created

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**estimate_id** | **str** | The  unique id of a particular quote | [optional] 
**estimate_number** | **str** | quote Serial number. | [optional] 
**var_date** | **str** | Date on the quote. | [optional] 
**reference_number** | **str** | Transaction reference number. | [optional] 
**is_pre_gst** | **bool** | Applicable for transactions that fall before july 1, 2017 | [optional] 
**place_of_supply** | **str** | Place where the goods/services are supplied to. (If not given, &lt;code&gt;place of contact&lt;/code&gt; given for the contact will be taken) | [optional] 
**gst_no** | **str** | 15 digit GST identification number of the customer. | [optional] 
**gst_treatment** | **str** | Choose whether the contact is GST registered/unregistered/consumer/overseas. Allowed values are &lt;code&gt; business_gst &lt;/code&gt; , &lt;code&gt; business_none &lt;/code&gt; , &lt;code&gt; overseas &lt;/code&gt; , &lt;code&gt; consumer &lt;/code&gt;. | [optional] 
**tax_treatment** | **str** | VAT treatment for the quote.Allowed Values:&lt;/br&gt;&lt;code&gt;home_country_mexico&lt;/code&gt;,&lt;code&gt;border_region_mexico&lt;/code&gt;,&lt;code&gt;non_mexico&lt;/code&gt; supported only for &lt;b&gt;MX&lt;/b&gt;. | [optional] 
**status** | **str** | Status of the quote. Allowed Values&lt;code&gt;draft&lt;/code&gt;, &lt;code&gt;sent&lt;/code&gt;,&lt;code&gt; invoiced &lt;/code&gt;, &lt;code&gt;accepted&lt;/code&gt;, &lt;code&gt;declined&lt;/code&gt; and &lt;code&gt;expired&lt;/code&gt; | [optional] 
**customer_id** | **str** | Customer ID on the quote. | [optional] 
**customer_name** | **str** | Name of the Customer to whom the quote is sent. | [optional] 
**contact_persons** | **List[str]** | Array of contact person(s) for whom quote has to be sent. | [optional] 
**currency_id** | **str** | The Unique ID of the customer | [optional] 
**currency_code** | **str** | Currency code of the currency in which the customer wants to pay. If currency_code is not specified here, the currency chosen in your Zoho Billing organization will be used for billing. currency_id and currency_symbol are set automatically in accordance to the currency_code. | [optional] 
**exchange_rate** | **float** | Foreign Exchange rate of the currency. | [optional] 
**expiry_date** | **str** | The date of expiration of the quotes | [optional] 
**discount** | **float** | Discount applied to the invoice. It can be either in % or in amount. e.g. 12.5% or 190. | [optional] 
**is_discount_before_tax** | **bool** | Used to specify how the discount has to applied. Either before or after the calculation of tax. | [optional] 
**discount_type** | **str** | How the discount is specified. Allowed values are entity_level or item_level.Allowed Values: &lt;code&gt;entity_level&lt;/code&gt; and &lt;code&gt;item_level&lt;/code&gt; | [optional] 
**is_inclusive_tax** | **bool** | Used to specify whether the line item rates are inclusive or exclusive of tax. | [optional] 
**is_viewed_by_client** | **bool** | To see view status, if viewed by client the quote from the portal or not | [optional] 
**client_viewed_time** | **str** | Time when the client viewed the quote | [optional] 
**line_items** | [**List[LineItemsInner]**](LineItemsInner.md) | Line items of an quote. | [optional] 
**shipping_charge** | **str** | Shipping charges applied to the invoice. | [optional] 
**adjustment** | **float** | Adjustments made to the invoice. | [optional] 
**adjustment_description** | **str** | Customize the adjustment description. E.g. Rounding off value. | [optional] 
**sub_total** | **float** | The sub total of the all items | [optional] 
**total** | **float** | quote total value. | [optional] 
**tax_total** | **float** | The total amount of the tax levied | [optional] 
**price_precision** | **int** | The precision value on the price | [optional] 
**taxes** | [**List[TaxesInner]**](TaxesInner.md) | List of the taxes levied | [optional] 
**billing_address** | [**BillingAddress**](BillingAddress.md) |  | [optional] 
**shipping_address** | [**ShippingAddress**](ShippingAddress.md) |  | [optional] 
**custom_fields** | [**List[CustomFieldsInner]**](CustomFieldsInner.md) | Custom fields for a quote. | [optional] 
**template_id** | **str** | ID of the template used for the quote | [optional] 
**template_name** | **str** | Name of the template used | [optional] 
**created_time** | **str** | The time of creation of the quote | [optional] 
**last_modified_time** | **str** | Last date of modification in quote | [optional] 
**salesperson_id** | **str** | Unique ID of the sales person | [optional] 
**salesperson_name** | **str** | Name of the sales person. | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_quotes.models.get_an_estimate_response_estimate import GetAnEstimateResponseEstimate

# TODO update the JSON string below
json = "{}"
# create an instance of GetAnEstimateResponseEstimate from a JSON string
get_an_estimate_response_estimate_instance = GetAnEstimateResponseEstimate.from_json(json)
# print the JSON string representation of the object
print(GetAnEstimateResponseEstimate.to_json())

# convert the object into a dict
get_an_estimate_response_estimate_dict = get_an_estimate_response_estimate_instance.to_dict()
# create an instance of GetAnEstimateResponseEstimate from a dict
get_an_estimate_response_estimate_from_dict = GetAnEstimateResponseEstimate.from_dict(get_an_estimate_response_estimate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


