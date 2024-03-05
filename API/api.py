import pandas as pd
from sodapy import Socrata
from math import ceil

soil_variables = ['ph_agua_suelo_2_5_1_0', 'potasio_k_intercambiable_cmol_kg', 'f_sforo_p_bray_ii_mg_kg']


def create_client():
    client = Socrata("www.datos.gov.co", None)
    return client


def get_data(dataset_identifier, **kwargs):
    client = create_client()
    result = client.get(dataset_identifier, **kwargs)
    return result


def convert_dataset_to_df(data):
    result_df = pd.DataFrame.from_records(data)
    if result_df.shape[1] == 0:
        raise ValueError(
            "No se encontraron valores con estos parametros, verifique que haya escrito todo de manera correcta")
    return result_df


def data_normalize(dataset_values):
    to_float = lambda x: float(x)

    for iterable in range(len(dataset_values)):
        try:
            dataset_values[iterable] = to_float(dataset_values[iterable])
        except ValueError:
            dataset_values.pop(iterable)


def calculate_median(data):
    medians = {}
    for soil_variable in soil_variables:
        values = data[soil_variable]
        data_normalize(values)
        length = len(values)

        if length % 2 == 0:
            poss_median1 = ceil(length / 2)
            poss_median2 = poss_median1 - 1
            median = (values[poss_median1] + values[poss_median2]) / 2
            medians[soil_variable] = median

        else:
            poss_median = ceil(length / 2)
            medians[soil_variable] = values[poss_median]

    return medians


def get_relevant_info(data):
    columns_dataframe = ["departamento", "municipio", "cultivo", "topografia"] + soil_variables
    new_df = pd.DataFrame()

    for column_name in columns_dataframe:
        new_df[column_name] = data[column_name]
    return new_df


def normalize_params(params):
    params["departamento"] = params["departamento"].upper()
    params["municipio"] = params["municipio"].upper()
    params["cultivo"] = params["cultivo"].title()