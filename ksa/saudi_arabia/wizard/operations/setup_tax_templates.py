import json
import os, frappe

from erpnext.setup.setup_wizard.operations.taxes_setup import from_detailed_data, simple_to_detailed

def setup_templates(doc, method=None):
	if doc.country == 'Saudi Arabia':
		file_path = os.path.join(os.path.dirname(__file__), "..", "data", "ksa_template.json")
		default_taxes = frappe.get_file_json(file_path)
		from_detailed_data(doc.name, default_taxes)
