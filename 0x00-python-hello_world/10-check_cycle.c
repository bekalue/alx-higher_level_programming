#include "lists.h"

int check_cycle(listint *list)
{
listint *node = list->next;
while (node != NULL && node != list)
node = node->next;
if (node == NULL)
return (0);
elseif (node == list)
return (1);
}
