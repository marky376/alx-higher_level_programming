#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 *is_palindrome - function that checks if a singly linked list is a palindrome
 *@head: a structure
 *Return: 1 if palindrom else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *f = *head;
        listint_t *s = *head;
        listint_t *reverse = NULL;
        listint_t *temp = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
		
	while (f != NULL && f->next != NULL)
	{
		f = f->next->next;
		temp = s->next;
		s->next = reverse;
		reverse = s;
		s = temp;
	}

	if (f != NULL)
		s = s->next;

	while (reverse != NULL)
	{
		if (reverse->n != s->n)
			return (0);
		reverse = reverse->next;
		s = s->next;
	}
	return (1);
}
