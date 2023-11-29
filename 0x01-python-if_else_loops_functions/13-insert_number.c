#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: structure
 * @number: value
 * Return: always success
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode;
	listint_t *current;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		exit(100);

	newnode->n = number;
	newnode->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		newnode->next = *head;
		*head = newnode;
		return (newnode);
	}
	current = *head;
	while (current->next != NULL && current->next->n < number)
	{
		current = current->next;
	}
	newnode->next = current->next;
	current->next = newnode;

	return (newnode);
}
