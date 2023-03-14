#    Copyright (C) 2020 GARCO Consulting <www.garcoconsulting.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Helpdesk Ticket SLA (colpari Version)",
    "summary": "Add SLA to the tickets for Helpdesk Management.",
    "author": "GARCO Consulting, Odoo Community Association (OCA) / colpari",
    "website": "https://github.com/colpari/oca-helpdesk",
    "license": "AGPL-3",
    "category": "After-Sales",
    "version": "15.0.0.0.0",
    "depends": ["base", "helpdesk_mgmt", "resource"],
    "data": [
        "data/helpdesk_sla_cron.xml",
        "security/ir.model.access.csv",
        "views/helpdesk_sla_views.xml",
        "views/helpdesk_ticket_views.xml",
        "views/helpdesk_ticket_team_views.xml",
    ],
}
