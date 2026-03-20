---
layout: article
title: 'Energy Is All You Need'
description: 'Thesis on why we need more nuclear and solar plus battery energy to power AI growth.'
github_repo: 'matejkajinic/energy-is-all-you-need'
github_url: 'https://github.com/matejkajinic/energy-is-all-you-need'
source_path: 'README.md'
last_commit_sha: 'cd4bad3371d533aec6c885df0c09012ecc95e446'
last_commit_date: '2024-06-18T12:00:00Z'
---

<!-- Generated at 2026-03-20T22:08:20Z by scripts/sync_writing.py -->

# Energy is all you need

There are two crucial currencies for the future:
*   FLOPS (computational power)
*   Watts (energy efficiency)

We need more intelligence and more energy.

# Computation power

*   Training OpenAI's GPT-4 required an estimated **21 billion petaFLOP** 
    (petaFLOP is 10¹⁵ floating point operations).

*   iPhone 12 is capable roughly **0.01 petaFLOP**. It would take 60,000 years to train GPT-4 on iPhone 12.

*   NVIDIA GB200 NVL72 is capable of **1440 petaFLOP** in single rack.


## Training compute of frontier AI models grows by 4-5x per year

**Notable models include:**
- **AlexNet** (c. 2012, ~10¹⁸ FLOP)
- **AlphaGo Master** (c. 2016, ~10²² FLOP)
- **AlphaGo Zero** (c. 2017, ~10²³)
- **GPT-3** (c. 2020, just below 10²⁴ FLOP)
- **PaLM** (c. 2022, ~10²⁴ FLOP)
- **GPT-4** (c. 2023, above 10²⁴ FLOP)
- **Gemini Ultra** (c. 2023, near the top right, ~10²⁵ FLOP)

The overall trend shows a massive and consistent increase in the computational power required to train frontier AI models over the last decade.

# Key needs of training and infrence

*   AI training workloads have unique requirements that are very dissimilar to those of typical hardware deployed in existing data centers.

*   First, models train for weeks or months, with network connectivity requirements being relativity limited to training data ingress. Training is latency insensitive and does not need to be near any major population centers.

*   AI training clusters can be deployed essentially anywhere in the world that makes economic sense, subject to data residency and compliance regulations.

*   The second major difference to keep in mind is – AI training workloads are extremely power hungry and tend to run AI hardware at power levels closer to their Thermal Design Power (TDP) than would a traditional non-accelerated hyperscale or enterprise workload.

*   Additionally, while CPU and storage servers consume on the order of 1kW, each AI server is now eclipsing 10kW. Coupled with the insensitivity towards latency and decreased importance of proximity to population centers, this means that the availability of abundant quantities of inexpensive electricity (and in the future - access to any grid supply at all) is of much higher relative importance for AI training workloads vs traditional workloads.

*   Inference on the other hand is eventually a larger workload than training, but it can also be quite distributed. The chips don't need to be centrally located, but the sheer volume will be outstanding.

# AI infrastructure demand

## Estimates of power

*   The IEA's recent Electricity 2024 report suggests 90 terawatt-hours (TWh) of power demand from AI data centers by 2026, which is equivalent to about 10 Gigawatts (GW) of data center Critical IT Power Capacity, or the equivalent of 7.3M H100s.

*   It's estimate that Nvidia alone will have shipped accelerators with the power needs of 5M+ H100s (mostly shipments of H100s, in fact) from 2021 through the end of 2024.

*   Datacenter power capacity growth will accelerate from a 12-15% CAGR to a 25% CAGR over the next few years.

*   Power demand will surge from 49 Gigawatts (GW) in 2023 to 96 GW by 2026, of which AI will consume ~40 GW.

*   The need for abundant, inexpensive power, and to quickly add electrical grid capacity while still meeting hyperscalers' carbon emissions commitments, coupled with chip export restrictions, will limit the regions and countries that can meet the surge in demand from AI data centers. This will also push carbon emission commitments as less important.

### Global data center critical IT power (Megawatts - MW)

| Year | Non-AI Data Center Critical IT Power (MW) | AI Data Center Critical IT Power (MW) | Total Critical IT Power (MW) |
| :---: | :---: | :---: | :---: |
| 2022 | 40,000 | 3,000 | 43,000 |
| 2023 | 42,000 | 7,000 | 49,000 |
| 2024 | 45,000 | 14,000 | 59,000 |
| 2025 | 50,000 | 20,000 | 70,000 |
| 2026 | 56,000 | 40,000 | 96,000 |
| 2027 | 60,000 | 60,000 | 120,000 |
| 2028 | 62,000 | 85,000 | 147,000 |


