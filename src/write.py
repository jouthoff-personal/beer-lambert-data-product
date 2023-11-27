def write_model_to_json(model):
    model.to_json('calibrated_model.json')


def write_predicted_concentrations_to_json(df):
    df.to_json('predicted_')