#include <stdio.h>
#include <signal.h>
#include <stdlib.h>
#include <unistd.h>



int main()
{
  void j(int);
 signal(SIGFPE,j);
 pid_t  processid=getpid();
 printf("process ID is %d",processid);

  int num1,num2;
  double result;
  while(1)
    {

      printf("\nPlease enter 2 numbers: \n");
      scanf("%d",&num1);
      scanf("%d",&num2);
      result=(double)num1/(double)num2;
      printf("the result is: %f",result);

      sleep(1);

    }
  
  return 0;  
  


}
void j(int sig)
{
  printf("Divide by 0. Now quitting program");
  exit(SIGFPE);
}
