# tigergraph-hackathon
In today’s hyper-digital world, algorithms determine what content we see. Narratives are forced upon us into an echo chamber. Confirmation Bias is the concept that when we see something that reinforces our current thinking, we are more inclined to believe and accept that as truth. In this graph challenge, we create a solution that empowers users to consider diverse perspectives and in turn – fosters critical thinking. 

For this Tiger Graph challenge, we extract post listings from Reddit across the entire community. We apply similarity and sentiment analysis to look for patterns.

Using these findings, we can run custom graph queries and traversals across our graph solution to suggest other posts that are relevant but different in their mood or subreddit community.

Offering diverse and alternative perspectives can break confirmation bias and foster critical thinking - allowing users to think for themselves.

The project involves: 
  - Tiger Graph
  - Python
  - Graphistry
  - Jupyter notebook
  - Reddit

## Query Instructions

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