### Estimated hyperscaler data center capacity (MW)

| Company | 2022 Capacity (MW) | Projected future capacity (MW) | Total (MW) |
| :--- | :---: | :---: | :---: |
| Google | 3024 | 2905 | 5929 |
| Microsoft | 2176 | 3344 | 5520 |
| Amazon | 2480 | 2533 | 5013 |
| Meta | 1790 | 2595 | 4385 |
| Apple | 600 | 1403 | 2003 |
| Alibaba | 1350 | 487 | 1837 |
| Huawei | 494 | 192 | 686 |
| Baidu | 608 | 36 | 644 |
| Tencent | 487 | 152 | 639 |


### Estimated data center construction by region (MW)

| Region | 2023 Inventory (MW) | Under construction (MW) | Total (MW) |
| :--- | :---: | :---: | :---: |
| Northern Virginia | 2499 | 1237 | 3736 |
| Atlanta | 310 | 733 | 1043 |
| Dallas-Ft. Worth | 565 | 287 | 852 |
| Chicago | 560 | 118 | 678 |
| Hillsboro | 262 | 281 | 543 |
| Silicon Valley | 428 | 113 | 541 |
| Phoenix | 360 | 164 | 524 |
| New York Tri-state | 190 | 126 | 316 |


## Current overview of huperscalers

*   OpenAI has plans to deploy hundreds of thousands of GPUs in their largest multi-site training cluster, which requires hundreds of megawatts of Critical IT Power.

*   Meta discusses an installed base of 650,000 H100 equivalent by the end of the year. They have currently 1M H100 in order.

*   GPU Cloud provider CoreWeave has big plans to invest $1.6B in a Plano, Texas facility, implying plans to spend for construction up to 50MW of Critical IT Power and install 30,000-40,000 GPUs in that facility alone with a clear pathway to a whole company 250MW datacenter footprint (equivalent to 180k H100s).

*   Microsoft has the largest pipeline of datacenter buildouts pre-AI era. They have been grabing any and all colocation space they can as well aggressively increasing their datacenter buildouts.

*   Amazon have made press releases about nuclear powered datacenters totaling 1,000MW. They were the last of the hyperscale's to wake up to AI.

*   Google, and Microsoft/OpenAI both have plans for larger than gigawatt class training clusters in the works.

*   From a supply perspective, sell side consensus estimates of 3M+ GPUs shipped by Nvidia in calendar year 2024 would correspond to over 4,200 MW of datacenter needs, nearly 10% of current global data center capacity, just for one year's GPU shipments.

*   AI is only going to grow in subsequent years, and Nvidia's GPUs are slated to get even more power hungry, with 1,000W, 1,200W, and 1,500W GPUs on the roadmap.

*   Nvidia is not the only company producing accelerators, with Google ramping custom inference accelerator production rapidly.

*   Going forward, Meta and Amazon will also ramp their in-house inference accelerators.


# NVIDIA systems

## DGX H100 SYSTEM

| Specification | Details |
| :--- | :--- |
| **GPUs** | 8x NVIDIA H100 Tensor Core GPUs |
| **GPU Memory** | 640GB total |
| **Performance** | 32 petaFLOPS |
| **System Power Usage** | ~11.3kW max |
| **Rack Units** | 8U |
| **CPU** | Dual 56-core 4th Gen Intel® Xeon® Scalable processors |

## DGX B200 SYSTEM

| Specification | Details |
| :--- | :--- |
| **GPUs** | 8x NVIDIA Blackwell GPUs |
| **GPU Memory** | 1,440GB total GPU memory |
| **Performance** | 72 petaFLOPS training and 144 petaFLOPS inference |
| **System Power Usage** | ~14.3kW max |
| **Rack Units** | 10U |
| **CPU** | 2 Intel® Xeon® Platinum 8570 Processors 112 Cores total, 2.1 GHz (Base), 4 GHz (Max Boost) |


## NVIDIA GB200 NVL72

| Specification | Details |
| :--- | :--- |
| **Configuration** | 36 Grace CPU : 72 Blackwell GPUs |
| **GPU Memory** | 1,440GB total GPU memory |
| **Performance** | 1,440 petaFLOPS |
| **System Power Usage** | ~120.0kW max |
| **Rack Units** | Full rack |
| **CPU** | 2,592 Arm® Neoverse V2 cores |


# Data centers

## Global data centers market

**74** Countries | **1004** Cities | **3362** Data Centers | **304** Providers


### Top 10 Colocation Providers

