### Calories-burnt-Prediction

- Built a interesting machine learning system that can predict the amount of calories burned during exercise 
We face this in our day-to-day life regularly a lot of people are very interested in the exercise that they do and the diet that they take 
and what is the amount of calories associated with them say for example how much calories they intake when they eat and how much
calories do they burn when they do exercises and things like that
here we will be using machine learning to solve this problem okay so first of all let's try to understand
 
the metabolic activities that are taking place when we do exercise so it helps us to understand

Consider that a person is exercising so he can be doing a heavy lifting like bench press
or he can be just running in a treadmill or say that before 4-5 hours of his workout he has taken
some good meal okay and the energy in this food will be used by that person so the body of that person to do that
exercise right so what happens is so 


let's say when the person eat something more no of carbohydrates are broken into more simpler forms like glucose and when the person do some exercises
this glucose will be broke down and it will be converted into energy using oxygen so the muscles that are doing exercise needs more oxygen, supplied by blood and  heartbeat will also increase means increased blood flow so this increased blood flow will give more oxygen to the muscle which oxygen this oxygen is
used to break those glucose molecules okay so this is what happens so the main thing that we can you know infer from here is when we do exercise the normal heartbeat will be more so you know normally in in normal conditions the average art bit will be around 75 beats per minute but when we are doing exercise the heartbeat can be you know more than 100 beats per minute so this is one of the important inference
and when this energy is used to do exercise only a part of this energy is
used the remaining part is converted into heat okay so the body temperature will
increase when we do exercise and as a result of which in order to reduce this temperature
our body will release sweat so this is the reason that we get sweat when we do exercise okay so to cool down this body
temperature so these are some important parameters which we need so what we will be doing is we will be taking the parameters such as
the duration for which the person is doing exercise and what is this average uh beats per
minute so our bit what is the average art bit of that person during the exercise and what is this body temperature so these parameters
will be used also the height and weight of the person will be used to predict how much calories the person
will be burning so this is our problem statement so this is what we are going to do in this particular project okay so i
hope you have understood what we are going to cover in this video now 




can find what is the amount of calories that the person is going to burn okay so the first step is getting
the data so once we have the data we cannot feed it directly to our machine learning algorithm so before feeding
we need to process the data so this step is called as data preprocessing where we you know we clean the data and do some processing on
it so this step is called as data pre-processing and after pre-processing we need to do
some data analysis so this data analysis helps us to understand our data set better so understanding our data set better you
know helps us to make better influence and better predictions so the third step will be data analysis where
we will use some visualization techniques where we try to plot the data in some plots and graphs
so once we analyze the data the next step is to split the data set into training data and test data
so the reason for this is so we will train our machine learning model with the training data and we will
evaluate our model so we will test our model with this test data okay so after we
split the data we need to train our machine learning algorithm so in this case we are going to use ixg boost
regressor so this is the machine learning model which we will be using in this particular case so we will be training
our xt boost regressor with the training data so once we train this xg boost regressor we will
evaluate this model with the help of test data so this is the workflow which we are going to follow here you can see here that we are using
a regressor model right so because this is an example of a regression problem so there are two types of problems in
supervised learning so one is classification and the another one is regression classification is all about classifying
let's say that we can take a project like diabetes prediction where we will try to predict whether a person has diabetes or not so
it is just a yes or no question right so those kind of problems are called as classification problem
and regression problem is something in which we you know try to find some particular value particular number so in this case we are
you know trying to find the calories burnt right so the amount of calories is nothing but a particular value or particular number
so this is an example of a regression problem so in case of diabetes we are just predicting yes or no so those kinds
of problems are called as classification problem so as this is a regression problem we are going to use
xg boost regressor okay so there are also other regression algorithms and the regression models so in this case let's
use xd boost regressor so with that being said let's get started with the coding part
