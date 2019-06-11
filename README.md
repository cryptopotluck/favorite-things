###Favorites Software Engineer Hiring Test

This is a Django small project I undertook for a coding interview. The requirements for this project are listed in the about page of the live project.

When starting this project I broke down the development processes into different sections and progressed in this order:
1. Templates 
    1. Build apps & urls
    2. Import a Template
    3. Break template into partials
    4. collectstatic & refactor
    5. Connect Datatables
    6. Connect MESSAGE_TAGS
    7. Connect Javascript Pluggins
    8. connect JQuery
2. Postgres Setup
3. User Model
    1. Create Account Model
    2. Add login, logout & register
    3. Create Signals
    4. Develop out Admin portal for Users
4. Favorite Model
    1. Integrate Rich Text (tinymce)
    2. Create Model
    3. Create Views
    4. Created Forms
    5. Developed Create, Detail, edit & Delete pages.
5. Built about page
6. Built Graphing page
    1. Added Dash & Plotly for graphing functionality
    2. Added the ability to fetch total posts created and display it via the graph.
7. GraphQl Support
    1. Imported & Connected API Functionality
    2. Created a root schema
        1. Mutations
        2. Query
    3. Created a Fav schema
        1. CreateType
        2. Query
        3. CreateFavorite
        4. UpdateFavorite
        5. DeleteFavorite
        6. Mutation
    4. Created a User schema
        1. UserType
        2. Query
        3. CreateUser
        4. Mutation
        
In total this project took a day to complete & half a day to launch onto the cloud for hosting. 

####Things I Learned:
Learned how to speed up my development time with this project & added a few new libraries into the project like tinymce.

####How to Install:
Installation of the project is relatively simple, I've included a requirements file & .gitignore so install the pip install requirements.txt. Setup a fresh database and connect it into the project, run migrations, collectstatic and you'll be running.

