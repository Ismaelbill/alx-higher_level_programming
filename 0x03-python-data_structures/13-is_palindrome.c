#include "lists.h"
#include <stdio.h>
#include <stddef.h>

/**
 * list_len - function that returns the number of elements
 * in a linked 'listint_t' list
 * @hh: pointer to struct node
 * Return: returns number of elements
 */
size_t list_len(listint_t *hh)
{
	int i = 0;

	while (hh != NULL)
	{
		i++;
		hh = hh->next;
	}
	return (i);
}

/**
 * is_palindrome - function checks if a singly linked list is a
 * palindrome
 * @head: list
 * Return: returns 0 if it's not a palindrome, otherwise 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int arr[list_len(temp)];
	int i = 0, j;

	if (*head == NULL)
		return (1);
	while (temp)
	{
		arr[i] = temp->n;
		temp = temp->next;
		i++;
	}
	for (j = 0; j < (i / 2); j++)
	{
		if (arr[j] != arr[i - j - 1])
			return (0);
	}
	return (1);
}
