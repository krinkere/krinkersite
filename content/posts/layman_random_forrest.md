Title: Layman's Introduction to Random Forests
Date: 2018-04-20 12:27
Modified: 2018-04-20 12:30
Status: published
Category: Reference
Tags: data science, machine learning
Slug: layman_random_forrest
Authors: Al Krinker
Summary: Layman's Introduction to Random Forests by Edwin Chen

Suppose you’re very indecisive, so whenever you want to watch a movie, you ask your friend Willow if she thinks you’ll like it. In order to answer, Willow first needs to figure out what movies you like, so you give her a bunch of movies and tell her whether you liked each one or not (i.e., you give her a labeled training set). Then, when you ask her if she thinks you’ll like movie X or not, she plays a 20 questions-like game with IMDB, asking questions like “Is X a romantic movie?”, “Does Johnny Depp star in X?”, and so on. She asks more informative questions first (i.e., she maximizes the information gain of each question), and gives you a yes/no answer at the end.

Thus, Willow is a **decision tree** for your movie preferences.

But Willow is only human, so she doesn’t always generalize your preferences very well (i.e., she overfits). In order to get more accurate recommendations, you’d like to ask a bunch of your friends, and watch movie X if most of them say they think you’ll like it. That is, instead of asking only Willow, you want to ask Woody, Apple, and Cartman as well, and they vote on whether you’ll like a movie (i.e., you build an **ensemble classifier**, aka a forest in this case).

Now you don’t want each of your friends to do the same thing and give you the same answer, so you first give each of them slightly different data. After all, you’re not absolutely sure of your preferences yourself  you told Willow you loved Titanic, but maybe you were just happy that day because it was your birthday, so maybe some of your friends shouldn’t use the fact that you liked Titanic in making their recommendations. Or maybe you told her you loved Cinderella, but actually you really really loved it, so some of your friends should give Cinderella more weight. So instead of giving your friends the same data you gave Willow, you give them slightly perturbed versions. You don’t change your love/hate decisions, you just say you love/hate some movies a little more or less (formally, you give each of your friends a **bootstrapped** version of your original training data). For example, whereas you told Willow that you liked Black Swan and Harry Potter and disliked Avatar, you tell Woody that you liked Black Swan so much you watched it twice, you disliked Avatar, and don’t mention Harry Potter at all.

By using this ensemble, you hope that while each of your friends gives somewhat idiosyncratic recommendations (Willow thinks you like vampire movies more than you do, Woody thinks you like Pixar movies, and Cartman thinks you just hate everything), the errors get canceled out in the majority. Thus, your friends now form a **bagged (bootstrap aggregated) forest** of your movie preferences.

There’s still one problem with your data, however. While you loved both Titanic and Inception, it wasn’t because you like movies that star Leonardio DiCaprio. Maybe you liked both movies for other reasons. Thus, you don’t want your friends to all base their recommendations on whether Leo is in a movie or not. So when each friend asks IMDB a question, only a random subset of the possible questions is allowed (i.e., **when you’re building a decision tree, at each node you use some randomness in selecting the attribute to split on**, say by randomly selecting an attribute or by selecting an attribute from a random subset). This means your friends aren’t allowed to ask whether Leonardo DiCaprio is in the movie whenever they want. So whereas previously you injected randomness at the data level, by perturbing your movie preferences slightly, now you’re injecting randomness at the model level, by making your friends ask different questions at different times.

And so **your friends now form a random forest**.