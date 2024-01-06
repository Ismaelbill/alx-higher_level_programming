#include "lists.h"

/**
 * list_len - function that counts the length of a linked list
 * @h: ptr to linked list
 * Return: returns the length of linked list
 */
size_t list_len(const listint_t *h)
{
	int i = 0;

	while (h != NULL)
	{
		i++;
		h = h->next;
	}
	return (i);
}

/**
 * is_palindrome - function checks if a singly linked list is a
 * palindrome
 * @head: ptr to ptr to linked list
 * Return: returns 1 if palindrome, otherwise 0
 */
 int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int *arr;
	int i = 0, j;

	if (*head == NULL)
		return (1);
	arr = malloc(sizeof(int) * list_len(temp));
	if (!arr)
		return (1);

	while(temp)
	{
		arr[i] = temp->n;
		temp = temp->next;
		i++;
	}
	for (j = 0; j < (i/2); j++)
	{
		if (arr[j] != arr[i - j - 1])
		{
			free(arr);
			return (0);
		}
	}
	free(arr);
	return (1);
}
