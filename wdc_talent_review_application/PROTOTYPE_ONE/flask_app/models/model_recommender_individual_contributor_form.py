from flask_app.config.mysqlconnection import connectToMySQL # Connecting to the DB

from flask_app.models import model_user, model_nominee #importing necessary model files for relationships


DATABASE = "wdc_prototype_one_db"

# Recommender Work contribution form for Individula Contribution
class RecommenderIndividualForm:
    def __init__(self, data):
        self.id = data['id']
        self.recommender_form_id = data['recommender_form_id']
        self.a = data['a']
        self.a = data['b']
        self.a = data['c']
        self.a = data['d']
        self.a = data['f']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']




############################################# CRUD FUNCTIONALITIES #############################################
   ############################## Consistent Naming Convention  #######################
                                    # create, 
                                    # get_all, get_many, get_one, 
                                    # update_one, update_many, 
                                    # delete_one, delete_many


############################################# CREATE / Insert (Returns an int as which is Id) #############################################
# Create Individual Work contribution Form
    @classmethod
    def create_contribution_individual(cls, data):
        # Insert query to save data from form to database
        query = "INSERT INTO individuals_contributors_forms (recommender_form_id, a, b, c, d, f) VALUES %(recommender_form_id)s,%(a)s,%(b)s,%(c)s,%(d)s,%(f)s );,"
        # store the returned info using a Variable
        results = connectToMySQL(DATABASE).query_db(query, data)
        # retuns an id so make sure to use get method to retrieve the actual data for the object / instance
        return results
    
############################################# READ (DATA type Returned is list of dictionaries) #############################################
    #Read All the Individual Questions
    @classmethod
    def get_all_individual_questions(cls):
        # Using Select * query to retrieve all the individula questions
        query = "SELECT * FROM individuals_contributors_forms;"
        # Need to assign the values from the database to a variable
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            # Create an empty list to store the list of objects / instances
            all_individual_questions = []
            # Now append the list of objects/ instances from cls
            # Using for loop to append
            for individual_question in results:
                all_individual_questions.append(cls(individual_question))
            return all_individual_questions # returns a list of objects
        return False