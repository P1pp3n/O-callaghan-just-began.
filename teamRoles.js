function expertiseRoles(Role,Slots,Taken){
    this.Role=Role;
    this.Slots=Slots;
    this.Taken=Taken;
    this.Availability=function(){
        return this.Slots-this.Taken;
    };
    
}
var itRole=new expertiseRoles("IT-Specialist",5,2);
var literatureRole=new expertiseRoles("Literature-Specialist",5,4);
var engineeringRole=new expertiseRoles("Engineering-Specialist",4,1);
var medicalRole=new expertiseRoles("Medical-Specialist",5,3);

var details1= itRole.Role + ' role: ';
    details1+=itRole.Availability();
var elRole=document.getElementById("IT");
    elRole.textContent=details1;

var details2= literatureRole.Role + ' role: ';
    details2+=literatureRole.Availability();
var elRole1=document.getElementById("LT");
    elRole1.textContent=details2;

var details3= engineeringRole.Role + ' role: ';
    details3+=engineeringRole.Availability();
var elRole2=document.getElementById("ET");
    elRole2.textContent=details3;

var details4= medicalRole.Role + ' role: ';
    details4+=medicalRole.Availability();
var elRole3=document.getElementById("MT");
    elRole3.textContent=details4;