#include <iostream>
#include <stdio.h>

using namespace std;

struct Stack {
  int size;
  int top;
  int *S;
};

void create(struct Stack *st) {
  printf("Enter Size");
  scanf("%d", &st->size);
  st->top = -1;
  st->S = (int *)malloc(st->size * sizeof(int));
}

void Display(struct Stack st) {
  int i;
  for (i = st.top; i >= 0; i--)
    printf("%d ", st.S[i]);
  printf("\n");
}

void push(struct Stack *st, int x) {
  if (st->top == st->size - 1)
    printf("Stack overflow\n");
  else {
    st->top++;
    st->S[st->top] = x;
  }
}

int pop(struct Stack *st) {
  int x = -1;

  if (st->top == -1)
    printf("Stack underflow\n");
  else {
    x = st->S[st->top--];
  }
  return x;
}

int main() {

  struct Stack st;
  create(&st);
  push(&st, 10);
  push(&st, 20);
  push(&st, 30);
  pop(&st);
  pop(&st);
  pop(&st);
  pop(&st);

  Display(st);
  return 0;
}
