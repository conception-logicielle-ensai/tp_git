from typing import List
from models.contact import Contact
from services.contact_service import ContactService


class ContactView:
    def __init__(self, service: ContactService) -> None:
        self.service = service

    def display_contacts(self, contacts: List[Contact]) -> None:
        if not contacts:
            print("Aucun contact à afficher.")
            return
        print("Liste des contacts :")
        for contact in contacts:
            print(contact)

    def display_message(self, message: str) -> None:
        print(message)

    def show_menu(self) -> None:
        print("\n1. Ajouter un contact")
        print("2. Afficher les contacts")
        print("3. Supprimer un contact")
        print("4. Quitter")

    def run(self) -> None:
        while True:
            self.show_menu()
            choice = input("Choisissez une option (1-4) : ")

            if choice == '1':
                name = input("Entrez le nom : ")
                phone = input("Entrez le numéro de téléphone : ")
                email = input("Entrez l'email : ")
                message = self.service.add_contact(name, phone, email)
                self.display_message(message)
            elif choice == '2':
                contacts = self.service.get_contacts()
                self.display_contacts(contacts)
            elif choice == '3':
                pass
            elif choice == '4':
                self.display_message("Au revoir !")
                break
            else:
                self.display_message("Option invalide. Veuillez réessayer.")
