# TigerGraph Graph for All Challenge Submission
## Challenge: Foster Critical Thinking

# Data Mining Perspectives
**Contributers and Contact Information:** Damie Brooks at damiebrooks@outlook.com, or on [Linkedin](https://www.linkedin.com/in/damiebrooks0803/)

**Problem Statement addressed:**

Human thought is prone to errors. In recent times, we have gotten better at understanding why those errors occur and how to utilize and exploit them. Modern advances in technology like Artificial Intelligence, big data, cloud computing, and blockchain can all be used to manipulate our cognitive biases in order to sell us products and services or make us value certain information more than others. One of the most notable of these cases is the utilization of confirmation bias by social media companies to create “filter bubbles” of opinions that a person agrees with. This not only prevents us from being well-informed, but ultimately leads to a lack of critical thinking and adds to polarization. If we only listen to and validate one way of thinking, and do not expand and question it, sooner or later we will become intolerant citizens. And when there is no more tolerance, the very foundations of our democratic coexistence begin to crack.

Identify a way to use these technologies to break through the confirmation bias and the filter bubbles enhanced by social media platforms. The aim is to foster critical thinking in digitally literate citizens who access and critically relate to different types of information, and who increasingly engage in dialogue with other points of view and with those who think differently. The goal is not to come up with an alternative business model for digital platforms or to eliminate the confirmation bias of the human mind, which would be almost impossible. Rather, it is to empower citizen-users with the necessary tools to be able to identify the presence of these biases and to consciously seek diverse perspectives and opinions on the same topic. 

**Description**: 

In today’s hyper-digital world, algorithms determine what content we see. Narratives are forced upon us into an echo chamber. Confirmation Bias is the concept that when we see something that reinforces our current thinking, we are more inclined to believe and accept that as truth. In this graph challenge, we create a solution that empowers users to consider diverse perspectives and in turn – fosters critical thinking. 

For this Tiger Graph challenge, we extract post listings from Reddit across the entire community. We apply similarity and sentiment analysis to look for patterns.

![Data Model](https://raw.githubusercontent.com/DamieBrooks0803/tigergraph-hackathon/main/FCT_graphDataModel.png)

Using these findings, we can run custom graph queries and traversals across our graph solution to suggest other posts that are relevant but different in their mood or subreddit community.

Offering diverse and alternative perspectives can break confirmation bias and foster critical thinking - allowing users to think for themselves.

![Solution Architecture](https://raw.githubusercontent.com/DamieBrooks0803/tigergraph-hackathon/main/FCT_TigerGraph_Arch_DamieBrooks.png)

The solution for our graph challenge involves 3 main steps: 

- Step 1: We extract data from Reddit and enrich the data with sentiment and similarity analysis. 
- Step 2: The data is loaded into Tiger Graph solution with various traversal and data science queries. 
- Step 3: Using a Jupyter notebook, Graphistry for visualization, and custom queries, we suggest posts that are relevant by topic, similar by content, but diverse in their viewpoint. 


## Written Defense
- **Impactful in solving a real world problem:**  

Psychology teaches that confirmation bias negatively affects our lives by causing us to limit our viewpoint, unfairly judge others who think differently, and subsequently causes us to make poorer decisioning choices because of this limited view. Seeing or believing only things that are in line with your current thinking, without fairly considering other perspectives, prevents us from being objective. When you can thinking critically while looking at various sides of a topic, it raises your empathy to others as well as helps you see the big picture. In social media, this translates to a more well-rounded acceptance of others and a generally happier outlook when confronted with information that would otherwise be distressing.

- **Innovative use case of graph:** 

My project considers the Social Media community of Reddit as the general "internet town square." Reddit communities span a wide range of topics. But because everything is text-based (with user generated content) there were opportunities for natural language processing and similarity analysis. My project embeds sentiment and similarity into the graph itself to make the queries simpler and more efficient. The graph traversal queries look for similar viewpoints based on their Reddit community but diverse based on sentiment and content. Embedding similarity and sentiment into the graph through the data model allows for simple queries, rather than trying to query for this analysis within the post nodes.

- **Ambitious and complex graph:**

The stock Reddit post data model is limited to a user posting a listing in a subreddit. The data model in my project extends this to include a "call type" - which type of extraction are we pulling from Reddit, as well as the similarity of subreddits by their name, and the sentiment of the post headline. We also include the mood, determined by the sentiment score of the headline. The size of my graph was limited to what my single cluster free tier would support - about 96,000 vertices, resulting in around 386,000 edges. Given a larger cluster, Reddit allows you to pull 100,000 pulls a day, so the size of the graph could be in the Trillions. This would optimize recommendations with a closer similarity score.

- **Applicable graph solution:** 

Any user generated content can leverage similarity and sentiment to offer recommendations to others. This type of graph model that I propose, and the solution architecture in my project can be widely applied to any industry or application that leverages user generated content such as, but not limited to: Product Reviews, Social Media Posts such as Twitter and Facebook, and Comments on Videos, Forums, Blogs, etc.

Other additions: 

 - **Data**: Custom polled Reddit data across all subreddits for the months of March and April, focusing on hot, controversial, and new posts. 
 - **Technology Stack**: Tigergraph, Python, GSQL, Jupyter, Streamlit, CSS, HTML, Graphistry

## Dependencies
Python libraries used:

### DATA EXTRACTION
- json 
- List
- pandas
- requests
- re
- string
- sched, time
- csv
- datetime
- VaderSentiment

### TIGERGRAPH
- pyTigerGraph
- pandas
- plotly express

### GRAPHISTRY
- graphistry

### STREAMLIT
- pandas
- streamlit
- streamlit components


## Installation

Instructions on installing, configuring, and running the project to replicate and assess it. 

1. Clone repository - [Tigergraph challenge on Github](https://github.com/DamieBrooks0803/tigergraph-hackathon)
2. Install dependencies
3. Access data

Run notebooks:

- RedditConnection.ipynb for running Tigergraph queries
(my free instance turns off on its own, so someone needs to turn it on in order for the queries to run)
- graphistry_example.ipynb for visualizing in Graphistry (not required for Tigergraph queries)
- In data folder, Reddit_large_5.csv is a sample of the extraction from Reddit

4. Steps to build/run project

Given a subreddit: War, Cryptocurrency, or Antiwork, visit the [streamlit app](https://share.streamlit.io/damiebrooks0803/tigergraph-hackathon/main/streamlitapp/streamlit_app.py) for recommended posts. 

![Recommendations from a sample war post](https://raw.githubusercontent.com/DamieBrooks0803/tigergraph-hackathon/main/recommendationUI.png)


Or run the queries yourself in your own python notebook or through my RedditConnection notebook...

## Instructions on how to run queries that are not included in the default notebooks
### Query Instructions

These are the queries can you run yourself through the RedditConnection juypyter notebook. Some are embedded within the notebook, but for those that aren't, I listed out the queries and what they do. 

Keep in mind the listing IDs and subreddits are case sensitive. 

#### AuthorMostPosts

Retrieve a list of the authors ordered by the most posts they have listed. Runs against the entire data set including all subreddits. Returns 10.

#### MostEngagingSubreddits
Retrieve a list of subreddits ordered by the most comments across all of their posts. Runs against the entire data set including all subreddits. Returns 20.

#### SimilarSubreddits

Retrieve a list of subreddit names that are most similar in name to a given subreddit name. 

#### SubredditMostPosts

Retrieve a list of subreddit names ordered by the most posts in that subreddit. Runs against the entire data set of subreddits. Returns 10.

### Use these queries to find listing IDs to use in the recommendation queries below.

_A listing id is created by removing the spaces from the headline/title of each listing then adding an underscore and then the subreddit the listing was posted in. This is because many listings are posted in more than one subreddit._

#### TopListingIDs
Returns the top 10 posts in the entire data set including all subreddits, ordered by the number of comments. 

#### TopListingIDsInSubAntiwork
Returns the top 10 posts in the Antiwork subreddit, ordered by the number of comments. 

#### TopListingIDsInSubCryptocurency
Returns the top 10 posts in the Cryptocurrency subreddit, ordered by the number of comments.

#### TopListingIDsInSubWar
Returns the top 10 posts in the War subreddit, ordered by the number of comments. 

#### TopListingIDsInSub
Returns the top 10 posts in a given subreddit by name, ordered by the number of comments. Use this as a generic version of the recommendation queries. 

### Our project UI queries:
#### Q1controversial

Given a post by listing id, retrieve a list of posts in that post's subreddit that are considered controversial (or polarizing, meaning they have a large number of up and down votes.)

#### Q2new

Given a post by listing id, retrieve a list of posts in that subreddit that are new and maybe don't have as much engagement yet, such as comments or votes. 

#### Q3sentiment

Given a post by listing id, retrieve a list of posts in that post's subreddit that has a varied sentiment from the given post. 

## Known Issues and Future Improvements

The Streamlit recommendation app is built using static data added in from the Q1, Q2, and Q3 queries. This was because I experienced performance issues when trying to extract the data from the database directly from the app. Future improvements would leverage installed queries that can be run automatically with dynamic data. I also sampled subreddits: War, Antiwork, and Cryptocurrency. Being able to show recommendations from any subreddit would be ideal. Finally, if I had a fully working cluster on Tigergraph, I would like to be able to continuously stream Reddit posts every day at 100,000+ records a day to get a bigger view of wider perspectives. However, even in the small sample, I think this illustrates the problem and opportunity with analyzing user-generated-content well. 

I did not include comments into my graph other than the number of comments on a post from an engagement perspective. Extending the graph solution to include comments would add in users that maybe don't post their own postings but will more likely comment on an existing post. 

## Reflections

One of the things that surprised me was how much time to took for me to ramp up on all of the new technologies. Originally, I expected the vast majority of my time would have been spent on the GSQL queries but I ended up spending a lot of time extracting the data from Reddit. If I had used a sample dataset that was already provided, it would have given me more time to get deeper in to the data science. What it taught me though is that a working end to end project has many moving parts that need to work in concert together. It's so much more than just putting a CSV in a database and writing a query to pull an answer out. 

This project gave me a lot of insight into our society as a whole because I saw posts and subreddits within the community that I would not have ever seen before. Because the Russian/Ukrainian war broke out right when the project started, I was able to see a lot of posts around that topic, good and bad. I also found it interesting how many people merely share existing posts or reshare content rather than write their own. And it surprised me that so many people don't post body content more than they do post an interesting headline.

Finally, I learned that Reddit does moderation of their content quite often - which impacts which posts you can show. It's hard to beat an echo chamber or a narative-forcing algorithm that removes content before anyone can even see it. And while I understand why that is done, I also see how it could be dangerous if wielded for the wrong reasons. 

## References

I appreciated the Tigergraph Data Model workshop and the Graph Gurus courses online to help me select which algorithm types I wanted to implement based on my data and also consider different ways to model the data to make it easier to query. 
