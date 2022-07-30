from cgitb import small
from flask import Flask, request
from flask import send_file, abort, render_template
import json
from insurance.config.configuration import Configuration
from insurance.logger import logging, get_log_dataframe
from insurance.exception import InsuranceException
from insurance.entity.insurance_predictor import InsuranceData, InsurancePredictor
import sys
from insurance.constant import *
from insurance.util.util import *
from insurance.constant import *
from insurance.pipeline.pipeline import Pipeline



ROOT_DIR
SAVED_MODELS_DIR_NAME = "saved_models"
MODEL_CONFIG_FILE_PATH = os.path.join(ROOT_DIR, config_path, "model.yaml")
INSURANCE_DATA_KEY = "insurance_data"
LOG_FOLDER_NAME = "insurance_logs"
INSURANCE_PREMIUM_KEY = "insurance_premium"
MODEL_DIR = os.path.join(ROOT_DIR, SAVED_MODELS_DIR_NAME)



app =Flask(__name__)


@app.route("/", methods = ['GET', 'POST'])
def index():

    try:
        return render_template('index.html')
    except Exception as e:
        raise InsuranceException(e, sys) from e


@app.route("/train", methods=['GET','POST'])
def train():

    try:
        message = ""
        pipeline = Pipeline(config=Configuration(current_time_stamp=get_current_time_stamp()))
        if not Pipeline.experiment.running_status:
            message = "Training Started ..."
            pipeline.start()

        else:
            message = "Training is already in progress."

        context = {
            "experiment": pipeline.get_experiments_status().to_html(classes='table table-striped col-12'),
            "message":message
        }

        return render_template('train.html', context=context)

    except Exception as e:
        raise InsuranceException(e, sys) from e


@app.route("/predict", methods = ['GET', 'POST'])
def predict():
    try:
        context = {
        INSURANCE_DATA_KEY: None,
        INSURANCE_PREMIUM_KEY: None
        }

        if request.method == "POST":
            age = int(request.form['age'])
            sex = str(request.form['sex'])
            bmi = int(request.form['bmi'])
            children = int(request.form['children'])
            smoker = str(request.form['smoker'])
            region = str(request.form['region'])
            

            insurance_data = InsuranceData(age=age,
                                            sex=sex,
                                            bmi=bmi,
                                            children=children,
                                            smoker=smoker,
                                            region=region)
            insurance_df = insurance_data.get_insurance_input_data_frame()
            insurance_predictor = InsurancePredictor(model_dir=MODEL_DIR)
            insurance_premium = insurance_predictor.predict(insurance_df)
            context = {
                INSURANCE_DATA_KEY:insurance_data.get_insurance_data_as_dict(),
                INSURANCE_PREMIUM_KEY: insurance_premium
            }
            return render_template('predict.html', context=context)
        return render_template('predict.html', context=context)

    except Exception as e:
        raise InsuranceException(e, sys) from e

    
@app.route('/view_experiment_hist', methods=['GET', 'POST'])
def view_experiment_history():
    experiment_df = Pipeline.get_experiments_status()
    context = {
        "experiment": experiment_df.to_html(classes='table table-striped col-12')
    }
    return render_template('experiment_history.html', context=context)


@app.route('/saved_models', defaults={'req_path': 'saved_models'})
@app.route('/saved_models/<path:req_path>')
def saved_models_dir(req_path):
    try:
        os.makedirs("saved_models", exist_ok=True)
        # Joining the base and the requested path
        print(f"req_path: {req_path}")
        abs_path = os.path.join(req_path)
        print(abs_path)
        # Return 404 if path doesn't exist
        if not os.path.exists(abs_path):
            return abort(404)

        # Check if path is a file and serve
        if os.path.isfile(abs_path):
            return send_file(abs_path)
        
        # Show directory contents
        files = {os.path.join(abs_path, file): file for file in os.listdir(abs_path)}

        result = {
        "files": files,
        "parent_folder": os.path.dirname(abs_path),
        "parent_label": abs_path
        }
        
        return render_template('saved_models_files.html', result=result)

    except Exception as e:
        raise InsuranceException(e, sys) from e


@app.route("/update_model_config", methods=['GET', 'POST'])
def update_model_config():
    try:
        if request.method == 'POST':
            model_config = request.form['new_model_config']
            model_config = model_config.replace("'", '"')
            print(model_config)
            model_config = json.loads(model_config)

            write_yaml_file(file_path=MODEL_CONFIG_FILE_PATH, data=model_config)

        model_config = read_yaml_file(file_path=MODEL_CONFIG_FILE_PATH)
        return render_template('update_model.html', result={"model_config": model_config})

    except  Exception as e:
        logging.exception(e)
        return str(e)


@app.route('/artifact', defaults={'req_path': 'insurance'})
@app.route('/artifact/<path:req_path>')
def render_artifact_dir(req_path):
    os.makedirs("insurance", exist_ok=True)
    # Joining the base and the requested path
    print(f"req_path: {req_path}")
    abs_path = os.path.join(req_path)
    print(abs_path)
    # Return 404 if path doesn't exist
    if not os.path.exists(abs_path):
        return abort(404)

    # Check if path is a file and serve
    if os.path.isfile(abs_path):
        if ".html" in abs_path:
            with open(abs_path, "r", encoding="utf-8") as file:
                content = ''
                for line in file.readlines():
                    content = f"{content}{line}"
                return content
        return send_file(abs_path)

    # Show directory contents
    files = {os.path.join(abs_path, file_name): file_name for file_name in os.listdir(abs_path) if
             "artifact" in os.path.join(abs_path, file_name)}

    result = {
        "files": files,
        "parent_folder": os.path.dirname(abs_path),
        "parent_label": abs_path
    }

    return render_template('files.html', result=result)
    


if __name__ == "__main__":
    app.run(debug=True)