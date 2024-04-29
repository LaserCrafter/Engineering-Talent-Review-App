from flask_app import app
from flask import render_template, redirect, request, session

# import the class files from models folder
from flask_app.models import  model_nominee, model_user,model_recommender_form, model_recommender_individual_contributor_form

############################################# RESTFUL ROUTE ARCHITECTURE #############################################
                                ################# table_name/id(if possible)/action #################
                                            #user/new -> DISPLAY ROUTE - Registration
                                            #user/create -> ACTION ROUTE - Creating a user
                                            #user/<int:id> -> DISPLAY   ROUTE  
                                            #user/<int:id>/edit -> DISPLAY ROUTE  
                                            #user/<int:id>/update -> ACTION ROUTE  
                                            #user/<int:id>/delete -> ACTION ROUTE  



############################################# CREATE | SAVE | INSERT ROUTES #############################################
#Display New Recommendation Form Route
@app.route('/recommend/new')
@model_user.User.restrict_access_based_on_role('Recommender') # Only the Recommender can access this route
def recommend_new():

    # STILL NEED TO CALL VALIDATIONS FROM MODEL #############
    
    # Trying to live display the selected Nominee info
    nominee = model_nominee.Nominee.get_one_nominee({'id': id})

    #Context is a dictionary of data from database  to access / display to html
    context = {
        'all_nominees' : model_nominee.Nominee.get_all_nominees(),  # Display list of nominees to select from 
        'nominee' : nominee,
    }
    return render_template('recommendation_new.html', **context)



#CREATE New Recommendation Action Route
@app.route('/recommend/create', methods=['POST'])
@model_user.User.restrict_access_based_on_role('Recommender') # Only the Recommender can access this route
def recommend_create():
        # STILL NEED TO CALL VALIDATIONS FROM MODEL #############

    # Getting a list of selected options from selected options in form for work_contributions by Recommender 
    work_contributions = request.form.getlist('work_contributions[]')


    # individual_questions = request.form.getlist('individual_question')
    # Getting the nominee_id to pass through the data for required values from Query 
    recommender_form_id = model_recommender_form.RecommenderForm.get_one_recommender({'id': id}) # (Being done through **reques.form)

    #Create the New Recommendation
        #Creating data dictionary to pass user id using session along with request.form
        #this is better than using session through hidden inputs in html to avoid end user to edit the form
    # individual_questions = model_recommender_individual_contributor_form.RecommenderIndividualForm.
    data = {
        **request.form,
        'user_id' : session['uuid'],
        'work_contributions' : work_contributions,
        # 'individual_question' : individual_questions,
        # 'recommender_form_id' : recommender_form_id,
        
    }
    # model_recommender_individual_contributor_form.RecommenderIndividualForm.create_contribution_individual(data)
    print("*********" * 12)
    print(request.form)
    model_recommender_form.RecommenderForm.create_recommendation(data)
    return redirect('/recommender/dashboard')



############################################# READ | SELECT DISPLAY ROUTE #############################################

#Display Recommender Dashboard Route
@app.route('/recommender/dashboard')
# Using Decorator to Call Validation from model_user to check the User Role 
@model_user.User.restrict_access_based_on_role('Recommender') # Only the Recommender can access this route
def recommender_dashboard():
    # # Check to see if User in session( )
    # if 'uuid' not in session:
    #     return redirect('/') # if User not in session then logout

    #Using Context to pass data from model with neccessary queries 
    context = {
        'all_nominees_nominator' : model_nominee.Nominee.get_all_nominees_nominator(), # make sure querry in model class is correct
        'all_nominees' : model_nominee.Nominee.get_all_nominees(),
        'all_users' : model_user.User.get_all(),
    }

    return render_template('recommender_dashboard.html', **context)


