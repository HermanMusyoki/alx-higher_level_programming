#include "lists.h"

/**
 * check_cycle - a function that checks for a cycle in a linked list
 * @list: the linked list to find the cycle from
 *
 * Return: 1 (success) or 0 otherwise (no cycle)
 */
int check_cycle(listint_t *list)
{
        listint_t *slow = list;
        listint_t *fast = list;

        if (!list)
                return (0);


        while (slow && fast && fast->next)
        {
                slow = slow->next;
                fast = fast->next->next;
                if (slow == fast)
                        return (1);
        }


        return (0);
}

