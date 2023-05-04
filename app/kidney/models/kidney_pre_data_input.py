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


    #     age: Age of the patient (float) - Range: Varies depending on the dataset, typically a positive value.

    # blood_pressure: Blood pressure of the patient (float) - Range: Varies depending on the dataset, typically measured in mmHg (millimeters of mercury).

    # specific_gravity: Specific gravity of urine (float) - Range: Varies depending on the dataset, typically measured between 1.005 and 1.025.

    # albumin: Presence of albumin in urine (float) - Range: Varies depending on the dataset, typically measured in g/dL (grams per deciliter).

    # sugar: Presence of sugar in urine (float) - Range: Varies depending on the dataset, typically measured in mg/dL (milligrams per deciliter).

    # red_blood_cells: Presence of red blood cells in urine (int) - Range: Usually represented as binary values (0 or 1) indicating the absence or presence of red blood cells.

    # pus_cell: Presence of pus cells in urine (int) - Range: Usually represented as binary values (0 or 1) indicating the absence or presence of pus cells.

    # pus_cell_clumps: Presence of clumps of pus cells in urine (int) - Range: Usually represented as binary values (0 or 1) indicating the absence or presence of pus cell clumps.

    # bacteria: Presence of bacteria in urine (int) - Range: Usually represented as binary values (0 or 1) indicating the absence or presence of bacteria.

    # blood_glucose_random: Random blood glucose level (float) - Range: Varies depending on the dataset, typically measured in mg/dL (milligrams per deciliter).

    # blood_urea: Blood urea level (float) - Range: Varies depending on the dataset, typically measured in mg/dL (milligrams per deciliter).

    # serum_creatinine: Serum creatinine level (float) - Range: Varies depending on the dataset, typically measured in mg/dL (milligrams per deciliter).

    # sodium: Sodium level in blood (float) - Range: Varies depending on the dataset, typically measured in mmol/L (millimoles per liter).

    # potassium: Potassium level in blood (float) - Range: Varies depending on the dataset, typically measured in mmol/L (millimoles per liter).

    # haemoglobin: Hemoglobin level in blood (float) - Range: Varies depending on the dataset, typically measured in g/dL (grams per deciliter).

    # packed_cell_volume: Packed cell volume in blood (float) - Range: Varies depending on the dataset, typically measured as a percentage.

    # white_blood_cell_count: White blood cell count (float) - Range: Varies depending on the dataset, typically measured in cells per microliter (mcL).

    # red_blood_cell_count: Red blood cell count (float) - Range: Varies depending on the dataset, typically measured in millions of cells per microliter (mcL).

    # hypertension: Presence of hypertension (int) - Range: Usually represented as binary values (0 or 1) indicating the absence or presence of hypertension.

    # diabetes_mellitus: Presence of diabetes mellitus (int) - Range: Usually represented as binary values (0 or 1) indicating the absence or presence of diabetes mellitus.

    # coronary_artery_disease: Presence or absence of coronary artery disease in the patient (int) - Represents the presence (1) or absence (0) of coronary artery disease in the patient.

    # appetite: Appetite of the patient (int) - Represents the appetite of the patient. It can have the following values:

    # 0: Poor
    # 1: Good

    # peda_edema: Presence or absence of pedal edema in the patient (int) - Represents the presence (1) or absence (0) of pedal edema in the patient.

    # anemia: Presence or absence of anemia in the patient (int) - Represents the presence (1) or absence (0) of anemia in the patient.