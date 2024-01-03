#include "lists.h"
#include <stddef.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNum = malloc(sizeof(listint_t)), *temp = *head;

	if (!*head)
		return (NULL);

	if (!newNum)
		return (NULL);

	newNum->n = number;
	newNum->next = NULL;

	if (head == NULL || newNum->n < temp->n)
	{
		newNum->next = temp;
		*head = newNum;
		return (newNum);
	}
	while (temp->next != NULL && temp->next->n < newNum->n)
	{
		temp = temp->next;
	}
	newNum->next = temp->next;
	temp->next = newNum;
	return (newNum);
}
