
  function buildCharts() {
	d3.json("/Final_Project").then((data) => {
	  var alcohol = data.map( x => x.alcohol);
	  var B12_Added = data.map(x => x.B12_Added);
	  var caffeine = data.map(x=> x.caffeine);
		var carbohydrates = data.map(x =>new Date(x.carbohydrates));
		var cholesterol = data.map(x => x.cholesterol);
		var sugar = data.map(x => x.sugar);
		var EvrToldPreDia= data.map(x =>x.EvrToldPreDia);

		console.log(alcohol)
		console.log(B12_Added)
		console.log(caffeine)
		console.log(carbohydrates)
		console.log(cholesterol)
		console.log(sugar)
    console.log(EvrToldPreDia);
  })};
	buildCharts();