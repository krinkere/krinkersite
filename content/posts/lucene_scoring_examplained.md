Title: Lucene scoring examplained
Date: 2015-04-30 19:48
Modified: 2018-03-15 12:30
Status: published
Category: Tutorial
Tags: lucene, search
Slug: Lucene_scoring_examplained
Authors: Al Krinker
Summary: Overview of Lucene scoring

Several good books already explain what Lucene scoring really means and how it is calculated in great detail with lots of basic concepts explain.
In this, post I am going to try to keep it high level for people already familiar with the basics and go straight for the scoring overview.

The factors involved in Lucene's scoring algorithm are as follows:<br />
1. tf = term frequency in document = measure of how often a term appears in the document<br />
2. idf = inverse document frequency = measure of how often the term appears across the index<br />
3. coord = number of terms in the query that were found in the document<br />
4. lengthNorm = measure of the importance of a term according to the total number of terms in the field<br />
5. queryNorm = normalization factor so that queries can be compared<br />
6. boost (index) = boost of the field at index-time<br />
7. boost (query) = boost of the field at query-time<br />

The implementation, implication and rationales of factors 1,2, 3 and 4 in DefaultSimilarity.java, which is what you get if you don't explicitly specify a similarity, are:
note: the implication of these factors should be read as, "Everything else being equal, … "

1. tf<br />
Implementation: sqrt(freq)<br />
Implication: the more frequent a term occurs in a document, the greater its score<br />
Rationale: documents which contains more of a term are generally more relevant

2. idf<br />
Implementation: log(numDocs/(docFreq+1)) + 1<br />
Implication: the greater the occurrence of a term in different documents, the lower its score<br />
Rationale: common terms are less important than uncommon ones

3. coord<br />
Implementation: overlap / maxOverlap<br />
Implication: of the terms in the query, a document that contains more terms will have a higher score<br />
Rationale: self-explanatory

4. lengthNorm<br />
Implementation: 1/sqrt(numTerms)<br />
Implication: a term matched in fields with less terms have a higher score<br />
Rationale: a term in a field with less terms is more important than one with more<br />
queryNorm is not related to the relevance of the document, but rather tries to make scores between different queries comparable. It is implemented as 1/sqrt(sumOfSquaredWeights)<br />
So, roughly speaking (quoting Mark Harwood from the mailing list),
    - Documents containing all the search terms are good
    - Matches on rare words are better than for common words
    - Long documents are not as good as short ones
    - Documents which mention the search terms many times are good

The mathematical definition of the scoring can be found in [org.apache.lucene.search.Class Similarity](https://lucene.apache.org/core/2_9_4/api/all/org/apache/lucene/search/Similarity.html )

### Customizing scoring
Its easy to customize the scoring algorithm. Just subclass DefaultSimilarity and override the method you want to customize.
For example, if you want to ignore how common a term appears across the index,
```java
Similarity sim = new DefaultSimilarity() {
  public float idf(int i, int i1) {
    return 1;
  }
}
```
and if you think for the title field, more terms is better
```java
Similarity sim = new DefaultSimilarity() {
  public float lengthNorm(String field, int numTerms) {
    if(field.equals("title")) return (float) (0.1 * Math.log(numTerms));
    else return super.lengthNorm(field, numTerms);
  }
}
```