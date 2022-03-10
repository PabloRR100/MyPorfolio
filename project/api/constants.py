from api.types import ExpandedEnum


class CompanyName(ExpandedEnum):
    ADIDAS = "Adidas"
    ALIBABA = "Alibaba"
    ALIBABA_EURO = "Alibaba (€)"
    ALPHABET = "Alphabet"
    APPLE = "Apple"
    BMW = "BMW"
    DISNEY = "Disney"
    FERRARI = "Ferrari"
    MICROSFOT = "Microsoft"
    NETFLIX = "Netflix"
    NVIDIA = "NVIDIA"
    VISA = "Visa"


Tickers = {
    CompanyName.ADIDAS: "ADS",
    CompanyName.ALIBABA: "BABA",
    CompanyName.ALIBABA_EURO: "AHLA",
    CompanyName.ALPHABET: "ABEA",
    CompanyName.APPLE: "APPL",
    CompanyName.BMW: "BMW",
    CompanyName.DISNEY: "DIS",
    CompanyName.FERRARI: "RACE",
    CompanyName.MICROSFOT: "MSFT",
    CompanyName.NETFLIX: "NFLX",
    CompanyName.NVIDIA: "NVDA",
    CompanyName.VISA: "V",
}


class Exchange(ExpandedEnum):
    NSY = "NSY"
    NDQ = "NDQ"
    XET = "XET"
    MIL = "MIL"