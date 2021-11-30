#include <stdio.h>
#include <unistd.h>
int main()
{
  printf("starting\n");
  fork();
  fork();
  fork();
  printf("hello\n");
  return 0;






}
