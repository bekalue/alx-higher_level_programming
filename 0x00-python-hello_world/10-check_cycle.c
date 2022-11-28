#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
  * check_cycle - checks for a cycle in a linked list
  *
  * @head: the first node in the list
  * Return: 0 if no cycle, 1 if cycle found
  */
int check_cycle(listint_t *head)
{
	listint_t *slow, *fast;
	int flag = 0;

	if (head == NULL)
		return (0);

	slow = fast = head;

	while (fast)
	{
		flag++;
		fast = fast->next;
		if (flag % 2 == 0)
			slow = slow->next;
		if (fast == slow)
			return (1);
	}

	return (0);
}
