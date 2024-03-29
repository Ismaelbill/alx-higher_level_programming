#include "lists.h"
#include <stddef.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNum = malloc(sizeof(listint_t)), *temp = *head;

	if (!newNum)
		return (NULL);

	newNum->n = number;
	newNum->next = NULL;

	if (!temp || newNum->n < temp->n)
	{
		newNum->next = temp;
		*head = newNum;
		return (*head);
	}
	while (temp)
	{
		if (!temp->next || newNum->n < temp->next->n)
		{
			newNum->next = temp->next;
			temp->next = newNum;
			return (temp);
		}
		temp = temp->next;
	}
	return (NULL);
}
