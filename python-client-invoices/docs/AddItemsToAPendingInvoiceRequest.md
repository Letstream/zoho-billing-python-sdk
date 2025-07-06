# AddItemsToAPendingInvoiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_items** | [**List[AddItemsToAPendingInvoiceRequestInvoiceItemsInner]**](AddItemsToAPendingInvoiceRequestInvoiceItemsInner.md) | The list of items which are all included in the invoice. Each item object will have &lt;code&gt;item_id&lt;/code&gt;, &lt;code&gt;name&lt;/code&gt;, &lt;code&gt;code&lt;/code&gt;, &lt;code&gt;price&lt;/code&gt;, &lt;code&gt;quantity&lt;/code&gt; and &lt;code&gt;item_total&lt;/code&gt;. description: Small description about the Invoice item. example: \&quot;Charges for this duration (from 16-April-2016 to 8-June-2016)\&quot; | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.add_items_to_a_pending_invoice_request import AddItemsToAPendingInvoiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddItemsToAPendingInvoiceRequest from a JSON string
add_items_to_a_pending_invoice_request_instance = AddItemsToAPendingInvoiceRequest.from_json(json)
# print the JSON string representation of the object
print(AddItemsToAPendingInvoiceRequest.to_json())

# convert the object into a dict
add_items_to_a_pending_invoice_request_dict = add_items_to_a_pending_invoice_request_instance.to_dict()
# create an instance of AddItemsToAPendingInvoiceRequest from a dict
add_items_to_a_pending_invoice_request_from_dict = AddItemsToAPendingInvoiceRequest.from_dict(add_items_to_a_pending_invoice_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


