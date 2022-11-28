#include "lists.h"
/**
 * check_cycle - checks if the linked list is cyclic or not
 * @list: pointer to the head of the list.
 *
 * Return: (1) if it is cyclic, otherwise (0).
 */
int check_cycle(listint_t *list)
{
	listint_t *node = list->next;

	if (list && list->next)
	{
		while (node != NULL && node != list)
			node = node->next;
		if (node == NULL)
			return (0);
		else if (node == list)
			return (1);
	}
	return (0);
}
