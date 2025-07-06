# CreateACreditNoteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | Customer ID of the customer for whom the credit note is raised. | 
**contact_persons** | **List[str]** | Contact Persons associated with the credit note. | [optional] 
**var_date** | **str** | The date on which credit note is raised. | 
**exchange_rate** | **str** | Exchange rate for the currency associated with the customer. | [optional] 
**creditnote_items** | [**List[CreateACreditNoteRequestCreditnoteItemsInner]**](CreateACreditNoteRequestCreditnoteItemsInner.md) | List of items involved in the credit note. This contains &lt;code&gt;item_id&lt;/code&gt;, &lt;code&gt;description&lt;/code&gt;, &lt;code&gt;quantity&lt;/code&gt;, &lt;code&gt;price&lt;/code&gt; and &lt;code&gt;item_total&lt;/code&gt;. | 
**creditnote_number** | **str** | Unique number generated (starts with CN) which will be displayed in the interface and credit notes. | 
**ignore_auto_number_generation** | **bool** | Set to true if you need to provide your own credit note number. | [optional] 
**reference_number** | **str** | Reference number generated for the payment. A string of your choice can also be used as the reference number. | [optional] 
**custom_fields** | [**List[ItemCustomFieldsInner]**](ItemCustomFieldsInner.md) | Additional fields for the Credit-Notes. | [optional] 
**notes** | **str** | A short note for the credit note. | [optional] 
**terms** | **str** | Terms &amp; condition to be displayed in the credit note. | [optional] 
**template_id** | **str** | Unique ID of the creditnote template | [optional] 
**tax_treatment** | **str** | VAT treatment for the invoice .Choose whether the contact falls under: &lt;/br&gt;&lt;code&gt;home_country_mexico&lt;/code&gt;,&lt;code&gt;border_region_mexico&lt;/code&gt;,&lt;code&gt;non_mexico&lt;/code&gt; supported only for &lt;b&gt;MX&lt;/b&gt;. | [optional] 
**cfdi_usage** | **str** | Choose CFDI Usage. Allowed values:&lt;/br&gt;&lt;code&gt;acquisition_of_merchandise&lt;/code&gt;, &lt;code&gt;return_discount_bonus&lt;/code&gt;, &lt;code&gt;general_expense&lt;/code&gt;, &lt;code&gt;buildings&lt;/code&gt;, &lt;code&gt;furniture_office_equipment&lt;/code&gt;, &lt;code&gt;transport_equipment&lt;/code&gt;, &lt;code&gt;computer_equipmentdye_molds_tools&lt;/code&gt;, &lt;code&gt;telephone_communication&lt;/code&gt;, &lt;code&gt;satellite_communication&lt;/code&gt;, &lt;code&gt;other_machinery_equipment&lt;/code&gt;, &lt;code&gt;hospital_expense&lt;/code&gt;, &lt;code&gt;medical_expense_disability&lt;/code&gt;, &lt;code&gt;funeral_expense&lt;/code&gt;, &lt;code&gt;donation&lt;/code&gt;, &lt;code&gt;interest_mortage_loans&lt;/code&gt;, &lt;code&gt;contribution_sar&lt;/code&gt;, &lt;code&gt;medical_expense_insurance_pormium&lt;/code&gt;, &lt;code&gt;school_transportation_expense&lt;/code&gt;, &lt;code&gt;deposit_saving_account&lt;/code&gt;, &lt;code&gt;payment_educational_service&lt;/code&gt;, &lt;code&gt;no_tax_effect&lt;/code&gt;, &lt;code&gt;payment&lt;/code&gt;, &lt;code&gt;payroll&lt;/code&gt;. | [optional] 
**cfdi_reference_type** | **str** | Choose CFDI Reference Type. Allowed values:&lt;/br&gt;&lt;code&gt;return_of_merchandise&lt;/code&gt;, &lt;code&gt;substitution_previous_cfdi&lt;/code&gt;, &lt;code&gt;transfer_of_goods&lt;/code&gt;, &lt;code&gt;invoice_generated_from_order&lt;/code&gt;, &lt;code&gt;cfdi_for_advance&lt;/code&gt;. | [optional] 

## Example

```python
from ls_zoho_billing_credit_notes.models.create_a_credit_note_request import CreateACreditNoteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateACreditNoteRequest from a JSON string
create_a_credit_note_request_instance = CreateACreditNoteRequest.from_json(json)
# print the JSON string representation of the object
print(CreateACreditNoteRequest.to_json())

# convert the object into a dict
create_a_credit_note_request_dict = create_a_credit_note_request_instance.to_dict()
# create an instance of CreateACreditNoteRequest from a dict
create_a_credit_note_request_from_dict = CreateACreditNoteRequest.from_dict(create_a_credit_note_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


