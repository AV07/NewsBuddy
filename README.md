# NewsBuddy

NewsBuddy is a web application that tackles the problem of fake news using a crowdsourcing approach. It empowers the users to debate upon the correctness of news articles and make an informed decision about an online news article's credibility. Users can agree/dispute with specific claims of an article and can submit reviews backed by certain reliable references (top news channels, reputed sources of information). The disputed sections of an article are highlighted and arguments provided by other users for the same are shown. Gamification features like badges encourage user participation and thereby make the system better.

## Folder Structure
```
.
├── README.md
├── annotation
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_alter_annotation_article.py
│   │   └── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── newsbuddy
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── package.json
├── requirements.txt
└── templates
    ├── annotator.annotateitpermissions.min.js
    ├── annotator.auth.min.js
    ├── annotator.document.min.js
    ├── annotator.filter.min.js
    ├── annotator.kitchensink.min.js
    ├── annotator.markdown.min.js
    ├── annotator.min.css
    ├── annotator.min.js
    ├── annotator.permissions.min.js
    ├── annotator.store.min.js
    ├── annotator.tags.min.js
    ├── annotator.unsupported.min.js
    ├── avatar1.png
    ├── homeBackground.svg
    ├── homepage.html
    └── index.html
```

## Build :gear:

#### Setup Virtual environment
```
python3 -m venv venv
```

#### Activate venv
```
source venv/bin/activate
```

#### Install Dependencies
```
pip install -r requirements.txt
```

#### Run Server
```
python3 manage.py runserver
```

## Preview 🎨

<img width="1200" alt="Screenshot 2021-05-16 at 16 58 54" src="https://user-images.githubusercontent.com/42066451/118395448-26dffe80-b668-11eb-96fd-a7f6c209ff1b.png">

## Team :star:
[Anuneet Anand](https://github.com/anuneetanand)            
[Atul Verma]()          
[Dhruv Yadav]()         
[Divyam Gupta](https://github.com/dgupta04)         
[Sanchit Trivedi](https://github.com/Sanchit-Trivedi)       
[Vishwesh Kumar](https://github.com/vishwesh-D-kumar)           
        
