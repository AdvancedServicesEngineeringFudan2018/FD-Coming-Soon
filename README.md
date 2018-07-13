## Heapmap around subway station

Considering changing to another scenario since the applyment for didi open data needs one week to check...

## Author

Hu Chenglong [[@sonnyhcl](github.com/sonnyhcl)]

Chen Xi [[@iamcxnoguigan](github.com/iamcxnoguigan)]

Teddy Mao [[@luvletter](github.com/luvletter)]

## Empathize

- If you implement the scenario, who would be your customers?
  - People who want to schedule their time to subway will be our customers.

## Define

- What do your users need?
  - People may want to know the traffic flow before they schedule their time to get subway. They may want to avoid the human traffic.

## Ideate

- Scenario

  - Didi open data provides us one way to measure the traffic around subway station. We can build a heatmap in different time scale to show the traffic in POI. Here our POI is subway station.
- Possible solutions

  - We can know the start point and end point from didi dataset and we can plot it as heatmap using amap API [lbs.amap.com](lbs.amap.com). We also want to add dataset of shared bicycles to rich our datasets and enhance our result. 
- Key involved stakeholders

  - Amap company
  - Ofo company or Mobike company
- Key metrics for evaluating
  - the congestion degree predicted using didi datasets or using mobike datasets
  - the matching degree of above two
- Similar or related scenarios
  - car traffic congestion in big cities.

## Prototype

Prototype as a website.

## Test

Choose 20 subway stations and evaluating the congestion degree predicted using didi datasets or using mobike datasets. 