| Provider | Locations |
| :--- | :--- |
| China Telecom | 382 locations |
| Equinix | 246 locations |
| Digital Realty | 231 locations |
| Amazon AWS | 165 locations |
| Lumen | 105 locations |
| Zenlayer | 97 locations |
| MOD Mission Critical | 94 locations |
| DataBank | 69 locations |
| Cogent Communications | 51 locations |
| Hivelocity | 45 locations |


## North America data center trends H2 2023

*   In 2023, primary market supply grew 26% year-over-year to 5,174.1 MW.

*   An all-time high of 3,077.8 MW was under construction in primary markets, a 46% year-over-year increase. Construction increased most in Atlanta, growing by 211% to 732.6 MW under construction.

*   Northern Virginia had a 42% year-over-year price increase, the largest among primary markets.

*   Preleasing activity in primary markets is strengthening, with 2,553.1 MW (83%) of the 3,077.8 MW under construction preleased.

*   The overall vacancy rate for primary markets remains near a record low, at 3.7%. With few relocation options, most tenants are renewing existing leases rather than seeking new facilities.

*   Power availability continued to influence data center operators' location decisions more than geography did.

### H2 2023 wholesale primary market fundamentals
| Market | Inventory (MW) | Y-o-Y Change (MW) | Available MW/Vacancy Rate | 2023 Net Absorption (MW) | Rental Rates (kW/mo)** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Northern Virginia** | 2,499.1 | ▲ 439.0 | 34.7 / 1.4% | 424.4 | $150-$190 |
| **Dallas-Ft. Worth** | 565.3 | ▲ 173.1 | 41.6 / 7.4% | 155.2 | $135-$170 |
| **Chicago** | 559.6 | ▲ 217.4 | 11.7 / 2.1% | 226.8 | $145-$155 |
| **Silicon Valley** | 427.7 | ▲ 48.1 | 31.0 / 7.3% | 25.7 | $155-$250 |
| **Phoenix** | 360.0 | ▲ 35.5 | 14.2 / 3.9% | 48.8 | $170-$200 |
| **Atlanta** | 310.0 | ▲ 57.5 | 41.1 / 13.3% | 18.0 | $120-$130 |
| **Hillsboro** | 262.4 | ▲ 94.0 | 6.5 / 2.5% | 93.3 | $125-$170 |
| **New York Tri-State**| 190.0 | ▲ 12.5 | 12.3 / 6.5% | 14.1 | $170-$180 |


### H2 2023 wholesale secondary market fundamentals
| Market | Inventory (MW) | Available MW/Vacancy Rate | 2023 Net Absorption (MW) | Rental Rates (kW/mo)** |
| :--- | :--- | :--- | :--- | :--- |
| **Central Washington** | 186.4 | 0.4 / 0.2% | 20.9 | $135-$175 |
| **Austin/San Antonio** | 162.2 | 2.8 / 1.8% | 6.7 | $140-$175 |
| **Southern California**| 160.5 | 34.6 / 21.6% | 6.8 | $135-$160 |
| **Seattle** | 138.9 | 10.0 / 7.2% | 10.6 | $135-$175 |
| **Houston** | 134.1 | 26.5 / 19.7% | 19.2 | $140-$175 |
| **Denver** | 92.9 | 17.2 / 18.5% | 8.2 | $135-$145 |
| **Minneapolis** | 59.6 | 14.7 / 24.7% | -3.2 | $120-$175 |
| **Charlotte/Raleigh** | 52.1 | 13.6 / 26.0% | -1.2 | $115-$130 |


### Average asking rental rate with Y-o-Y % change for primary markets

- **2014 to 2017:** A gradual decline from ~$145 to ~$130.
- **2017 to 2022:** Rates hovered between ~$125 and ~$130.
- **2022 to 2023:** A significant jump in price, with a Y-o-Y change of **+18.6%**. The average rate rose to over $150/kW/month.


## Data center layout and constraints

*   While the DGX H100 server requires 10.2 kilowatts (kW) of IT Power, most colocation data centers can still only support a power capacity of ~12 kW per rack. Typical Hyperscale datacenter can deliver higher power capacity.

*   Server deployments will therefore vary depending on the power supply and cooling capacity available, with only 2-3 DGX H100 servers deployed where power/cooling constrained, and entire rows rack space sitting empty to double the power delivery density from 12 kW to 24 kW in colocation data centers.

*   As data centers are increasingly designed with AI workloads in mind, racks will be able to achieve power densities of 30-40kW+ using air cooling by using specialized equipment to increase airflow.

