# -*- coding: utf-8 -*-

###########################################
#                libraries                #
###########################################
import json
###########################################

class JsonLoader():
    """Représente le chargement des données d'un fichier JSON.
    Args:
        filename: Nom du fichier JSON a charger.
        settings: dictionnaire contenant les données du fichier JSON.
    """

    def __init__(self, filename:str):
        self._filename = filename
        self._settings:dict = self.load_settings()

    def get_setting(self, obj: str, key: str) -> str or int:
        """Obtenir un paramètre en particulier.
        Args:
            obj: Objet du fichier JSON.
            key: Clé du fichier JSON.
        Returns:
            La valeur contenu à l'endroit indiqué par obj et key.
        """
        try:
            return self._settings[obj][key]
        except FileNotFoundError:
            raise FileNotFoundError(f"Settings file 'settings.json' not found.")
        except json.JSONDecodeError as e:
            raise JSONDecodeError(f"Invalid JSON data in 'settings.json': {e}")

    def load_settings(self) -> dict:
        """Charge le fichier JSON.
        Returns:
            Un dictionnaire contenant les données du fichier JSON.
        """
        with open(self._filename, 'r') as f:
            return json.load(f)

    def save_settings(self) -> None:
        """Sauvegarder de nouvelles données dans le fichier JSON."""
        with open(self._filename, 'w') as f:
            json.dump(self._settings, f, indent=4)

    def modify_settings(self, obj: str, key: str, value: str or int) -> None:
        """Modifier le fichier JSON et l'attribut settings.
        Args:
            obj: Objet du fichier JSON.
            key: Clé du fichier JSON.
            value: La valeur contenu à l'endroit indiqué par obj et key.
        Raises:
            FileNotFoundError: Si le fichier JSON n'a pas été trouvé.
            json.JSONDecodeError: S'il y a eu un problème lors de la lecture/écriture du fichier.
        """
        try:
            self._settings[obj][key] = value
            self.save_settings()
        except FileNotFoundError:
            raise FileNotFoundError(f"Settings file 'settings.json' not found.")
        except json.JSONDecodeError as e:
            raise JSONDecodeError(f"Invalid JSON data in 'settings.json': {e}")