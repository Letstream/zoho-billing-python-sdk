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
**payment_terms** | **int** | Payment Due details for the invoices. | [optional] 
**payment_terms_label** | **str** | Label for the paymet due details. | [optional] 
**custom_fields** | [**List[CreateASubscriptionRequestCustomerCustomFieldsInner]**](CreateASubscriptionRequestCustomerCustomFieldsInner.md) | Additional fields for the invoices. | [optional] 
**place_of_contact** | **str** | Customer&#39;s place of contact. | [optional] 
**gst_no** | **str** | GSTIN Number for the customer. | [optional] 
**gst_treatment** | **str** | GST Treatment for the customer.&lt;br&gt;Allowed values for &lt;strong&gt;&lt;code&gt;gst_treatment&lt;/code&gt;&lt;/strong&gt; : &lt;br&gt;&lt;code&gt;business_gst&lt;/code&gt;, &lt;code&gt;business_none&lt;/code&gt;, &lt;code&gt;consumer&lt;/code&gt;, &lt;code&gt;overseas&lt;/code&gt;&lt;br&gt; &lt;code&gt;business_gst&lt;/code&gt; - For a GST Registered business owner. &lt;br&gt;&lt;code&gt;business_none&lt;/code&gt; - For a GST unregistered business owner. &lt;br&gt;&lt;code&gt;consumer&lt;/code&gt; - For a consumer. &lt;br&gt;&lt;code&gt;overseas&lt;/code&gt; - Customer for whom you export your goods/services. | [optional] 
**vat_treatment** | **str** | (Optional) VAT treatment for the invoices. VAT treatment denotes the location of the customer, if the customer resides in UK then the VAT treatment is &lt;code&gt;uk&lt;/code&gt;. If the customer is in an EU country &amp; VAT registered, you are resides in Northen Ireland and selling Goods then his VAT treatment is &lt;code&gt;eu_vat_registered&lt;/code&gt;, if he resides outside of the UK then his VAT treatment is &lt;code&gt;overseas&lt;/code&gt; (For Pre Brexit, this can be split as &lt;code&gt;eu_vat_registered&lt;/code&gt;, &lt;code&gt;eu_vat_not_registered&lt;/code&gt; and &lt;code&gt;non_eu&lt;/code&gt;). | [optional] 
**vat_reg_no** | **str** | VAT Registration number of a contact with length should be between 2 and 12 characters. | [optional] 
**country_code** | **str** | Two letter country code of a contact with VAT treatment as &lt;code&gt;eu_vat_registered&lt;/code&gt;. (This node is only available for EU VAT registered  customers.) | [optional] 
**is_taxable** | **str** | Set to true if customer&#39;s transactions must be tax inclusive. | [optional] 
**tax_id** | **str** | Unique ID of the tax or tax group that can be collected from the contact. Tax can be given only if &lt;code&gt;is_taxable&lt;/code&gt; is &lt;code&gt;true&lt;/code&gt;. | [optional] 
**tax_authority_id** | **str** | Unique ID of the tax authority. Tax authority depends on the location of the customer. For example, if the customer is located in NY, then the tax authority is NY tax authority. | 
**tax_authority_name** | **str** | Unique name of the tax authority. Either tax_authority_id or tax_authority_name can be given. | 
**tax_exemption_id** | **str** | Unique ID of the tax exemption. | [optional] 
**tax_exemption_code** | **str** | Unique code of the tax exemption. | [optional] 

## Example

```python
from ls_zoho_billing_subscription.models.create_a_subscription_request_customer import CreateASubscriptionRequestCustomer

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


