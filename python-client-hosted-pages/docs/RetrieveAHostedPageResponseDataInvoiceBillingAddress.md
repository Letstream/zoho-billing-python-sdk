# RetrieveAHostedPageResponseDataInvoiceBillingAddress

Customer's billing address object. It contains <code>attention</code>, <code>street</code>, <code>city</code>, <code>state</code>, <code>zip</code>, <code>country</code> and <code>fax</code>.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** | City of the customer’s billing address. | [optional] 
**state** | **str** | State of the customer’s billing address. | [optional] 
**zip** | **str** | Zip code of the customer’s billing address. | [optional] 
**country** | **str** | Country of the customer’s billing address. | [optional] 
**fax** | **str** | Fax number of the customer&#39;s billing address. | [optional] 

## Example

```python
from ls_zoho_billing_hosted_pages.models.retrieve_a_hosted_page_response_data_invoice_billing_address import RetrieveAHostedPageResponseDataInvoiceBillingAddress

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveAHostedPageResponseDataInvoiceBillingAddress from a JSON string
retrieve_a_hosted_page_response_data_invoice_billing_address_instance = RetrieveAHostedPageResponseDataInvoiceBillingAddress.from_json(json)
# print the JSON string representation of the object
print(RetrieveAHostedPageResponseDataInvoiceBillingAddress.to_json())

# convert the object into a dict
retrieve_a_hosted_page_response_data_invoice_billing_address_dict = retrieve_a_hosted_page_response_data_invoice_billing_address_instance.to_dict()
# create an instance of RetrieveAHostedPageResponseDataInvoiceBillingAddress from a dict
retrieve_a_hosted_page_response_data_invoice_billing_address_from_dict = RetrieveAHostedPageResponseDataInvoiceBillingAddress.from_dict(retrieve_a_hosted_page_response_data_invoice_billing_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


