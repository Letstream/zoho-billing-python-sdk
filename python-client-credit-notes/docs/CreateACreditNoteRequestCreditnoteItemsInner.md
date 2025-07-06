# CreateACreditNoteRequestCreditnoteItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A small description about the item. | [optional] 
**code** | **str** | Unique code for the creditnote line item. | 
**account_id** | **str** | Unique ID to denote the account. | [optional] 
**quantity** | **int** | Quantity of the item included. | 
**tags** | [**List[TagsInner]**](TagsInner.md) |  | [optional] 
**item_custom_fields** | [**List[ItemCustomFieldsInner]**](ItemCustomFieldsInner.md) | Custom fields for a item. | [optional] 
**tax_id** | **str** | Unique to denote the tax associate dto the creditnote | [optional] 
**tds_tax_id** | **str** | ID of the TDS tax. | [optional] 
**tax_exemption_id** | **str** | Unique ID of the tax exemption. | [optional] 
**tax_exemption_code** | **str** | Unique code of the tax exemption. | [optional] 
**price** | **float** | The price of the item included. | 
**sat_item_key_code** | **str** | Add SAT Item Key Code for your goods/services. Download the &lt;a href&#x3D; http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI_V_4_07122022.xls  &gt;CFDI Catalogs.&lt;/a&gt; | [optional] 
**unitkey_code** | **str** | Add SAT Unit Key Code for your goods/services. Download the &lt;a href&#x3D; http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI_V_4_07122022.xls  &gt;CFDI Catalogs.&lt;/a&gt; | [optional] 

## Example

```python
from ls_zoho_billing_credit_notes.models.create_a_credit_note_request_creditnote_items_inner import CreateACreditNoteRequestCreditnoteItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateACreditNoteRequestCreditnoteItemsInner from a JSON string
create_a_credit_note_request_creditnote_items_inner_instance = CreateACreditNoteRequestCreditnoteItemsInner.from_json(json)
# print the JSON string representation of the object
print(CreateACreditNoteRequestCreditnoteItemsInner.to_json())

# convert the object into a dict
create_a_credit_note_request_creditnote_items_inner_dict = create_a_credit_note_request_creditnote_items_inner_instance.to_dict()
# create an instance of CreateACreditNoteRequestCreditnoteItemsInner from a dict
create_a_credit_note_request_creditnote_items_inner_from_dict = CreateACreditNoteRequestCreditnoteItemsInner.from_dict(create_a_credit_note_request_creditnote_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


