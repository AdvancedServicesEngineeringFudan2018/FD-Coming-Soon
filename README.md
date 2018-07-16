# Accessibility Heatmap over Residence

Showing the accessibility heatmap and candidate list.

## Author

Hu Chenglong [[@sonnyhcl](github.com/sonnyhcl)]

Chen Xi [[@iamcxnoguigan](github.com/iamcxnoguigan)]

Teddy Mao [[@luvletter](github.com/luvletter)]

## Empathize

- If you want to rent a house, where would you like to choose?
  - Of course, convenient transportation is critical.

## Define

- What do your users need?
  - People may want to know the transportation about, for example, know how long will take for start from his residence in Shanghai.

## Ideate

- Scenario
  - We are trying to divided the city into x by y cells. Using bus and metro line data to estimate time to spend from one to another, and trying to classify them as a block. 

- Possible solutions
  - Bus line and metro line information is accessible to public and can be fetch by [8684](http://www.8684.cn/). Full metadata is also accessible from [FourSquare API](https://developer.foursquare.com/places-api)

- Key involved stakeholders
  - 8864
  - Foursquare
  - OpenStreetMaps

- Key metrics for evaluating
  - The precision of the estimation of ETA and the candidate list.
  - The resolution of the heatmap.

- Similar or related scenarios
  - The place of interest recommendation on Airbnb

## Prototype

Prototype as a website.

## Test

Create the heatmap for every Shanghai University.

## Reference
- [life circle report by Amap](http://report.amap.com/mobile/life.do)
- [the vein of the city](https://www.96486d9b.xyz/City-Vein/html/shanghai.html)

# Framwork

![dataflow](./ASEDataflowFramework.png)