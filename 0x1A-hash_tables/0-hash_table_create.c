#include "hash_tables.h"

/**
 * hash_table_create - func that creates a hash table
 * @size: size of the array
 * Return: Returns a pointer to the newly created hash table,
 * if it fails returns NULL
 */

hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t *hashNode = NULL;
	unsigned long int i;

	hashNode = malloc(sizeof(hash_table_t));

	if (!hashNode)
		return (NULL);

	hashNode->size = size;
	hashNode->array = malloc(sizeof(hash_node_t *) * size);
	if (!hashNode->array)
	{
		free(hashNode);
		return (NULL);
	}

	for (i = 0; i < size; i++)
		hashNode->array[i] = NULL;

	return (hashNode);
}
