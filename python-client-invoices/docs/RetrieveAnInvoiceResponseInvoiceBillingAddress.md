# RetrieveAnInvoiceResponseInvoiceBillingAddress

Customer's billing address object. It contains <code>street</code>, <code>city</code>, <code>state</code>,<code>zip</code> and <code>country</code>.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** | Name of the city of the customer&#39;s billing address. | [optional] 
**state** | **str** | Name of the state of the customer&#39;s billing address. | [optional] 
**zip** | **str** | Zip code of the customer&#39;s billing address. | [optional] 
**country** | **str** | Name of the country of the customer&#39;s billing address. | [optional] 
**fax** | **str** | Customer&#39;s fax number. | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.retrieve_an_invoice_response_invoice_billing_address import RetrieveAnInvoiceResponseInvoiceBillingAddress

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveAnInvoiceResponseInvoiceBillingAddress from a JSON string
retrieve_an_invoice_response_invoice_billing_address_instance = RetrieveAnInvoiceResponseInvoiceBillingAddress.from_json(json)
# print the JSON string representation of the object
print(RetrieveAnInvoiceResponseInvoiceBillingAddress.to_json())

# convert the object into a dict
retrieve_an_invoice_response_invoice_billing_address_dict = retrieve_an_invoice_response_invoice_billing_address_instance.to_dict()
# create an instance of RetrieveAnInvoiceResponseInvoiceBillingAddress from a dict
retrieve_an_invoice_response_invoice_billing_address_from_dict = RetrieveAnInvoiceResponseInvoiceBillingAddress.from_dict(retrieve_an_invoice_response_invoice_billing_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


