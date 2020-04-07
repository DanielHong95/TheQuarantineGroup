import pandas as pd
import csv
import json

us_confirmed = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv"
us_deaths = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv"
global_cases = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
global_deaths = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
global_recovered = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"

us_confirmed_df = pd.read_csv(us_confirmed)
us_deaths_df = pd.read_csv(us_deaths)
global_cases_df = pd.read_csv(global_cases)
global_deaths_df = pd.read_csv(global_deaths)
global_recovered_df = pd.read_csv(global_recovered)


def get_state_info():
    states_data = pd.DataFrame(
        us_deaths_df[
            ["UID", "iso2", "Admin2", "Province_State", "Population", "Lat", "Long_"]
        ]
    ).rename(columns={"iso2": "Country_Abbrv", "Admin2": "County", "Long_": "Long"})
    state_info = states_data.to_dict(orient="records")
    return state_info


def get_us_covid_info():
    us_cases_clean = pd.melt(
        us_confirmed_df.drop(
            columns=[
                "iso2",
                "iso3",
                "code3",
                "FIPS",
                "Admin2",
                "Province_State",
                "Country_Region",
                "Lat",
                "Long_",
                "Combined_Key",
            ]
        ),
        id_vars="UID",
        var_name="Date",
    ).rename(columns={"value": "Confirmed_Cases"})

    us_deaths_clean = pd.melt(
        us_deaths_df.drop(
            columns=[
                "iso2",
                "iso3",
                "code3",
                "FIPS",
                "Admin2",
                "Province_State",
                "Country_Region",
                "Lat",
                "Long_",
                "Combined_Key",
                "Population",
            ]
        ),
        id_vars="UID",
        var_name="Date",
    ).rename(columns={"value": "Deaths"})

    us_covid_data = pd.merge(
        us_cases_clean, us_deaths_clean, how="left", on=["UID", "Date"]
    )

    us_covid_info = us_covid_data.to_dict(orient="records")
    return us_covid_info
