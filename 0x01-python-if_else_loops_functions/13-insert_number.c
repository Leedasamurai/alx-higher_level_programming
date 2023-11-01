#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - number a sorted singly linked list
 *
 * @head: pointers to a pointer to the head of list
 * @number: number that must be inserted
 *
 * Return: address of the new node or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *current, *temp;

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	current = *head;
	while (current->next != NULL && current->next->n < number)
	{
		current = current->next;
	}

	temp = current->next;
	current->next = new_node;
	new_node->next = temp;

	return (new_node);
}
