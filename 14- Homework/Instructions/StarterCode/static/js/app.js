// from data.js
var tableData = data;
var tbody = d3.select("tbody");
// YOUR CODE HERE!

function rendertable(x) {data.forEach(function(x) {
  console.log(x);
  var row = tbody.append("tr");
  Object.entries(x).forEach(function([key, value]) {
    console.log(key, value);
    // Append a cell to the row for each value
    // in the weather report object
    var cell = row.append("td");
    cell.text(value);
  });
});
}

rendertable(tableData)
var inputdata = d3.select("#datetime");

var inputText = d3.select("#datetime")
var button = d3.select("filter-btn")

// filter data with desired date
function changeHandler(){
    console.log(inputText.property("value"));
    var filteredData = tableData.filter(sighting => (sighting.datetime === inputText);
    d3.event.preventDefault();
    rendertable(filteredData)
}

// event listener to handle change and click
inputText.on("change", changeHandler)
button.on("click", changeHandler)

//d3.select("#datetime").on("change", function() {
  // What will be logged out? What is `this` in this case?
  //console.log("it's working");
  // Answer: It will console log the `button` element.

  //let filteredData = tableData.filter((row) => {
  //remove data before triggering tbody
  //return (row.datetime === inputdata)
//});


//rendertable(filteredData)
//let filteredData = tableData.filter(row => {
  //remove data before triggering tbody
//  return (row.datetime === inputdata)

//});

//for other filters look for empty strings 5 inputs 3
//if string is empty if 
//if a b c d is true then output them
//

//d3.event.preventDefault();


//on change d3 
//function handleChange(event) {
//var inputText = d3.event.target.value;

//}

//text.on("change", handleChange);

//filter
//function sighting(info) {
// return info.datetime === inputText;
//  }


