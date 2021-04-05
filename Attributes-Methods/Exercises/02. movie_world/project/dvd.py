class DVD:
    __months = {
        "01": "January", "02": "February", "03": "March",
        "04": "April", "05": "May", "06": "June",
        "07": "July", "08": "August", "09": "September",
        "10": "October", "11": "November", "12": "December"
    }

    def __init__(self, name, id, creation_year, creation_month,  age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} " \
               f"{self.creation_year}) has age restriction {self.age_restriction}. " \
               f"Status: {'rented' if self.is_rented else 'not rented'}"

    @classmethod
    def from_date(cls, id, name, date, age_restriction):
        month, year = date.split(".")[1:]
        month_str = DVD.__months[month]
        return cls(name, id, int(year), month_str, age_restriction)