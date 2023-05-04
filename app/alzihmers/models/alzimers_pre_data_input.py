from pydantic import BaseModel

# we must pay attention to the models that must be scaled
# before being sended (depending on the trained on data )
class DataInput(BaseModel):
    M_F: int
    Age: int
    EDUC: int
    SES: float
    MMSE: float
    eTIV: int
    nWBV: float
    ASF: float

    # M_F: This represents the gender of the individual, where 0 typically denotes male and 1 denotes female.
    # Age: This represents the age of the individual in years.
    # EDUC: This represents the educational level of the individual, typically measured in years of education completed.
    # SES: This represents the socioeconomic status of the individual, which is often measured using a numerical scale or index.
    # MMSE: This represents the Mini-Mental State Examination score, which is a cognitive assessment tool used to evaluate cognitive function and screen for dementia.
    # eTIV: This represents the estimated total intracranial volume, which is a measure of the total volume inside the skull.
    # nWBV: This represents the normalized whole brain volume, which is a measure of the brain volume normalized by the intracranial volume.
    # ASF: This represents the atlas scaling factor, which is a measure used to scale the MRI images to a common template or atlas.

# an instance or dictionary of key value pair to test
data = {
    "M_F": 0,
    "Age": 73,
    "EDUC": 8,
    "SES": 5.0,
    "MMSE": 25.0,
    "eTIV": 1151,
    "nWBV": 0.743,
    "ASF": 1.525
}

input_data = DataInput(**data)

# Pass the input_data to your models for prediction
