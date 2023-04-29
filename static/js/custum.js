let Profile = {
    Name : "Navdeep",
    Height: 5.7,
    Age : 28,
    Mobile:1234567890,
    sayHello(){
        console.log("I am coming from Profile " + this.Mobile + " I am coming from Car" + car.brand) ;
    }   
};


let car = {
    brand : "Model",
    model : "Safari"
}


Profile.sayHello();