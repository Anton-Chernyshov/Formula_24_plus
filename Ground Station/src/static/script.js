/*
function updateData(){
fetch("/update")
.then(resp => resp.json())
.then(data => {
	document.getElementById().innerText = data.;
});
}
setinterval(updateData, 500);
*/

import $ from "/jquery.js";
var myData = [];

var myChart = $('#myChart').epoch({ type: 'time.line', data: myData });

function testChart(){
	var randomInt = Math.random() * 1000;
	console.log(randomInt);
	myData.push({time: Date.now(), y: randomInt});
	myChart.update(myData);
}




testChart();
setInterval(testChart, 500);