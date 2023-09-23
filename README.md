# Computational Scientist's Toolbox Assignment
<!---->
<!-- This repository contains a pdf conversion of the presented slides, in case you missed anything during the lecture. -->
<!---->
<!-- To complete the lecture, carry out the following tasks (i.e., homework): -->
<!---->
<!-- 1. Create a free GitHub account if you don't already have one. -->
<!-- 2. Fork this repository. -->
<!-- 3. Create a markdown (.md) named "solution_<your name>.md" file that will contain the following: -->
<!-- 4. The title of the following papers pivotal to our knowledge: -->
<!--   - MCC Van Dyke et al., 2019 -->
<!--   - JT Harvey, Applied Ergonomics, 2002 -->
<!--   - DW Ziegler et al., 2005 -->
<!-- 5. Create one plot from the dataset "istherecorrelation.csv", with DPI=300. The objective is to visualize the data in a way that you consider representative. Include the resulting plot image in the markdown file and add a few lines of interpretation on the data. -->
<!-- 6. Commit and push these two files to your fork. -->
<!-- 7. Create a pull request for me to this (the original) repo. (Hint: you can use the "New pull request" button and then do a "compare across forks"). -->
<!-- 8. You are done, I will see the pull requests and check your work. -->

Welcome to the GitHub repo for my Computational Scientist's Toolbox Assignment. 

We were supplied with a sample csv file containing some data to analyze. Unfortunetaly the metadata for the file is missing, there for it is unclear what the second column of the `.csv` file means.

The Correlation's are as follows

|                                     | Year        | WO [x1000]  | NL Beer consumption [x1000 hectoliter] |
|-------------------------------------|-------------|-------------|----------------------------------------|
| Year                                | 1.000000    | 0.984562    | 0.825067                               |
| WO [x1000]                          | 0.984562    | 1.000000    | 0.818064                               |
| NL Beer consumption [x1000 hectoliter] | 0.825067    | 0.818064    | 1.000000                               |

We can clearly see that tehre is a strong correlation between all three variables.

This can also clearly be see in the following plot:
[!BeerConsumption.Png]
