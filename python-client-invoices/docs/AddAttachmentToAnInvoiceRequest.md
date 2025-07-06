# AddAttachmentToAnInvoiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_send_in_mail** | **bool** | True to send the attachment with the invoice when emailed. | [optional] 
**attachment** | **bytearray** | The file to be attached.Allowed Extensions: &lt;code&gt;gif&lt;/code&gt;, &lt;code&gt;png&lt;/code&gt;, &lt;code&gt;jpeg&lt;/code&gt;, &lt;code&gt;jpg&lt;/code&gt;, &lt;code&gt;bmp&lt;/code&gt; and &lt;code&gt;pdf&lt;/code&gt; | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.add_attachment_to_an_invoice_request import AddAttachmentToAnInvoiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddAttachmentToAnInvoiceRequest from a JSON string
add_attachment_to_an_invoice_request_instance = AddAttachmentToAnInvoiceRequest.from_json(json)
# print the JSON string representation of the object
print(AddAttachmentToAnInvoiceRequest.to_json())

# convert the object into a dict
add_attachment_to_an_invoice_request_dict = add_attachment_to_an_invoice_request_instance.to_dict()
# create an instance of AddAttachmentToAnInvoiceRequest from a dict
add_attachment_to_an_invoice_request_from_dict = AddAttachmentToAnInvoiceRequest.from_dict(add_attachment_to_an_invoice_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


