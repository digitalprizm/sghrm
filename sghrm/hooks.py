# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "sghrm"
app_title = "Sghrm"
app_publisher = "Digitalprizm"
app_description = "Manages Singapore Hrm"
app_icon = "octicon octicon-file-directory"
app_color = "blue"
app_email = "contact@digitalprizm.net"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sghrm/css/sghrm.css"
# app_include_js = "/assets/sghrm/js/sghrm.js"

# include js, css files in header of web template
# web_include_css = "/assets/sghrm/css/sghrm.css"
# web_include_js = "/assets/sghrm/js/sghrm.js"
fixtures = ['Custom Field', 'Property Setter',"Print Format"]
# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}
doctype_js = {
    "Employee":["custom_script/employee.js"],
    "Salary Slip":["custom_script/salary_slip.js"]
}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "sghrm.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "sghrm.install.before_install"
# after_install = "sghrm.install.after_install"
after_install = "sghrm.sghrm.custom_script.install.after_install"
# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sghrm.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"sghrm.tasks.all"
# 	],
# 	"daily": [
# 		"sghrm.tasks.daily"
# 	],
# 	"hourly": [
# 		"sghrm.tasks.hourly"
# 	],
# 	"weekly": [
# 		"sghrm.tasks.weekly"
# 	]
# 	"monthly": [
# 		"sghrm.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "sghrm.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "sghrm.event.get_events"
# }

