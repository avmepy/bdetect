the project is divided into sub-projects

most packages contain the review.ipynb to explain how the functions work

more about each:


1. Bot:

    bot written in sikuli
    plays the game presented in the game-apk branch

2. Parser:

    - read logs
    - union logs
    - splitting into windows

3. Features:

    - extract features from logs

4. Classifier:

    - with the help of various classifiers, it distinguishes the
        game of еру bot from a game of a human,
        as well as the game of two different people

5. Boosting:

    - update classifiers


6. Approximator:

   - visually separates players by features

7. Logs and Union_logs:

    - example of logs and union_logs respectively