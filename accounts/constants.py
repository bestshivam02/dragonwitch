from django.core.validators import RegexValidator
# alphanumeric = RegexValidator(r'^[a-zA-Z ]*$', 'Only alpha characters are allowed.')
number = RegexValidator(r'^^(\+\d{1,3})?,?\s?\d{8,13}', 'Only numbers are allowed.')

DEVICE_TYPE = [
    (1,'Android'),
    (2,'ios'),
        ]

USER_ROLE = ((1, "SuperAdmin"),(3,"User"))

SIZE = (
    (1, "SMALL"),
    (2,"MEDIUM"),
    (3,"LARGE"),
    (4,"XLARGE"),
    (5,"XXLARGE")
    )