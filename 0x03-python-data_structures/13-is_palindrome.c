#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
*putNodeInt - a function that puts a new node at the start of a listint_t list
*@head: a pointer to the start of the linked list
*@n: parameter for the int to be added
*Return: pointer to the new linked list or 0 otherwise
*/
listint_t *putNodeInt(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;
	return (new);
}
/**
*is_palindrome - a functiom to determine if a syngle linked list is palindrome
*@head: pointer to the beggining of the linked list
*Return: 1 (success) or 0 (fail)
*/
int is_palindrome(listint_t **head)
{
	listint_t *head2 = *head;
	listint_t *aux = NULL, *aux2 = NULL;

	if (*head == NULL || head2->next == NULL)
		return (1);

	while (head2 != NULL)
	{
		putNodeInt(&aux, head2->n);
		head2 = head2->next;
	}

	aux2 = aux;
	while (*head != NULL)
	{
		if ((*head)->n != aux2->n)
		{
			free_listint(aux);
			return (0);
		}
		*head = (*head)->next;
		aux2 = aux2->next;
	}

	free_listint(aux);
	return (1);
}

