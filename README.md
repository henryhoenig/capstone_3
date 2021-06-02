# Examining Twitter Content Around #StopTheSteal


![hash45](https://user-images.githubusercontent.com/29707241/119089742-3f397b80-b9d0-11eb-979b-1a327f737211.png)

&nbsp;

### Objectives and Procedures

* Use network analysis and topic modeling to examine the content around the #StopTheSteal hashtag shortly before and after the storming of the U.S. Capitol. The purpose was to see what topics and people were associated in the minds of those tweeting #StopTheSteal at this time.

* I scraped all tweets containing #StopTheSteal from Jan. 5 until Jan. 7. That was about 16,000 tweets from about 7,000 acccounts. The data did not include follower lists, which are more difficult and far more time consuming to scrape. 

* Note: Twitter permanently suspended more than 70,000 accounts that were "primarily dedicated to sharing QAnon content" in the days after Jan. 6. This naturally affected the results, but I thought it was worth examining the content generated by people not primarily concerned with spreading QAnon content.

* I conducted network analysis on co-occurrences of hashtags and mentions, as well as topic modeling on the text using Latent Dirichlet Allocation. I chose only the most frequently occurring hashtags and mentions to build the network graphs.

&nbsp;
### Exploratory Data Analysis

* With the elimination of the QAnon accounts, the most prolific tweeters were largely unknown.

![top_tweeters2](https://user-images.githubusercontent.com/29707241/120519959-d9b69900-c398-11eb-88aa-884111191b43.png)

&nbsp;
* The single most retweeted tweet came from Terrence Williams, an actor. He tweeted a video of a woman, a Trump supporter, being asked to leave a flight to Washington, D.C., on Jan. 5, apparently because she made a joke about not wearing a mask. 

* Jeff Hall's tweet, sent in the early morning hours of Jan. 6, showed dozens of people marching for Trump on the streets of Tokyo.


![most_retweeted_singles](https://user-images.githubusercontent.com/29707241/120520270-35812200-c399-11eb-929c-38bc6e1f62dd.png)

&nbsp;

* Most of those gathering the most retweets in total only sent one or two tweets. 

![most_retweeted](https://user-images.githubusercontent.com/29707241/120528069-a5df7180-c3a0-11eb-8cb3-56f1be76cd35.png)

&nbsp;




### Looking at Hashtag and Mentions With Network Analysis

* Getting even more selective offers a clearer view of some of the connections among hashtags. 

* The thicker the lines, the stronger the connection (the more frequent the co-occurrence).


![hash65_screen2](https://user-images.githubusercontent.com/29707241/119090099-c981df80-b9d0-11eb-8143-1fd7d973928a.png)


&nbsp;


* Zooming in on sub-graphs in the main graph offers a more granular view. 

* #MAGA was the hashtag most strongly linked to #StopTheSteal.

![MAGA45](https://user-images.githubusercontent.com/29707241/119091045-13b79080-b9d2-11eb-99e8-5083ba91af8b.png)


&nbsp;
* Naturally, the name Trump was also closely linked to #StopTheSteal.

![trump45](https://user-images.githubusercontent.com/29707241/119090241-ffbf5f00-b9d0-11eb-8a01-239a33b85c5f.png)


&nbsp;

* Kraken was the name Trump lawyer Sidney Powell gave to what she said was a cache of documents that would prove Trump won.

![kraken45](https://user-images.githubusercontent.com/29707241/119090291-106fd500-b9d1-11eb-9a83-aab7c397aa63.png)


&nbsp;

* This Japanese phrase translates roughly as "turn it over," with revolutionary connotations. 

* QAnon has a significant following in Japan.

![turnitover45](https://user-images.githubusercontent.com/29707241/119090368-2b424980-b9d1-11eb-9beb-2c9ba62527ca.png)


&nbsp;
* A network graph of some of the most frequent mentions


![mentions50_curved](https://user-images.githubusercontent.com/29707241/119090821-b6234400-b9d1-11eb-86dc-3b0bd3630351.png)

&nbsp;


* Zooming in on the co-occurring mentions

![trumpmentions](https://user-images.githubusercontent.com/29707241/119091138-39449a00-b9d2-11eb-8f3f-ddf5bbb67be3.png)


&nbsp;
![supremecourt](https://user-images.githubusercontent.com/29707241/119091302-7741be00-b9d2-11eb-9bd0-7793ce394770.png)



&nbsp;
* Ezra Cohen-Watnick was a senior Trump intelligence official who some believed was "Q". 

![ezracohen](https://user-images.githubusercontent.com/29707241/119091162-42ce0200-b9d2-11eb-9a30-a59860b0b203.png)


&nbsp;
* Far-right news organizations Newsmax and One America News were prominent in the mentions.

![newsmax](https://user-images.githubusercontent.com/29707241/119091353-8a548e00-b9d2-11eb-8211-11dfd30b51d5.png)


&nbsp;


### Conclusions

* Network analysis requires a great deal of context and interpretation. It is clear that despite the removal of tens of thousands of QAnon-driven accounts, the content surrounding #StopTheSteal remained highly conspiratorial and angry. 

* Many of the most prominent QAnon slogans remained at the center of the conversation, as did many of the people most associated with QAnon and conspiracy theories regarding the election. These included Ezra Cohen, Brandon Straka, Sidney Powell and Lin Wood. Far right news organizations Newsmax, One America News and Breitbart News also remained at the center of the conversation. Senator Josh Hawley, the subject of much derision in the mainstream media, did not receive much attention in tweets with #StopTheSteal. 

### Further Consideration

* Given more time, I would like to scrape and examine the user-follower networks. I would also like to use clustering and word embedding to get a clearer look at the segmentation of communities and conversations. 

* I also plan to automate this entire process, to enable quick and reproducible examinations of Twitter conversations. 
