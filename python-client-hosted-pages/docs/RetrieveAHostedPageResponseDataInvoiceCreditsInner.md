# RetrieveAHostedPageResponseDataInvoiceCreditsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creditnote_id** | **str** | Unique ID denoting the credit note. | [optional] 
**creditnotes_number** | **str** | Reference number for the credit note. | [optional] 
**credited_date** | **str** | Date on which the credit were applied | [optional] 
**credited_amount** | **str** | Credited amount for the invoice | [optional] 

## Example

```python
from ls_zoho_billing_hosted_pages.models.retrieve_a_hosted_page_response_data_invoice_credits_inner import RetrieveAHostedPageResponseDataInvoiceCreditsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveAHostedPageResponseDataInvoiceCreditsInner from a JSON string
retrieve_a_hosted_page_response_data_invoice_credits_inner_instance = RetrieveAHostedPageResponseDataInvoiceCreditsInner.from_json(json)
# print the JSON string representation of the object
print(RetrieveAHostedPageResponseDataInvoiceCreditsInner.to_json())

# convert the object into a dict
retrieve_a_hosted_page_response_data_invoice_credits_inner_dict = retrieve_a_hosted_page_response_data_invoice_credits_inner_instance.to_dict()
# create an instance of RetrieveAHostedPageResponseDataInvoiceCreditsInner from a dict
retrieve_a_hosted_page_response_data_invoice_credits_inner_from_dict = RetrieveAHostedPageResponseDataInvoiceCreditsInner.from_dict(retrieve_a_hosted_page_response_data_invoice_credits_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


