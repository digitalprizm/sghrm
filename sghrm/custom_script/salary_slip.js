
cur_frm.add_fetch("employee", "employee_cpf", "employee_cpf");
cur_frm.add_fetch("employee", "employer_cpf", "employer_cpf");

frappe.ui.form.on("Salary Slip", "validate", function(frm) {
var net_total=0;
   if(cur_frm.doc.earnings){
       for(var i = 0 ; i < cur_frm.doc.earnings.length ; i++){
            if(cur_frm.doc.earnings[i].cpf_deductable==1){
                net_total+=cur_frm.doc.earnings[i].amount;
            }
        }
  }
var du_total=0;
   if(cur_frm.doc.deductions){
       for(var i = 0 ; i < cur_frm.doc.deductions.length ; i++){
            if(cur_frm.doc.deductions[i].salary_component!="EMPLOYEE CPF"){
                du_total+=cur_frm.doc.deductions[i].amount;
            }
       }
  }

var e_type_p = false;
for(var i = 0 ; i < cur_frm.doc.deductions.length ; i++){
    if(cur_frm.doc.deductions[i].salary_component=="EMPLOYEE CPF"){
        e_type_p = true
    }
}
console.log(e_type_p);
if(e_type_p){
    for(var i = 0 ; i < cur_frm.doc.deductions.length ; i++){
        if(cur_frm.doc.deductions[i].salary_component=="EMPLOYEE CPF"){
            cur_frm.doc.deductions[i].amount=Math.round(net_total*cur_frm.doc.employee_cpf/100);
        }
    }
}
else{
    var row = frappe.model.add_child(cur_frm.doc, "deductions");
    row.salary_component = "EMPLOYEE CPF";
    row.amount = Math.round(net_total*cur_frm.doc.employee_cpf/100);
}

refresh_field("deductions");
var sub_total=0;
sub_total=cur_frm.doc.gross_pay - du_total;
console.log(sub_total);
var total_sal =0;
for(var i = 0 ; i < cur_frm.doc.deductions.length ; i++){
    if(cur_frm.doc.deductions[i].salary_component == "EMPLOYEE CPF"){
                total_sal=sub_total-cur_frm.doc.deductions[i].amount;
        }
        console.log(total_sal);
        console.log("hey.."); 
    }
cur_frm.set_value("net_pay",total_sal);
cur_frm.doc.employer_cpf_amount = Math.round(sub_total*cur_frm.doc.employer_cpf/100);
console.log(cur_frm.doc.employer_cpf_amount );
});