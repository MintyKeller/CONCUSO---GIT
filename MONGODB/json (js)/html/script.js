
fetch('data.json')
  .then(function(response) { 
    return response.json(); 
  })
  .then(function(obj) {
    document.getElementById("demo").innerHTML = 
      obj.employees[1].firstName + " " + obj.employees[1].lastName;
  });
