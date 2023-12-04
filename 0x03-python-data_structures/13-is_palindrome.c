#include "lists.h"

/**
 * nodeReverse - a function that  reverses a linked list
 * @head: a double pointer to the start of the linked list
 *
 * Return: An address to the first node in the newly created list
 */
void nodeReverse(listint_t **head)
{
  listint_t *prev = NULL;
  listint_t *current = *head;
  listint_t *next = NULL;

  while (current)
    {
      next = current->next;
      current->next = prev;
      prev = current;
      current = next;
    }

  *head = prev;
}

/**
 * is_palindrome - a function that determines if a linked list is a palindrome
 * @head: a pointer to the linked list to check
 *
 * Return: 1 (success) or 0 (fail)
 */
int is_palindrome(listint_t **head)
{
  listint_t *slow = *head, *fast = *head, *temp = *head, *dup = NULL;

  if (*head == NULL || (*head)->next == NULL)
    return (1);

  while (1)
    {
      fast = fast->next->next;
      if (!fast)
	{
	  dup = slow->next;
	  break;
	}
      if (!fast->next)
	{
	  dup = slow->next->next;
	  break;
	}
      slow = slow->next;
    }

  nodeReverse(&dup);

  while (dup && temp)
    {
      if (temp->n == dup->n)
	{
	  dup = dup->next;
	  temp = temp->next;
	}
      else
	return (0);
    }

  if (!dup)
    return (1);

  return (0);
}

