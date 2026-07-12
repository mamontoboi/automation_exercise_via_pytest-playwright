from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class User:
    name: str
    email: str
    password: str
    title: Optional[str] = None
    birth_date: Optional[date] = None
    lastname: Optional[str] = None
    company: Optional[str] = None
    address: Optional[str] = None
    zipcode: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    mobile_number: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    date_of_birth: Optional[tuple[str, str, str]] = None
    zip: Optional[str] = None
    mobile: Optional[str] = None

    def to_create_account_payload(self) -> dict:
        birth_date = self.birth_date
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "title": self.title or "",
            "birth_year": birth_date.strftime("%Y") if birth_date else None,
            "birth_month": birth_date.strftime("%m") if birth_date else None,
            "birth_date": birth_date.strftime("%d") if birth_date else None,
            "firstname": self.name,
            "lastname": self.lastname or "",
            "company": self.company or "",
            "address1": self.address or "",
            "address2": self.address or "",
            "country": self.country or "",
            "zipcode": self.zipcode or "",
            "state": self.state or "",
            "city": self.city or "",
            "mobile_number": self.mobile_number or "",
        }