# Environnements_de_Tests

## Documenation
- `test_osdetectory.py`
	- 'mocker' est une "fixure" fournie par `pytest-mock`, qui va nous permettre de créer des "mocks" (des objets simulés) pour remplacer des parties du code réel pendant les tests.
		- `def test_obtenir_sys_info(mocker):`
			- Ici, on utilise `mocker.path` pour remplacer temporairement la fonction `platform.uname` par une version "mockée" (simulée) de cette fonction.
			-  On crée un object "mock" (simulé) qui va renvoyer des valeurs spécifiques quand on appelle les différents attributs comme 'system', 'node', etc.
			- Ces valeurs simulent ce qu'on obtiendrait d'un vrai appel à `platform.uname`.
			- On définit ici ce à quoi on s'attend : un dictionnaire avec toutes les informations système simulées (celles qu'on a définies juste au-dessus).
			- On appelle la vrai fonction `obtenir_sys_info` du module `os_detector`.
			- Grâce à `mocker.patch`, à chaque fois que cette fonction appellera `platform_uname`, elle utilisera notre version mockée avec les valeur simulées.
			- On vérifie ensuite que le résultat de la fonction est bien égal à ce à quoi on s'attend (c'est-à-dire le dictionnaire `exprected_result`).