# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Sales Pro QubiQ",
    "summary": "All pro modules for the Sales application",
    "version": "17.0.1.0.0",
    "category": "Pro",
    "website": "https://www.qubiq.es",
    "author": "QubiQ, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "sale_management",
        "partner_contact_personal_information_page",
        "partner_vat_unique",
        "sale_order_line_menu",
        "sale_order_archive",
        "partner_sale_pivot",
        "partner_contact_access_link",
    ],
    "data": [
    ],
}
