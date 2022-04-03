USING PYTHON(3.9) and FLASK FRAMEWORK
1. CREATE A VIRTUAL ENV (python3 -m venv env) and ACTIVATE ENV (./env/Script/activate)
2. INSTALL ALL MODULES (pip install -r requirements.txt)
3. UPDATED CONNECTION SETTINGS in app.py (db_name,user_name,password,host)
4. LOOK OUT URLS
5. http://127.0.0.1:5000/ (GET ALL WORDS) using get method
6. http://127.0.0.1:5000/add (ADD ONE WORD) using post method and json parameter eg: {
    "word" : "newton"
}
7. http://127.0.0.1:5000/update (EDIT ONE WORD) using post method and json parameter eg: {
    "old_word" : "Araon1",
    "new_word" : "Newton"
}
8. http://127.0.0.1:5000/delete (DELETE ONE WORD)using post method and json parameter eg: {
    "delete_word" : "Aaron2"
}
9. PLEASE ADD incubyte.postman_collection.json file in postman and get more information.