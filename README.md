# movie-recommendation-system
A Web Base user-item Movie Recommendation Engine using Collaborative Filtering By scikit-surprise and
The recommendation based on the underlying idea that is if two persons both liked certian common movies,then the movies that one person has liked that the other person has not yet watched can be recommended to him.   
### Screenshot

###### Home page
![home]()

###### Recommendation page
![recom]()

###### Rating page
![rate]()

### Technologies Used

#### Web Technologies
Html , Css , JavaScript , Bootstrap , Django

#### Machine Learning Library In Python3
Numpy , Pandas , scikit-surprise

#### Database
SQLite

##### Requirements
```
python 3.6

pip3

virtualenv
```
##### Setup to run

Extract zip file in your computer

Open terminal/cmd promt

Goto that Path

Example

```
cd ~/movie-recommendation-system
```
Create a new virtual environment on that directory

```
virtualenv .
```

Activate Your Virtual Environment

for Linux
```
source bin/activate
```
for Windows
```
cd Scripts
then
activate
```
To install Dependencies

```
pip install -r requirements.txt
```

### Creating Local Server

Goto src directory, example

```
cd ../movie-recommendation-system/src
```
To run
```
python manage.py runserver
```
Now open your browser and go to this address
```
http://127.0.0.1:8000
```

