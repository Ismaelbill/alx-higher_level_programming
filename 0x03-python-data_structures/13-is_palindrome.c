#include "lists.h"

/**
 * is_palindrome - function checks if a singly linked list is a
 * palindrome
 * @head: list
 * Return: returns 0 if it's not a palindrome, otherwise 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int arr[1024], arr2[1024];
	int i = 0, j, k;

	if (*head == NULL || head == NULL)
		return (1);
	while(temp)
	{
		arr[i] = temp->n;
		arr2[i] = temp->n;
		temp = temp->next;
		i++;
	}
	for (j = 0; j < (i/2); j++)
	{
		k = arr[j];
		arr[j] = arr[i - j - 1];
		arr[i - j - 1] = k;
	}
	for (j = 0; j < i; j++)
	{
		if (arr[j] != arr2[j])
			return (0);
	}
	return (1);
}
