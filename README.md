# This is an attempt to learn tech tools
lesson 2

## A collaboration between a Washingtonian and a Parisian 

### The goals are to learn:
 * GitHub
 * Python 3
 * C
 * Django
 * SOLID principles
 
 ### The exercice's goals are:
 
  * making a Class who works like a Dict
  
 l. We must be able to create the dictionary in several ways:

		Empty: the constructor is called without passing any parameters
		to it and the created dictionary is empty.

		Copied from a dictionary: we pass as a parameter of the constructor 
		a dictionary that we copy later in our object. One can thus write constructor 
		(dictionary) and the keys and values ​​contained in the dictionary are copied in
		the constructed object.    ## I did'nt made it :/

		Pre-filled thanks to keys and values ​​passed in parameter: like the usual dictionaries,
		one must here have the possibility of pre-filling our object with key-values ​​pairs passed 
		in parameter (constructor (cle1 = value1, cle2 = value2, ...)).

 l. Keys and values ​​must be paired. In other words, if one tries to delete a key, the corresponding
	value must also be deleted. The keys and values ​​are in lists of the same size, it will be enough 
	to take the index in a list to know which object corresponds to it in the other. For example, the 
	index key 0 is coupled with the index value 0.

 l. we must be able to interact with our container object thanks to the square brackets, to recover a
	value (object [cle]), to modify it (object [cle] = value) or to remove it (del object [cle]).

 l. When we try to modify a value, if the key exists we overwrite the old value, if it does not exist
	we add the key-value pair at the end of the dictionary.

 l. We must be able to know thanks to the keyword in if a key is in our dictionary (key in dictionary).

 l. We must be able to request the size of the dictionary with the len function.

 l. We must be able to display our dictionary directly in the interpreter or through the print function.
	The display must be similar to that of the usual dictionaries ({cle1: value1, cle2: value2, ...}).

 l. The object must set the sort methods to sort and reverse to reverse. The sorting of the object must
	be done according to the keys.

 l. The object must be able to be traveled. When one writes for a dictionary, one has to go through the
	list of keys contained in the dictionary. ## I did'nt made it too :/

 l. Like the dictionaries, three methods keys () (returning the list of keys), values ​​() (returning the
	list of values) and items () (returning couples (key, value)) must be implemented. The return type 
	of these methods is left to your initiative: it can be iterators or generators (as long as you can
	browse them).

 l. We must be able to add two ordered dictionaries (dico1 + dico2); the keys and values ​​of the second 
	dictionary are added to the first.