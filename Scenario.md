# Scenario
Showing the accessibility heatmap and candidate list.

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
  - We use Amap ETA API to get the data and draw the different colors(which stand for time in different range). Then add 3rd Po I information.

- Key involved stakeholders
  - Amap
  - HousePricing
  - Meituan PoI

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

- [life circle report by Amap](http://report.Amap.com/mobile/life.do)
- [the vein of the city](https://www.96486d9b.xyz/City-Vein/html/shanghai.html)
