# Global Agricultural Crop Yield EDA Project
## Why this topic?
I choice this topic because I've always been interested in food production and how it changes over time due to various factors. I found this worldwide dataset about many different crops for many different years and countries. I was interested to learn more about the various crop yield rates so I chose to do my project on this dataset. My ultimate goal was to look at how/if the yield changes impacted the the price of the crop.

## The dataset
The dataset used for this analysis came from the Food and Argricultural Organization (FAO) of the United Nations. The FAO's Crops dataset consists of area harvested (ha), production (tons), and yield (hg/ha) data for 173 crops broken out by country and years 1961-2017. The FAO allows you to download the entire dataset 40,000+ rows, and each row details a crop, a country, and the columns provide details about that crop and country for 50+ years.

Also used in my project is a crop price dataset that also came from the FAO. The price dataset included the producer price per ton of a crop, by country by year. Similar to the crop production dataset, this dataset can by downloaded in its entirety at the FAO's website. 

[Food and Argricultural Organization of the United Nations - Data](http://www.fao.org/faostat/en/#data)

## What crops have had the largest yield increase globally? 

I was interested to know which crops had the largest increase in yield (ha/hg) for the 1961 - 2017 timeframe. I analyzed this in a number of different ways to narrow down which crops had the most significant increase.

### Number of years with a significant increase

First by using the crop yield data, for a given crop I averaged the yield rate for all countries that procuded that crop. Then I calculated the global yield change rate year over year for each crop.

For example here is the yield rate of change for Avocados globally from 2000 to 2010:

![Avocado Yield List](/images/avocadoyieldlist.png)

By analyzing the crop yield data, I identified crops where the yield rate change was greater than a given threshold for the greatest number of years. **Olives, Pistachios, Quinoa, Hempseed, and Cloves** were all identified as crops that had a 5% or greater yield increase rate for 20 or more years between 1961 and 2017. Of those crops, I noticed that even though they had a large number of years that the yield rate change was significant, it was largely due to the erradic year over year yield. 

For example, even though Olives yield did increase by more than 5% for more than 20 years, it was spread across many years when the yield had dropped significantly in the previous year.

![Olives](/images/olivesyield.png)

One crop that did stand out was Cloves, which did not seem to drop between yield rate increases on average. This made me wonder which crops increased their yield for the longest period of time consistently. 

### Consistent increase in yield

I calculated which crops had the largest number of years where the yield consistently increased by looking at the year over year change rate in yield when the change rate did not fall below zero. The top crops from this analysis were **Vegetables Primary, Cloves, Nutmeg, mace and cardamoms, Cassava leaves, Pumpkins, squash and gourds**.

Interestingly Cloves was still near the very top of the list. Starting in the early 1990s, the Cloves yield started to increase and continued to inclear through 2017. The production of Cloves during this time also on average was increasing.

![Cloves_Global](/images/cloves_yield_prod.png)

Cloves is an interesting crop to come out of this analysis, so maybe you are wondering what they are used for like I was? You are in luck, [here](https://www.thespruceeats.com/cloves-765162) are some of its uses. Or if you are a fan of a particular Starbucks beverage, you may be thinking of thinking of [this](https://www.starbucks.com/menu/drinks/espresso/pumpkin-spice-latte?ct=39988).

While it was interesting that Cloves had one of the most consistent year over year yield growth, I wanted to know the distribution among the countries where it is produced. I wanted to know if this average is being driven by one country primarily, or if it is a true representation of the entire global production. 

I found that the global Cloves productions is dominated by Indonesia. The following two graphs are looking countries that produce the largest quantity of Cloves 
![Cloves prod by country](/images/clovesproductioncountries.png)

But interestingly, Indonesia is not the largest driver of the clove yield rate increase. The United Republic of Tanzania and Sri Lanka are much more responsible for the increase in yield.
![Cloves yield by country](/images/clovesyieldcountries.png) 

## Price data
My plan was to take a look at the producer pricing data for the crops that had the highest yield increases, to see how/if the producer price was impacted by the increase in yield. 

### Cleaning the price data
The price data needed a bit more data cleaning than the crops production data. The biggest hurdle was that the FAO's website did not indicate if the price data had been adjusted for inflation, so I assumed that it had not been. I used the [cpi library](https://github.com/datadesk/cpi) to adjust each USD value to the current data equivalent.

### Pitfalls of the price dataset
While I was cleaning the data, I found in the price dataset was that it only included years 1991 - 2017, and it did not contain all of the crops that I for which had production and yield data. For example, the crop with the most consistent yield increase (Vegetables Primary) was not included in the price data. Similarly, even if a crop was included it did not have data for all the countries and it had many nulls for the countries where it did have some data.

To continue with the Cloves theme, I took a look at the price data I had for Cloves. Most of this information is from Sri Lanka which contributed some to the overall yield increase, but was not the primary driver.

Although it may be increasing slightly over time there was not a strong correlation between the yield increase and the price, so I chose to not pursue the price angle further given the time allotted for this project.

![Cloves price data](/images/clovesprice.png)

## Compound annual growth rate
As futher analysis of the yield growth and how it compared across crops, I calculated the compound annual growth rate (CAGR) for global average yield per crop. The CAGR was supposed to provided insight into the average yield change rate of the crop over time, but I couldn't really figure out how to use it in the time allotted for the project.

## Future work

#### Continue price data comparison
Since the price data is already cleaned and adjusted for inflation, I would like to pursue the comparison between yield and pricing future. Since it did not pan out looking at the top two crops with the most consistently growing yield (Vegetables Primary and Cloves), I want to look at some of the other crops than were also growing in yield consistently. Also, it would be interesting to compare to the production to the price data as well, to see as a particular crop's production was growing if it had an impact on its price.  

#### Compound annual growth rate
Since I have calculated the CAGR for all crops, I'd like to spend more time understanding how this data could be utilized for furture analysis.

#### Hypothesis testing
My main goal of this project was to run hypothesis tests on the crops that had the most consistent yield and compare them to the yield rates of the population of crops. I struggled to set up a test and ran out of time, so I would like to complete this goal as future work on this project.