*   The future use of direct to chip liquid cooling opens the door to even higher power density by potentially reducing per rack power usage by 10% by eliminating the use of fan power, and lowering PUE by 0.2-0.3 by reducing or eliminating the need for ambient air cooling.


## Density

*   The trend towards higher power density per rack is driven by networking, compute efficiency and cost per compute. Roughly 90% of colocation data center costs are from power and 10% is from physical space.

*   The data hall where IT equipment is installed is typically only about 30-40% of a data center's total gross floor area, so designing a data hall that is 30% larger will only require 10% more gross floor area for the entire data center.

*   Considering that 80% of the GPU cost of ownership is from capital costs, with 20% related to hosting (which bakes in the colocation data center costs) the cost of additional space is 2-3% of total cost of ownership for an AI cluster.

*   Most existing colocation data centers are not ready for rack densities above 20kW per rack.

*   Chip production constraints will meaningfully improve in 2024, but certain hyperscale's and colocation data centers run straight into a data center capacity bottleneck.

*   Limits of 12-15kW power in traditional colocation will be an obstacle to achieving ideal physical density of AI super clusters.


## Data center constrains list

Some of the constrains are mentioned before, but there is more to consider:

*   **Energy** (3-5+ years to build capacity)
*   **Energy density per rack** (designing and cabling for 1MW+ of energy per 42U size rack)
*   **Capabilities to build new data centers and execution** (18-24 months for delivery)
*   **Grid network connection and power distribution** (transformers, switchgears, substation, transmission lines)
*   **Thermal dissipation/cooling of server racks** (challenge of cooling over 120kW and not long into the future 1MW per rack which opens two-phase cooling)
*   **Networking** (proximity between GPUs and positioning of racks, close is better and easier but not always possible)
*   **Load/weight per square meter/square foot** (static weight and point load)


# Current pain points

## Data center cunstructoin delays

| Delay Duration | Percentage of Respondents |
| :--- | :---: |
| 3-6 months | 38.80% |
| 6-9 months | 16.30% |
| 9-12 months | 15.50% |
| 12-18 months | 14.70% |
| 0-3 months | 9.30% |
| 18+ months | 5.40% |


## Insufficient power planning

| Factor | Importance |
| :--- | :---: |
| Availability of secure grid power | 16.40% |
| Cost of power | 13.30% |
| Access to renewable energy | 11.50% |
| Availability of workforce and skills| 11.20% |
| Capital expenditure | 10.40% |
| Network proximity | 10.20% |
| Tax breaks/financial incentives | 8.10% |
| Favorable regulation | 6.80% |
| Proximity to client populations | 4.70% |
| Community acceptance | 4.20% |
| Availability of water | 3.40% |


# Data center math

Simple calculation based on 20,480 GPUs (H100)

*   1x H100 GPU = ~$30,000
    
    **20,480 x H100 = ~$614.40M capex for GPUs**

*   1,389W per GPU -> 20,480 GPUs = 28.4 MW power
    
    1MW can power ~ 1,000 homes
   
    28.4 MW can power ~28,400 homes

*   **28.4 MW * 0.083 USD/kWh = ~$20.70M electricity per year**

Applying same formula, 100k cluster consumes ~140-150MW and will cost ~$100-130M in electricity per year.

## Data center power usage in the US

*   Data center Critical IT Capacity in the US will need to triple from 2023 to 2027.

| Metric | Units | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 | 2027 | 2028 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| AI Data Center Critical IT Power | MW | 318 | 640 | 1,102 | 3,332 | 8,499 | 16,356 | 28,140 | 41,337 | 56,280 |
| Non-AI Data Center Critical IT Power | MW | 14,231| 16,395| 18,376| 19,221| 19,798| 21,382| 23,520| 25,637| 27,175|
| **Critical IT Power** | **MW** | **14,550**| **17,035**| **19,478**| **22,553**| **28,297**| **37,738**| **51,660**| **66,974**| **83,455**|
| Utilization Rate | % | 65% | 66% | 66% | 67% | 70% | 72% | 73% | 74% | 75% |
| Critical IT Power Consumed | MW | 9,505 | 11,169| 12,826| 15,159| 19,668| 26,983| 37,800| 49,733| 62,688|
| Power Usage Effectiveness (PUE) | Ratio | 1.59 | 1.56 | 1.53 | 1.47 | 1.4 | 1.34 | 1.3 | 1.26 | 1.22 |
| Data Center Utility Power Consumed| MW | 15,142| 17,407| 19,660| 22,323| 27,538| 36,263| 48,957| 62,521| 76,684|
| **Data Center Actual Power Usage, per year** | **TWh** | **133** | **152** | **172** | **196** | **241** | **318** | **429** | **548** | **672** |
| As % of United States Power Generation| % | 3.30% | 3.70% | 4.00% | 4.50% | 5.50% | 7.10% | 9.50% | 12.00%| 14.60%|


