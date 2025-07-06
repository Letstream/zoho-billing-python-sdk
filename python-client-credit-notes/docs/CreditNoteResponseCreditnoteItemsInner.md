# CreditNoteResponseCreditnoteItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** | Unique string generated for the item to which a refund is to be made. | [optional] 
**description** | **str** | A small description about the item. | [optional] 
**code** | **str** | Unique code for the creditnote line item. | [optional] 
**tags** | [**List[TagsInner]**](TagsInner.md) |  | [optional] 
**item_custom_fields** | [**List[ItemCustomFieldsInner]**](ItemCustomFieldsInner.md) | Custom fields for a item. | [optional] 
**name** | **str** | Name of the credit | [optional] 
**type** | **int** | Type of the creditnote line item. | [optional] 
**account_id** | **str** | Unique ID to denote the account. | [optional] 
**account_name** | **str** | Name of the account. | [optional] 
**quantity** | **int** | Quantity of the item included. | [optional] 
**tax_id** | **str** | Unique to denote the tax associate dto the creditnote | [optional] 
**tds_tax_id** | **str** | ID of the TDS tax. | [optional] 
**price** | **float** | The price of the item included. | [optional] 
**item_total** | **float** | Total credits raised by this item. This would be the multiplicative product of item price and quantity. | [optional] 
**sat_item_key_code** | **str** | Add SAT Item Key Code for your goods/services. Download the &lt;a href&#x3D; http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI_V_4_07122022.xls  &gt;CFDI Catalogs.&lt;/a&gt; | [optional] 
**unitkey_code** | **str** | Add SAT Unit Key Code for your goods/services. Download the &lt;a href&#x3D; http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI_V_4_07122022.xls  &gt;CFDI Catalogs.&lt;/a&gt; | [optional] 

## Example

```python
from ls_zoho_billing_credit_notes.models.credit_note_response_creditnote_items_inner import CreditNoteResponseCreditnoteItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreditNoteResponseCreditnoteItemsInner from a JSON string
credit_note_response_creditnote_items_inner_instance = CreditNoteResponseCreditnoteItemsInner.from_json(json)
# print the JSON string representation of the object
print(CreditNoteResponseCreditnoteItemsInner.to_json())

# convert the object into a dict
credit_note_response_creditnote_items_inner_dict = credit_note_response_creditnote_items_inner_instance.to_dict()
# create an instance of CreditNoteResponseCreditnoteItemsInner from a dict
credit_note_response_creditnote_items_inner_from_dict = CreditNoteResponseCreditnoteItemsInner.from_dict(credit_note_response_creditnote_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


