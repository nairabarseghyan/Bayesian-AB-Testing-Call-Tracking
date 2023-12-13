# Bayesian-AB-Testing-Call-Tracking
Bayesian A/B testing for Call Tracking applications. Project for the class DS223 Marketing Analytics, American University of Armenia  
[https://pypi.org/project/bayesian-ab-testing/](https://pypi.org/project/bayesian-ab-testing/)

[Official documentation](https://mkdocs.bayesian.movsisyan.info)

### Project Proposal 

Bayesian AB testing is widely used for analyzing business performances in various aspects. One of the fields that Bayesian AB testing is useful, is analyzing performance of advertisements. Online businesses analyze advertisements and make better decisions, which helps them to minimize budget spending on advertisements that do not work. However, the majority of businesses are operating offline, and promoting their products and services with offline advertising. We wanted to investigate how offline businesses can use this Bayesian AB testing to make better decisions concerning their advertisement types and advertisement budget. 

Solution found to the above problem is a technology called call-tracking. Call tracking assigns a phone number for each offline marketing method that businesses use to track. Examples are flyers, billboards, tv advertisements etc. For each call made through this tracking numbers calls are forwarded to the destination phone number - main phone number of the business. Call tracking system records the source of the call and returns the collected data to the business. In this way businesses get information about where the customer saw the advertisement , after which they made a call. 

The aim of this project is to analyze call-tracking data of the businesses using bayesian AB testing method. This will help businesses track the advertisement sources that bring the most results and invest in best performing advertisements. We plan on experimenting with various bayesian AB testing methods covered during our class and finding the best one for the specific needs of this project. 


### How to install

```
pip install bayesian_ab_testing
```

### How to run

```
python run.py
```

Prioritized functionality
➢	Must Have
Implemented bayesian AB testing algorithm (yet to be chosen from epsilon greedy and Optimistic Initial Values)
User Friendly API
 
➢	Could Have 
Connection with already existing and operating call tracking system (for example google ads call tracking https://support.google.com/google-ads/answer/6095882?hl=en)



Roles:

Project/Product Manager: Anush Aghinyan
Database Developer: Anahit Navoyan
Data scientists: Yeva Avetisyan, Naira Maria Barseghyan
API Developer: Mher Movsisyan



