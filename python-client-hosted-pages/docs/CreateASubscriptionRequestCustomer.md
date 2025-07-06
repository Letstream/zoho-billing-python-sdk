# CreateASubscriptionRequestCustomer

Customer object of the customer for whom you want to create a subscription. Each object contains <code>display_name</code>, <code>company_name</code>, <code>first_name</code>, <code>last_name</code>, <code>email</code>, <code>fax</code>, <code>currency_code</code> and <code>billing_address</code>.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | This will be name which will be displayed in the interface and invoices. | 
**salutation** | **str** | Salutation of the customer. | [optional] 
**first_name** | **str** | First name of the customer. | [optional] 
**last_name** | **str** | Last name of the customer. | [optional] 
**email** | **str** | Email address of the customer. | 
**company_name** | **str** | Registered name of the company the customer represents. | [optional] 
**billing_address** | [**BillingAddress**](BillingAddress.md) |  | [optional] 
**shipping_address** | [**ShippingAddress**](ShippingAddress.md) |  | [optional] 
**pricebook_id** | **str** | A Pricebook that has currency same as that of the customer | [optional] 
**payment_terms** | **int** | Payment Due details for the invoices. | [optional] 
**payment_terms_label** | **str** | Label for the paymet due details. | [optional] 
**exchange_rate** | **float** | This will be the exchange rate provided for the organization&#39;s currency and the customer&#39;s currency. The subscription fee would be the multiplicative product of the original price and the exchange rate. | [optional] 
**currency_code** | **str** | Currency code of the currency in which the customer wants to pay. If &lt;code&gt;currency_code&lt;/code&gt; is not specified here, the currency chosen in your Zoho Billing organization will be used for billing. &lt;code&gt;currency_id&lt;/code&gt; and &lt;code&gt;currency_symbol&lt;/code&gt; are set automatically in accordance to the currency_code. | [optional] 
**vat_treatment** | **str** | VAT treatment for the credit-note. VAT treatment denotes the location of the customer, if the customer resides in UK then the VAT treatment is &#x60;uk&#x60;. If the customer is in a EU country &amp; if he is VAT registered then his VAT treatment is &#x60;eu_vat_registered&#x60;, if he resides in EU &amp; if he is not VAT registered then his VAT treatment is &#x60;eu_vat_not_registered&#x60; and if he resides outside the EU then his VAT treatment is &#x60;non_eu&#x60;. | [optional] 
**vat_reg_no** | **str** | VAT Registration number of a contact with VAT treatment as &lt;code&gt;eu_vat_registered&lt;/code&gt;. Length should be between 2 and 12 characters. (This node is only available for EU VAT registered  customers.) | [optional] 
**country_code** | **str** | Two letter country code of a contact with VAT treatment as &lt;code&gt;eu_vat_registered&lt;/code&gt;. (This node is only available for EU VAT registered  customers.) | [optional] 
**is_taxable** | **str** | Set to true if customer&#39;s transactions must be tax inclusive. | [optional] 
**tax_id** | **str** | Unique ID of the tax or tax group that can be collected from the contact. Tax can be given only if &lt;code&gt;is_taxable&lt;/code&gt; is &lt;code&gt;true&lt;/code&gt;. | [optional] 
**tax_authority_id** | **str** | Unique ID of the tax authority. Tax authority depends on the location of the customer. For example, if the customer is located in NY, then the tax authority is NY tax authority. | 
**tax_authority_name** | **str** | Unique name of the tax authority. | 
**tax_exemption_id** | **str** | Unique ID of the tax exemption. | [optional] 
**tax_exemption_code** | **str** | Unique code of the tax exemption. | [optional] 
**default_templates** | [**CreateASubscriptionRequestCustomerDefaultTemplates**](CreateASubscriptionRequestCustomerDefaultTemplates.md) |  | [optional] 
**place_of_contact** | **str** |  | [optional] 
**gst_no** | **str** | GSTIN Number for the customer. | [optional] 
**gst_treatment** | **str** | GST Treatment for the customer.&lt;br&gt;Allowed values for &lt;strong&gt;&lt;code&gt;gst_treatment&lt;/code&gt;&lt;/strong&gt; : &lt;br&gt;&lt;code&gt;business_gst&lt;/code&gt;, &lt;code&gt;business_none&lt;/code&gt;, &lt;code&gt;consumer&lt;/code&gt;, &lt;code&gt;overseas&lt;/code&gt;&lt;br&gt; &lt;code&gt;business_gst&lt;/code&gt; - For a GST Registered business owner. &lt;br&gt;&lt;code&gt;business_none&lt;/code&gt; - For a GST unregistered business owner. &lt;br&gt;&lt;code&gt;consumer&lt;/code&gt; - For a consumer. &lt;br&gt;&lt;code&gt;overseas&lt;/code&gt; - Customer for whom you export your goods/services. | [optional] 

## Example

```python
from ls_zoho_billing_hosted_pages.models.create_a_subscription_request_customer import CreateASubscriptionRequestCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of CreateASubscriptionRequestCustomer from a JSON string
create_a_subscription_request_customer_instance = CreateASubscriptionRequestCustomer.from_json(json)
# print the JSON string representation of the object
print(CreateASubscriptionRequestCustomer.to_json())

# convert the object into a dict
create_a_subscription_request_customer_dict = create_a_subscription_request_customer_instance.to_dict()
# create an instance of CreateASubscriptionRequestCustomer from a dict
create_a_subscription_request_customer_from_dict = CreateASubscriptionRequestCustomer.from_dict(create_a_subscription_request_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