# Infrastructure and energy

## US, East Asia, Western Europe and Middle East - overview

*   The energy supply situation in the US stands in stark contrast to East Asia and Western Europe, which host about 15% and 18% of global data center capacity, respectively. While the US is self-sufficient in natural gas, countries such as Japan, Taiwan, Singapore, and Korea import well over 90% of their gas and coal needs.

*   In Western Europe, electricity generation has been slowly declining, with a 5% drop cumulatively over the past five years. One reason for the drop is that nuclear power has become a political non-starter, causing nuclear power generation to decline massively.

*   A strong focus on the “environment” has led to dirty fuel sources such as coal also declining dramatically over the same time, although the cleanest power in the world nuclear has been replaced with coal and natural gas in some instances.

*   Renewable energy is increasing within Europe's power mix, but not fast enough, leaving many Europeans countries to scramble to pivot more towards natural gas, which now stands at 35-45% of the power generation mix for major Western European countries.

*   Europe is slowed building with many regulations and restrictions on the data center and manufacturing industries already in place. While small projects and pipelines for data centers are in progress, especially in France who at least has somewhat realized the geopolitical necessity, no one is planning to build Gigawatt class clusters in Europe.

*   Europe has less than 4% of globally deployed AI Accelerator FLOPs based on estimates.

*   Middle East is opening as a new strategic hub in geopolitical relationship with US. ASIC companies like Groq and Cerebras are having tight relationships with Middle East and most revenue coming from that region.


## Electricity generation - selected regions

-   **China:** Shows dramatic and steep growth, starting below the US in 2000 and rising sharply to become the world's largest electricity generator, exceeding 8,000 TWh by 2023.

-   **United States:** Generation has remained relatively flat, hovering around 4,000 TWh for the entire period.

-   **European Union (27):** Shows a slight decline over the period, starting above 2,500 TWh and ending slightly below it.

-   **Japan, South Korea, France, Germany, United Kingdom, Taiwan:** All show relatively flat or slightly declining generation, clustered much lower on the chart (all below 1,000 TWh).


## Building out AI infrastructure at scale

The AI data center industry is going to need the following:

*   Inexpensive electricity costs given the immense amount of power to be consumed on an ongoing basis, particularly since inference needs will only compound over time.

*   Stability and robustness of energy supply chain against geopolitical and weather disturbances to decrease likelihood of energy price volatility, as well as the ability to quickly ramp up fuel production and thus rapidly provision power generation at great scale.

*   Power generation with a low carbon intensity power mix overall, and that suitable to stand up massive quantities of renewable energy that can produce at reasonable economics.

**Countries that can provide this are contenders to be Real AI Superpowers.**

**This underscores a strong case for nuclear energy as a future source, capable of providing hundreds of megawatts to over gigawatt of electrical energy.**

**No energy source surpasses nuclear in terms of energy density, stability, predictability over extended periods, and safety.**


# Conclusion

*   Europe has less than 4% of global AI Accelerator FLOPs and is falling behind. Politics limit energy to support new builds or parts to be an AI superpower.

*   Most people knew about chip or GPU shortages over the last few years. That segment is slowly recovering and may recover first. Chip production is mainly done in Taiwan by TSMC, but is resolving by building chip fabs on US ground.

*   The biggest problem is energy, then energy density. The US and Europe had little growth in energy production over the last decade. Getting new energy sources and increasing production is hard. The energy grid is the next problem since it wasn't designed for those loads and lacks investment to upgrade (on average 40-50 years old).

*   After solving the issue of delivering over 1MW per rack in data centers, power is needed to cool equipment with two-phase cooling. Gigawatt data centers will be a huge challenge. Swings in power can blow up grid and will need stabilization.

*   Networking in data centers is the next step. If GPU servers are far apart, more fiber/cabling is needed, increasing costs. The short reach enables lower cost multimode optical transceivers as opposed to expensive single mode.

*   Parts of the problems can be solved using nuclear energy and building data centers near nuclear power plants. Solar and BESS (Battery Energy Storage System) are much faster deployed and more scalable in current environment.

*   Most currently built data centers are powered with natural gas and gas turbine supply chain can't follow demand.

*   **We have not resolved any part of the supply chain to meet AI demand for the next decade, with energy being the most challenging issue.**
