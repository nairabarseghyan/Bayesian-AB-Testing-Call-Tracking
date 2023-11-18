# Bayesian-AB-Testing-Call-Tracking
Bayesian A/B testing for Call Tracking applications. Project for the class DS223 Marketing Analytics, American University of Armenia


### Project Proposal 

Bayesian AB testing is widely used for analyzing business performances in various aspects. One of the fields that Bayesian AB testing is useful, is analyzing performance of advertisements. Online businesses analyze advertisements and make better decisions, which helps them to minimize budget spending on advertisements that do not work. However, the majority of businesses are operating offline, and promoting their products and services with offline advertising. We wanted to investigate how offline businesses can use this Bayesian AB testing to make better decisions concerning their advertisement types and advertisement budget. 

Solution found to the above problem is a technology called call-tracking. Call tracking assigns a phone number for each offline marketing method that businesses use to track. Examples are flyers, billboards, tv advertisements etc. For each call made through this tracking numbers calls are forwarded to the destination phone number - main phone number of the business. Call tracking system records the source of the call and returns the collected data to the business. In this way businesses get information about where the customer saw the advertisement , after which they made a call. 

The aim of this project is to analyze call-tracking data of the businesses using bayesian AB testing method. This will help businesses track the advertisement sources that bring the most results and invest in best performing advertisements. We plan on experimenting with various bayesian AB testing methods covered during our class and finding the best one for the specific needs of this project. 


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

Case scenarios 

Case example 1 

Background: Our customer is a marketing manager for a local restaurant. The restaurant has been in business for several years.
They are exploring new ways to increase customer engagement and foot traffic. 
Traditional marketing methods like distributing fliers and investing in billboard advertisements have been successful in the past, 
but they want to determine which channel is more effective in driving customer calls and reservations.

Objective: The goal is to optimize the marketing budget and focus on the channel that generates more calls, ultimately leading to increased reservations and revenue. 

Implementation: 

Step 1: A/B Testing Setup

Fliers Marketing (Group A):
Design and distribute fliers in the local community.
Include a unique phone number (A) on the fliers that will be used exclusively for tracking calls generated from this marketing channel.

Billboards Marketing (Group B):
Invest in a strategically placed billboards across key locations in the city.
Display a different unique phone number (B) on the billboards for call tracking purposes.

Step 2: Call Tracking and Analysis

Call Tracking System: 
Implement a call tracking system that records the number of calls received on both unique phone numbers (A andB). 
Collect additional data such as call duration, time of day, and customer inquiries.

Analysis Period:
Run the A/B test for a specific period, for example, four weeks. 
That we can ensure a sufficient sample size. 

Step 3: Evaluation and Decision Making

Metrics to Analyze:
Compare the total number of calls recieved from the fliers (Group A) and billboards (Group B).
Analyze call duration and the quality of leads generated from each channel.

Step 4: Decision and Future Strategy

Identify the Winning Channel: 
Determine which marketing channel (fliers or billboards) generated more calls and better quality leads. 

Budget Allocation:
Based on the results, allocate a higher percentage of the marketing budget to the more effective channel.


Case example 2

Background: Our customer is a marketing director for an upscale spa and wellness center. 
The spa has a loyal customer base, and they want to introduce a set of new premium services to their customers. 
To optimize the marketing strategy, they want to determine the effectiveness of promoting these services through email and direct mail campaigns targeted at existing customers.

Objective: The goal is to identify the most effective communication channel for promoting new services to customers, considering both cost effectiveness and customer engagement.

Implementation: 

Step 1: A/B Testing Setup

Email Campaign (Group A):
Design a visually appealing email campaign showcasing the new premium services.
Include a unique phone number (A) in the email for call tracking purposes.

Direct Mail (Group B):
Create attractive postcards highlighting the new services and mail them to existing customers.
Use a different unique phone number (B) on the postcards for call tracking.

Step 2: Call Tracking and Analysis

Call Tracking System: 

Implement a call tracking system that records the number of calls received on both unique phone numbers (A andB). 
Track additional metrics, such as appointment bookings or service inquiries.

Analysis Period:
Run the A/B test for a specific period, for example, four weeks. 
That we can ensure a sufficient sample size. 

Step 3: Evaluation and Decision Making

Metrics to Analyze:
Compare the total number of calls received from the email campaign (Group A) and direct mail campaign (Group B).
Assess the conversion rates for appointment bookings or service inquiries from each channel.

Step 4: Decision and Future Strategy

Identify the Winning Channel: 
Determine whether the email campaign or the direct mail campaign was more effective in generating calls and customer engagement. 

Cost-Benefit Analysis:
Consider the cost associated with each channel, including email campaign costs and the expenses related to designing, printing, and delivering postcards.

Optimization:
Based on the results, optimize the marketing strategy for promoting new services to existing customers. 
This may involve adjusting the budget allocation or refining the messaging for the chosen channel.  








