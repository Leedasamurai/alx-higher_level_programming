#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 *
 * @list: pointer to head of link list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *behind, *front;

	if (list == NULL || list->next == NULL)
		return (0);

	behind = list;
	front = list;

	while (front != NULL && front->next != NULL)
	{
		behind = behind->next;
		front = front->next->next;

		if (behind == front)
			return (1);
	}
	return (0);
}

