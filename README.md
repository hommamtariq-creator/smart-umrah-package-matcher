# Smart Umrah Package Matcher

Final project for the Building AI course

## Summary

Smart Umrah Package Matcher is an AI-assisted recommendation idea that helps travelers find Umrah packages that fit their preferences for budget, trip length, hotel distance, airline, and room type. It ranks available packages by how closely they match the traveler's needs.

## Background

Choosing an Umrah package can involve comparing many details at the same time: price, number of days, hotel distance, airline, baggage, and room type. Comparing these factors manually can be time-consuming, especially when many packages are available.

The goal of this project is to make the comparison easier by turning a traveler's preferences into a ranked list of relevant packages.

The problem is interesting because a useful recommendation does not have to mean simply showing the cheapest package. Different travelers value different things. One person may prioritize a lower price, while another may care more about being close to the Haram or having a particular airline.

## Data and AI techniques

The system would use structured package information such as:

* package price
* trip duration
* Makkah and Madinah hotel distance
* airline
* room type
* baggage allowance
* other package features that can be represented numerically

For a first prototype, each package can be represented as a feature vector. A traveler's preferences can be converted into another vector, and a similarity or distance measure can be used to compare them.

A simple approach is a weighted nearest-neighbor style method. Each preference is given a weight according to how important it is to the traveler. Packages with smaller weighted distance from the preference vector receive higher rankings.

The weights could be changed by the user. For example, a traveler could give more importance to price and hotel distance and less importance to airline preference.

## How is it used?

A traveler enters preferences such as:

1. approximate budget
2. desired number of days
3. preferred hotel distance
4. preferred airline, if any
5. room type
6. relative importance of each preference

The system compares the request with the available packages and displays the closest matches first. The user can then inspect the package details and make the final decision.

The recommendation should support the traveler rather than automatically make a booking. Package information would need to be checked against the current offer before purchase.

## Challenges

The system would have several limitations:

* Recommendations are only as useful as the package data provided to the system.
* Prices, availability, hotel distances, flights, and other package details can change.
* A numerical similarity score cannot capture every personal preference.
* A recommendation system should not hide important package conditions just because they reduce the similarity score.
* Personal data should be minimized and protected.
* The system should clearly distinguish recommendations from confirmed availability or booking information.

There is also a risk of overfitting the weights to a small group of users. The model should be evaluated on different types of traveler preferences rather than only on the examples used during development.

## What next?

A future version could learn preference weights from anonymous feedback, such as which packages users inspect or select. It could also include a larger and continuously updated package database, explain why each package was recommended, and compare several packages side by side.

A later version could use machine learning to learn from historical choices, while still showing the user which features influenced the recommendation.

## Acknowledgments

* This project was created as a final project idea for the Building AI course by Reaktor Innovations and the University of Helsinki.
* The initial project concept, structure, and prototype are original work for this submission.
* Any future external datasets, images, code, or other materials should only be used with appropriate permission or an applicable open-source or Creative Commons license.
