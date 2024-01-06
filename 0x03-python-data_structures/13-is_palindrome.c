#include "lists.h"

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
	while(temp)
	{
		arr[i] = temp->n;
		temp = temp->next;
		i++;
	}
	for (j = 0; j < (i/2); j++)
	{
		if (arr[j] != arr[i - j - 1])
			return (0);
	}
	return (1);
}
