frappe.ui.form.on("Employee", "validate", function(frm) {
   frm.doc.age = Math.floor(frappe.datetime.get_diff(frappe.datetime.get_today(),cur_frm.fields_dict.date_of_birth.value)/365); 
});
frappe.ui.form.on("Employee", "onload", function(frm) {
   frm.doc.age =  Math.floor(frappe.datetime.get_diff(frappe.datetime.get_today(),cur_frm.fields_dict.date_of_birth.value)/365); 
});