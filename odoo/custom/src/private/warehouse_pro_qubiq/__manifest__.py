# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Warehouse Pro QubiQ",
    "summary": "All pro modules for the Warehouse application",
    "version": "17.0.1.0.0",
    "category": "Pro",
    "website": "https://www.qubiq.es",
    "author": "QubiQ, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "stock",
        "stock_move_line_auto_fill",
        "stock_move_location",
        "stock_picking_back2draft",
        "stock_picking_invoice_link",
        "stock_picking_sale_order_link",
        "stock_landed_costs",
        "stock_search_supplierinfo_code",
        "purchase_stock_picking_invoice_link",
        "stock_picking_purchase_order_link",
    ],
    "data": [
    ],
}
