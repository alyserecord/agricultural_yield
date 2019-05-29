# Global Agricultural Yield
## The dataset
The dataset used for this analysis came from the Food and Argricultural Organization (FAO) of the United Nations. The FAO's Crops dataset consists of area harvested (ha), production (tons), and yield (hg/ha) data for 173 crops broken out by country and years 1961-2017. 

## What crops have had the most consistent yield increase globally? 

By using the crop yield data, I calculated the yeild change rate year over year for the global yeild average of each crop.

For example here is the yield rate of change for Avocados globally from 2000 to 2010:
![Avocado Yield List](/images/avocadoyieldlist.png)

By analyzing the crop yield data, I identified crops where the yeild rate change was greater than a given threshold for the greatest number of years. Olive, Pistachios, Quinoa, Hempseed, and Cloves are all crops that had a 5% or greater yeild change rate for 20 or more years between 1961 and 2017. Of those, I began to notice that even though they had a large number of years that the Yeild rate change was significant, it was largely due to the irradic year over year yield. 

For example, even though Olives yeild did increase by more than 5% for more than 20 years, it was spread across many years when the yield had dropped in previous years.

![Olives](/images/olivesyield.png)

One crop that did stand out was Cloves, which did not seem to drop between yeild rate increases on average. This made me wonder which crops increased their yield for the longest period of time consistenly. After additional analysis to look for crops who's global yield average had increased for the highest number of years without decreasing, it was indeed Cloves that had the most consistent yield growth.

![Cloves_Global](/images/cloves_yield_prod.png)

While it was interesting that cloves had the most consitent yield growth, I wanted to know the distribution among the countries where it is produced. I wanted to know if this average is being driven by one country primarily, or if it is a true representation of the entire global production. 

The global clove productions is dominated by Indonesia, but interestingly Indonesia is not the largest driver of the clove yield rate increase. The United Republic of Tanzinia and Sri Lanka are much more responsible for the increase in yield.

![Cloves prod by country](/images/clovesprodcountries.png)
![Cloves prod by country](/images/clovesyieldcountries.png)

## Hypothesis Test

Null Hypothesis: The producer price of Cloves was not impacted by the increase in yeild.
Alternate Hypothesis: The producer price was lower or higher depending on the increase in yeild.

