def write_model_to_json(model):
    model.to_json('calibrated_model.json')


def write_predicted_concentrations_to_json(df, run):
    df.to_json('/prediction_files/predicted_' + run['client'] + run['date'])