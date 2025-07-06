# Customer

Customer object of the customer for whom you want to create a subscription. Each object contains <code>display_name</code>, <code>company_name</code>, <code>first_name</code>, <code>last_name</code>, <code>email</code>, <code>fax</code>, <code>currency_code</code> and <code>billing_address</code>.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | First name of the customer. | [optional] 
**last_name** | **str** | Last name of the customer. | [optional] 
**display_name** | **str** | This will be name which will be displayed in the interface and invoices. | [optional] 
**email** | **str** | Email address of the customer. | [optional] 
**company_name** | **str** | Registered name of the company the customer represents. | [optional] 
**currency_code** | **str** | Currency code of the currency in which the customer wants to pay. If &lt;code&gt;currency_code&lt;/code&gt; is not specified here, the currency chosen in your Zoho Billing organization will be used for billing. &lt;code&gt;currency_id&lt;/code&gt; and &lt;code&gt;currency_symbol&lt;/code&gt; are set automatically in accordance to the currency_code. | [optional] 
**phone** | **str** | Customer’s landline or fixed-line number. | [optional] 
**mobile** | **str** | Customer’s mobile phone number. | [optional] 
**place_of_contact** | **str** |  | [optional] 

## Example

```python
from ls_zoho_billing_hosted_pages.models.customer import Customer

# TODO update the JSON string below
json = "{}"
# create an instance of Customer from a JSON string
customer_instance = Customer.from_json(json)
# print the JSON string representation of the object
print(Customer.to_json())

# convert the object into a dict
customer_dict = customer_instance.to_dict()
# create an instance of Customer from a dict
customer_from_dict = Customer.from_dict(customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


