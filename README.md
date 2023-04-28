## Calories-burnt-Prediction

- Built a interesting machine learning system that can predict the amount of calories burned during exercise 
We face this in our day-to-day life regularly a lot of people are very interested in the exercise that they do and the diet that they take 
and what is the amount of calories associated with them say for example how much calories they intake when they eat and how much
calories do they burn when they do exercises and things like that
here we will be using machine learning to solve this problem okay so first of all let's try to understand
 
the metabolic activities that are taking place when we do exercise so it helps us to understand

when we exercise okay so let's consider that a person is exercising so he can be doing a heavy lifting like bench press
1:13
or he can be just running in a treadmill and let's say that before four or five hours of his workout uh he has taken
1:19
some good meal okay and the energy in this food will be used by that person so the body of that person to do that
1:25
exercise right so what happens is so let's say that the person ate something that is you know
1:31
more of carbohydrates so this carbohydrates would be broken into more simpler forms like glucose and when the person do some exercises
1:39
this glucose will be broke down and it will be converted into energy using oxygen so the muscles that are you
1:46
know doing exercise need more oxygen and this oxygen is supplied by blood right and what happens is as the body requires
1:53
more oxygen now the art the heartbeat will increase a lot okay so increased arc beat means increased
2:00
blood flow so this increased blood flow will give more oxygen to the muscle which oxygen you know this oxygen is
2:07
used to break those glucose molecules okay so this is what happens so the main thing that we can you know
2:13
infer from here is when we do exercise the normal heartbeat will be more so you know normally in in normal
2:19
conditions the average art bit will be around 75 beats per minute but when we are doing exercise the orbit
2:25
can be you know more than 100 beats per minute so this is one of the important inference
2:30
and when this energy is used to do exercise only a part of this energy is
2:35
used the remaining part is converted into heat okay so the body temperature will
2:41
increase when we do exercise and as a result of which in order to reduce this temperature
2:46
our body will release sweat so this is the reason that we get sweat when we do exercise okay so to cool down this body
2:52
temperature so these are some important parameters which we need so what we will be doing is we will be taking the parameters such as
2:59
the duration for which the person is doing exercise and what is this average uh beats per
3:04
minute so our bit what is the average art bit of that person during the exercise and what is this body temperature so these parameters
3:11
will be used also the height and weight of the person will be used to predict how much calories the person
3:16
will be burning so this is our problem statement so this is what we are going to do in this particular project okay so i
3:22
hope you have understood what we are going to cover in this video now let's understand what is the workflow we will do for this project
3:28
okay the first step will be to collect the data so this is you know the main thing about machine learning is
3:34
it learns from the data right so we need appropriate data to train our machine learning model
3:39
so that it can find what is the amount of calories that the person is going to burn okay so the first step is getting
3:44
the data so once we have the data we cannot feed it directly to our machine learning algorithm so before feeding
3:50
we need to process the data so this step is called as data preprocessing where we you know we clean the data and do some processing on
3:57
it so this step is called as data pre-processing and after pre-processing we need to do
4:02
some data analysis so this data analysis helps us to understand our data set better so understanding our data set better you
4:08
know helps us to make better influence and better predictions so the third step will be data analysis where
4:14
we will use some visualization techniques where we try to plot the data in some plots and graphs
4:19
so once we analyze the data the next step is to split the data set into training data and test data
4:25
so the reason for this is so we will train our machine learning model with the training data and we will
4:31
evaluate our model so we will test our model with this test data okay so after we
4:37
split the data we need to train our machine learning algorithm so in this case we are going to use ixg boost
4:42
regressor so this is the machine learning model which we will be using in this particular case so we will be training
4:47
our xt boost regressor with the training data so once we train this xg boost regressor we will
4:54
evaluate this model with the help of test data so this is the workflow which we are going to follow here you can see here that we are using
5:00
a regressor model right so because this is an example of a regression problem so there are two types of problems in
5:06
supervised learning so one is classification and the another one is regression classification is all about classifying
5:12
let's say that we can take a project like diabetes prediction where we will try to predict whether a person has diabetes or not so
5:19
it is just a yes or no question right so those kind of problems are called as classification problem
5:24
and regression problem is something in which we you know try to find some particular value particular number so in this case we are
5:31
you know trying to find the calories burnt right so the amount of calories is nothing but a particular value or particular number
5:37
so this is an example of a regression problem so in case of diabetes we are just predicting yes or no so those kinds
5:43
of problems are called as classification problem so as this is a regression problem we are going to use
5:48
xg boost regressor okay so there are also other regression algorithms and the regression models so in this case let's
5:54
use xd boost regressor so with that being said let's get started with the coding part
