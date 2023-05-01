    # age: Measurement is in years.
    # blood_pressure: Measurement is in mmHg (millimeters of mercury).
    # specific_gravity: Measurement is unitless.
    # albumin: Measurement is in g/dL (grams per deciliter).
    # sugar: Measurement is in mg/dL (milligrams per deciliter).
    # red_blood_cells: Measurement is in cells/μL (cells per microliter).
    # pus_cell: Measurement is binary (0 or 1) indicating the presence or absence of pus cells.
    # pus_cell_clumps: Measurement is binary (0 or 1) indicating the presence or absence of pus cell clumps.
    # bacteria: Measurement is binary (0 or 1) indicating the presence or absence of bacteria.
    # blood_glucose_random: Measurement is in mg/dL (milligrams per deciliter).
    # blood_urea: Measurement is in mg/dL (milligrams per deciliter).
    # serum_creatinine: Measurement is in mg/dL (milligrams per deciliter).
    # sodium: Measurement is in mEq/L (milliequivalents per liter).
    # potassium: Measurement is in mEq/L (milliequivalents per liter).
    # haemoglobin: Measurement is in g/dL (grams per deciliter).
    # packed_cell_volume: Measurement is in percentage (%).
    # white_blood_cell_count: Measurement is in cells/μL (cells per microliter).
    # red_blood_cell_count: Measurement is in millions of cells/μL (millions of cells per microliter).
    # hypertension: Measurement is binary (0 or 1) indicating the presence or absence of hypertension.
    # diabetes_mellitus: Measurement is binary (0 or 1) indicating the presence or absence of diabetes mellitus.
    # coronary_artery_disease: Measurement is binary (0 or 1) indicating the presence or absence of coronary artery disease.
    # appetite: Measurement is binary (0 or 1) indicating the presence or absence of appetite.
    # peda_edema: Measurement is binary (0 or 1) indicating the presence or absence of pedal edema.
    # aanemia: Measurement is binary (0 or 1) indicating the presence or absence of anemia.

from pydantic import BaseModel


class kidney_dis_pre_input(BaseModel):
    age: float
    blood_pressure: float
    specific_gravity: float
    albumin: float
    sugar: float
    red_blood_cells: int
    pus_cell: int
    pus_cell_clumps: int
    bacteria: int
    blood_glucose_random: float
    blood_urea: float
    serum_creatinine: float
    sodium: float
    potassium: float
    haemoglobin: float
    packed_cell_volume: float
    white_blood_cell_count: float
    red_blood_cell_count: float
    hypertension: int
    diabetes_mellitus: int
    coronary_artery_disease: int
    appetite: int
    peda_edema: int