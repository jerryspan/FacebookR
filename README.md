# FacebookR
### Facebook Post Reactions dataset 

---
**Paper: Social Emotion Mining Techniques for Facebook Posts Reaction Prediction** (accepted at ICAART 2018)

This dataset was created for a research project at the Department of Data Science and Knowledge Engineering (Maastricht University). The dataset contains facebook posts, their correlating comments, an emotion lexicon and labled sentences. 

## Usage
### Database 
The database used in this project is **[MongoDB](https://www.mongodb.com/)**. The files in this repository are dumb-files created by MongoDB. So, one can unzip the files, start MongoDB on your machine and use the following command to import the files in your MongoDB:
```bash
mongorestore -d <name_of_the_database> <your_path_to_the_github_files>
```

### Python 3 scripts
We also provide Python 3 scripts that can be used to work with the data. One needs to install [pymongo](https://api.mongodb.com/python/current/) to use these scripts. 

---
#### database_access.py

``DataStorage`` is a base class (abstract class) for accessing/reading/writing to the MongoDB.  

#### mongodb.py
``MongodbStorage`` inherits from ``DataStorage`` and contains the implemented database access (default database name is "research\_project", the user should use ``<name_of_the_database>`` as specified in the import command). There are various methods to read and write information to the database tables. 

####data_types.py
Furthermore, ``Post``, ``Comment`` and ``Emotion`` are three data classes that can hold information of the corresponding database tables. 
