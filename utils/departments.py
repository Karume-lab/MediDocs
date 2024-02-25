CARDIOLOGIST = "CL"
DERMATOLOGIST = "DL"
EMERGENCY_MEDICINE_SPECIALIST = "EMC"
IMMUNOLOGIST = "IL"
ANESTHESIOLOGISTS = "AL"
COLON_AND_RECTAL_SURGEON = "CRS"
UNSPECIALIZED = "UN"

department_choices = [
    (CARDIOLOGIST, "Cardiologist"),
    (DERMATOLOGIST, "Dermatologists"),
    (EMERGENCY_MEDICINE_SPECIALIST, "Emergency Medicine Specialists"),
    (IMMUNOLOGIST, "Immunologists"),
    (ANESTHESIOLOGISTS, "Anesthesiologists"),
    (COLON_AND_RECTAL_SURGEON, "Colon and Rectal Surgeons"),
    (UNSPECIALIZED, "Unspecialized"),
]

def get_departments():
    return department_choices
