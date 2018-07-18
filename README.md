# Accessibility Heatmap over Residence

Showing the accessibility heatmap and candidate list.

## Author

[Chenglong Hu @sonnyhcl](github.com/sonnyhcl)

[Chen Xi @iamcxnoguigan](github.com/iamcxnoguigan)

[Teddy Mao @luvletter](github.com/luvletter)

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

## Missions

### Section 1 : Basic Heatmap

1. find out the usage of Amap, almost frontend -> cx
2. verify the usage of Amap batch API -> hcl
3. design the iterate algorithms -> mct

### Section 2 : Third-Party Data

1. ~~Swarm API: both frontend and backend~~ (**canceled because this API is disabled**)
2. find PoI using Meituan.

### Section 3 : More features if possible

1. House price and renting price => to generate house heatmap or label from [HousePricing](https://github.com/PENGZhaoqing/HousePricing).
2. Find other service which provide the real-time friend location.
3. Interact between two people who want to find place for specific purpose. Find the overlap of their transportation cycle and find the result in PoI.
4. Store the result every hour so that user can see the change in a period, and it will be possible to forecast the situation later.

## Quality of Data

> Elaborate more!!!

- It needs plenty of queries and of course a lot of time to query Amap url for enough possible points getting real-time life cycles.

## Elasticity Rules

- Queries should be produced in batch or concurrently rather than serially.
  - It can help reduce the burden of our servers.

- Results should be rendered asynchronously. Fetch one result and render one.
  - It can make users feel much better in a simple way rather than adding more servers.

## QoD Metrics

- Q: **Domain-specific metrics**
  - Need specific tools and expertise for determining metrics
- A: We assume that life circle is continuous and uninterrupted. So if we wanna know the edge of 20 minutes life cycle, we can first search one PoInt in one direction for 20 minutes distance, and then we have a rough 20 minutes radius. Then we search the ring around the 20 minutes circle. It can help us reduce query times a lot and better use batch query provided by Amap.

-------------

- Q: **Evaluation**
  - Cannot done by software only: humans are required
  - Exact versus inexact evaluation due to big and streaming data
- A: There are some parameters that still need human to define which is better.

-------------

- Q&A: **Complex integration model**
  - Where to put QoD evaluators and why?
  - How evaluators obtain the data to be evaluated?
- A: QoD is both needed for the input data and output data. For us, our input is the data from Amap API and our output data is the feedback of the users.

-------------

- Q: **Impact of QoD evaluation on performance of data analytics workflows**
- A: It can help us reduce a lot when querying using Amap API. However, it need much more human attention.

### Tool

- [Telegraf](http://www.telegraf.rs/)
  - store the input evaluation, output and user feedback.

## Where We Use

### Third-Party Service Provider

- Design of APIs: parameters, quantity, output items
- The update frequency and quality
- The review score from the provider, like the comment in OpenStreetMaps

### Output Data

- Calculate the precision by comparing output data with the real value
- Receive the user feedback and suggestion

## Diagram

![dataflow](image/ASEDataflowFramework.png)