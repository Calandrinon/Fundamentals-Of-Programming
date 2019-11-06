from ui import UI
from service import Service
from repository import Repository
from validation import Validator

def main():
    validator_instance = Validator()
    repository_instance = Repository()
    service_instance = Service(repository_instance, validator_instance)
    ui_instance = UI(service_instance)

main()
