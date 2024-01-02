#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - function checks is there a cycle
 * @list: pointer to list 'struct'
 * Return: 1 if cyclical, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	fast = list;
	slow = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
