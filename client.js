
class Employee {
    constructor(obj) {
        this.EMPLid = obj.EMPLid;
        this.name = obj.name;
        this.client = obj.client;
    }
    print() {
        console.log(this.to_string());
    }
    to_string() {
        return "Id: " + this.id + ", name: " + this.NAME + ", client: " + this.client;
    }
    to_table_entry() {
        return '<tr><td>' +
            this.EMPLid + '</td><td>' +
            this.name + '</td><td>' +
            this.client + '</td><td>';
    }
};
